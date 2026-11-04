# GiraBairro — Especificação Funcional do MVP

## 1. Visão do MVP

O GiraBairro MVP é uma plataforma para gestão de equipas de futebol comunitário, cujo foco principal é a marcação e gestão de jogos entre equipas, o registo de comparências, a confirmação bilateral dos resultados e a criação de um ranking comunitário baseado no desempenho e na seriedade das equipas.

Cada utilizador poderá criar uma conta, registar uma equipa e assumir o papel de **Administrador/Responsável da equipa**. Esse responsável cadastra os jogadores, define os contactos responsáveis por receber chamadas de outras equipas e gere os pedidos de marcação de jogos.

### Objetivos
- Facilitar a descoberta e contacto entre equipas de futebol comunitário.
- Permitir marcar e gerir jogos entre equipas.
- Registar jogadores, respetivos números de camisola e posições.
- Registar a comparência ou falta de comparência de cada equipa.
- Garantir a confirmação dos resultados pelas duas equipas.
- Criar um ranking por localização, considerando vitórias e indicadores de seriedade.

## 2. Atores do sistema

| Ator | Descrição |
|---|---|
| Utilizador registado | Pessoa que cria e acede a uma conta GiraBairro. |
| Administrador/Responsável da equipa | Utilizador que regista e administra uma equipa, plantel, contactos e jogos. |
| Responsável de contacto | Pessoa indicada pela equipa para receber contactos de marcação de jogos. Pode ser o administrador ou outro membro. |
| Equipa adversária | Equipa que recebe, aceita, recusa ou participa num pedido de jogo. |
| Administrador da plataforma | Responsável pela moderação e gestão global da plataforma. |

> No MVP, o administrador da equipa é o responsável principal pela gestão dos dados e atividades da equipa. A possibilidade de atribuir acessos independentes a outros responsáveis pode ser mantida como extensão futura, se não for necessária no lançamento.

## 3. Requisitos funcionais

### RF-01 — Registo e autenticação de utilizadores
- RF-01.01 — O sistema deve permitir que um utilizador crie uma conta.
- RF-01.02 — O sistema deve solicitar nome completo, telefone e palavra-passe no registo.
- RF-01.03 — O sistema deve validar que o telefone não está associado a outra conta.
- RF-01.04 — O sistema deve permitir ao utilizador iniciar sessão.
- RF-01.05 — O sistema deve permitir terminar sessão.
- RF-01.06 — O sistema deve permitir ao utilizador consultar e editar os seus dados básicos.
- RF-01.07 — O sistema deve permitir recuperar ou redefinir a palavra-passe.

### RF-02 — Registo e gestão de equipa
- RF-02.01 — O sistema deve permitir ao utilizador autenticado registar uma equipa.
- RF-02.02 — O sistema deve associar automaticamente o utilizador criador à equipa como Administrador/Responsável.
- RF-02.03 — O sistema deve solicitar nome da equipa, bairro, município, província e contacto principal.
- RF-02.04 — O sistema deve permitir inserir o emblema da equipa, caso disponível.
- RF-02.05 — O sistema deve permitir inserir a descrição da equipa, caso disponível.
- RF-02.06 — O sistema deve permitir editar os dados da equipa ao seu responsável.
- RF-02.07 — O sistema deve apresentar o perfil público da equipa.
- RF-02.08 — O sistema deve permitir pesquisar equipas por nome e localização.
- RF-02.09 — O sistema deve impedir a criação de duplicados evidentes, por exemplo nome da equipa e bairro iguais, sujeito à validação definida pelo sistema.

### RF-03 — Gestão de jogadores
- RF-03.01 — O responsável deve poder cadastrar jogadores na equipa.
- RF-03.02 — O cadastro do jogador deve conter, no mínimo, nome, número de camisola e posição.
- RF-03.03 — O sistema deve permitir editar os dados de um jogador.
- RF-03.04 — O sistema deve permitir remover ou desativar um jogador do plantel.
- RF-03.05 — O sistema deve apresentar a lista de jogadores da equipa.
- RF-03.06 — O sistema deve validar que o número de camisola não está repetido no plantel ativo da mesma equipa.
- RF-03.07 — O sistema deve permitir definir posições, por exemplo guarda-redes, defesa, médio e avançado.

### RF-04 — Contactos responsáveis da equipa
- RF-04.01 — O responsável da equipa deve poder indicar um ou mais contactos para receber chamadas e pedidos de marcação.
- RF-04.02 — Cada contacto deve conter nome, telefone e função ou relação com a equipa.
- RF-04.03 — O responsável deve poder definir um contacto como principal.
- RF-04.04 — O responsável deve poder editar ou remover contactos.
- RF-04.05 — O perfil público da equipa deve apresentar os contactos autorizados para marcação de jogos.
- RF-04.06 — O sistema deve permitir que a equipa seja contactada por outras equipas através dos contactos definidos.

### RF-05 — Descoberta e solicitação de jogos
- RF-05.01 — O sistema deve permitir consultar equipas disponíveis para marcar jogos.
- RF-05.02 — O sistema deve permitir filtrar equipas por bairro, município ou província.
- RF-05.03 — O responsável deve poder enviar uma solicitação de jogo a outra equipa.
- RF-05.04 — A solicitação deve conter equipa desafiante, equipa desafiada, data proposta, hora proposta, local/campo e observação opcional.
- RF-05.05 — A equipa destinatária deve poder aceitar ou recusar a solicitação.
- RF-05.06 — A equipa destinatária deve poder propor uma nova data, hora ou local.
- RF-05.07 — O sistema deve informar ambas as equipas sobre o estado da solicitação.
- RF-05.08 — O sistema deve criar o jogo como confirmado apenas após aceitação da equipa destinatária.
- RF-05.09 — O sistema deve permitir cancelar um jogo confirmado, indicando o motivo.
- RF-05.10 — O sistema deve permitir consultar jogos pendentes, confirmados, concluídos e cancelados.
- RF-05.11 — O sistema deve identificar a equipa mandante e a equipa visitante, quando aplicável.

### RF-06 — Gestão de jogos
- RF-06.01 — O sistema deve atribuir um identificador único a cada jogo.
- RF-06.02 — O sistema deve apresentar os detalhes do jogo às duas equipas.
- RF-06.03 — O sistema deve permitir que cada equipa registe a sua comparência após a data do jogo.
- RF-06.04 — A comparência deve ter pelo menos os estados: compareceu, falta de comparência ou ainda não registada.
- RF-06.05 — O sistema deve guardar separadamente a comparência declarada por cada equipa.
- RF-06.06 — O sistema deve permitir registar o resultado do jogo por cada equipa.
- RF-06.07 — O resultado deve conter golos da equipa A e golos da equipa B.
- RF-06.08 — O sistema deve guardar separadamente os resultados declarados pelas duas equipas.
- RF-06.09 — O sistema deve considerar o resultado confirmado quando os valores submetidos pelas duas equipas forem iguais.
- RF-06.10 — O sistema deve marcar o resultado como pendente de confirmação quando os valores forem diferentes ou só uma equipa tiver submetido.
- RF-06.11 — O sistema deve permitir corrigir um resultado submetido antes da confirmação bilateral.
- RF-06.12 — O sistema deve permitir consultar o histórico de jogos de cada equipa.
- RF-06.13 — O sistema deve impedir o registo de resultado antes da data do jogo, exceto se o jogo for explicitamente marcado como já realizado por um administrador autorizado.

### RF-07 — Comparência e seriedade das equipas
- RF-07.01 — O sistema deve registar a comparência de cada equipa separadamente.
- RF-07.02 — O sistema deve permitir que uma equipa declare que compareceu.
- RF-07.03 — O sistema deve permitir que uma equipa declare que a adversária faltou, associando essa declaração ao seu próprio registo de comparência.
- RF-07.04 — O sistema deve apresentar o estado de comparência das duas equipas.
- RF-07.05 — O sistema deve sinalizar casos em que as declarações de comparência são contraditórias.
- RF-07.06 — O sistema deve calcular indicadores de comparência a partir dos jogos registados.
- RF-07.07 — O sistema deve apresentar o número de jogos agendados, jogos em que compareceu e faltas de comparência da equipa.
- RF-07.08 — O sistema deve permitir consultar o histórico de comparência.
- RF-07.09 — O sistema deve evitar que uma única declaração unilateral seja tratada automaticamente como falta confirmada da adversária.

### RF-08 — Confirmação de resultados e divergências
- RF-08.01 — O sistema deve exigir a submissão do resultado pelas duas equipas.
- RF-08.02 — O sistema deve comparar automaticamente os resultados submetidos.
- RF-08.03 — O sistema deve confirmar o resultado quando os dois registos forem iguais.
- RF-08.04 — O sistema deve manter o resultado pendente quando os registos forem diferentes.
- RF-08.05 — O sistema deve notificar ambas as equipas sobre uma divergência.
- RF-08.06 — O sistema deve permitir que as equipas atualizem os seus registos para resolver a divergência.
- RF-08.07 — O sistema deve permitir encaminhar uma divergência para análise do administrador da plataforma.
- RF-08.08 — O sistema deve guardar o histórico das submissões e alterações do resultado.
- RF-08.09 — O sistema deve utilizar apenas resultados confirmados no cálculo do ranking de vitórias.

### RF-09 — Ranking de equipas e estrelas
- RF-09.01 — O sistema deve gerar um ranking de equipas por localização.
- RF-09.02 — O sistema deve permitir consultar ranking por bairro, município e província.
- RF-09.03 — O sistema deve calcular o número de vitórias a partir dos resultados confirmados.
- RF-09.04 — O sistema deve ordenar as equipas segundo os critérios de ranking definidos.
- RF-09.05 — O sistema deve apresentar a posição da equipa no ranking.
- RF-09.06 — O sistema deve apresentar o número de vitórias, empates e derrotas da equipa.
- RF-09.07 — O sistema deve apresentar indicadores de comparência e faltas de comparência.
- RF-09.08 — O sistema deve representar o nível ou classificação da equipa por estrelas.
- RF-09.09 — O sistema deve atualizar o ranking quando um resultado for confirmado ou quando uma comparência for validada.
- RF-09.10 — O sistema deve permitir consultar o ranking geral e os rankings locais.
- RF-09.11 — O sistema deve mostrar os critérios utilizados para atribuir estrelas e ordenar equipas.

> **Regra por definir:** o número de estrelas não deve ser atribuído de forma arbitrária. É necessário decidir se depende apenas de vitórias, de uma combinação entre vitórias e comparência, ou de um sistema de pontos. Esta regra será especificada antes da implementação.

### RF-10 — Notificações essenciais
- RF-10.01 — O sistema deve notificar a equipa quando receber uma solicitação de jogo.
- RF-10.02 — O sistema deve notificar a equipa quando uma solicitação for aceite ou recusada.
- RF-10.03 — O sistema deve notificar as equipas sobre alterações ou cancelamentos de jogos.
- RF-10.04 — O sistema deve notificar as equipas quando se aproximar a data de um jogo.
- RF-10.05 — O sistema deve notificar a equipa adversária quando uma comparência ou resultado for submetido.
- RF-10.06 — O sistema deve notificar as equipas sobre divergências nos resultados ou comparências.
- RF-10.07 — As notificações devem estar disponíveis dentro da aplicação.

### RF-11 — Administração básica da plataforma
- RF-11.01 — O administrador da plataforma deve poder consultar utilizadores e equipas registadas.
- RF-11.02 — O administrador deve poder suspender ou reativar contas e equipas.
- RF-11.03 — O administrador deve poder analisar divergências de resultados e comparências.
- RF-11.04 — O administrador deve poder corrigir um registo mediante justificação.
- RF-11.05 — O sistema deve guardar o utilizador, data e motivo de cada alteração administrativa.
- RF-11.06 — O administrador deve poder consultar indicadores gerais: equipas, jogadores, jogos marcados e jogos concluídos.

## 4. Regras de negócio

- RN-01 — Uma equipa deve ter um utilizador responsável associado.
- RN-02 — O responsável da equipa pode gerir os dados da equipa e o respetivo plantel.
- RN-03 — Cada jogador cadastrado deve possuir nome, número de camisola e posição.
- RN-04 — O número de camisola não pode repetir-se entre jogadores ativos da mesma equipa.
- RN-05 — Um jogo só fica confirmado na agenda após aceitação da equipa destinatária.
- RN-06 — A comparência de cada equipa deve ser registada separadamente.
- RN-07 — Uma declaração unilateral de falta de comparência não deve, por si só, constituir uma falta confirmada da equipa adversária; casos contraditórios devem ser sinalizados ou analisados.
- RN-08 — O resultado oficial do MVP só é confirmado quando as duas equipas submetem o mesmo marcador.
- RN-09 — Resultados pendentes ou contestados não contam para o ranking de vitórias.
- RN-10 — O ranking deve ser calculado a partir dos jogos e resultados confirmados.
- RN-11 — A classificação por estrelas deve ter critérios explícitos e transparentes.
- RN-12 — Todas as alterações relevantes a jogos, comparências e resultados devem manter histórico.
- RN-13 — Uma equipa só pode submeter comparência e resultado em jogos nos quais está envolvida, através do seu responsável autorizado.

## 5. Telas do MVP

### TEL-01 — Página inicial / apresentação
**Objetivo:** apresentar a plataforma e permitir iniciar registo ou sessão.

Elementos:
- Nome e identidade visual GiraBairro.
- Breve descrição da plataforma.
- Botão “Criar conta”.
- Botão “Iniciar sessão”.
- Pesquisa ou acesso à lista pública de equipas.
- Destaque para rankings locais, se disponíveis publicamente.

### TEL-02 — Registo de utilizador
Elementos:
- Nome completo.
- Número de telefone.
- Palavra-passe.
- Confirmação da palavra-passe.
- Aceitação dos termos de utilização.
- Botão “Registar”.
- Link para iniciar sessão.

### TEL-03 — Iniciar sessão
Elementos:
- Número de telefone.
- Palavra-passe.
- Botão “Entrar”.
- Link “Recuperar palavra-passe”.
- Link para criar conta.

### TEL-04 — Registo da equipa
Elementos:
- Nome da equipa.
- Bairro.
- Município.
- Província.
- Contacto principal.
- Emblema (opcional).
- Descrição (opcional).
- Identificação do utilizador como Administrador/Responsável.
- Botão “Registar equipa”.

### TEL-05 — Dashboard do responsável da equipa
Elementos:
- Nome e emblema da equipa.
- Resumo de jogos próximos.
- Solicitações de jogos pendentes.
- Jogos por confirmar (comparência/resultados).
- Total de jogadores.
- Vitórias, empates e derrotas.
- Posição no ranking local.
- Indicador de estrelas/seriedade.
- Atalhos: “Gerir jogadores”, “Contactos”, “Marcar jogo”, “Ver jogos”, “Ver ranking”.

### TEL-06 — Perfil e gestão da equipa
Elementos:
- Nome, emblema e descrição.
- Bairro, município e província.
- Contacto principal.
- Responsável da equipa.
- Lista de jogadores.
- Estatísticas resumidas.
- Botão “Editar equipa”.
- Botão “Gerir contactos”.

### TEL-07 — Lista de jogadores
Elementos:
- Lista/tabela de jogadores.
- Nome do jogador.
- Número de camisola.
- Posição.
- Estado (ativo/inativo).
- Botão “Adicionar jogador”.
- Ações “Editar” e “Desativar/Remover”.

### TEL-08 — Cadastro/edição de jogador
Elementos:
- Nome completo.
- Número de camisola.
- Posição (seletor).
- Estado do jogador.
- Botão “Guardar”.
- Botão “Cancelar”.

### TEL-09 — Gestão de contactos da equipa
Elementos:
- Lista de contactos para marcação de jogos.
- Nome.
- Telefone.
- Função/relação com a equipa.
- Indicação de contacto principal.
- Botão “Adicionar contacto”.
- Ações “Editar” e “Remover”.

### TEL-10 — Pesquisa/listagem de equipas
Elementos:
- Campo de pesquisa por nome.
- Filtros por bairro, município e província.
- Cartões de equipas com nome, localização, emblema e posição no ranking.
- Acesso ao perfil da equipa.
- Ação “Solicitar jogo”.
- Acesso aos contactos públicos definidos pela equipa.

### TEL-11 — Perfil público de equipa
Elementos:
- Nome e emblema.
- Localização.
- Contactos para marcação.
- Plantel (nome, número e posição, conforme configuração de visibilidade).
- Histórico de jogos.
- Vitórias, empates e derrotas.
- Ranking e estrelas.
- Botão “Solicitar jogo”.

### TEL-12 — Solicitar/Marcar jogo
Elementos:
- Equipa adversária.
- Data proposta.
- Hora proposta.
- Campo/local.
- Equipa mandante e visitante (se aplicável).
- Observação opcional.
- Botão “Enviar solicitação”.

### TEL-13 — Solicitações de jogos
Elementos:
- Separadores: recebidas e enviadas.
- Nome das equipas envolvidas.
- Data, hora e local propostos.
- Estado da solicitação.
- Ações: “Aceitar”, “Recusar”, “Propor alteração” (para solicitações recebidas).
- Ação “Cancelar solicitação” (quando aplicável).

### TEL-14 — Agenda/lista de jogos
Elementos:
- Separadores: próximos, pendentes, concluídos e cancelados.
- Nome das equipas.
- Data, hora e local.
- Estado do jogo.
- Estado de comparência de cada equipa.
- Estado de confirmação do resultado.
- Acesso aos detalhes do jogo.

### TEL-15 — Detalhes do jogo
Elementos:
- Identificador do jogo.
- Equipas envolvidas.
- Data, hora e local.
- Estado do jogo.
- Comparência declarada por cada equipa.
- Resultado submetido por cada equipa.
- Estado de confirmação ou divergência.
- Histórico de alterações.
- Ações disponíveis conforme o estado: registar comparência, submeter resultado, corrigir submissão, cancelar ou consultar.

### TEL-16 — Registo de comparência
Elementos:
- Identificação do jogo.
- Equipa do utilizador.
- Opções: “A nossa equipa compareceu” ou “A nossa equipa não compareceu”.
- Campo de observação opcional.
- Indicação do estado da equipa adversária, se já registado.
- Botão “Confirmar comparência”.

> A falta da equipa adversária deve ser registada como declaração e não considerada confirmada automaticamente se não houver confirmação ou procedimento de análise definido.

### TEL-17 — Registo de resultado
Elementos:
- Identificação do jogo.
- Nome da equipa A e equipa B.
- Campo de golos da equipa A.
- Campo de golos da equipa B.
- Botão “Submeter resultado”.
- Indicação de que o resultado será comparado com a submissão da outra equipa.

### TEL-18 — Confirmação/divergência de resultado
Elementos:
- Resultado submetido pela equipa A.
- Resultado submetido pela equipa B.
- Estado: aguardando outra equipa, confirmado ou divergente.
- Aviso em caso de divergência.
- Ação “Editar o nosso resultado” antes da confirmação.
- Ação “Solicitar análise” quando necessário.

### TEL-19 — Ranking de equipas
Elementos:
- Ranking geral.
- Filtros por bairro, município e província.
- Posição.
- Emblema e nome da equipa.
- Estrelas/classificação.
- Número de vitórias.
- Empates e derrotas.
- Indicadores de comparência.
- Explicação dos critérios de ranking.
- Acesso ao perfil da equipa.

### TEL-20 — Notificações
Elementos:
- Lista de notificações.
- Solicitações recebidas.
- Aceitação/recusa de jogos.
- Lembretes de jogos.
- Avisos de comparência.
- Avisos de resultado confirmado ou divergente.
- Estado lida/não lida.
- Acesso ao jogo ou equipa relacionada.

### TEL-21 — Perfil do utilizador
Elementos:
- Nome completo.
- Telefone.
- Dados básicos editáveis.
- Equipa administrada.
- Opção de alterar palavra-passe.
- Opção de terminar sessão.

### TEL-22 — Painel administrativo básico
Elementos:
- Total de utilizadores.
- Total de equipas.
- Total de jogadores.
- Total de jogos.
- Jogos com resultados pendentes ou divergentes.
- Equipas/utilizadores suspensos.
- Lista de casos que necessitam de análise.
- Ações de consulta, suspensão/reativação e análise de divergências.

## 6. Navegação principal sugerida

### Para o responsável da equipa
- Dashboard
- Minha equipa
- Jogadores
- Marcar jogo
- Solicitações
- Jogos
- Ranking
- Notificações
- Perfil

### Para visitante/utilizador sem equipa
- Página inicial
- Equipas
- Ranking
- Iniciar sessão
- Criar conta

### Para administrador da plataforma
- Dashboard administrativo
- Utilizadores
- Equipas
- Jogos
- Divergências
- Moderação

## 7. Estados essenciais

### Solicitação de jogo
- Pendente
- Aceite/Confirmada
- Recusada
- Alteração proposta
- Cancelada

### Jogo
- Agendado
- Em aguardo de comparência
- Em aguardo de resultado
- Resultado pendente de confirmação
- Resultado confirmado
- Divergência
- Cancelado
- Concluído

### Comparência por equipa
- Não registada
- Compareceu (declarado)
- Falta de comparência (declarada)
- Em divergência/análise
- Validada

### Resultado
- Não submetido
- Aguardando submissão adversária
- Confirmado
- Divergente
- Em análise administrativa

## 8. Fora do âmbito do MVP

Para manter o foco na primeira versão, ficam fora do MVP:
- Gestão de campeonatos e torneios formais.
- Inscrição de equipas em campeonatos.
- Gestão de árbitros e escalas de arbitragem.
- Pagamentos, mensalidades e bilheteira.
- Transmissão de jogos em direto.
- Chat interno completo.
- Mercado e transferências de jogadores.
- Descoberta avançada de talentos.
- Inteligência artificial e previsões de resultados.
- Gestão médica e de lesões.
- Gestão de equipamentos e inventário.
- Patrocínios e publicidade.
- Gamificação avançada e prémios digitais.
- Integração com calendários externos.
- Aplicação móvel nativa, caso a primeira versão seja web responsiva.

## 9. Decisões a definir antes do desenvolvimento

1. **Estrelas e ranking:** quantas estrelas existem e que fórmula as atribui? Apenas vitórias ou também comparência e seriedade?
2. **Falta de comparência:** basta uma declaração da equipa presente ou é necessária confirmação da adversária/validação administrativa?
3. **Contactos:** os contactos telefónicos serão públicos para todas as pessoas ou apenas para utilizadores autenticados?
4. **Número de equipas por utilizador:** um responsável poderá administrar mais de uma equipa?
5. **Jogos:** será permitido marcar jogos apenas entre equipas registadas na plataforma?
6. **Resultado divergente:** quem decide o resultado final quando as equipas não concordam?
7. **Alteração após confirmação:** será possível reabrir um resultado confirmado e quem poderá fazê-lo?
8. **Localização do ranking:** o ranking será organizado por bairro, município, província e também geral?
9. **Visibilidade do plantel:** os nomes dos jogadores serão públicos no perfil da equipa?
10. **Canal de notificações:** na primeira versão, as notificações serão apenas internas ou também por SMS/WhatsApp?

## 10. Resumo do escopo

O MVP do GiraBairro deve permitir que o utilizador:
1. Crie uma conta.
2. Registe uma equipa e fique associado como responsável.
3. Cadastre os jogadores com nome, número e posição.
4. Defina contactos que recebem chamadas/pedidos de jogos.
5. Pesquise equipas por localização.
6. Solicite, aceite, recuse ou ajuste uma marcação de jogo.
7. Registe a comparência da sua equipa.
8. Submeta o resultado do jogo.
9. Confirme o resultado através da correspondência das submissões das duas equipas.
10. Consulte histórico e estatísticas básicas.
11. Veja rankings locais e gerais, com vitórias e indicadores de seriedade.

**Princípio central do MVP:** a plataforma deve registar de forma clara e auditável quem marcou o jogo, quem compareceu e qual resultado foi confirmado por ambas as equipas.
