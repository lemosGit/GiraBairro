# User Stories — GiraBairro

| Campo | Valor |
|-------|-------|
| Task | M1-08 (#26) |
| Versão | 1.0 — 2026-11-08 |
| Total | 31 user stories — cobrem **todos** os RF Must e Should (verificado por script) |
| Formato | *Como* <persona>, *quero* <acção>, *para* <benefício>. Critérios em **Dado / Quando / Então** |

## Índice

| US | Persona | Resumo | Prioridade | Telas |
|----|---------|--------|:----------:|-------|
| [US-001](#us-001) | PER-02 | Criar uma conta com o meu nome, telefone e palavra-passe | Must | TEL-02 |
| [US-002](#us-002) | PER-02 | Iniciar e terminar sessão com o meu telefone | Must | TEL-03, TEL-21 |
| [US-003](#us-003) | PER-02 | Recuperar a palavra-passe através de um código enviado por SMS | Must | TEL-03 |
| [US-004](#us-004) | PER-03 | Consultar e editar os meus dados e alterar a palavra-passe | Should | TEL-21 |
| [US-005](#us-005) | PER-02 | Registar a minha equipa com nome, localização e contacto principal | Must | TEL-04 |
| [US-006](#us-006) | PER-03 | Adicionar emblema e descrição e editar os dados da equipa | Should | TEL-06 |
| [US-007](#us-007) | PER-01 | Pesquisar equipas por nome e localização e ver o seu perfil público | Must | TEL-10, TEL-11 |
| [US-008](#us-008) | PER-03 | Cadastrar jogadores com nome, número e posição | Must | TEL-07, TEL-08 |
| [US-009](#us-009) | PER-03 | Editar, desactivar ou remover jogadores e definir a visibilidade do plantel | Must | TEL-07, TEL-08 |
| [US-010](#us-010) | PER-03 | Indicar os contactos que recebem pedidos de jogo e escolher o principal | Must | TEL-09 |
| [US-011](#us-011) | PER-03 | Ver os contactos de outra equipa quando tenho sessão iniciada | Must | TEL-11 |
| [US-012](#us-012) | PER-03 | Enviar uma solicitação de jogo com data, hora, campo e observação | Must | TEL-12 |
| [US-013](#us-013) | PER-03 | Aceitar ou recusar uma solicitação recebida | Must | TEL-13 |
| [US-014](#us-014) | PER-03 | Propor outra data, hora ou local | Should | TEL-13 |
| [US-015](#us-015) | PER-03 | Cancelar uma solicitação enviada ou um jogo confirmado indicando o motivo | Must | TEL-13, TEL-15 |
| [US-016](#us-016) | PER-03 | Ver os meus jogos por estado e o detalhe de cada um | Must | TEL-14, TEL-15 |
| [US-017](#us-017) | PER-03 | Declarar se a minha equipa compareceu | Must | TEL-16 |
| [US-018](#us-018) | PER-03 | Declarar que a adversária faltou | Must | TEL-16 |
| [US-019](#us-019) | PER-03 | Ver os indicadores de comparência da minha equipa e de outras | Must | TEL-05, TEL-11 |
| [US-020](#us-020) | PER-03 | Submeter o resultado do jogo | Must | TEL-17 |
| [US-021](#us-021) | PER-03 | Ver se o resultado foi confirmado ou está em divergência | Must | TEL-18 |
| [US-022](#us-022) | PER-03 | Corrigir o nosso resultado ou pedir análise | Must | TEL-18 |
| [US-023](#us-023) | PER-01 | Consultar o ranking geral e por província, município ou bairro | Must | TEL-19 |
| [US-024](#us-024) | PER-03 | Ver as estrelas e os critérios usados | Must | TEL-19, TEL-05 |
| [US-025](#us-025) | PER-03 | Ver um dashboard com o essencial da minha equipa | Must | TEL-05 |
| [US-026](#us-026) | PER-03 | Receber notificações dentro da aplicação e marcá-las como lidas | Must | TEL-20 |
| [US-027](#us-027) | PER-03 | Receber um lembrete antes do jogo | Should | TEL-20 |
| [US-028](#us-028) | PER-05 | Consultar utilizadores, equipas e indicadores gerais | Must | TEL-22 |
| [US-029](#us-029) | PER-05 | Suspender ou reactivar contas e equipas | Should | TEL-22 |
| [US-030](#us-030) | PER-05 | Analisar divergências de resultado e de comparência e decidir com justificação | Must | TEL-22 |
| [US-031](#us-031) | PER-05 | Marcar um jogo como já realizado para permitir registos | Should | TEL-22 |

## US-001

**Como** PER-02, **quero** criar uma conta com o meu nome, telefone e palavra-passe, **para** poder registar e gerir a minha equipa.

- **RF:** RF-01.01, RF-01.02, RF-01.03
- **Telas:** TEL-02
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que estou na página de registo, **quando** preencho nome, telefone, palavra-passe igual na confirmação e aceito os termos, **então** a conta é criada e fico com sessão iniciada.
2. **Dado** que o telefone já pertence a outra conta, **quando** tento registar-me, **então** vejo a mensagem 'Este número já está registado' e nenhuma conta é criada (RF-01.03).
3. **Dado** que a palavra-passe tem menos de 8 caracteres, **quando** submeto o formulário, **então** o campo é assinalado com a regra a cumprir (RNF-021).

## US-002

**Como** PER-02, **quero** iniciar e terminar sessão com o meu telefone, **para** aceder aos meus dados com segurança.

- **RF:** RF-01.04, RF-01.05
- **Telas:** TEL-03, TEL-21
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que tenho conta, **quando** introduzo telefone e palavra-passe correctos, **então** entro no dashboard (ou no registo de equipa, se ainda não tiver).
2. **Dado** que errei a palavra-passe 5 vezes em 15 min, **quando** tento entrar de novo, **então** o acesso fica bloqueado temporariamente (RNF-021).
3. **Dado** que tenho sessão iniciada, **quando** escolho 'Terminar sessão', **então** a sessão é invalidada e volto à página inicial.

## US-003

**Como** PER-02, **quero** recuperar a palavra-passe através de um código enviado por SMS, **para** não perder o acesso à conta.

- **RF:** RF-01.07
- **Telas:** TEL-03
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que esqueci a palavra-passe, **quando** peço recuperação com o meu telefone, **então** recebo um código de 6 dígitos válido por 10 min (RNF-025).
2. **Dado** que recebi o código, **quando** introduzo o código e uma nova palavra-passe, **então** a palavra-passe é alterada e as outras sessões terminam.
3. **Dado** que introduzi o código errado 3 vezes, **quando** tento de novo, **então** o código é invalidado e tenho de pedir outro.

## US-004

**Como** PER-03, **quero** consultar e editar os meus dados e alterar a palavra-passe, **para** manter o perfil actualizado.

- **RF:** RF-01.06
- **Telas:** TEL-21
- **Prioridade:** Should

**Critérios de aceitação**

1. **Dado** que estou no meu perfil, **quando** altero o nome e guardo, **então** o novo nome aparece em todo o sistema.
2. **Dado** que quero mudar a palavra-passe, **quando** indico a actual e a nova, **então** a alteração só é aceite se a actual estiver correcta.

## US-005

**Como** PER-02, **quero** registar a minha equipa com nome, localização e contacto principal, **para** começar a marcar jogos.

- **RF:** RF-02.01, RF-02.02, RF-02.03, RF-02.09
- **Telas:** TEL-04
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que tenho conta e ainda não administro equipa, **quando** preencho nome, província, município, bairro e contacto principal, **então** a equipa é criada e fico como responsável (RF-02.02).
2. **Dado** que já administro uma equipa, **quando** tento registar outra, **então** o sistema impede (RN-18).
3. **Dado** que já existe uma equipa com o mesmo nome no mesmo bairro, **quando** tento registar, **então** vejo um aviso de possível duplicado e o registo é impedido (RF-02.09).

## US-006

**Como** PER-03, **quero** adicionar emblema e descrição e editar os dados da equipa, **para** apresentar bem a equipa.

- **RF:** RF-02.04, RF-02.05, RF-02.06
- **Telas:** TEL-06
- **Prioridade:** Should

**Critérios de aceitação**

1. **Dado** que sou responsável da equipa, **quando** carrego uma imagem JPG/PNG/WebP até 2 MB, **então** o emblema aparece em miniatura em cartões e perfil (RNF-003).
2. **Dado** que sou responsável da equipa, **quando** edito o bairro e guardo, **então** a equipa passa a aparecer nos rankings do novo bairro.
3. **Dado** que não sou responsável desta equipa, **quando** tento editá-la, **então** o pedido é recusado (RN-02, RNF-023).

## US-007

**Como** PER-01, **quero** pesquisar equipas por nome e localização e ver o seu perfil público, **para** conhecer equipas e adversários.

- **RF:** RF-02.07, RF-02.08, RF-05.01, RF-05.02
- **Telas:** TEL-10, TEL-11
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que estou na pesquisa, **quando** escrevo parte do nome e escolho um município, **então** vejo cartões com nome, emblema, localização, estrelas e posição no ranking.
2. **Dado** que abro o perfil de uma equipa, **quando** sou visitante, **então** vejo localização, histórico, V/E/D e estrelas; contactos e nomes do plantel ficam ocultos (RN-17, RN-22).
3. **Dado** que a equipa está suspensa, **quando** pesquiso, **então** ela não aparece como disponível para jogos (RN-19).

## US-008

**Como** PER-03, **quero** cadastrar jogadores com nome, número e posição, **para** ter o plantel organizado.

- **RF:** RF-03.01, RF-03.02, RF-03.05, RF-03.06, RF-03.07
- **Telas:** TEL-07, TEL-08
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que estou na lista de jogadores, **quando** adiciono nome, número 10 e posição 'Médio', **então** o jogador aparece activo na lista.
2. **Dado** que o número 10 já pertence a um jogador activo, **quando** tento adicionar outro com o 10, **então** vejo 'Número já em uso' (RN-04).
3. **Dado** que estou a escolher a posição, **quando** abro o seletor, **então** vejo guarda-redes, defesa, médio e avançado.

## US-009

**Como** PER-03, **quero** editar, desactivar ou remover jogadores e definir a visibilidade do plantel, **para** manter o plantel actualizado e proteger os jogadores.

- **RF:** RF-03.03, RF-03.04
- **Telas:** TEL-07, TEL-08
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que um jogador saiu da equipa, **quando** desactivo-o, **então** fica inactivo, deixa de contar para a regra do número e o número fica livre.
2. **Dado** que quero esconder nomes do público, **quando** altero a visibilidade do plantel, **então** visitantes deixam de ver os nomes (RN-22).

## US-010

**Como** PER-03, **quero** indicar os contactos que recebem pedidos de jogo e escolher o principal, **para** outras equipas saberem a quem ligar.

- **RF:** RF-04.01, RF-04.02, RF-04.03, RF-04.04
- **Telas:** TEL-09
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que estou na gestão de contactos, **quando** adiciono nome, telefone e função, **então** o contacto aparece na lista.
2. **Dado** que tenho dois contactos, **quando** marco um como principal, **então** só esse fica marcado como principal.
3. **Dado** que removo o último contacto, **quando** confirmo, **então** o sistema exige manter pelo menos o contacto principal da equipa (RF-02.03).

## US-011

**Como** PER-03, **quero** ver os contactos de outra equipa quando tenho sessão iniciada, **para** combinar o jogo por telefone se necessário.

- **RF:** RF-04.05, RF-04.06
- **Telas:** TEL-11
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que tenho sessão iniciada, **quando** abro o perfil de outra equipa, **então** vejo os contactos autorizados com botão para ligar.
2. **Dado** que sou visitante, **quando** abro o perfil, **então** vejo 'Entrar para ver o contacto' (RN-17).

## US-012

**Como** PER-03, **quero** enviar uma solicitação de jogo com data, hora, campo e observação, **para** marcar um jogo de forma registada.

- **RF:** RF-05.03, RF-05.04, RF-05.11, RF-10.01
- **Telas:** TEL-12
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que encontrei uma equipa activa, **quando** preencho data futura, hora, campo e observação e envio, **então** a solicitação fica 'Pendente' e a outra equipa é notificada.
2. **Dado** que a data é no passado, **quando** tento enviar, **então** o envio é recusado.
3. **Dado** que quero indicar quem é o mandante, **quando** escolho mandante/visitante, **então** a informação aparece no jogo (RF-05.11).

## US-013

**Como** PER-03, **quero** aceitar ou recusar uma solicitação recebida, **para** decidir com quem jogo.

- **RF:** RF-05.05, RF-05.07, RF-05.08, RF-10.02
- **Telas:** TEL-13
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que recebi uma solicitação pendente, **quando** aceito, **então** é criado um jogo 'Agendado' com identificador único e as duas equipas são notificadas (RN-05).
2. **Dado** que recebi uma solicitação, **quando** recuso, **então** fica 'Recusada' e a desafiante é notificada; nenhum jogo é criado.

## US-014

**Como** PER-03, **quero** propor outra data, hora ou local, **para** chegar a acordo sem começar do zero.

- **RF:** RF-05.06
- **Telas:** TEL-13
- **Prioridade:** Should

**Critérios de aceitação**

1. **Dado** que recebi uma solicitação, **quando** proponho nova data e campo, **então** fica 'Alteração proposta' e a desafiante é notificada.
2. **Dado** que a minha solicitação recebeu uma alteração, **quando** aceito, **então** é criado o jogo com os novos dados.

## US-015

**Como** PER-03, **quero** cancelar uma solicitação enviada ou um jogo confirmado indicando o motivo, **para** avisar a tempo quando não podemos jogar.

- **RF:** RF-05.09, RF-10.03
- **Telas:** TEL-13, TEL-15
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que tenho um jogo agendado para daqui a 3 dias, **quando** cancelo com motivo, **então** o jogo fica 'Cancelado', a adversária é notificada e não há penalização.
2. **Dado** que o jogo é daqui a 10 horas, **quando** cancelo, **então** o cancelamento conta como falta da minha equipa e sou avisado antes de confirmar (RN-24).

## US-016

**Como** PER-03, **quero** ver os meus jogos por estado e o detalhe de cada um, **para** saber o que tenho de fazer.

- **RF:** RF-05.10, RF-06.01, RF-06.02, RF-06.12
- **Telas:** TEL-14, TEL-15
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que tenho jogos, **quando** abro a agenda, **então** vejo separadores próximos, pendentes, concluídos e cancelados com estado de comparência e resultado.
2. **Dado** que abro um jogo, **quando** sou uma das equipas, **então** vejo identificador, equipas, data/hora/local, estados e as acções disponíveis.

## US-017

**Como** PER-03, **quero** declarar se a minha equipa compareceu, **para** registar a nossa seriedade.

- **RF:** RF-06.03, RF-06.04, RF-06.05, RF-07.01, RF-07.02, RF-07.04, RF-10.05
- **Telas:** TEL-16
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que a hora do jogo já passou, **quando** declaro 'A nossa equipa compareceu', **então** fica 'Compareceu (declarado)' e a adversária é notificada.
2. **Dado** que o jogo ainda não começou, **quando** tento declarar, **então** a acção está indisponível (RN-23).
3. **Dado** que a adversária já declarou, **quando** abro o registo, **então** vejo o estado declarado por ela.

## US-018

**Como** PER-03, **quero** declarar que a adversária faltou, **para** que a falta conte para a seriedade dela, de forma justa.

- **RF:** RF-07.03, RF-07.05, RF-07.09, RF-10.06
- **Telas:** TEL-16
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que compareci e a adversária não, **quando** declaro a falta dela, **então** a falta fica 'declarada' e a adversária tem 48 h para concordar ou contestar (RN-16).
2. **Dado** que a adversária não respondeu em 48 h, **quando** o prazo termina, **então** a falta fica confirmada.
3. **Dado** que a adversária contesta, **quando** submete a contestação, **então** o caso fica 'Em análise' e aparece ao administrador.

## US-019

**Como** PER-03, **quero** ver os indicadores de comparência da minha equipa e de outras, **para** avaliar a seriedade.

- **RF:** RF-07.06, RF-07.07, RF-07.08
- **Telas:** TEL-05, TEL-11
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que a equipa tem jogos, **quando** abro o perfil, **então** vejo jogos agendados, comparências, faltas e a taxa de comparência.

## US-020

**Como** PER-03, **quero** submeter o resultado do jogo, **para** que o marcador fique registado.

- **RF:** RF-06.06, RF-06.07, RF-06.08, RF-08.01, RF-10.05
- **Telas:** TEL-17
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que o jogo já começou, **quando** indico golos da equipa A e da B e submeto, **então** o resultado fica 'Aguardando a outra equipa' e a adversária é notificada.
2. **Dado** que o jogo ainda não começou, **quando** tento submeter, **então** a acção está indisponível (RF-06.13).

## US-021

**Como** PER-03, **quero** ver se o resultado foi confirmado ou está em divergência, **para** saber se conta para o ranking.

- **RF:** RF-06.09, RF-06.10, RF-08.02, RF-08.03, RF-08.04, RF-08.05, RF-08.09, RF-10.06
- **Telas:** TEL-18
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que as duas equipas submeteram 2–1, **quando** a segunda submissão é guardada, **então** o resultado fica 'Confirmado' e o ranking é actualizado.
2. **Dado** que uma submeteu 2–1 e a outra 1–1, **quando** a segunda é guardada, **então** fica 'Divergente', ambas são notificadas e o jogo não conta para o ranking (RN-09).

## US-022

**Como** PER-03, **quero** corrigir o nosso resultado ou pedir análise, **para** resolver uma divergência.

- **RF:** RF-06.11, RF-08.06, RF-08.07, RF-08.08
- **Telas:** TEL-18
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que o resultado está divergente, **quando** corrijo para o mesmo marcador da adversária, **então** fica 'Confirmado' e o histórico guarda as duas versões.
2. **Dado** que a divergência continua, **quando** peço análise, **então** o caso vai para o administrador.
3. **Dado** que passaram 72 h sem acordo, **quando** o prazo termina, **então** o caso vai automaticamente para o administrador (RN-20).

## US-023

**Como** PER-01, **quero** consultar o ranking geral e por província, município ou bairro, **para** ver as melhores equipas da minha zona.

- **RF:** RF-09.01, RF-09.02, RF-09.04, RF-09.05, RF-09.10
- **Telas:** TEL-19
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que estou no ranking, **quando** escolho um município, **então** vejo posição, emblema, nome, estrelas, V/E/D e comparência das equipas desse município.
2. **Dado** que duas equipas têm os mesmos pontos, **quando** vejo o ranking, **então** fica à frente a de maior comparência (RN-15).

## US-024

**Como** PER-03, **quero** ver as estrelas e os critérios usados, **para** perceber e confiar na classificação.

- **RF:** RF-09.03, RF-09.06, RF-09.07, RF-09.08, RF-09.09, RF-09.11
- **Telas:** TEL-19, TEL-05
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que a minha equipa tem 2 jogos confirmados, **quando** vejo o perfil, **então** aparece 'Nova' em vez de estrelas (RN-14).
2. **Dado** que um resultado foi confirmado, **quando** abro o ranking, **então** as estrelas e posição reflectem-no em ≤ 60 s (RNF-005).
3. **Dado** que estou no ranking, **quando** abro 'Como funcionam as estrelas?', **então** vejo o texto público da RN-11.

## US-025

**Como** PER-03, **quero** ver um dashboard com o essencial da minha equipa, **para** saber logo o que fazer.

- **RF:** RF-09.05, RF-06.12
- **Telas:** TEL-05
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que entro no sistema, **quando** abro o dashboard, **então** vejo próximos jogos, solicitações pendentes, jogos por confirmar, nº de jogadores, V/E/D, posição local e estrelas.

## US-026

**Como** PER-03, **quero** receber notificações dentro da aplicação e marcá-las como lidas, **para** não perder nada importante.

- **RF:** RF-10.01, RF-10.02, RF-10.03, RF-10.05, RF-10.06, RF-10.07
- **Telas:** TEL-20
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que ocorreu um evento do meu jogo, **quando** abro as notificações, **então** vejo-o como não lido com ligação ao jogo ou equipa.
2. **Dado** que abro uma notificação, **quando** toco nela, **então** fica lida e sou levado ao jogo.

## US-027

**Como** PER-03, **quero** receber um lembrete antes do jogo, **para** não me esquecer.

- **RF:** RF-10.04
- **Telas:** TEL-20
- **Prioridade:** Should

**Critérios de aceitação**

1. **Dado** que tenho um jogo amanhã, **quando** faltam 24 h, **então** recebo um lembrete com data, hora e local (RNF-046).

## US-028

**Como** PER-05, **quero** consultar utilizadores, equipas e indicadores gerais, **para** acompanhar a plataforma.

- **RF:** RF-11.01, RF-11.06
- **Telas:** TEL-22
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que sou administrador, **quando** abro o painel, **então** vejo totais de utilizadores, equipas, jogadores, jogos marcados e concluídos.

## US-029

**Como** PER-05, **quero** suspender ou reactivar contas e equipas, **para** travar abusos.

- **RF:** RF-11.02
- **Telas:** TEL-22
- **Prioridade:** Should

**Critérios de aceitação**

1. **Dado** que uma equipa abusa, **quando** suspendo-a com motivo, **então** deixa de aparecer como disponível e não pode enviar solicitações; a acção fica auditada.

## US-030

**Como** PER-05, **quero** analisar divergências de resultado e de comparência e decidir com justificação, **para** garantir dados fiáveis.

- **RF:** RF-11.03, RF-11.04, RF-11.05, RF-08.07
- **Telas:** TEL-22
- **Prioridade:** Must

**Critérios de aceitação**

1. **Dado** que há um caso em análise, **quando** comparo as submissões e o histórico e decido 2–1 com justificação, **então** o resultado fica confirmado, o ranking é recalculado e a decisão fica auditada (quem, quando, motivo).
2. **Dado** que uma equipa pede reabertura 3 dias após a confirmação, **quando** reabro com justificação, **então** o resultado volta a 'Em análise administrativa' (RN-21).

## US-031

**Como** PER-05, **quero** marcar um jogo como já realizado para permitir registos, **para** resolver casos de jogos registados tarde.

- **RF:** RF-06.13
- **Telas:** TEL-22
- **Prioridade:** Should

**Critérios de aceitação**

1. **Dado** que um jogo passou do prazo de 7 dias, **quando** marco-o como realizado com justificação, **então** as equipas voltam a poder submeter comparência e resultado.
