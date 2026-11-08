# Contrato da API — resumo

| Campo | Valor |
|-------|-------|
| Task | M3-05 (#42) |
| Fonte | [`openapi.yaml`](openapi.yaml) — OpenAPI 3.0.3, validado com `openapi-spec-validator` |
| Gerado por | `scripts/gerar_openapi.py` (enums importados de `scripts/modelo_dados.py`) |
| Base URL | `/v1` |

**60 operações** em 50 caminhos · 50 schemas · todos os grupos RF-01 a RF-11 cobertos.

Ver no navegador: colar o `openapi.yaml` em <https://editor.swagger.io> (ou, a partir da M5-11, abrir `/docs` na API).

## Regras gerais

- `Authorization: Bearer <access_token>`; *Opcional* = funciona sem sessão mas devolve mais dados com sessão (ex.: telefones dos contactos — RN-17).
- 403 sempre que o utilizador não é responsável da equipa / participante do jogo (RN-13), está suspenso, ou não é admin.
- 409 para conflitos de estado (máquinas de estados do M2-08) e 422 para validação/regra de negócio.

## Operações

| Método | Caminho | Resumo | Acesso | Requisitos | Respostas |
|--------|---------|--------|--------|-----------|-----------|
| `POST` | `/auth/registo` | Criar conta | Público | RF-01.01–03, UC01 | 201, 409, 422, 429 |
| `POST` | `/auth/sessoes` | Iniciar sessão | Público | RF-01.04, UC02, RNF-021 | 200, 401, 403, 423, 429 |
| `DELETE` | `/auth/sessoes` | Terminar sessão (revoga o refresh token) | Autenticado | RF-01.05 | 204, 401 |
| `POST` | `/auth/sessoes/renovar` | Renovar tokens (refresh rotativo) | Público | ADR-006 | 200, 401 |
| `POST` | `/auth/recuperacao` | Pedir código de recuperação por SMS | Público | RF-01.07, UC03 | 202, 429 |
| `POST` | `/auth/recuperacao/confirmar` | Confirmar código e definir nova palavra-passe | Público | RF-01.07, RNF-025 | 204, 422, 429 |
| `GET` | `/me` | Dados do utilizador actual | Autenticado | RF-01.06, TEL-21 | 200, 401 |
| `PATCH` | `/me` | Editar dados básicos | Autenticado | RF-01.06 | 200, 401, 422 |
| `POST` | `/me/palavra-passe` | Alterar palavra-passe | Autenticado | TEL-21 | 204, 401, 422 |
| `GET` | `/provincias` | Listar províncias | Público | — | 200 |
| `GET` | `/provincias/{provincia_id}/municipios` | Municípios de uma província | Público | — | 200 |
| `GET` | `/municipios/{municipio_id}/bairros` | Bairros de um município | Público | — | 200 |
| `GET` | `/equipas` | Pesquisar equipas | Opcional | RF-02.08, RF-05.01–02, TEL-10 | 200, 401 |
| `POST` | `/equipas` | Registar equipa | Autenticado | RF-02.01–03, RF-02.09, RN-18, UC04 | 201, 401, 409, 422 |
| `GET` | `/equipas/{equipa_id}` | Perfil público da equipa | Opcional | RF-02.07, RF-04.05, RN-17, RN-22, TEL-11 | 200, 401, 404 |
| `PATCH` | `/equipas/{equipa_id}` | Editar equipa | Autenticado | RF-02.06, RN-02 | 200, 401, 403, 404, 409, 422 |
| `PUT` | `/equipas/{equipa_id}/emblema` | Carregar emblema | Autenticado | RF-02.04, RNF-003 | 200, 401, 403, 422 |
| `GET` | `/equipas/{equipa_id}/jogos` | Histórico de jogos da equipa | Opcional | RF-06.12, RF-07.08 | 200, 401 |
| `GET` | `/equipas/{equipa_id}/jogadores` | Listar jogadores (inclui inactivos) | Autenticado | RF-03.05, TEL-07 | 200, 401, 403 |
| `POST` | `/equipas/{equipa_id}/jogadores` | Adicionar jogador | Autenticado | RF-03.01–02, RN-04 | 201, 401, 403, 409, 422 |
| `PATCH` | `/equipas/{equipa_id}/jogadores/{jogador_id}` | Editar / activar / desactivar jogador | Autenticado | RF-03.03–04 | 200, 401, 403, 404, 409, 422 |
| `DELETE` | `/equipas/{equipa_id}/jogadores/{jogador_id}` | Remover jogador | Autenticado | RF-03.04 | 204, 401, 403, 404 |
| `GET` | `/equipas/{equipa_id}/contactos` | Listar contactos | Autenticado | RF-04, TEL-09 | 200, 401, 403 |
| `POST` | `/equipas/{equipa_id}/contactos` | Adicionar contacto | Autenticado | RF-04.01–03 | 201, 401, 403, 422 |
| `PATCH` | `/equipas/{equipa_id}/contactos/{contacto_id}` | Editar contacto / definir principal | Autenticado | RF-04.03–04 | 200, 401, 403, 404, 422 |
| `DELETE` | `/equipas/{equipa_id}/contactos/{contacto_id}` | Remover contacto | Autenticado | RF-04.04 | 204, 401, 403, 404, 409 |
| `GET` | `/solicitacoes` | Listar solicitações da minha equipa | Autenticado | TEL-13 | 200, 401, 403 |
| `POST` | `/solicitacoes` | Solicitar jogo | Autenticado | RF-05.03–04, RN-19, UC08 | 201, 401, 403, 404, 422, 429 |
| `GET` | `/solicitacoes/{solicitacao_id}` | Detalhe da solicitação | Autenticado | — | 200, 401, 403, 404 |
| `POST` | `/solicitacoes/{solicitacao_id}/aceitar` | Aceitar (cria o jogo) | Autenticado | RF-05.05, RF-05.08, RN-05, UC09 | 200, 401, 403, 404, 409 |
| `POST` | `/solicitacoes/{solicitacao_id}/recusar` | Recusar | Autenticado | RF-05.05 | 200, 401, 403, 404, 409 |
| `POST` | `/solicitacoes/{solicitacao_id}/propostas` | Propor alteração de data/hora/local | Autenticado | RF-05.06 | 201, 401, 403, 404, 409, 422 |
| `POST` | `/solicitacoes/{solicitacao_id}/cancelar` | Cancelar solicitação | Autenticado | RF-05.09, UC10 | 200, 401, 403, 404, 409 |
| `GET` | `/jogos` | Agenda da minha equipa | Autenticado | RF-05.10, TEL-14 | 200, 401, 403 |
| `GET` | `/jogos/{jogo_id}` | Detalhe do jogo | Opcional | RF-06.01–02, TEL-15 | 200, 401, 404 |
| `GET` | `/jogos/{jogo_id}/historico` | Histórico de alterações do jogo | Autenticado | RF-08.08, RN-12, TEL-15 | 200, 401, 403, 404 |
| `POST` | `/jogos/{jogo_id}/cancelar` | Cancelar jogo | Autenticado | RF-05.09, RN-24, UC10 | 200, 401, 403, 404, 409 |
| `PUT` | `/jogos/{jogo_id}/comparencias/minha` | Declarar comparência da minha equipa | Autenticado | RF-06.03–05, RF-07.01–03, RN-06, RN-16, RN-23, UC11 | 200, 401, 403, 404, 409, 422 |
| `POST` | `/jogos/{jogo_id}/comparencias/minha/concordar` | Concordar com a falta declarada pela adversária | Autenticado | RN-16, UC11b | 200, 401, 403, 404, 409 |
| `POST` | `/jogos/{jogo_id}/comparencias/minha/contestar` | Contestar a falta declarada (abre caso) | Autenticado | RF-07.05, RN-16, UC11b | 200, 401, 403, 404, 409 |
| `GET` | `/jogos/{jogo_id}/resultados` | Submissões das duas equipas | Opcional | TEL-18 | 200, 401 |
| `POST` | `/jogos/{jogo_id}/resultados` | Submeter ou corrigir o resultado da minha equipa | Autenticado | RF-06.06–11, RF-08.01–04, RN-08, UC12 | 201, 401, 403, 404, 409, 422 |
| `POST` | `/jogos/{jogo_id}/casos` | Pedir análise ou reabertura ao administrador | Autenticado | RF-08.07, RN-20, RN-21, UC13 | 201, 401, 403, 404, 409 |
| `GET` | `/ranking` | Ranking | Opcional | RF-09, RN-15, TEL-19, UC14 | 200, 401, 422 |
| `GET` | `/ranking/criterios` | Critérios públicos do ranking e das estrelas | Público | RF-09.11, RN-11 | 200 |
| `GET` | `/notificacoes` | Listar notificações | Autenticado | RF-10.07, TEL-20 | 200, 401 |
| `POST` | `/notificacoes/{notificacao_id}/lida` | Marcar como lida | Autenticado | — | 204, 401, 404 |
| `POST` | `/notificacoes/lidas` | Marcar todas como lidas | Autenticado | — | 204, 401 |
| `POST` | `/dispositivos` | Registar dispositivo para push (app) | Autenticado | M8-06 | 204, 401, 422 |
| `GET` | `/dashboard` | Resumo do responsável | Autenticado | TEL-05, M6-12 | 200, 401, 403 |
| `GET` | `/admin/indicadores` | Indicadores gerais | Admin | RF-11.06, TEL-22 | 200, 401, 403 |
| `GET` | `/admin/utilizadores` | Consultar utilizadores | Admin | RF-11.01 | 200, 401, 403 |
| `POST` | `/admin/utilizadores/{utilizador_id}/estado` | Suspender / reactivar utilizador | Admin | RF-11.02, RF-11.05 | 204, 401, 403, 404 |
| `GET` | `/admin/equipas` | Consultar equipas | Admin | RF-11.01 | 200, 401, 403 |
| `POST` | `/admin/equipas/{equipa_id}/estado` | Suspender / reactivar equipa | Admin | RF-11.02, RN-19 | 204, 401, 403, 404 |
| `GET` | `/admin/casos` | Casos para análise | Admin | RF-11.03, TEL-22 | 200, 401, 403 |
| `GET` | `/admin/casos/{caso_id}` | Detalhe do caso | Admin | — | 200, 401, 403, 404 |
| `POST` | `/admin/casos/{caso_id}/resolver` | Resolver caso com decisão e justificação | Admin | RF-11.04–05, RN-20, RN-21, UC17 | 200, 401, 403, 404, 409, 422 |
| `POST` | `/admin/casos/{caso_id}/rejeitar` | Rejeitar caso (ex.: reabertura fora de prazo) | Admin | RN-21 | 200, 401, 403, 404, 409 |
| `POST` | `/admin/jogos/{jogo_id}/marcar-realizado` | Marcar jogo como realizado (reabre a janela de registo) | Admin | RF-06.13, UC22 | 200, 401, 403, 404, 409 |
