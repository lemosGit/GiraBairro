# Acta — Decisões pendentes do MVP

| Campo | Valor |
|-------|-------|
| Task | M1-11 (#22) |
| Data | 2026-11-08 |
| Decisor | Dono do produto (lemosGit) |
| Origem | Especificação, secção 9 — "Decisões a definir antes do desenvolvimento" |
| Estado | ✅ Decidido — a confirmar formalmente na validação (M1-10) |

## Decisões

| # | Tema | Decisão | Consequência nos requisitos |
|---|------|---------|-----------------------------|
| 1 | **Estrelas e ranking** | Estrelas de 1 a 5 a partir de um **índice = 60 % aproveitamento + 40 % comparência**; equipa "Nova" até ter 3 jogos confirmados. Ordem do ranking: pontos → comparência → saldo de golos → golos marcados. | Detalhe e exemplos em [`regras-negocio.md`](../../01-requisitos/regras-negocio.md#rn-11) (M1-12). Novas RN-14, RN-15 |
| 2 | **Falta de comparência** | A falta declarada contra a adversária fica **confirmada** se a equipa acusada **concordar** ou **não responder em 48 h**; se **contestar**, o caso vai para **análise do administrador**. | RN-07 detalhada; nova RN-16; estados de comparência "Em divergência/análise" e "Validada" (spec §7) |
| 3 | **Visibilidade dos contactos** | Telefones dos contactos visíveis **só para utilizadores autenticados**; visitantes vêem o nome e "Entrar para ver o contacto". | RF-04.05 detalhado; RNF-024; nova RN-17 |
| 4 | **Equipas por utilizador** | **Uma equipa por conta** no MVP; o modelo de dados fica preparado para N (relação utilizador–equipa com papel). | RF-02.01 com restrição; nova RN-18; M2-03 deve prever a relação |
| 5 | **Jogos com equipas não registadas** | **Só entre equipas registadas** na plataforma. | RF-05.03 restrito a equipas activas; nova RN-19 |
| 6 | **Resultado divergente** | As equipas têm **72 h** para corrigir; se a divergência persistir, ou se uma equipa **pedir análise**, o **administrador decide** com justificação. Até à decisão o jogo **não conta** para o ranking. | RF-08.04–08.07 detalhados; nova RN-20; RN-09 mantém-se |
| 7 | **Reabrir resultado confirmado** | Só o **administrador** pode reabrir/corrigir, com justificação registada, a pedido de uma equipa até **7 dias** após a confirmação. | RF-11.04; nova RN-21 |
| 8 | **Níveis do ranking** | **Geral, por província, por município e por bairro**. | RF-09.01, RF-09.02, RF-09.10 confirmados |
| 9 | **Visibilidade do plantel** | **Configurável pela equipa**. Por defeito: visitantes vêem **número e posição**; utilizadores autenticados vêem também o **nome**. | RF-03 ganha campo de visibilidade; TEL-11; nova RN-22 |
| 10 | **Canal de notificações** | Notificações **só internas** no MVP; **SMS apenas para o código de recuperação** de palavra-passe. WhatsApp fica para versão futura. | RF-10.07; M6-14 mantém-se *could*; M3-08 foca em SMS/OTP |

## Pressupostos a confirmar na validação (M1-10)

| # | Pressuposto | Motivo |
|---|-------------|--------|
| P-1 | Um jogo em que a adversária faltou (falta confirmada) **não atribui pontos** à equipa presente, mas também **não a penaliza** na comparência. | A especificação não define vitória por falta de comparência (W.O.); evita equipas a "ganhar" jogos sem jogar. |
| P-2 | Cancelar um jogo confirmado com **menos de 24 h** de antecedência conta como **falta** da equipa que cancela. | Seriedade (objectivo OBJ-04) sem penalizar cancelamentos atempados. |
| P-3 | As submissões de comparência e resultado só ficam disponíveis **a partir da hora marcada** do jogo e até **7 dias** depois. | RF-06.03 / RF-06.13 exigem "após a data do jogo"; o limite evita registos tardios. |

## Impacto no backlog

- Issue #23 (M1-12) desbloqueada; fórmula definida.
- M6-14 (SMS/WhatsApp) mantém prioridade *could* (decisão 10).
- M3-06 (segurança) deve incluir as regras de visibilidade das decisões 3 e 9.
- M2-03 (MER) deve modelar: prazo de resposta da falta (48 h), prazo de correcção da divergência (72 h), janela de reabertura (7 dias), visibilidade do plantel.
