# Padrão Arquitectural do Backend — GiraBairro (FastAPI)

| Campo | Valor |
|-------|-------|
| Task | M3-04 (#41) |
| Versão | 1.0 — 2026-11-08 |
| Base | [Diagrama de classes](../02-modelagem/diagrama-classes/README.md), [ADR-002](adr/ADR-002-fastapi-api.md), [ADR-004](adr/ADR-004-postgresql-sqlalchemy.md) |

## 1. Padrão: monólito modular em camadas

A API é **um único serviço**, dividido em **módulos de negócio** (um por grupo de RF, igual às issues do M6). Cada módulo tem **4 camadas** com dependências num só sentido:

```
router (HTTP)  →  service (casos de uso)  →  domain (regras puras)
                         ↓
                  repository (SQLAlchemy)  →  PostgreSQL
```

| Camada | Responsabilidade | Pode depender de | Não pode |
|--------|------------------|------------------|----------|
| `router.py` | Rotas FastAPI, validação de entrada/saída (schemas Pydantic), códigos HTTP, autenticação/autorização por dependência | `service`, `schemas` | Aceder à BD directamente |
| `service.py` | Orquestra um caso de uso (UC): abre transacção, chama repositórios e regras de domínio, regista auditoria, emite eventos | `domain`, `repository`, `core` | Conhecer HTTP |
| `domain.py` | Entidades e **regras de negócio puras** (RN-04, RN-08, RN-11, RN-16…), sem I/O — testáveis sem BD | nada (só biblioteca padrão) | Importar FastAPI ou SQLAlchemy |
| `repository.py` | Consultas SQLAlchemy, `SELECT … FOR UPDATE`, paginação | `models` | Regras de negócio |
| `models.py` | Tabelas SQLAlchemy (espelho do [dicionário de dados](../02-modelagem/dicionario-dados.md)) | — | — |
| `schemas.py` | Modelos Pydantic de pedido/resposta (fonte do OpenAPI) | — | — |

**Porquê:** as regras do GiraBairro (confirmação bilateral, prazos, fórmula das estrelas) são o valor do produto; isolá-las em `domain.py` permite testá-las exaustivamente (exemplos da RN-11, máquinas de estados do M2-08) sem base de dados, e mudar a camada HTTP ou a BD sem lhes tocar.

## 2. Módulos

| Módulo | RF | Issue M6 | Classes de domínio |
|--------|----|----------|--------------------|
| `auth` | RF-01.01–05, 01.07 | M5-05, M5-06 | Utilizador, CodigoRecuperacao, Sessao |
| `utilizadores` | RF-01.06 | M6-01 | Utilizador |
| `localizacao` | RF-02.03 | M5-04 (seeds) | Provincia, Municipio, Bairro |
| `equipas` | RF-02 | M6-02 | Equipa, MembroEquipa |
| `jogadores` | RF-03 | M6-03 | Jogador |
| `contactos` | RF-04 | M6-04 | ContactoEquipa |
| `solicitacoes` | RF-05.01–08 | M6-05 | SolicitacaoJogo, PropostaAlteracao |
| `jogos` | RF-05.09–11, RF-06.01–02, 06.12–13 | M6-06 | Jogo |
| `comparencias` | RF-06.03–05, RF-07 | M6-07 | Comparencia |
| `resultados` | RF-06.06–11, RF-08 | M6-08 | SubmissaoResultado |
| `ranking` | RF-09 | M6-09 | EstatisticaEquipa, CalculadoraRanking |
| `notificacoes` | RF-10 | M6-10 | Notificacao, ServicoNotificacoes |
| `admin` | RF-11 | M6-11 | CasoAnalise |
| `dashboard` | TEL-05 | M6-12 | (consulta agregada) |

> `jogos`, `comparencias` e `resultados` partilham o **agregado `Jogo`** (M2-06): as alterações de comparência e resultado passam sempre por métodos que validam o estado do jogo.

## 3. Estrutura de pastas (`apps/api`)

```
apps/api/
├── pyproject.toml            ← dependências (uv), ruff, mypy, pytest
├── alembic.ini
├── migrations/               ← Alembic (M5-03)
├── app/
│   ├── main.py               ← cria a app FastAPI, regista routers e middlewares
│   ├── core/
│   │   ├── config.py         ← definições por ambiente (pydantic-settings) — M3-07
│   │   ├── database.py       ← engine async, sessão por pedido, transacções
│   │   ├── security.py       ← Argon2id, JWT, refresh tokens — ADR-006
│   │   ├── deps.py           ← dependências: utilizador_actual, exige_responsavel(equipa), exige_admin
│   │   ├── errors.py         ← excepções de domínio → respostas HTTP padrão (M5-07)
│   │   ├── auditoria.py      ← registar(entidade, antes, depois, motivo) — M5-09
│   │   ├── eventos.py        ← barramento de eventos em memória (resultado_confirmado, …)
│   │   ├── relogio.py        ← "agora" injectável (testes de prazos)
│   │   └── logging.py        ← logs JSON + Sentry
│   ├── modules/
│   │   ├── equipas/
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   ├── service.py
│   │   │   ├── domain.py
│   │   │   ├── repository.py
│   │   │   └── models.py
│   │   ├── jogos/ …          ← (mesma estrutura em todos os módulos da secção 2)
│   │   └── ranking/ …
│   ├── integrations/
│   │   ├── sms.py            ← interface EnviadorSMS + implementações (M3-08)
│   │   ├── push.py           ← Expo Push
│   │   └── storage.py        ← S3 / MinIO
│   └── worker/
│       ├── main.py           ← APScheduler + advisory lock — ADR-008
│       └── tarefas.py        ← expirar_faltas(), expirar_divergencias(), enviar_lembretes()
└── tests/
    ├── unit/                 ← domain.py de cada módulo (sem BD)
    ├── integration/          ← serviços + PostgreSQL (testcontainers)
    └── api/                  ← rotas via httpx (contrato, códigos HTTP, autorização)
```

## 4. Convenções transversais

| Tema | Convenção |
|------|-----------|
| Transacções | Uma transacção por pedido de escrita, aberta no `service`; auditoria e estatísticas na **mesma** transacção (RN-12, ADR-007) |
| Concorrência | `repository.obter_jogo_para_actualizar(id)` usa `SELECT … FOR UPDATE` (RNF-035) |
| Erros | Excepções de domínio (`RegraNegocioViolada`, `EstadoInvalido`, `NaoAutorizado`, `NaoEncontrado`) → `422`, `409`, `403`, `404` com corpo padrão `{codigo, mensagem, detalhes}` |
| Autorização | Dependências FastAPI por rota: `exige_responsavel_da_equipa`, `exige_participante_do_jogo` (RN-13), `exige_admin` |
| Tempo | Datas em UTC; `relogio.agora()` injectável para testar prazos de 48 h/72 h/7 dias |
| Eventos | `eventos.publicar("resultado_confirmado", jogo)` → subscritores: `ranking.recalcular`, `notificacoes.criar` (síncronos no MVP) |
| Paginação | `?pagina=&tamanho=` (máx. 50), resposta `{itens, total, pagina}` |
| Nomes | Código e BD em português `snake_case`, iguais ao dicionário de dados |

## 5. Frontends

| App | Estrutura | Notas |
|-----|-----------|-------|
| `apps/web` (Next.js) | `app/(publico)/…`, `app/(responsavel)/…`, `app/(admin)/…`, `components/`, `lib/api.ts` | Grupos de rotas por persona (M7-05) |
| `apps/mobile` (Expo) | `app/(auth)/…`, `app/(tabs)/inicio|jogos|ranking|notificacoes|perfil`, `components/`, `lib/api.ts` | Separadores definidos em M8-04 |
| `packages/api-client` | Gerado de `openapi.yaml` | Nunca editado à mão |
