# ADR-003 — React Native com Expo para a app móvel

| Campo | Valor |
|-------|-------|
| Estado | ✅ Aceite |
| Data | 2026-11-08 |
| Decisor | Dono do produto + equipa |
| Relacionado | [stack.md](../stack.md) |

## Contexto

O dono do produto decidiu incluir uma app móvel no MVP (decisão 11). O PER-03 usa sobretudo Android e precisa de registar comparência e resultado no campo, com rede instável.

## Decisão

Usar **React Native com Expo** (managed workflow, Expo Router, EAS Build), em TypeScript.

## Alternativas consideradas

| Alternativa | Porque não |
|-------------|------------|
| Flutter | Bom desempenho, mas Dart não é partilhado com a web |
| App nativa Kotlin | Melhor integração, mas exige outra equipa/linguagem |
| Só PWA | Mais simples, mas push e funcionamento offline mais limitados |

## Consequências

- Reutiliza o cliente gerado do OpenAPI e a lógica de dados (TanStack Query)
- Builds e actualizações OTA pela EAS sem máquina Mac/Android dedicada
- M8 passa a must; aumenta o esforço total do MVP
