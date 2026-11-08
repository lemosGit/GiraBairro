# ADR-002 — FastAPI para a API

| Campo | Valor |
|-------|-------|
| Estado | ✅ Aceite |
| Data | 2026-11-08 |
| Decisor | Dono do produto + equipa |
| Relacionado | [stack.md](../stack.md) |

## Contexto

Web e app consomem a mesma API. O contrato tem de ser explícito (M3-05) e a API tem de ser rápida (RNF-004) e bem validada.

## Decisão

Usar **FastAPI (Python)** com Pydantic, gerindo dependências com `uv`.

## Alternativas consideradas

| Alternativa | Porque não |
|-------------|------------|
| NestJS (TypeScript) | Uma só linguagem, mas não foi a escolha do dono do produto |
| Django REST | Painel admin pronto, mas mais pesado e síncrono por defeito |
| Spring Boot | Mais configuração para um MVP |

## Consequências

- OpenAPI gerado automaticamente → cliente TypeScript gerado para web e app
- Duas linguagens no projecto; fronteira pelo contrato
- Python facilita futuras análises de dados (rankings, estatísticas)
