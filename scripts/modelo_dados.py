# -*- coding: utf-8 -*-
"""
Fonte única do modelo de dados do GiraBairro (M2-04 / M2-05).
Gera: docs/02-modelagem/src/mer-logico.mmd e docs/02-modelagem/dicionario-dados.md
Uso:  python3 scripts/modelo_dados.py && python3 scripts/render_mermaid.py docs/02-modelagem/src/mer-logico.mmd

Colunas: (nome, tipo, tamanho, nulo, chave, default, descrição)
  chave: PK | FK→tabela.col | UK | UK(grupo) | ""
"""
import os

U = "gen_random_uuid()"
NOW = "now()"

ENUMS = {
    "papel_utilizador": ["utilizador", "admin"],
    "estado_conta": ["activa", "suspensa"],
    "papel_membro": ["responsavel"],
    "posicao_jogador": ["guarda_redes", "defesa", "medio", "avancado"],
    "visibilidade_plantel": ["publico", "autenticados", "privado"],
    "estado_solicitacao": ["pendente", "alteracao_proposta", "aceite", "recusada", "cancelada"],
    "estado_jogo": ["agendado", "aguarda_comparencia", "aguarda_resultado", "resultado_pendente", "divergencia",
                    "em_analise", "concluido", "cancelado"],
    "estado_resultado": ["nao_submetido", "aguarda_adversaria", "confirmado", "divergente", "em_analise"],
    "estado_comparencia": ["nao_registada", "compareceu_declarado", "falta_declarada", "em_analise", "validada",
                           "falta_confirmada"],
    "declaracao_adversaria": ["compareceu", "faltou"],
    "tipo_caso": ["divergencia_resultado", "comparencia_contestada", "comparencia_contraditoria", "reabertura_resultado",
                  "jogo_fora_de_prazo"],
    "estado_caso": ["aberto", "em_analise", "resolvido", "rejeitado"],
    "tipo_notificacao": ["solicitacao_recebida", "solicitacao_aceite", "solicitacao_recusada", "alteracao_proposta",
                         "jogo_cancelado", "lembrete_jogo", "comparencia_submetida", "falta_declarada",
                         "resultado_submetido", "resultado_confirmado", "resultado_divergente", "caso_resolvido"],
    "accao_auditoria": ["criar", "actualizar", "eliminar", "decisao_admin", "automatico"],
}

TABLES = [
 ("provincia", "Províncias (divisão territorial de 1.º nível)", [
  ("id", "SMALLINT", "", "Não", "PK", "", "Identificador"),
  ("nome", "VARCHAR", "60", "Não", "UK", "", "Nome da província")]),
 ("municipio", "Municípios de cada província", [
  ("id", "INTEGER", "", "Não", "PK", "", "Identificador"),
  ("provincia_id", "SMALLINT", "", "Não", "FK→provincia.id", "", "Província a que pertence"),
  ("nome", "VARCHAR", "80", "Não", "UK(provincia_id,nome)", "", "Nome do município")]),
 ("bairro", "Bairros de cada município", [
  ("id", "INTEGER", "", "Não", "PK", "", "Identificador"),
  ("municipio_id", "INTEGER", "", "Não", "FK→municipio.id", "", "Município a que pertence"),
  ("nome", "VARCHAR", "100", "Não", "UK(municipio_id,nome)", "", "Nome do bairro")]),
 ("utilizador", "Contas de acesso (RF-01)", [
  ("id", "UUID", "", "Não", "PK", U, "Identificador"),
  ("nome_completo", "VARCHAR", "120", "Não", "", "", "Nome completo (RF-01.02)"),
  ("telefone", "VARCHAR", "20", "Não", "UK", "", "Telefone em formato E.164, único (RF-01.03)"),
  ("palavra_passe_hash", "VARCHAR", "255", "Não", "", "", "Hash Argon2id/bcrypt (RNF-020)"),
  ("papel", "ENUM papel_utilizador", "", "Não", "", "'utilizador'", "Papel na plataforma (PER-05 = admin)"),
  ("estado", "ENUM estado_conta", "", "Não", "", "'activa'", "Suspensão (RF-11.02)"),
  ("termos_aceites_em", "TIMESTAMPTZ", "", "Não", "", "", "Aceitação dos termos (TEL-02, RNF-026)"),
  ("tentativas_falhadas", "SMALLINT", "", "Não", "", "0", "Contador de logins falhados (RNF-021)"),
  ("bloqueado_ate", "TIMESTAMPTZ", "", "Sim", "", "", "Bloqueio temporário (RNF-021)"),
  ("criado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Data de criação"),
  ("actualizado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Última alteração")]),
 ("codigo_recuperacao", "Códigos OTP de recuperação de palavra-passe (RF-01.07)", [
  ("id", "UUID", "", "Não", "PK", U, "Identificador"),
  ("utilizador_id", "UUID", "", "Não", "FK→utilizador.id", "", "Dono do código"),
  ("codigo_hash", "VARCHAR", "255", "Não", "", "", "Hash do código de 6 dígitos"),
  ("expira_em", "TIMESTAMPTZ", "", "Não", "", "", "Validade ≤ 10 min (RNF-025)"),
  ("tentativas", "SMALLINT", "", "Não", "", "0", "Tentativas usadas (máx. 3)"),
  ("usado_em", "TIMESTAMPTZ", "", "Sim", "", "", "Quando foi usado"),
  ("criado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Data de criação")]),
 ("sessao", "Refresh tokens das sessões (ADR-006) — acrescentada em M3-05", [
  ("id", "UUID", "", "Não", "PK", U, "Identificador"),
  ("utilizador_id", "UUID", "", "Não", "FK→utilizador.id", "", "Dono da sessão"),
  ("refresh_token_hash", "VARCHAR", "255", "Não", "UK", "", "Hash do refresh token (rotativo)"),
  ("cliente", "VARCHAR", "20", "Não", "", "", "web | mobile"),
  ("expira_em", "TIMESTAMPTZ", "", "Não", "", "", "Validade (30 dias)"),
  ("revogada_em", "TIMESTAMPTZ", "", "Sim", "", "", "Logout, recuperação de palavra-passe ou suspensão"),
  ("criado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Início da sessão")]),
 ("dispositivo_push", "Tokens de notificação push da app (M8-06) — acrescentada em M3-05", [
  ("id", "UUID", "", "Não", "PK", U, "Identificador"),
  ("utilizador_id", "UUID", "", "Não", "FK→utilizador.id", "", "Dono do dispositivo"),
  ("token", "VARCHAR", "255", "Não", "UK", "", "Expo push token"),
  ("plataforma", "VARCHAR", "10", "Não", "", "", "android | ios"),
  ("activo", "BOOLEAN", "", "Não", "", "true", "Falso quando o token é rejeitado ou no logout"),
  ("criado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Registo do dispositivo")]),
 ("equipa", "Equipas de bairro (RF-02)", [
  ("id", "UUID", "", "Não", "PK", U, "Identificador"),
  ("nome", "VARCHAR", "80", "Não", "", "", "Nome da equipa"),
  ("nome_normalizado", "VARCHAR", "80", "Não", "UK(nome_normalizado,bairro_id)", "", "Nome sem acentos/maiúsculas para detectar duplicados (RF-02.09)"),
  ("bairro_id", "INTEGER", "", "Não", "FK→bairro.id", "", "Localização (município e província por herança)"),
  ("emblema_url", "VARCHAR", "255", "Sim", "", "", "Emblema (RF-02.04)"),
  ("descricao", "TEXT", "", "Sim", "", "", "Descrição (RF-02.05)"),
  ("visibilidade_plantel", "ENUM visibilidade_plantel", "", "Não", "", "'autenticados'", "Quem vê os nomes dos jogadores (RN-22)"),
  ("estado", "ENUM estado_conta", "", "Não", "", "'activa'", "Suspensão (RF-11.02, RN-19)"),
  ("criado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Data de criação"),
  ("actualizado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Última alteração")]),
 ("membro_equipa", "Responsável da equipa (RN-01, RN-18)", [
  ("utilizador_id", "UUID", "", "Não", "PK, FK→utilizador.id", "", "Utilizador (PK ⇒ no máx. 1 equipa — RN-18)"),
  ("equipa_id", "UUID", "", "Não", "FK→equipa.id", "", "Equipa"),
  ("papel", "ENUM papel_membro", "", "Não", "", "'responsavel'", "Papel na equipa"),
  ("criado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Data de associação")]),
 ("jogador", "Plantel (RF-03)", [
  ("id", "UUID", "", "Não", "PK", U, "Identificador"),
  ("equipa_id", "UUID", "", "Não", "FK→equipa.id", "", "Equipa"),
  ("nome", "VARCHAR", "120", "Não", "", "", "Nome do jogador (RN-03)"),
  ("numero_camisola", "SMALLINT", "", "Não", "", "", "1–99; único entre activos da equipa (índice parcial — RN-04)"),
  ("posicao", "ENUM posicao_jogador", "", "Não", "", "", "Posição (RF-03.07)"),
  ("activo", "BOOLEAN", "", "Não", "", "true", "Activo/inactivo (RF-03.04)"),
  ("criado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Data de criação")]),
 ("contacto_equipa", "Contactos para marcação de jogos (RF-04)", [
  ("id", "UUID", "", "Não", "PK", U, "Identificador"),
  ("equipa_id", "UUID", "", "Não", "FK→equipa.id", "", "Equipa"),
  ("nome", "VARCHAR", "120", "Não", "", "", "Nome do contacto"),
  ("telefone", "VARCHAR", "20", "Não", "", "", "Telefone (visível só a autenticados — RN-17)"),
  ("funcao", "VARCHAR", "60", "Não", "", "", "Função/relação com a equipa"),
  ("principal", "BOOLEAN", "", "Não", "", "false", "Contacto principal; 1 por equipa (índice parcial)")]),
 ("solicitacao_jogo", "Pedidos de jogo (RF-05)", [
  ("id", "UUID", "", "Não", "PK", U, "Identificador"),
  ("equipa_desafiante_id", "UUID", "", "Não", "FK→equipa.id", "", "Quem pede"),
  ("equipa_desafiada_id", "UUID", "", "Não", "FK→equipa.id", "", "Quem recebe (≠ desafiante)"),
  ("data_hora", "TIMESTAMPTZ", "", "Não", "", "", "Data/hora proposta (UTC — RNF-034)"),
  ("local", "VARCHAR", "150", "Não", "", "", "Campo/local proposto"),
  ("equipa_mandante_id", "UUID", "", "Sim", "FK→equipa.id", "", "Mandante, se aplicável (RF-05.11)"),
  ("observacao", "TEXT", "", "Sim", "", "", "Observação opcional"),
  ("estado", "ENUM estado_solicitacao", "", "Não", "", "'pendente'", "Estado da solicitação"),
  ("aguarda_resposta_de_id", "UUID", "", "Sim", "FK→equipa.id", "", "Equipa que tem de responder (muda após alteração)"),
  ("motivo", "TEXT", "", "Sim", "", "", "Motivo de recusa/cancelamento"),
  ("criado_por", "UUID", "", "Não", "FK→utilizador.id", "", "Utilizador que enviou"),
  ("criado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Data de envio"),
  ("actualizado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Última alteração")]),
 ("proposta_alteracao", "Contra-propostas numa solicitação (RF-05.06)", [
  ("id", "UUID", "", "Não", "PK", U, "Identificador"),
  ("solicitacao_id", "UUID", "", "Não", "FK→solicitacao_jogo.id", "", "Solicitação"),
  ("proposta_por_equipa_id", "UUID", "", "Não", "FK→equipa.id", "", "Equipa que propõe"),
  ("data_hora", "TIMESTAMPTZ", "", "Não", "", "", "Nova data/hora"),
  ("local", "VARCHAR", "150", "Não", "", "", "Novo local"),
  ("observacao", "TEXT", "", "Sim", "", "", "Observação"),
  ("criado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Data da proposta")]),
 ("jogo", "Jogos agendados (RF-06)", [
  ("id", "UUID", "", "Não", "PK", U, "Identificador único do jogo (RF-06.01)"),
  ("codigo", "VARCHAR", "12", "Não", "UK", "", "Código curto legível, ex.: GB-2026-00042"),
  ("solicitacao_id", "UUID", "", "Não", "FK→solicitacao_jogo.id, UK", "", "Solicitação que o originou (RN-05)"),
  ("equipa_a_id", "UUID", "", "Não", "FK→equipa.id", "", "Equipa A (mandante, ou desafiante por defeito)"),
  ("equipa_b_id", "UUID", "", "Não", "FK→equipa.id", "", "Equipa B"),
  ("data_hora", "TIMESTAMPTZ", "", "Não", "", "", "Data/hora acordada (UTC)"),
  ("local", "VARCHAR", "150", "Não", "", "", "Campo/local"),
  ("estado", "ENUM estado_jogo", "", "Não", "", "'agendado'", "Estado do jogo"),
  ("estado_resultado", "ENUM estado_resultado", "", "Não", "", "'nao_submetido'", "Estado do resultado oficial"),
  ("golos_a", "SMALLINT", "", "Sim", "", "", "Golos oficiais de A (só quando confirmado)"),
  ("golos_b", "SMALLINT", "", "Sim", "", "", "Golos oficiais de B (só quando confirmado)"),
  ("confirmado_em", "TIMESTAMPTZ", "", "Sim", "", "", "Quando o resultado foi confirmado"),
  ("divergente_desde", "TIMESTAMPTZ", "", "Sim", "", "", "Início do prazo de 72 h (RN-20)"),
  ("realizado_admin", "BOOLEAN", "", "Não", "", "false", "Marcado como realizado pelo admin (RF-06.13)"),
  ("lembrete_enviado_em", "TIMESTAMPTZ", "", "Sim", "", "", "Lembrete (RF-10.04)"),
  ("cancelado_por_equipa_id", "UUID", "", "Sim", "FK→equipa.id", "", "Quem cancelou"),
  ("motivo_cancelamento", "TEXT", "", "Sim", "", "", "Motivo (RF-05.09)"),
  ("cancelado_em", "TIMESTAMPTZ", "", "Sim", "", "", "Quando foi cancelado (RN-24)"),
  ("criado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Data de criação")]),
 ("comparencia", "Comparência declarada por cada equipa (RF-07)", [
  ("id", "UUID", "", "Não", "PK", U, "Identificador"),
  ("jogo_id", "UUID", "", "Não", "FK→jogo.id, UK(jogo_id,equipa_id)", "", "Jogo"),
  ("equipa_id", "UUID", "", "Não", "FK→equipa.id", "", "Equipa a que a comparência se refere"),
  ("estado", "ENUM estado_comparencia", "", "Não", "", "'nao_registada'", "Estado da comparência desta equipa"),
  ("declarou_adversaria", "ENUM declaracao_adversaria", "", "Sim", "", "", "O que esta equipa declarou sobre a adversária"),
  ("observacao", "TEXT", "", "Sim", "", "", "Observação (TEL-16)"),
  ("declarado_por", "UUID", "", "Sim", "FK→utilizador.id", "", "Quem declarou"),
  ("declarado_em", "TIMESTAMPTZ", "", "Sim", "", "", "Quando declarou"),
  ("prazo_resposta_ate", "TIMESTAMPTZ", "", "Sim", "", "", "Fim das 48 h para responder a falta declarada (RN-16)")]),
 ("submissao_resultado", "Versões do resultado submetido por equipa (RF-06.08, RF-08.08)", [
  ("id", "UUID", "", "Não", "PK", U, "Identificador"),
  ("jogo_id", "UUID", "", "Não", "FK→jogo.id", "", "Jogo"),
  ("equipa_id", "UUID", "", "Não", "FK→equipa.id", "", "Equipa que submeteu"),
  ("golos_a", "SMALLINT", "", "Não", "", "", "Golos da equipa A (≥ 0)"),
  ("golos_b", "SMALLINT", "", "Não", "", "", "Golos da equipa B (≥ 0)"),
  ("versao", "SMALLINT", "", "Não", "UK(jogo_id,equipa_id,versao)", "1", "Nº da versão (correcções — RF-06.11)"),
  ("actual", "BOOLEAN", "", "Não", "", "true", "Última versão desta equipa"),
  ("submetido_por", "UUID", "", "Não", "FK→utilizador.id", "", "Quem submeteu"),
  ("criado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Quando submeteu")]),
 ("caso_analise", "Casos para o administrador (RF-08.07, RF-11.03)", [
  ("id", "UUID", "", "Não", "PK", U, "Identificador"),
  ("jogo_id", "UUID", "", "Não", "FK→jogo.id", "", "Jogo em causa"),
  ("tipo", "ENUM tipo_caso", "", "Não", "", "", "Tipo de caso"),
  ("estado", "ENUM estado_caso", "", "Não", "", "'aberto'", "Estado do caso"),
  ("aberto_por_equipa_id", "UUID", "", "Sim", "FK→equipa.id", "", "Equipa que pediu (nulo se automático)"),
  ("motivo", "TEXT", "", "Sim", "", "", "Motivo do pedido"),
  ("decisao", "JSONB", "", "Sim", "", "", "Decisão aplicada (ex.: {golos_a:2, golos_b:1})"),
  ("justificacao", "TEXT", "", "Sim", "", "", "Justificação obrigatória ao resolver (RF-11.04)"),
  ("resolvido_por", "UUID", "", "Sim", "FK→utilizador.id", "", "Administrador"),
  ("criado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Abertura"),
  ("resolvido_em", "TIMESTAMPTZ", "", "Sim", "", "", "Resolução")]),
 ("notificacao", "Notificações internas (RF-10)", [
  ("id", "UUID", "", "Não", "PK", U, "Identificador"),
  ("utilizador_id", "UUID", "", "Não", "FK→utilizador.id", "", "Destinatário"),
  ("tipo", "ENUM tipo_notificacao", "", "Não", "", "", "Tipo de evento"),
  ("mensagem", "VARCHAR", "255", "Não", "", "", "Texto"),
  ("jogo_id", "UUID", "", "Sim", "FK→jogo.id", "", "Jogo relacionado"),
  ("solicitacao_id", "UUID", "", "Sim", "FK→solicitacao_jogo.id", "", "Solicitação relacionada"),
  ("lida_em", "TIMESTAMPTZ", "", "Sim", "", "", "Quando foi lida (nulo = não lida)"),
  ("criado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Criação")]),
 ("registo_auditoria", "Histórico imutável de alterações (RN-12, RF-11.05)", [
  ("id", "BIGINT", "", "Não", "PK", "identity", "Identificador sequencial"),
  ("entidade", "VARCHAR", "40", "Não", "", "", "Tabela afectada (ex.: jogo)"),
  ("entidade_id", "UUID", "", "Não", "", "", "Registo afectado"),
  ("accao", "ENUM accao_auditoria", "", "Não", "", "", "Tipo de acção"),
  ("valor_anterior", "JSONB", "", "Sim", "", "", "Estado antes"),
  ("valor_novo", "JSONB", "", "Sim", "", "", "Estado depois"),
  ("motivo", "TEXT", "", "Sim", "", "", "Justificação (obrigatória em decisao_admin)"),
  ("utilizador_id", "UUID", "", "Sim", "FK→utilizador.id", "", "Autor (nulo = sistema)"),
  ("criado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Momento da alteração")]),
 ("estatistica_equipa", "Cache derivada para ranking e indicadores (RN-11, RNF-005)", [
  ("equipa_id", "UUID", "", "Não", "PK, FK→equipa.id", "", "Equipa"),
  ("jogos_confirmados", "INTEGER", "", "Não", "", "0", "J"),
  ("vitorias", "INTEGER", "", "Não", "", "0", "V"),
  ("empates", "INTEGER", "", "Não", "", "0", "E"),
  ("derrotas", "INTEGER", "", "Não", "", "0", "D"),
  ("pontos", "INTEGER", "", "Não", "", "0", "Pts = 3V + E"),
  ("golos_marcados", "INTEGER", "", "Não", "", "0", "Golos marcados"),
  ("golos_sofridos", "INTEGER", "", "Não", "", "0", "Golos sofridos"),
  ("jogos_agendados", "INTEGER", "", "Não", "", "0", "G (RN-11 §3.1)"),
  ("comparencias", "INTEGER", "", "Não", "", "0", "C"),
  ("faltas_confirmadas", "INTEGER", "", "Não", "", "0", "Faltas confirmadas"),
  ("indice", "NUMERIC", "4,3", "Não", "", "0", "I = 0,6·A + 0,4·Cp"),
  ("estrelas", "SMALLINT", "", "Sim", "", "", "1–5; nulo = 'Nova' (RN-14)"),
  ("actualizado_em", "TIMESTAMPTZ", "", "Não", "", NOW, "Último recálculo")]),
]

CHECKS = [
 ("jogador", "numero_camisola BETWEEN 1 AND 99"),
 ("jogador", "UNIQUE (equipa_id, numero_camisola) WHERE activo — índice parcial (RN-04)"),
 ("contacto_equipa", "UNIQUE (equipa_id) WHERE principal — 1 contacto principal por equipa (RF-04.03)"),
 ("solicitacao_jogo", "equipa_desafiante_id <> equipa_desafiada_id"),
 ("jogo", "equipa_a_id <> equipa_b_id"),
 ("jogo", "(golos_a IS NULL) = (golos_b IS NULL) AND golos_a >= 0 AND golos_b >= 0"),
 ("submissao_resultado", "golos_a >= 0 AND golos_b >= 0"),
 ("submissao_resultado", "UNIQUE (jogo_id, equipa_id) WHERE actual"),
 ("caso_analise", "estado <> 'resolvido' OR (justificacao IS NOT NULL AND resolvido_por IS NOT NULL)"),
 ("registo_auditoria", "Sem UPDATE/DELETE: só INSERT (permissões da BD — RNF-031)"),
 ("registo_auditoria", "accao <> 'decisao_admin' OR motivo IS NOT NULL"),
]


def mermaid():
    def mtype(t):
        return t.replace("ENUM ", "enum_").replace(" ", "_")
    L = ["%% M2-04 — Modelo lógico do GiraBairro (gerado por scripts/modelo_dados.py — não editar à mão)", "erDiagram"]
    rels = []
    for name, _, cols in TABLES:
        L.append(f"    {name} {{")
        for c in cols:
            keys = []
            if "PK" in c[4]: keys.append("PK")
            if "FK" in c[4]: keys.append("FK")
            if "UK" in c[4] and "PK" not in c[4]: keys.append("UK")
            L.append(f"        {mtype(c[1])} {c[0]} {','.join(keys)}".rstrip())
            for part in c[4].split(","):
                part = part.strip()
                if part.startswith("FK→"):
                    tgt = part[3:].split(".")[0]
                    rels.append((tgt, name, c[0], c[3] == "Sim", "PK" in c[4] or "UK" in c[4] and "(" not in c[4]))
        L.append("    }")
    for tgt, src, col, nullable, one in rels:
        left = "|o" if nullable else "||"
        right = "o|" if one else "o{"
        L.append(f'    {tgt} {left}--{right} {src} : "{col}"')
    return "\n".join(L) + "\n"


def dicionario():
    L = ["# Dicionário de Dados — GiraBairro", "", "| Campo | Valor |", "|-------|-------|",
         "| Task | M2-05 (#33) |", "| Versão | 1.0 — 2026-11-08 |",
         "| SGBD de referência | PostgreSQL (tipos `UUID`, `TIMESTAMPTZ`, `JSONB`, `ENUM`) — a confirmar em M3-01 |",
         "| Gerado por | `scripts/modelo_dados.py` (fonte única; também gera o modelo lógico) |", "",
         "Convenções: nomes em `snake_case` português; datas em **UTC** (`TIMESTAMPTZ`) mostradas em WAT (RNF-034); "
         "`UK(a,b)` = unicidade composta; FK com `ON DELETE RESTRICT` salvo indicação.", "",
         f"**{len(TABLES)} tabelas · {sum(len(t[2]) for t in TABLES)} atributos · {len(ENUMS)} enumerações**", "",
         "## Índice", ""]
    L += [f"- [`{t[0]}`](#{t[0].replace('_', '_')}) — {t[1]}" for t in TABLES]
    for name, desc, cols in TABLES:
        L += ["", f"## {name}", "", desc, "",
              "| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |",
              "|--------|----------|------|---------|------|-------|---------|-----------|"]
        for c in cols:
            L.append(f"| `{name}` | `{c[0]}` | {c[1]} | {c[2] or '—'} | {c[3]} | {c[4] or '—'} | "
                     f"{('`'+c[5]+'`') if c[5] else '—'} | {c[6]} |")
        ch = [x[1] for x in CHECKS if x[0] == name]
        if ch:
            L += ["", "Restrições:"] + [f"- `{x}`" if "—" not in x else f"- {x}" for x in ch]
    L += ["", "## Enumerações", "", "| Enum | Valores |", "|------|---------|"]
    L += [f"| `{k}` | {', '.join('`'+v+'`' for v in vs)} |" for k, vs in ENUMS.items()]
    L += ["", "## Correspondência com os estados da especificação (§7)", "",
          "| Especificação | Enum | Valores |", "|---------------|------|---------|",
          "| Solicitação de jogo | `estado_solicitacao` | Pendente → `pendente`; Aceite/Confirmada → `aceite`; Recusada → `recusada`; Alteração proposta → `alteracao_proposta`; Cancelada → `cancelada` |",
          "| Jogo | `estado_jogo` | Agendado → `agendado`; Em aguardo de comparência → `aguarda_comparencia`; Em aguardo de resultado → `aguarda_resultado`; Resultado pendente de confirmação → `resultado_pendente`; Divergência → `divergencia`; Cancelado → `cancelado`; Concluído → `concluido`; Resultado confirmado ⇒ `concluido` + `estado_resultado=confirmado`; acrescentado `em_analise` |",
          "| Comparência por equipa | `estado_comparencia` | Não registada → `nao_registada`; Compareceu (declarado) → `compareceu_declarado`; Falta de comparência (declarada) → `falta_declarada`; Em divergência/análise → `em_analise`; Validada → `validada`; acrescentado `falta_confirmada` (RN-16) |",
          "| Resultado | `estado_resultado` | Não submetido → `nao_submetido`; Aguardando submissão adversária → `aguarda_adversaria`; Confirmado → `confirmado`; Divergente → `divergente`; Em análise administrativa → `em_analise` |"]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "02-modelagem")
    open(os.path.join(root, "src", "mer-logico.mmd"), "w", encoding="utf-8").write(mermaid())
    open(os.path.join(root, "dicionario-dados.md"), "w", encoding="utf-8").write(dicionario())
    print(f"{len(TABLES)} tabelas, {sum(len(t[2]) for t in TABLES)} atributos")
