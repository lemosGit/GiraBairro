# Revisão Cruzada da Modelagem — GiraBairro

| Campo | Valor |
|-------|-------|
| Task | M2-09 (#37) |
| Data | 2026-11-08 |
| Método | Verificação automática por script (nomes de entidades, tabelas, classes, estados × enums) + revisão manual da checklist |
| Resultado | ✅ Consistente — sem divergências por resolver |

## 1. Verificações automáticas

| Verificação | Resultado |
|-------------|-----------|
| Estados de `estados-solicitacao` = enum `estado_solicitacao` | ✅ 5/5, sem diferenças |
| Estados de `estados-jogo` = enum `estado_jogo` | ✅ 8/8, sem diferenças |
| Estados de `estados-comparencia` = enum `estado_comparencia` | ✅ 6/6, sem diferenças |
| Estados de `estados-resultado` = enum `estado_resultado` | ✅ 5/5, sem diferenças |
| Entidades do MER conceptual ↔ tabelas do modelo lógico | ✅ 17/17; `estatistica_equipa` só no lógico — **intencional** (cache derivada, RNF-005) |
| Modelo lógico ↔ dicionário de dados | ✅ Gerados da mesma fonte (`scripts/modelo_dados.py`) — 18 tabelas, 152 atributos |
| Classes ↔ tabelas | ✅ ver justificações abaixo |

### Diferenças classes ↔ tabelas (justificadas)

| Elemento | Onde existe | Justificação |
|----------|-------------|--------------|
| `CalculadoraRanking`, `ServicoNotificacoes` | Só classes | Serviços sem estado persistente |
| `provincia`, `municipio` | Só tabelas | Representados por `Bairro.municipio()`/`provincia()` (objectos de valor de localização) |
| `membro_equipa` | Só tabela | Implementa a associação `Utilizador "1" -- "0..1" Equipa` (RN-18) |
| `codigo_recuperacao` | Só tabela | Infra-estrutura de autenticação (fora do modelo de domínio) |

## 2. Checklist (roteiro §11.7 + Gate M2)

| # | Item | Estado |
|---|------|:------:|
| 1 | Cada caso de uso **Must** do fluxo central tem diagrama de sequência (UC02, UC08/09, UC11/11b/19, UC12, UC13/17) | ✅ |
| 2 | Os restantes UC Must são CRUD simples cobertos por US com critérios de aceitação | ✅ |
| 3 | MER, classes e dicionário consistentes (secção 1) | ✅ |
| 4 | Nomes iguais aos da documentação (PER-0X, RF, RN, UC, entidades) | ✅ |
| 5 | Cardinalidades: Jogo 1—2 Comparência; Jogo 1—N Submissão; Utilizador 1—0..1 Equipa | ✅ |
| 6 | Todas as RN com impacto em dados têm suporte no modelo (ver tabela "Regra → modelo" no [MER](mer/README.md)) | ✅ |
| 7 | Todos os diagramas têm fonte editável (`src/*.mmd`) + imagem (`img/*.png` e `.svg`) | ✅ 16 diagramas |
| 8 | Legível em A4: casos de uso divididos em 3 pacotes; MER lógico e classes em alta resolução (SVG disponível) | ✅ |
| 9 | Endpoints das sequências marcados como provisórios até à M3-05 | ✅ |

## 3. Pontos passados ao M3

1. Confirmar **PostgreSQL** (tipos `UUID`, `JSONB`, `ENUM`, índices parciais) na M3-01.
2. Contrato OpenAPI (M3-05) a partir dos endpoints provisórios das sequências.
3. Estratégia de **tarefas agendadas** (prazos 48 h/72 h, lembretes) e de **eventos** (notificações, ranking).
4. Permissões da BD para a auditoria imutável (RNF-031) na M3-06.
