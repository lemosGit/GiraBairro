# ADR-007 — Cálculo do ranking com tabela de estatísticas recalculada por evento

| Campo | Valor |
|-------|-------|
| Estado | ✅ Aceite |
| Data | 2026-11-08 |
| Decisor | Dono do produto + equipa |
| Relacionado | [stack.md](../stack.md) |

## Contexto

O ranking tem de reflectir confirmações em ≤ 60 s (RNF-005), em 4 níveis geográficos, e seguir a fórmula da RN-11.

## Decisão

Ao confirmar/corrigir um resultado ou uma falta, a API **recalcula a `estatistica_equipa` das duas equipas na mesma transacção**. O ranking é uma consulta ordenada sobre essa tabela, filtrada por localização.

## Alternativas consideradas

| Alternativa | Porque não |
|-------------|------------|
| Calcular tudo em cada pedido | Lento com muitas equipas |
| Recálculo nocturno em lote | Violaria RNF-005 |
| Vista materializada | Refresh global caro e menos controlável |

## Consequências

- Ranking sempre coerente com os jogos confirmados
- A fórmula vive num só módulo (`CalculadoraRanking`) testado com os exemplos da RN-11
- Comando administrativo para recalcular tudo, se a fórmula mudar
