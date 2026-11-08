# ADR-001 — Next.js para a interface web

| Campo | Valor |
|-------|-------|
| Estado | ✅ Aceite |
| Data | 2026-11-08 |
| Decisor | Dono do produto + equipa |
| Relacionado | [stack.md](../stack.md) |

## Contexto

O GiraBairro precisa de páginas públicas leves para visitantes em rede móvel lenta (RNF-001/002) e de uma área autenticada interactiva para o responsável de equipa (TEL-05 a TEL-22).

## Decisão

Usar **Next.js (App Router) com TypeScript e Tailwind CSS**, com SSR/ISR nas páginas públicas e PWA.

## Alternativas consideradas

| Alternativa | Porque não |
|-------------|------------|
| React SPA (Vite) | Sem SSR: primeira carga mais pesada e pior SEO das páginas públicas |
| Angular | Mais pesado; menos alinhado com a app React Native |
| Laravel/Blade | Mudaria a linguagem do backend escolhida (FastAPI) |

## Consequências

- Partilha de TypeScript e de conhecimento React com a app (ADR-003)
- Precisa de um servidor Node para SSR (contentor `web`)
- Sessão gerida por rotas do Next.js com cookies HttpOnly (ADR-006)
