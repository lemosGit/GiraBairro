# Regras de Negócio — GiraBairro

| Campo | Valor |
|-------|-------|
| Tasks | M1-06 (#21), M1-12 (#23 — secção RN-11) |
| Versão | 1.0 — 2026-11-08 |
| Fontes | Especificação §4 (RN-01 a RN-13); [acta de decisões](../00-gestao/actas/decisoes-mvp.md) (RN-14 a RN-22) |

> Os códigos **RN-NN** da especificação mantêm-se. As regras novas (RN-14+) resultam das decisões da M1-11.

## 1. Regras da especificação (RN-01 a RN-13)

| Código | Regra | RF relacionados | Observação |
|--------|-------|-----------------|-----------|
| RN-01 | Uma equipa deve ter um utilizador responsável associado. | RF-02.02 | Ver RN-18 (uma equipa por conta) |
| RN-02 | O responsável da equipa pode gerir os dados da equipa e o respectivo plantel. | RF-02.06, RF-03 | |
| RN-03 | Cada jogador cadastrado deve possuir nome, número de camisola e posição. | RF-03.02 | Posições: guarda-redes, defesa, médio, avançado (RF-03.07) |
| RN-04 | O número de camisola não pode repetir-se entre jogadores **activos** da mesma equipa. | RF-03.06 | Números de 1 a 99 (proposta) |
| RN-05 | Um jogo só fica confirmado na agenda após aceitação da equipa destinatária. | RF-05.08 | Uma proposta de alteração exige aceitação da equipa que a recebe |
| RN-06 | A comparência de cada equipa é registada separadamente. | RF-06.05, RF-07.01 | |
| RN-07 | Uma declaração unilateral de falta não constitui, por si só, falta confirmada; casos contraditórios são sinalizados ou analisados. | RF-07.03, RF-07.05, RF-07.09 | Procedimento em **RN-16** |
| RN-08 | O resultado oficial só é confirmado quando as duas equipas submetem o mesmo marcador. | RF-06.09, RF-08.03 | Excepção: decisão do administrador (RN-20) |
| RN-09 | Resultados pendentes ou contestados não contam para o ranking. | RF-08.09 | |
| RN-10 | O ranking é calculado a partir dos jogos e resultados confirmados. | RF-09.03 | |
| <a id="rn-11"></a>RN-11 | A classificação por estrelas tem critérios explícitos e transparentes. | RF-09.08, RF-09.11 | **Fórmula na secção 3** (M1-12) |
| RN-12 | Todas as alterações relevantes a jogos, comparências e resultados mantêm histórico. | RF-08.08, RF-11.05 | Histórico imutável (RNF-031) |
| RN-13 | Uma equipa só submete comparência e resultado em jogos em que participa, através do seu responsável. | RF-06.03, RF-06.06 | Verificado no servidor (RNF-023) |

## 2. Regras novas (decisões da M1-11)

| Código | Regra | Decisão | RF relacionados |
|--------|-------|:------:|-----------------|
| RN-14 | Uma equipa só recebe estrelas depois de ter **3 jogos com resultado confirmado**; antes disso aparece como **"Nova"**. | 1 | RF-09.08 |
| RN-15 | Ordem do ranking: **pontos** (V=3, E=1, D=0) → **taxa de comparência** → **saldo de golos** → **golos marcados** → ordem alfabética. | 1 | RF-09.04 |
| RN-16 | Quando uma equipa declara a falta da adversária, a acusada tem **48 h** para **concordar** ou **contestar**. Concordar ou não responder → falta **confirmada**. Contestar → caso **em análise** pelo administrador. | 2 | RF-07.03, RF-07.05, RF-07.09, RF-11.03 |
| RN-17 | Os telefones dos contactos só são visíveis a **utilizadores autenticados**. | 3 | RF-04.05, RF-04.06 |
| RN-18 | Cada conta administra **no máximo uma equipa** no MVP. | 4 | RF-02.01, RF-02.02 |
| RN-19 | Só é possível solicitar jogos a **equipas registadas e activas** (não suspensas). | 5 | RF-05.03, RF-11.02 |
| RN-20 | Em caso de resultado divergente, as equipas têm **72 h** para corrigir. Se persistir, ou se uma equipa pedir análise, o **administrador decide** com justificação; a decisão confirma o resultado. | 6 | RF-08.04–RF-08.07, RF-11.03, RF-11.04 |
| RN-21 | Um resultado confirmado só pode ser **reaberto pelo administrador**, com justificação, a pedido de uma das equipas feito **até 7 dias** após a confirmação. | 7 | RF-11.04 |
| RN-22 | A visibilidade do plantel é **configurável pela equipa**. Por defeito: visitantes vêem número e posição; utilizadores autenticados vêem também o nome. | 9 | RF-03.05, TEL-11 |
| RN-23 | Comparência e resultado só podem ser submetidos **a partir da hora marcada** do jogo e **até 7 dias** depois (salvo intervenção do administrador). | P-3 | RF-06.03, RF-06.13 |
| RN-24 | Cancelar um jogo confirmado com **menos de 24 h** de antecedência conta como **falta de comparência** da equipa que cancela. | P-2 | RF-05.09, RF-07.06 |
| RN-25 | Uma falta confirmada da adversária **não dá pontos** à equipa presente e **não lhe reduz** a taxa de comparência. | P-1 | RF-07.06, RF-09.03 |

> RN-23 a RN-25 vêm dos pressupostos P-1 a P-3 da acta e foram **aprovados** na validação (M1-10).

## 3. RN-11 — Fórmula do ranking e das estrelas (M1-12)

### 3.1 Definições

Considera-se para cada equipa, no âmbito do ranking (geral, província, município ou bairro):

| Símbolo | Definição |
|---------|-----------|
| **J** | Jogos com **resultado confirmado** (RN-08, RN-20) |
| **V, E, D** | Vitórias, empates e derrotas nesses jogos |
| **Pts** | 3·V + 1·E + 0·D |
| **Aproveitamento (A)** | Pts / (3·J) — entre 0 e 1 |
| **Agendados (G)** | Jogos confirmados cuja hora já passou, excluindo os cancelados com ≥ 24 h de antecedência e aqueles em que a **adversária** teve falta confirmada (RN-25) |
| **Compareceu (C)** | Jogos de G em que a equipa **não** tem falta confirmada |
| **Comparência (Cp)** | C / G — entre 0 e 1 (se G = 0, Cp = 1) |
| **Índice (I)** | **0,6 · A + 0,4 · Cp** |

### 3.2 Estrelas

| Estrelas | Índice I | Condição adicional |
|----------|----------|--------------------|
| "Nova" | — | J < 3 (RN-14) |
| ★★★★★ | I ≥ 0,80 | J ≥ 3 |
| ★★★★☆ | 0,65 ≤ I < 0,80 | J ≥ 3 |
| ★★★☆☆ | 0,50 ≤ I < 0,65 | J ≥ 3 |
| ★★☆☆☆ | 0,35 ≤ I < 0,50 | J ≥ 3 |
| ★☆☆☆☆ | I < 0,35 | J ≥ 3 |

As estrelas são **as mesmas em todos os níveis** do ranking (calculadas com todos os jogos da equipa); a **posição** é que varia conforme o filtro.

### 3.3 Ordenação (RN-15)

1. Pts (maior primeiro)
2. Cp (maior primeiro)
3. Saldo de golos (maior primeiro)
4. Golos marcados (maior primeiro)
5. Nome da equipa (ordem alfabética)

Equipas "Novas" aparecem no ranking com a sua posição por pontos, marcadas como "Nova".

### 3.4 Exemplos resolvidos

**Exemplo 1 — equipa forte e séria**
J = 10 (7V, 2E, 1D) → Pts = 23 → A = 23/30 = 0,767
G = 11, C = 11 → Cp = 1,00
I = 0,6·0,767 + 0,4·1,00 = 0,460 + 0,400 = **0,860 → ★★★★★**

**Exemplo 2 — ganha muito mas falta**
J = 8 (6V, 0E, 2D) → Pts = 18 → A = 18/24 = 0,750
G = 12, C = 8 (4 faltas confirmadas) → Cp = 0,667
I = 0,450 + 0,267 = **0,717 → ★★★★☆**
*(Apesar de um aproveitamento quase igual ao exemplo 1, perde uma estrela pelas faltas.)*

**Exemplo 3 — equipa recente**
J = 2 (2V) → **"Nova"** (RN-14), mesmo com A = 1,00.

**Exemplo 4 — desempate**
Equipa X: Pts = 15, Cp = 0,90 · Equipa Y: Pts = 15, Cp = 1,00 → **Y à frente de X** (2.º critério).

**Exemplo 5 — muitas derrotas mas sempre presente**
J = 6 (0V, 1E, 5D) → Pts = 1 → A = 1/18 = 0,056
G = 6, C = 6 → Cp = 1,00
I = 0,033 + 0,400 = **0,433 → ★★☆☆☆**
*(A seriedade garante pelo menos 2 estrelas a quem cumpre sempre.)*

### 3.5 Texto público (para TEL-19)

> **Como funcionam as estrelas?** As estrelas combinam **resultados** (60 %) e **seriedade** (40 %). Os resultados contam 3 pontos por vitória e 1 por empate, só em jogos com o marcador confirmado pelas duas equipas. A seriedade é a percentagem de jogos marcados em que a equipa compareceu. Uma equipa precisa de 3 jogos confirmados para ganhar estrelas. No ranking, quem tem mais pontos fica à frente; em caso de empate, conta a seriedade, depois o saldo de golos e os golos marcados.

### 3.6 Recalcular

O índice e o ranking são recalculados sempre que (RF-09.09, RNF-005): um resultado é confirmado ou corrigido pelo administrador; uma falta é confirmada ou anulada; um jogo é cancelado.
