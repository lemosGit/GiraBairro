# ADR-008 — Worker Python com APScheduler e advisory lock

| Campo | Valor |
|-------|-------|
| Estado | ✅ Aceite |
| Data | 2026-11-08 |
| Decisor | Dono do produto + equipa |
| Relacionado | [stack.md](../stack.md) |

## Contexto

Os prazos de 48 h (RN-16) e 72 h (RN-20) e os lembretes (RF-10.04) exigem processamento periódico (UC19).

## Decisão

Um processo **worker** (mesma base de código da API) corre **APScheduler a cada 15 min**; cada execução obtém um *advisory lock* do PostgreSQL para nunca correr em duplicado.

## Alternativas consideradas

| Alternativa | Porque não |
|-------------|------------|
| Celery + Redis | Mais infra-estrutura para pouco volume |
| Cron do sistema | Menos portável entre ambientes |
| Verificar prazos só quando alguém abre o jogo | Notificações e ranking atrasados |

## Consequências

- Sem Redis no MVP
- Tarefas idempotentes e auditadas com autor 'sistema'
- Se o volume crescer, migra-se para uma fila (ARQ/Celery) sem mudar o domínio
