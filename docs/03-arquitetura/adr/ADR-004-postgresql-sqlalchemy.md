# ADR-004 — PostgreSQL com SQLAlchemy e Alembic

| Campo | Valor |
|-------|-------|
| Estado | ✅ Aceite |
| Data | 2026-11-08 |
| Decisor | Dono do produto + equipa |
| Relacionado | [stack.md](../stack.md) |

## Contexto

O modelo do M2 usa `UUID`, `ENUM`, `JSONB`, índices parciais (RN-04, RF-04.03) e transacções com bloqueio de linha (RNF-035).

## Decisão

Usar **PostgreSQL**, acedido por **SQLAlchemy 2 (async) + asyncpg**, com migrações **Alembic** geradas a partir do dicionário de dados.

## Alternativas consideradas

| Alternativa | Porque não |
|-------------|------------|
| MySQL/MariaDB | Sem índices parciais nem `JSONB` equivalente |
| MongoDB | O domínio é relacional e precisa de transacções e restrições |

## Consequências

- Restrições de negócio garantidas também na BD
- Migrações versionadas no repositório (M5-03)
- Testes de integração com PostgreSQL real (testcontainers)
