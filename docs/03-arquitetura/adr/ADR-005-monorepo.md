# ADR-005 — Monorepo com apps/api, apps/web, apps/mobile e packages/api-client

| Campo | Valor |
|-------|-------|
| Estado | ✅ Aceite |
| Data | 2026-11-08 |
| Decisor | Dono do produto + equipa |
| Relacionado | [stack.md](../stack.md) |

## Contexto

Três aplicações dependem do mesmo contrato; alterações na API devem actualizar os clientes no mesmo PR.

## Decisão

Um único repositório com **pnpm workspaces** (web, mobile, api-client) e `uv` (api).

## Alternativas consideradas

| Alternativa | Porque não |
|-------------|------------|
| Repositórios separados | Contratos dessincronizados; PRs coordenados entre repos |

## Consequências

- CI detecta qual app mudou e corre só os testes necessários
- Um só quadro, um só conjunto de issues e de releases
