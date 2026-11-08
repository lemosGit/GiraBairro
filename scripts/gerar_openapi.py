#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera docs/03-arquitetura/openapi.yaml (M3-05) — contrato da API do GiraBairro.
Enums vêm de scripts/modelo_dados.py (fonte única), para o contrato nunca divergir do dicionário.
Uso: python3 scripts/gerar_openapi.py
Na M5-11 o FastAPI passa a gerar o OpenAPI a partir do código; este ficheiro é o contrato de referência
contra o qual o código é testado (teste de contrato em CI).
"""
import os
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modelo_dados import ENUMS  # noqa: E402

REF = lambda n: {"$ref": f"#/components/schemas/{n}"}  # noqa: E731
UUID = {"type": "string", "format": "uuid"}
DT = {"type": "string", "format": "date-time"}
STR = lambda n=None, **k: {"type": "string", **({"maxLength": n} if n else {}), **k}  # noqa: E731
INT = lambda mn=None, mx=None: {"type": "integer", **({"minimum": mn} if mn is not None else {}),  # noqa: E731
                                **({"maximum": mx} if mx is not None else {})}
BOOL = {"type": "boolean"}
ARR = lambda s: {"type": "array", "items": s}  # noqa: E731
NULL = lambda s: {**s, "nullable": True}  # noqa: E731


def obj(props, req=None, desc=None):
    o = {"type": "object", "properties": props}
    if req:
        o["required"] = req
    if desc:
        o["description"] = desc
    return o


def enum(name):
    return {"type": "string", "enum": ENUMS[name]}


SCHEMAS = {
    "Erro": obj({"codigo": STR(example="regra_negocio_violada"), "mensagem": STR(example="Número já em uso"),
                 "detalhes": {"type": "object", "additionalProperties": True}}, ["codigo", "mensagem"],
                "Corpo padrão de erro (padrao-backend.md §4)"),
    "Telefone": STR(20, pattern=r"^\+?[0-9]{9,15}$", example="+244923000000"),
    "PalavraPasse": STR(128, minLength=8, format="password"),
    "TokenPar": obj({"access_token": STR(), "refresh_token": STR(), "expira_em": DT, "tipo": STR(example="Bearer")},
                    ["access_token", "refresh_token", "expira_em"]),
    "RegistoIn": obj({"nome_completo": STR(120), "telefone": REF("Telefone"), "palavra_passe": REF("PalavraPasse"),
                      "aceita_termos": {"type": "boolean", "enum": [True]}},
                     ["nome_completo", "telefone", "palavra_passe", "aceita_termos"]),
    "LoginIn": obj({"telefone": REF("Telefone"), "palavra_passe": REF("PalavraPasse"),
                    "cliente": {"type": "string", "enum": ["web", "mobile"]}}, ["telefone", "palavra_passe", "cliente"]),
    "Sessao": obj({"tokens": REF("TokenPar"), "utilizador": REF("Utilizador")}, ["tokens", "utilizador"]),
    "Utilizador": obj({"id": UUID, "nome_completo": STR(), "telefone": REF("Telefone"),
                       "papel": enum("papel_utilizador"), "estado": enum("estado_conta"),
                       "equipa_id": NULL(UUID)}, ["id", "nome_completo", "telefone", "papel", "estado"]),
    "UtilizadorPatch": obj({"nome_completo": STR(120)}),
    "Local": obj({"id": INT(), "nome": STR()}, ["id", "nome"]),
    "Localizacao": obj({"bairro": REF("Local"), "municipio": REF("Local"), "provincia": REF("Local")},
                       ["bairro", "municipio", "provincia"]),
    "Estrelas": obj({"estrelas": NULL(INT(1, 5)), "nova": BOOL, "indice": {"type": "number", "format": "float"}},
                    ["nova"], "Estrelas (null + nova=true se J < 3 — RN-14)"),
    "EquipaResumo": obj({"id": UUID, "nome": STR(), "emblema_url": NULL(STR()), "localizacao": REF("Localizacao"),
                         "classificacao": REF("Estrelas"), "posicao_municipio": NULL(INT(1)),
                         "taxa_comparencia": {"type": "number", "format": "float"},
                         "disponivel": BOOL}, ["id", "nome", "localizacao", "classificacao", "disponivel"]),
    "EquipaIn": obj({"nome": STR(80), "bairro_id": INT(), "descricao": NULL(STR(1000)),
                     "contacto_principal": REF("ContactoIn")}, ["nome", "bairro_id", "contacto_principal"]),
    "EquipaPatch": obj({"nome": STR(80), "bairro_id": INT(), "descricao": NULL(STR(1000)),
                        "visibilidade_plantel": enum("visibilidade_plantel")}),
    "EquipaPerfil": {"allOf": [REF("EquipaResumo"), obj({
        "descricao": NULL(STR()), "visibilidade_plantel": enum("visibilidade_plantel"),
        "contactos": ARR(REF("Contacto")), "plantel": ARR(REF("JogadorPublico")),
        "estatisticas": REF("Estatisticas"), "responsavel_nome": STR()},
        desc="Contactos com telefone só para autenticados (RN-17); nomes do plantel conforme RN-22")]},
    "Estatisticas": obj({k: INT(0) for k in ["jogos_confirmados", "vitorias", "empates", "derrotas", "pontos",
                                             "golos_marcados", "golos_sofridos", "jogos_agendados", "comparencias",
                                             "faltas_confirmadas"]}),
    "JogadorIn": obj({"nome": STR(120), "numero_camisola": INT(1, 99), "posicao": enum("posicao_jogador"),
                      "activo": BOOL}, ["nome", "numero_camisola", "posicao"]),
    "Jogador": obj({"id": UUID, "nome": STR(), "numero_camisola": INT(1, 99), "posicao": enum("posicao_jogador"),
                    "activo": BOOL}, ["id", "nome", "numero_camisola", "posicao", "activo"]),
    "JogadorPublico": obj({"nome": NULL(STR()), "numero_camisola": INT(1, 99), "posicao": enum("posicao_jogador")},
                          ["numero_camisola", "posicao"], "nome = null quando oculto (RN-22)"),
    "ContactoIn": obj({"nome": STR(120), "telefone": REF("Telefone"), "funcao": STR(60), "principal": BOOL},
                      ["nome", "telefone", "funcao"]),
    "Contacto": obj({"id": UUID, "nome": STR(), "telefone": NULL(REF("Telefone")), "funcao": STR(),
                     "principal": BOOL}, ["id", "nome", "funcao", "principal"], "telefone = null para visitantes (RN-17)"),
    "SolicitacaoIn": obj({"equipa_desafiada_id": UUID, "data_hora": DT, "local": STR(150),
                          "equipa_mandante_id": NULL(UUID), "observacao": NULL(STR(500))},
                         ["equipa_desafiada_id", "data_hora", "local"]),
    "PropostaIn": obj({"data_hora": DT, "local": STR(150), "observacao": NULL(STR(500))}, ["data_hora", "local"]),
    "Proposta": obj({"id": UUID, "proposta_por_equipa_id": UUID, "data_hora": DT, "local": STR(),
                     "observacao": NULL(STR()), "criado_em": DT}),
    "Solicitacao": obj({"id": UUID, "desafiante": REF("EquipaResumo"), "desafiada": REF("EquipaResumo"),
                        "data_hora": DT, "local": STR(), "equipa_mandante_id": NULL(UUID),
                        "observacao": NULL(STR()), "estado": enum("estado_solicitacao"),
                        "aguarda_resposta_de_id": NULL(UUID), "propostas": ARR(REF("Proposta")),
                        "jogo_id": NULL(UUID), "criado_em": DT},
                       ["id", "desafiante", "desafiada", "data_hora", "local", "estado"]),
    "MotivoIn": obj({"motivo": STR(500)}, ["motivo"]),
    "MotivoOpcionalIn": obj({"motivo": NULL(STR(500))}),
    "Comparencia": obj({"equipa_id": UUID, "estado": enum("estado_comparencia"),
                        "declarou_adversaria": NULL(enum("declaracao_adversaria")), "observacao": NULL(STR()),
                        "declarado_em": NULL(DT), "prazo_resposta_ate": NULL(DT)}, ["equipa_id", "estado"]),
    "ComparenciaIn": obj({"compareceu": BOOL, "adversaria": NULL(enum("declaracao_adversaria")),
                          "observacao": NULL(STR(500))}, ["compareceu"],
                         "adversaria obrigatória se compareceu = true"),
    "ResultadoIn": obj({"golos_a": INT(0, 99), "golos_b": INT(0, 99)}, ["golos_a", "golos_b"]),
    "Submissao": obj({"equipa_id": UUID, "golos_a": INT(0), "golos_b": INT(0), "versao": INT(1), "actual": BOOL,
                      "criado_em": DT}, ["equipa_id", "golos_a", "golos_b", "versao", "actual"]),
    "Jogo": obj({"id": UUID, "codigo": STR(example="GB-2026-00042"), "equipa_a": REF("EquipaResumo"),
                 "equipa_b": REF("EquipaResumo"), "data_hora": DT, "local": STR(), "estado": enum("estado_jogo"),
                 "estado_resultado": enum("estado_resultado"), "golos_a": NULL(INT(0)), "golos_b": NULL(INT(0)),
                 "comparencias": ARR(REF("Comparencia")), "submissoes": ARR(REF("Submissao")),
                 "janela_registo_aberta": BOOL, "accoes": ARR(STR(example="submeter_resultado")),
                 "divergente_desde": NULL(DT), "motivo_cancelamento": NULL(STR())},
                ["id", "codigo", "equipa_a", "equipa_b", "data_hora", "local", "estado", "estado_resultado"],
                "accoes = acções disponíveis para o utilizador actual (TEL-15)"),
    "RegistoHistorico": obj({"accao": enum("accao_auditoria"), "entidade": STR(), "valor_anterior": NULL(
        {"type": "object"}), "valor_novo": NULL({"type": "object"}), "motivo": NULL(STR()),
        "autor": NULL(STR()), "criado_em": DT}),
    "CasoIn": obj({"tipo": {"type": "string", "enum": ["divergencia_resultado", "reabertura_resultado"]},
                   "motivo": STR(1000)}, ["tipo", "motivo"]),
    "Caso": obj({"id": UUID, "jogo": REF("Jogo"), "tipo": enum("tipo_caso"), "estado": enum("estado_caso"),
                 "motivo": NULL(STR()), "aberto_por_equipa_id": NULL(UUID), "decisao": NULL({"type": "object"}),
                 "justificacao": NULL(STR()), "criado_em": DT, "resolvido_em": NULL(DT)},
                ["id", "jogo", "tipo", "estado"]),
    "DecisaoIn": obj({"golos_a": NULL(INT(0, 99)), "golos_b": NULL(INT(0, 99)),
                      "comparencia": NULL(obj({"equipa_id": UUID, "compareceu": BOOL})),
                      "justificacao": STR(2000, minLength=10)}, ["justificacao"],
                     "Justificação obrigatória (RF-11.04)"),
    "EntradaRanking": obj({"posicao": INT(1), "equipa": REF("EquipaResumo"), "estatisticas": REF("Estatisticas"),
                           "classificacao": REF("Estrelas"), "saldo_golos": INT()},
                          ["posicao", "equipa", "estatisticas", "classificacao"]),
    "Criterios": obj({"texto": STR(), "pesos": obj({"aproveitamento": {"type": "number"},
                                                    "comparencia": {"type": "number"}}),
                      "limiares_estrelas": ARR(obj({"estrelas": INT(1, 5), "indice_minimo": {"type": "number"}})),
                      "jogos_minimos": INT(), "desempate": ARR(STR())}, desc="RN-11 / RF-09.11"),
    "Notificacao": obj({"id": UUID, "tipo": enum("tipo_notificacao"), "mensagem": STR(), "jogo_id": NULL(UUID),
                        "solicitacao_id": NULL(UUID), "lida": BOOL, "criado_em": DT},
                       ["id", "tipo", "mensagem", "lida", "criado_em"]),
    "DispositivoIn": obj({"token": STR(255), "plataforma": {"type": "string", "enum": ["android", "ios"]}},
                         ["token", "plataforma"]),
    "Dashboard": obj({"equipa": REF("EquipaResumo"), "proximos_jogos": ARR(REF("Jogo")),
                      "solicitacoes_pendentes": ARR(REF("Solicitacao")), "jogos_por_confirmar": ARR(REF("Jogo")),
                      "total_jogadores": INT(0), "estatisticas": REF("Estatisticas"),
                      "posicao_municipio": NULL(INT(1)), "classificacao": REF("Estrelas"),
                      "notificacoes_nao_lidas": INT(0)}, desc="TEL-05"),
    "Indicadores": obj({k: INT(0) for k in ["utilizadores", "equipas", "jogadores", "jogos_marcados",
                                            "jogos_concluidos", "casos_abertos", "resultados_divergentes",
                                            "contas_suspensas", "equipas_suspensas"]}, desc="TEL-22 / RF-11.06"),
}
for name in ["EquipaResumo", "Solicitacao", "Jogo", "Notificacao", "Caso", "Utilizador", "EntradaRanking"]:
    SCHEMAS[f"Pagina{name}"] = obj({"itens": ARR(REF(name)), "total": INT(0), "pagina": INT(1), "tamanho": INT(1, 50)},
                                   ["itens", "total", "pagina", "tamanho"])

P_ID = lambda n, d: {"name": n, "in": "path", "required": True, "schema": UUID, "description": d}  # noqa: E731
Q = lambda n, s, d="": {"name": n, "in": "query", "required": False, "schema": s, "description": d}  # noqa: E731
PAG = [Q("pagina", INT(1)), Q("tamanho", INT(1, 50))]
E = lambda *codes: codes  # noqa: E731

ERRS = {"400": "Pedido mal formado", "401": "Não autenticado", "403": "Proibido (RN-13, suspensão ou papel)",
        "404": "Não encontrado", "409": "Conflito de estado (ex.: janela fechada, já respondida)",
        "422": "Validação ou regra de negócio violada", "423": "Conta bloqueada temporariamente",
        "429": "Demasiados pedidos (RNF-027)"}


def op(tag, summary, ok="200", resp=None, body=None, params=None, auth="resp", errs=(), refs="", desc=None,
       multipart=False):
    o = {"tags": [tag], "summary": summary}
    d = []
    if refs:
        d.append(f"**Requisitos:** {refs}")
    if desc:
        d.append(desc)
    if d:
        o["description"] = "\n\n".join(d)
    if params:
        o["parameters"] = params
    if body:
        ct = "multipart/form-data" if multipart else "application/json"
        o["requestBody"] = {"required": True, "content": {ct: {"schema": body}}}
    o["responses"] = {ok: {"description": "OK" if ok == "200" else ("Criado" if ok == "201" else "Sem conteúdo")}}
    if resp:
        o["responses"][ok]["content"] = {"application/json": {"schema": resp}}
    base = [] if auth == "public" else ["401"]
    if auth in ("resp", "admin"):
        base.append("403")
    for c in list(base) + list(errs):
        o["responses"][c] = {"$ref": f"#/components/responses/E{c}"}
    if auth == "public":
        o["security"] = []
    elif auth == "opcional":
        o["security"] = [{}, {"bearer": []}]
    if auth == "admin":
        o["x-papel"] = "admin"
    return o


EQ = P_ID("equipa_id", "Equipa")
JG = P_ID("jogo_id", "Jogo")
SO = P_ID("solicitacao_id", "Solicitação")
CA = P_ID("caso_id", "Caso")

PATHS = {
    "/auth/registo": {"post": op("auth", "Criar conta", "201", REF("Sessao"), REF("RegistoIn"), auth="public",
                                 errs=E("409", "422", "429"), refs="RF-01.01–03, UC01",
                                 desc="409 se o telefone já existe (RF-01.03).")},
    "/auth/sessoes": {
        "post": op("auth", "Iniciar sessão", "200", REF("Sessao"), REF("LoginIn"), auth="public",
                   errs=E("401", "403", "423", "429"), refs="RF-01.04, UC02, RNF-021"),
        "delete": op("auth", "Terminar sessão (revoga o refresh token)", "204", auth="user", refs="RF-01.05")},
    "/auth/sessoes/renovar": {"post": op("auth", "Renovar tokens (refresh rotativo)", "200", REF("TokenPar"),
                                         obj({"refresh_token": STR()}, ["refresh_token"]), auth="public",
                                         errs=E("401",), refs="ADR-006")},
    "/auth/recuperacao": {"post": op("auth", "Pedir código de recuperação por SMS", "202",
                                     body=obj({"telefone": REF("Telefone")}, ["telefone"]), auth="public",
                                     errs=E("429",), refs="RF-01.07, UC03",
                                     desc="Responde sempre 202, exista ou não a conta (não revela contas).")},
    "/auth/recuperacao/confirmar": {"post": op("auth", "Confirmar código e definir nova palavra-passe", "204",
                                               body=obj({"telefone": REF("Telefone"), "codigo": STR(6, pattern="^[0-9]{6}$"),
                                                         "nova_palavra_passe": REF("PalavraPasse")},
                                                        ["telefone", "codigo", "nova_palavra_passe"]),
                                               auth="public", errs=E("422", "429"), refs="RF-01.07, RNF-025")},
    "/me": {"get": op("utilizadores", "Dados do utilizador actual", "200", REF("Utilizador"), auth="user",
                      refs="RF-01.06, TEL-21"),
            "patch": op("utilizadores", "Editar dados básicos", "200", REF("Utilizador"), REF("UtilizadorPatch"),
                        auth="user", errs=E("422",), refs="RF-01.06")},
    "/me/palavra-passe": {"post": op("utilizadores", "Alterar palavra-passe", "204",
                                     body=obj({"actual": REF("PalavraPasse"), "nova": REF("PalavraPasse")},
                                              ["actual", "nova"]), auth="user", errs=E("422",), refs="TEL-21")},
    "/provincias": {"get": op("localizacao", "Listar províncias", "200", ARR(REF("Local")), auth="public")},
    "/provincias/{provincia_id}/municipios": {"get": op(
        "localizacao", "Municípios de uma província", "200", ARR(REF("Local")), auth="public",
        params=[{"name": "provincia_id", "in": "path", "required": True, "schema": INT()}])},
    "/municipios/{municipio_id}/bairros": {"get": op(
        "localizacao", "Bairros de um município", "200", ARR(REF("Local")), auth="public",
        params=[{"name": "municipio_id", "in": "path", "required": True, "schema": INT()}])},
    "/equipas": {
        "get": op("equipas", "Pesquisar equipas", "200", REF("PaginaEquipaResumo"), auth="opcional",
                  params=[Q("q", STR(80), "Nome (parcial)"), Q("provincia_id", INT()), Q("municipio_id", INT()),
                          Q("bairro_id", INT()), Q("disponiveis", BOOL, "Só equipas activas")] + PAG,
                  refs="RF-02.08, RF-05.01–02, TEL-10"),
        "post": op("equipas", "Registar equipa", "201", REF("EquipaPerfil"), REF("EquipaIn"), auth="user",
                   errs=E("409", "422"), refs="RF-02.01–03, RF-02.09, RN-18, UC04",
                   desc="409 se o utilizador já administra uma equipa (RN-18) ou duplicado nome+bairro (RF-02.09).")},
    "/equipas/{equipa_id}": {
        "get": op("equipas", "Perfil público da equipa", "200", REF("EquipaPerfil"), auth="opcional",
                  params=[EQ], errs=E("404",), refs="RF-02.07, RF-04.05, RN-17, RN-22, TEL-11"),
        "patch": op("equipas", "Editar equipa", "200", REF("EquipaPerfil"), REF("EquipaPatch"), params=[EQ],
                    errs=E("404", "409", "422"), refs="RF-02.06, RN-02")},
    "/equipas/{equipa_id}/emblema": {"put": op(
        "equipas", "Carregar emblema", "200", obj({"emblema_url": STR()}),
        obj({"ficheiro": {"type": "string", "format": "binary"}}, ["ficheiro"]), params=[EQ],
        errs=E("422",), refs="RF-02.04, RNF-003", desc="JPG/PNG/WebP até 2 MB.", multipart=True)},
    "/equipas/{equipa_id}/jogos": {"get": op("equipas", "Histórico de jogos da equipa", "200", REF("PaginaJogo"),
                                             auth="opcional", params=[EQ] + PAG, refs="RF-06.12, RF-07.08")},
    "/equipas/{equipa_id}/jogadores": {
        "get": op("jogadores", "Listar jogadores (inclui inactivos)", "200", ARR(REF("Jogador")), params=[EQ],
                  refs="RF-03.05, TEL-07"),
        "post": op("jogadores", "Adicionar jogador", "201", REF("Jogador"), REF("JogadorIn"), params=[EQ],
                   errs=E("409", "422"), refs="RF-03.01–02, RN-04", desc="409 se o número já está em uso (RN-04).")},
    "/equipas/{equipa_id}/jogadores/{jogador_id}": {
        "patch": op("jogadores", "Editar / activar / desactivar jogador", "200", REF("Jogador"), REF("JogadorIn"),
                    params=[EQ, P_ID("jogador_id", "Jogador")], errs=E("404", "409", "422"), refs="RF-03.03–04"),
        "delete": op("jogadores", "Remover jogador", "204", params=[EQ, P_ID("jogador_id", "Jogador")],
                     errs=E("404",), refs="RF-03.04")},
    "/equipas/{equipa_id}/contactos": {
        "get": op("contactos", "Listar contactos", "200", ARR(REF("Contacto")), params=[EQ], refs="RF-04, TEL-09"),
        "post": op("contactos", "Adicionar contacto", "201", REF("Contacto"), REF("ContactoIn"), params=[EQ],
                   errs=E("422",), refs="RF-04.01–03")},
    "/equipas/{equipa_id}/contactos/{contacto_id}": {
        "patch": op("contactos", "Editar contacto / definir principal", "200", REF("Contacto"), REF("ContactoIn"),
                    params=[EQ, P_ID("contacto_id", "Contacto")], errs=E("404", "422"), refs="RF-04.03–04"),
        "delete": op("contactos", "Remover contacto", "204", params=[EQ, P_ID("contacto_id", "Contacto")],
                     errs=E("404", "409"), refs="RF-04.04", desc="409 se for o último contacto principal.")},
    "/solicitacoes": {
        "get": op("solicitacoes", "Listar solicitações da minha equipa", "200", REF("PaginaSolicitacao"),
                  params=[Q("tipo", {"type": "string", "enum": ["recebidas", "enviadas"]}),
                          Q("estado", enum("estado_solicitacao"))] + PAG, refs="TEL-13"),
        "post": op("solicitacoes", "Solicitar jogo", "201", REF("Solicitacao"), REF("SolicitacaoIn"),
                   errs=E("404", "422", "429"), refs="RF-05.03–04, RN-19, UC08")},
    "/solicitacoes/{solicitacao_id}": {"get": op("solicitacoes", "Detalhe da solicitação", "200",
                                                 REF("Solicitacao"), params=[SO], errs=E("404",))},
    "/solicitacoes/{solicitacao_id}/aceitar": {"post": op(
        "solicitacoes", "Aceitar (cria o jogo)", "200", REF("Jogo"), params=[SO], errs=E("404", "409"),
        refs="RF-05.05, RF-05.08, RN-05, UC09")},
    "/solicitacoes/{solicitacao_id}/recusar": {"post": op(
        "solicitacoes", "Recusar", "200", REF("Solicitacao"), REF("MotivoOpcionalIn"), params=[SO],
        errs=E("404", "409"), refs="RF-05.05")},
    "/solicitacoes/{solicitacao_id}/propostas": {"post": op(
        "solicitacoes", "Propor alteração de data/hora/local", "201", REF("Solicitacao"), REF("PropostaIn"),
        params=[SO], errs=E("404", "409", "422"), refs="RF-05.06")},
    "/solicitacoes/{solicitacao_id}/cancelar": {"post": op(
        "solicitacoes", "Cancelar solicitação", "200", REF("Solicitacao"), REF("MotivoOpcionalIn"), params=[SO],
        errs=E("404", "409"), refs="RF-05.09, UC10")},
    "/jogos": {"get": op("jogos", "Agenda da minha equipa", "200", REF("PaginaJogo"),
                         params=[Q("separador", {"type": "string",
                                                 "enum": ["proximos", "pendentes", "concluidos", "cancelados"]})] + PAG,
                         refs="RF-05.10, TEL-14")},
    "/jogos/{jogo_id}": {"get": op("jogos", "Detalhe do jogo", "200", REF("Jogo"), auth="opcional", params=[JG],
                                   errs=E("404",), refs="RF-06.01–02, TEL-15")},
    "/jogos/{jogo_id}/historico": {"get": op("jogos", "Histórico de alterações do jogo", "200",
                                             ARR(REF("RegistoHistorico")), params=[JG], errs=E("404",),
                                             refs="RF-08.08, RN-12, TEL-15")},
    "/jogos/{jogo_id}/cancelar": {"post": op("jogos", "Cancelar jogo", "200", REF("Jogo"), REF("MotivoIn"),
                                             params=[JG], errs=E("404", "409"), refs="RF-05.09, RN-24, UC10",
                                             desc="Se faltar < 24 h, conta como falta da equipa que cancela (RN-24).")},
    "/jogos/{jogo_id}/comparencias/minha": {"put": op(
        "comparencias", "Declarar comparência da minha equipa", "200", REF("Jogo"), REF("ComparenciaIn"),
        params=[JG], errs=E("404", "409", "422"), refs="RF-06.03–05, RF-07.01–03, RN-06, RN-16, RN-23, UC11")},
    "/jogos/{jogo_id}/comparencias/minha/concordar": {"post": op(
        "comparencias", "Concordar com a falta declarada pela adversária", "200", REF("Jogo"), params=[JG],
        errs=E("404", "409"), refs="RN-16, UC11b")},
    "/jogos/{jogo_id}/comparencias/minha/contestar": {"post": op(
        "comparencias", "Contestar a falta declarada (abre caso)", "200", REF("Jogo"), REF("MotivoIn"), params=[JG],
        errs=E("404", "409"), refs="RF-07.05, RN-16, UC11b")},
    "/jogos/{jogo_id}/resultados": {
        "get": op("resultados", "Submissões das duas equipas", "200", ARR(REF("Submissao")), auth="opcional",
                  params=[JG], refs="TEL-18"),
        "post": op("resultados", "Submeter ou corrigir o resultado da minha equipa", "201", REF("Jogo"),
                   REF("ResultadoIn"), params=[JG], errs=E("404", "409", "422"),
                   refs="RF-06.06–11, RF-08.01–04, RN-08, UC12",
                   desc="Cria nova versão. Confirma se coincidir com a adversária; senão fica divergente.")},
    "/jogos/{jogo_id}/casos": {"post": op("resultados", "Pedir análise ou reabertura ao administrador", "201",
                                          REF("Caso"), REF("CasoIn"), params=[JG], errs=E("404", "409"),
                                          refs="RF-08.07, RN-20, RN-21, UC13")},
    "/ranking": {"get": op("ranking", "Ranking", "200", REF("PaginaEntradaRanking"), auth="opcional",
                           params=[Q("ambito", {"type": "string", "enum": ["geral", "provincia", "municipio", "bairro"],
                                                "default": "geral"}),
                                   Q("local_id", INT(), "Obrigatório se âmbito ≠ geral")] + PAG,
                           errs=E("422",), refs="RF-09, RN-15, TEL-19, UC14")},
    "/ranking/criterios": {"get": op("ranking", "Critérios públicos do ranking e das estrelas", "200",
                                     REF("Criterios"), auth="public", refs="RF-09.11, RN-11")},
    "/notificacoes": {"get": op("notificacoes", "Listar notificações", "200", REF("PaginaNotificacao"), auth="user",
                                params=[Q("nao_lidas", BOOL)] + PAG, refs="RF-10.07, TEL-20")},
    "/notificacoes/{notificacao_id}/lida": {"post": op("notificacoes", "Marcar como lida", "204", auth="user",
                                                       params=[P_ID("notificacao_id", "Notificação")],
                                                       errs=E("404",))},
    "/notificacoes/lidas": {"post": op("notificacoes", "Marcar todas como lidas", "204", auth="user")},
    "/dispositivos": {"post": op("notificacoes", "Registar dispositivo para push (app)", "204",
                                 body=REF("DispositivoIn"), auth="user", errs=E("422",), refs="M8-06")},
    "/dashboard": {"get": op("dashboard", "Resumo do responsável", "200", REF("Dashboard"), refs="TEL-05, M6-12")},
    "/admin/indicadores": {"get": op("admin", "Indicadores gerais", "200", REF("Indicadores"), auth="admin",
                                     refs="RF-11.06, TEL-22")},
    "/admin/utilizadores": {"get": op("admin", "Consultar utilizadores", "200", REF("PaginaUtilizador"),
                                      auth="admin", params=[Q("q", STR()), Q("estado", enum("estado_conta"))] + PAG,
                                      refs="RF-11.01")},
    "/admin/utilizadores/{utilizador_id}/estado": {"post": op(
        "admin", "Suspender / reactivar utilizador", "204",
        body=obj({"estado": enum("estado_conta"), "motivo": STR(500)}, ["estado", "motivo"]), auth="admin",
        params=[P_ID("utilizador_id", "Utilizador")], errs=E("404",), refs="RF-11.02, RF-11.05")},
    "/admin/equipas": {"get": op("admin", "Consultar equipas", "200", REF("PaginaEquipaResumo"), auth="admin",
                                 params=[Q("q", STR()), Q("estado", enum("estado_conta"))] + PAG, refs="RF-11.01")},
    "/admin/equipas/{equipa_id}/estado": {"post": op(
        "admin", "Suspender / reactivar equipa", "204",
        body=obj({"estado": enum("estado_conta"), "motivo": STR(500)}, ["estado", "motivo"]), auth="admin",
        params=[EQ], errs=E("404",), refs="RF-11.02, RN-19")},
    "/admin/casos": {"get": op("admin", "Casos para análise", "200", REF("PaginaCaso"), auth="admin",
                               params=[Q("estado", enum("estado_caso")), Q("tipo", enum("tipo_caso"))] + PAG,
                               refs="RF-11.03, TEL-22")},
    "/admin/casos/{caso_id}": {"get": op("admin", "Detalhe do caso", "200", REF("Caso"), auth="admin", params=[CA],
                                         errs=E("404",))},
    "/admin/casos/{caso_id}/resolver": {"post": op(
        "admin", "Resolver caso com decisão e justificação", "200", REF("Caso"), REF("DecisaoIn"), auth="admin",
        params=[CA], errs=E("404", "409", "422"), refs="RF-11.04–05, RN-20, RN-21, UC17")},
    "/admin/casos/{caso_id}/rejeitar": {"post": op(
        "admin", "Rejeitar caso (ex.: reabertura fora de prazo)", "200", REF("Caso"), REF("MotivoIn"), auth="admin",
        params=[CA], errs=E("404", "409"), refs="RN-21")},
    "/admin/jogos/{jogo_id}/marcar-realizado": {"post": op(
        "admin", "Marcar jogo como realizado (reabre a janela de registo)", "200", REF("Jogo"), REF("MotivoIn"),
        auth="admin", params=[JG], errs=E("404", "409"), refs="RF-06.13, UC22")},
}

TAGS = [("auth", "Conta e sessão — RF-01"), ("utilizadores", "Perfil — RF-01.06"),
        ("localizacao", "Províncias, municípios, bairros"), ("equipas", "Equipas — RF-02"),
        ("jogadores", "Plantel — RF-03"), ("contactos", "Contactos — RF-04"),
        ("solicitacoes", "Solicitações de jogo — RF-05"), ("jogos", "Jogos — RF-05/06"),
        ("comparencias", "Comparência — RF-07"), ("resultados", "Resultados e divergências — RF-06/08"),
        ("ranking", "Ranking e estrelas — RF-09"), ("notificacoes", "Notificações — RF-10"),
        ("dashboard", "Dashboard — TEL-05"), ("admin", "Administração — RF-11 (papel admin)")]

DOC = {
    "openapi": "3.0.3",
    "info": {"title": "GiraBairro API", "version": "0.1.0",
             "description": ("Contrato da API do GiraBairro (M3-05). Consumido pela web (Next.js) e pela app "
                             "(React Native).\n\n- Autenticação: `Authorization: Bearer <access_token>` (ADR-006).\n"
                             "- Datas em ISO 8601 UTC; a interface mostra em `Africa/Luanda` (RNF-034).\n"
                             "- Erros no formato `Erro`.\n- Operações de escrita sobre uma equipa/jogo exigem ser "
                             "responsável dessa equipa / participante do jogo (RN-13) → 403.\n"
                             "- Rotas `/admin/*` exigem papel `admin`.")},
    "servers": [{"url": "http://localhost:8000/v1", "description": "Desenvolvimento"},
                {"url": "https://api.staging.girabairro.example/v1", "description": "Staging (domínio a definir — M3-07)"}],
    "tags": [{"name": n, "description": d} for n, d in TAGS],
    "security": [{"bearer": []}],
    "paths": PATHS,
    "components": {
        "securitySchemes": {"bearer": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}},
        "responses": {f"E{c}": {"description": d, "content": {"application/json": {"schema": REF("Erro")}}}
                      for c, d in ERRS.items()},
        "schemas": SCHEMAS},
}

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "03-arquitetura", "openapi.yaml")
    with open(out, "w", encoding="utf-8") as f:
        f.write("# Gerado por scripts/gerar_openapi.py — editar o script, não este ficheiro.\n")
        yaml.safe_dump(DOC, f, allow_unicode=True, sort_keys=False, width=120)
    n = sum(len(v) for v in PATHS.values())
    print(f"{len(PATHS)} caminhos, {n} operações, {len(SCHEMAS)} schemas")
