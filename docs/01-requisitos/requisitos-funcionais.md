# Requisitos Funcionais — GiraBairro

| Campo | Valor |
|-------|-------|
| Task | M1-04 (#19) |
| Versão | 1.0 — 2026-11-08 |
| Fonte | [`GiraBairro_MVP_Requisitos_Funcionais_Telas.md`](../../GiraBairro_MVP_Requisitos_Funcionais_Telas.md), secção 3 |
| Personas | [personas.md](personas.md) |

> Os códigos **RF-XX.YY** da especificação mantêm-se (o roteiro sugere `RF-001`, mas renumerar quebraria a rastreabilidade com a especificação já aprovada). A coluna **Prioridade** foi preenchida na M1-07 — ver [priorizacao-moscow.md](priorizacao-moscow.md).

## Resumo por módulo

| Grupo | Módulo | Nº RF | Persona principal | Telas |
|-------|--------|:----:|-------------------|-------|
| RF-01 | Registo e autenticação de utilizadores | 7 | PER-02 | TEL-02, TEL-03, TEL-21 |
| RF-02 | Registo e gestão de equipa | 9 | PER-03 | TEL-04, TEL-06, TEL-10, TEL-11 |
| RF-03 | Gestão de jogadores | 7 | PER-03 | TEL-07, TEL-08 |
| RF-04 | Contactos responsáveis da equipa | 6 | PER-03 | TEL-09, TEL-11 |
| RF-05 | Descoberta e solicitação de jogos | 11 | PER-03 | TEL-10, TEL-12, TEL-13, TEL-14 |
| RF-06 | Gestão de jogos | 13 | PER-03 | TEL-14, TEL-15, TEL-16, TEL-17 |
| RF-07 | Comparência e seriedade das equipas | 9 | PER-03 | TEL-15, TEL-16 |
| RF-08 | Confirmação de resultados e divergências | 9 | PER-03 | TEL-17, TEL-18, TEL-22 |
| RF-09 | Ranking de equipas e estrelas | 11 | PER-01, PER-03 | TEL-05, TEL-11, TEL-19 |
| RF-10 | Notificações essenciais | 7 | PER-03 | TEL-20 |
| RF-11 | Administração básica da plataforma | 6 | PER-05 | TEL-22 |
| | **Total** | **95** | | |


## RF-01 — Registo e autenticação de utilizadores

| Código | Descrição | Persona | Prioridade | Origem |
|--------|-----------|---------|------------|--------|
| RF-01.01 | O sistema deve permitir que um utilizador crie uma conta. | PER-02 | Must | Especificação §3 |
| RF-01.02 | O sistema deve solicitar nome completo, telefone e palavra-passe no registo. | PER-02 | Must | Especificação §3 |
| RF-01.03 | O sistema deve validar que o telefone não está associado a outra conta. | PER-02 | Must | Especificação §3 |
| RF-01.04 | O sistema deve permitir ao utilizador iniciar sessão. | PER-02, PER-03, PER-05 | Must | Especificação §3 |
| RF-01.05 | O sistema deve permitir terminar sessão. | PER-02, PER-03, PER-05 | Must | Especificação §3 |
| RF-01.06 | O sistema deve permitir ao utilizador consultar e editar os seus dados básicos. | PER-02, PER-03 | Should | Especificação §3 |
| RF-01.07 | O sistema deve permitir recuperar ou redefinir a palavra-passe. | PER-02 | Must | Especificação §3 |

## RF-02 — Registo e gestão de equipa

| Código | Descrição | Persona | Prioridade | Origem |
|--------|-----------|---------|------------|--------|
| RF-02.01 | O sistema deve permitir ao utilizador autenticado registar uma equipa. | PER-03 | Must | Especificação §3 |
| RF-02.02 | O sistema deve associar automaticamente o utilizador criador à equipa como Administrador/Responsável. | PER-03 | Must | Especificação §3 |
| RF-02.03 | O sistema deve solicitar nome da equipa, bairro, município, província e contacto principal. | PER-03 | Must | Especificação §3 |
| RF-02.04 | O sistema deve permitir inserir o emblema da equipa, caso disponível. | PER-03 | Should | Especificação §3 |
| RF-02.05 | O sistema deve permitir inserir a descrição da equipa, caso disponível. | PER-03 | Could | Especificação §3 |
| RF-02.06 | O sistema deve permitir editar os dados da equipa ao seu responsável. | PER-03 | Must | Especificação §3 |
| RF-02.07 | O sistema deve apresentar o perfil público da equipa. | PER-01, PER-03 | Must | Especificação §3 |
| RF-02.08 | O sistema deve permitir pesquisar equipas por nome e localização. | PER-01, PER-02, PER-03 | Must | Especificação §3 |
| RF-02.09 | O sistema deve impedir a criação de duplicados evidentes, por exemplo nome da equipa e bairro iguais, sujeito à validação definida pelo sistema. | PER-03 | Should | Especificação §3 |

## RF-03 — Gestão de jogadores

| Código | Descrição | Persona | Prioridade | Origem |
|--------|-----------|---------|------------|--------|
| RF-03.01 | O responsável deve poder cadastrar jogadores na equipa. | PER-03 | Must | Especificação §3 |
| RF-03.02 | O cadastro do jogador deve conter, no mínimo, nome, número de camisola e posição. | PER-03 | Must | Especificação §3 |
| RF-03.03 | O sistema deve permitir editar os dados de um jogador. | PER-03 | Must | Especificação §3 |
| RF-03.04 | O sistema deve permitir remover ou desativar um jogador do plantel. | PER-03 | Must | Especificação §3 |
| RF-03.05 | O sistema deve apresentar a lista de jogadores da equipa. | PER-03 | Must | Especificação §3 |
| RF-03.06 | O sistema deve validar que o número de camisola não está repetido no plantel ativo da mesma equipa. | PER-03 | Must | Especificação §3 |
| RF-03.07 | O sistema deve permitir definir posições, por exemplo guarda-redes, defesa, médio e avançado. | PER-03 | Must | Especificação §3 |

## RF-04 — Contactos responsáveis da equipa

| Código | Descrição | Persona | Prioridade | Origem |
|--------|-----------|---------|------------|--------|
| RF-04.01 | O responsável da equipa deve poder indicar um ou mais contactos para receber chamadas e pedidos de marcação. | PER-03 | Must | Especificação §3 |
| RF-04.02 | Cada contacto deve conter nome, telefone e função ou relação com a equipa. | PER-03 | Must | Especificação §3 |
| RF-04.03 | O responsável deve poder definir um contacto como principal. | PER-03 | Should | Especificação §3 |
| RF-04.04 | O responsável deve poder editar ou remover contactos. | PER-03 | Must | Especificação §3 |
| RF-04.05 | O perfil público da equipa deve apresentar os contactos autorizados para marcação de jogos. | PER-01, PER-03, PER-04 | Must | Especificação §3 |
| RF-04.06 | O sistema deve permitir que a equipa seja contactada por outras equipas através dos contactos definidos. | PER-03, PER-04 | Must | Especificação §3 |

## RF-05 — Descoberta e solicitação de jogos

| Código | Descrição | Persona | Prioridade | Origem |
|--------|-----------|---------|------------|--------|
| RF-05.01 | O sistema deve permitir consultar equipas disponíveis para marcar jogos. | PER-01, PER-03 | Must | Especificação §3 |
| RF-05.02 | O sistema deve permitir filtrar equipas por bairro, município ou província. | PER-01, PER-03 | Must | Especificação §3 |
| RF-05.03 | O responsável deve poder enviar uma solicitação de jogo a outra equipa. | PER-03 | Must | Especificação §3 |
| RF-05.04 | A solicitação deve conter equipa desafiante, equipa desafiada, data proposta, hora proposta, local/campo e observação opcional. | PER-03 | Must | Especificação §3 |
| RF-05.05 | A equipa destinatária deve poder aceitar ou recusar a solicitação. | PER-03 | Must | Especificação §3 |
| RF-05.06 | A equipa destinatária deve poder propor uma nova data, hora ou local. | PER-03 | Should | Especificação §3 |
| RF-05.07 | O sistema deve informar ambas as equipas sobre o estado da solicitação. | PER-03 | Must | Especificação §3 |
| RF-05.08 | O sistema deve criar o jogo como confirmado apenas após aceitação da equipa destinatária. | PER-03 | Must | Especificação §3 |
| RF-05.09 | O sistema deve permitir cancelar um jogo confirmado, indicando o motivo. | PER-03 | Must | Especificação §3 |
| RF-05.10 | O sistema deve permitir consultar jogos pendentes, confirmados, concluídos e cancelados. | PER-03 | Must | Especificação §3 |
| RF-05.11 | O sistema deve identificar a equipa mandante e a equipa visitante, quando aplicável. | PER-03 | Could | Especificação §3 |

## RF-06 — Gestão de jogos

| Código | Descrição | Persona | Prioridade | Origem |
|--------|-----------|---------|------------|--------|
| RF-06.01 | O sistema deve atribuir um identificador único a cada jogo. | PER-03 | Must | Especificação §3 |
| RF-06.02 | O sistema deve apresentar os detalhes do jogo às duas equipas. | PER-03 | Must | Especificação §3 |
| RF-06.03 | O sistema deve permitir que cada equipa registe a sua comparência após a data do jogo. | PER-03 | Must | Especificação §3 |
| RF-06.04 | A comparência deve ter pelo menos os estados: compareceu, falta de comparência ou ainda não registada. | PER-03 | Must | Especificação §3 |
| RF-06.05 | O sistema deve guardar separadamente a comparência declarada por cada equipa. | PER-03 | Must | Especificação §3 |
| RF-06.06 | O sistema deve permitir registar o resultado do jogo por cada equipa. | PER-03 | Must | Especificação §3 |
| RF-06.07 | O resultado deve conter golos da equipa A e golos da equipa B. | PER-03 | Must | Especificação §3 |
| RF-06.08 | O sistema deve guardar separadamente os resultados declarados pelas duas equipas. | PER-03 | Must | Especificação §3 |
| RF-06.09 | O sistema deve considerar o resultado confirmado quando os valores submetidos pelas duas equipas forem iguais. | PER-03 | Must | Especificação §3 |
| RF-06.10 | O sistema deve marcar o resultado como pendente de confirmação quando os valores forem diferentes ou só uma equipa tiver submetido. | PER-03 | Must | Especificação §3 |
| RF-06.11 | O sistema deve permitir corrigir um resultado submetido antes da confirmação bilateral. | PER-03 | Must | Especificação §3 |
| RF-06.12 | O sistema deve permitir consultar o histórico de jogos de cada equipa. | PER-01, PER-03 | Must | Especificação §3 |
| RF-06.13 | O sistema deve impedir o registo de resultado antes da data do jogo, exceto se o jogo for explicitamente marcado como já realizado por um administrador autorizado. | PER-03, PER-05 | Should | Especificação §3 |

## RF-07 — Comparência e seriedade das equipas

| Código | Descrição | Persona | Prioridade | Origem |
|--------|-----------|---------|------------|--------|
| RF-07.01 | O sistema deve registar a comparência de cada equipa separadamente. | PER-03 | Must | Especificação §3 |
| RF-07.02 | O sistema deve permitir que uma equipa declare que compareceu. | PER-03 | Must | Especificação §3 |
| RF-07.03 | O sistema deve permitir que uma equipa declare que a adversária faltou, associando essa declaração ao seu próprio registo de comparência. | PER-03 | Must | Especificação §3 |
| RF-07.04 | O sistema deve apresentar o estado de comparência das duas equipas. | PER-03 | Must | Especificação §3 |
| RF-07.05 | O sistema deve sinalizar casos em que as declarações de comparência são contraditórias. | PER-03 | Must | Especificação §3 |
| RF-07.06 | O sistema deve calcular indicadores de comparência a partir dos jogos registados. | PER-03 | Must | Especificação §3 |
| RF-07.07 | O sistema deve apresentar o número de jogos agendados, jogos em que compareceu e faltas de comparência da equipa. | PER-03 | Must | Especificação §3 |
| RF-07.08 | O sistema deve permitir consultar o histórico de comparência. | PER-01, PER-03 | Should | Especificação §3 |
| RF-07.09 | O sistema deve evitar que uma única declaração unilateral seja tratada automaticamente como falta confirmada da adversária. | PER-03 | Must | Especificação §3 |

## RF-08 — Confirmação de resultados e divergências

| Código | Descrição | Persona | Prioridade | Origem |
|--------|-----------|---------|------------|--------|
| RF-08.01 | O sistema deve exigir a submissão do resultado pelas duas equipas. | PER-03 | Must | Especificação §3 |
| RF-08.02 | O sistema deve comparar automaticamente os resultados submetidos. | PER-03 | Must | Especificação §3 |
| RF-08.03 | O sistema deve confirmar o resultado quando os dois registos forem iguais. | PER-03 | Must | Especificação §3 |
| RF-08.04 | O sistema deve manter o resultado pendente quando os registos forem diferentes. | PER-03 | Must | Especificação §3 |
| RF-08.05 | O sistema deve notificar ambas as equipas sobre uma divergência. | PER-03 | Must | Especificação §3 |
| RF-08.06 | O sistema deve permitir que as equipas atualizem os seus registos para resolver a divergência. | PER-03 | Must | Especificação §3 |
| RF-08.07 | O sistema deve permitir encaminhar uma divergência para análise do administrador da plataforma. | PER-03, PER-05 | Must | Especificação §3 |
| RF-08.08 | O sistema deve guardar o histórico das submissões e alterações do resultado. | PER-03 | Must | Especificação §3 |
| RF-08.09 | O sistema deve utilizar apenas resultados confirmados no cálculo do ranking de vitórias. | PER-03 | Must | Especificação §3 |

## RF-09 — Ranking de equipas e estrelas

| Código | Descrição | Persona | Prioridade | Origem |
|--------|-----------|---------|------------|--------|
| RF-09.01 | O sistema deve gerar um ranking de equipas por localização. | PER-01, PER-03 | Must | Especificação §3 |
| RF-09.02 | O sistema deve permitir consultar ranking por bairro, município e província. | PER-01, PER-03 | Must | Especificação §3 |
| RF-09.03 | O sistema deve calcular o número de vitórias a partir dos resultados confirmados. | PER-01, PER-03 | Must | Especificação §3 |
| RF-09.04 | O sistema deve ordenar as equipas segundo os critérios de ranking definidos. | PER-01, PER-03 | Must | Especificação §3 |
| RF-09.05 | O sistema deve apresentar a posição da equipa no ranking. | PER-01, PER-03 | Must | Especificação §3 |
| RF-09.06 | O sistema deve apresentar o número de vitórias, empates e derrotas da equipa. | PER-01, PER-03 | Must | Especificação §3 |
| RF-09.07 | O sistema deve apresentar indicadores de comparência e faltas de comparência. | PER-01, PER-03 | Must | Especificação §3 |
| RF-09.08 | O sistema deve representar o nível ou classificação da equipa por estrelas. | PER-01, PER-03 | Must | Especificação §3 |
| RF-09.09 | O sistema deve atualizar o ranking quando um resultado for confirmado ou quando uma comparência for validada. | PER-01, PER-03 | Must | Especificação §3 |
| RF-09.10 | O sistema deve permitir consultar o ranking geral e os rankings locais. | PER-01, PER-03 | Must | Especificação §3 |
| RF-09.11 | O sistema deve mostrar os critérios utilizados para atribuir estrelas e ordenar equipas. | PER-01, PER-03 | Must | Especificação §3 |

## RF-10 — Notificações essenciais

| Código | Descrição | Persona | Prioridade | Origem |
|--------|-----------|---------|------------|--------|
| RF-10.01 | O sistema deve notificar a equipa quando receber uma solicitação de jogo. | PER-03 | Must | Especificação §3 |
| RF-10.02 | O sistema deve notificar a equipa quando uma solicitação for aceite ou recusada. | PER-03 | Must | Especificação §3 |
| RF-10.03 | O sistema deve notificar as equipas sobre alterações ou cancelamentos de jogos. | PER-03 | Must | Especificação §3 |
| RF-10.04 | O sistema deve notificar as equipas quando se aproximar a data de um jogo. | PER-03 | Should | Especificação §3 |
| RF-10.05 | O sistema deve notificar a equipa adversária quando uma comparência ou resultado for submetido. | PER-03 | Must | Especificação §3 |
| RF-10.06 | O sistema deve notificar as equipas sobre divergências nos resultados ou comparências. | PER-03 | Must | Especificação §3 |
| RF-10.07 | As notificações devem estar disponíveis dentro da aplicação. | PER-03 | Must | Especificação §3 |

## RF-11 — Administração básica da plataforma

| Código | Descrição | Persona | Prioridade | Origem |
|--------|-----------|---------|------------|--------|
| RF-11.01 | O administrador da plataforma deve poder consultar utilizadores e equipas registadas. | PER-05 | Must | Especificação §3 |
| RF-11.02 | O administrador deve poder suspender ou reativar contas e equipas. | PER-05 | Should | Especificação §3 |
| RF-11.03 | O administrador deve poder analisar divergências de resultados e comparências. | PER-05 | Must | Especificação §3 |
| RF-11.04 | O administrador deve poder corrigir um registo mediante justificação. | PER-05 | Must | Especificação §3 |
| RF-11.05 | O sistema deve guardar o utilizador, data e motivo de cada alteração administrativa. | PER-05 | Must | Especificação §3 |
| RF-11.06 | O administrador deve poder consultar indicadores gerais: equipas, jogadores, jogos marcados e jogos concluídos. | PER-05 | Should | Especificação §3 |
