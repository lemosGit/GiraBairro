# Dicionário de Dados — GiraBairro

| Campo | Valor |
|-------|-------|
| Task | M2-05 (#33) |
| Versão | 1.0 — 2026-11-08 |
| SGBD de referência | PostgreSQL (tipos `UUID`, `TIMESTAMPTZ`, `JSONB`, `ENUM`) — a confirmar em M3-01 |
| Gerado por | `scripts/modelo_dados.py` (fonte única; também gera o modelo lógico) |

Convenções: nomes em `snake_case` português; datas em **UTC** (`TIMESTAMPTZ`) mostradas em WAT (RNF-034); `UK(a,b)` = unicidade composta; FK com `ON DELETE RESTRICT` salvo indicação.

**18 tabelas · 152 atributos · 14 enumerações**

## Índice

- [`provincia`](#provincia) — Províncias (divisão territorial de 1.º nível)
- [`municipio`](#municipio) — Municípios de cada província
- [`bairro`](#bairro) — Bairros de cada município
- [`utilizador`](#utilizador) — Contas de acesso (RF-01)
- [`codigo_recuperacao`](#codigo_recuperacao) — Códigos OTP de recuperação de palavra-passe (RF-01.07)
- [`equipa`](#equipa) — Equipas de bairro (RF-02)
- [`membro_equipa`](#membro_equipa) — Responsável da equipa (RN-01, RN-18)
- [`jogador`](#jogador) — Plantel (RF-03)
- [`contacto_equipa`](#contacto_equipa) — Contactos para marcação de jogos (RF-04)
- [`solicitacao_jogo`](#solicitacao_jogo) — Pedidos de jogo (RF-05)
- [`proposta_alteracao`](#proposta_alteracao) — Contra-propostas numa solicitação (RF-05.06)
- [`jogo`](#jogo) — Jogos agendados (RF-06)
- [`comparencia`](#comparencia) — Comparência declarada por cada equipa (RF-07)
- [`submissao_resultado`](#submissao_resultado) — Versões do resultado submetido por equipa (RF-06.08, RF-08.08)
- [`caso_analise`](#caso_analise) — Casos para o administrador (RF-08.07, RF-11.03)
- [`notificacao`](#notificacao) — Notificações internas (RF-10)
- [`registo_auditoria`](#registo_auditoria) — Histórico imutável de alterações (RN-12, RF-11.05)
- [`estatistica_equipa`](#estatistica_equipa) — Cache derivada para ranking e indicadores (RN-11, RNF-005)

## provincia

Províncias (divisão territorial de 1.º nível)

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `provincia` | `id` | SMALLINT | — | Não | PK | — | Identificador |
| `provincia` | `nome` | VARCHAR | 60 | Não | UK | — | Nome da província |

## municipio

Municípios de cada província

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `municipio` | `id` | INTEGER | — | Não | PK | — | Identificador |
| `municipio` | `provincia_id` | SMALLINT | — | Não | FK→provincia.id | — | Província a que pertence |
| `municipio` | `nome` | VARCHAR | 80 | Não | UK(provincia_id,nome) | — | Nome do município |

## bairro

Bairros de cada município

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `bairro` | `id` | INTEGER | — | Não | PK | — | Identificador |
| `bairro` | `municipio_id` | INTEGER | — | Não | FK→municipio.id | — | Município a que pertence |
| `bairro` | `nome` | VARCHAR | 100 | Não | UK(municipio_id,nome) | — | Nome do bairro |

## utilizador

Contas de acesso (RF-01)

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `utilizador` | `id` | UUID | — | Não | PK | `gen_random_uuid()` | Identificador |
| `utilizador` | `nome_completo` | VARCHAR | 120 | Não | — | — | Nome completo (RF-01.02) |
| `utilizador` | `telefone` | VARCHAR | 20 | Não | UK | — | Telefone em formato E.164, único (RF-01.03) |
| `utilizador` | `palavra_passe_hash` | VARCHAR | 255 | Não | — | — | Hash Argon2id/bcrypt (RNF-020) |
| `utilizador` | `papel` | ENUM papel_utilizador | — | Não | — | `'utilizador'` | Papel na plataforma (PER-05 = admin) |
| `utilizador` | `estado` | ENUM estado_conta | — | Não | — | `'activa'` | Suspensão (RF-11.02) |
| `utilizador` | `termos_aceites_em` | TIMESTAMPTZ | — | Não | — | — | Aceitação dos termos (TEL-02, RNF-026) |
| `utilizador` | `tentativas_falhadas` | SMALLINT | — | Não | — | `0` | Contador de logins falhados (RNF-021) |
| `utilizador` | `bloqueado_ate` | TIMESTAMPTZ | — | Sim | — | — | Bloqueio temporário (RNF-021) |
| `utilizador` | `criado_em` | TIMESTAMPTZ | — | Não | — | `now()` | Data de criação |
| `utilizador` | `actualizado_em` | TIMESTAMPTZ | — | Não | — | `now()` | Última alteração |

## codigo_recuperacao

Códigos OTP de recuperação de palavra-passe (RF-01.07)

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `codigo_recuperacao` | `id` | UUID | — | Não | PK | `gen_random_uuid()` | Identificador |
| `codigo_recuperacao` | `utilizador_id` | UUID | — | Não | FK→utilizador.id | — | Dono do código |
| `codigo_recuperacao` | `codigo_hash` | VARCHAR | 255 | Não | — | — | Hash do código de 6 dígitos |
| `codigo_recuperacao` | `expira_em` | TIMESTAMPTZ | — | Não | — | — | Validade ≤ 10 min (RNF-025) |
| `codigo_recuperacao` | `tentativas` | SMALLINT | — | Não | — | `0` | Tentativas usadas (máx. 3) |
| `codigo_recuperacao` | `usado_em` | TIMESTAMPTZ | — | Sim | — | — | Quando foi usado |
| `codigo_recuperacao` | `criado_em` | TIMESTAMPTZ | — | Não | — | `now()` | Data de criação |

## equipa

Equipas de bairro (RF-02)

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `equipa` | `id` | UUID | — | Não | PK | `gen_random_uuid()` | Identificador |
| `equipa` | `nome` | VARCHAR | 80 | Não | — | — | Nome da equipa |
| `equipa` | `nome_normalizado` | VARCHAR | 80 | Não | UK(nome_normalizado,bairro_id) | — | Nome sem acentos/maiúsculas para detectar duplicados (RF-02.09) |
| `equipa` | `bairro_id` | INTEGER | — | Não | FK→bairro.id | — | Localização (município e província por herança) |
| `equipa` | `emblema_url` | VARCHAR | 255 | Sim | — | — | Emblema (RF-02.04) |
| `equipa` | `descricao` | TEXT | — | Sim | — | — | Descrição (RF-02.05) |
| `equipa` | `visibilidade_plantel` | ENUM visibilidade_plantel | — | Não | — | `'autenticados'` | Quem vê os nomes dos jogadores (RN-22) |
| `equipa` | `estado` | ENUM estado_conta | — | Não | — | `'activa'` | Suspensão (RF-11.02, RN-19) |
| `equipa` | `criado_em` | TIMESTAMPTZ | — | Não | — | `now()` | Data de criação |
| `equipa` | `actualizado_em` | TIMESTAMPTZ | — | Não | — | `now()` | Última alteração |

## membro_equipa

Responsável da equipa (RN-01, RN-18)

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `membro_equipa` | `utilizador_id` | UUID | — | Não | PK, FK→utilizador.id | — | Utilizador (PK ⇒ no máx. 1 equipa — RN-18) |
| `membro_equipa` | `equipa_id` | UUID | — | Não | FK→equipa.id | — | Equipa |
| `membro_equipa` | `papel` | ENUM papel_membro | — | Não | — | `'responsavel'` | Papel na equipa |
| `membro_equipa` | `criado_em` | TIMESTAMPTZ | — | Não | — | `now()` | Data de associação |

## jogador

Plantel (RF-03)

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `jogador` | `id` | UUID | — | Não | PK | `gen_random_uuid()` | Identificador |
| `jogador` | `equipa_id` | UUID | — | Não | FK→equipa.id | — | Equipa |
| `jogador` | `nome` | VARCHAR | 120 | Não | — | — | Nome do jogador (RN-03) |
| `jogador` | `numero_camisola` | SMALLINT | — | Não | — | — | 1–99; único entre activos da equipa (índice parcial — RN-04) |
| `jogador` | `posicao` | ENUM posicao_jogador | — | Não | — | — | Posição (RF-03.07) |
| `jogador` | `activo` | BOOLEAN | — | Não | — | `true` | Activo/inactivo (RF-03.04) |
| `jogador` | `criado_em` | TIMESTAMPTZ | — | Não | — | `now()` | Data de criação |

Restrições:
- `numero_camisola BETWEEN 1 AND 99`
- UNIQUE (equipa_id, numero_camisola) WHERE activo — índice parcial (RN-04)

## contacto_equipa

Contactos para marcação de jogos (RF-04)

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `contacto_equipa` | `id` | UUID | — | Não | PK | `gen_random_uuid()` | Identificador |
| `contacto_equipa` | `equipa_id` | UUID | — | Não | FK→equipa.id | — | Equipa |
| `contacto_equipa` | `nome` | VARCHAR | 120 | Não | — | — | Nome do contacto |
| `contacto_equipa` | `telefone` | VARCHAR | 20 | Não | — | — | Telefone (visível só a autenticados — RN-17) |
| `contacto_equipa` | `funcao` | VARCHAR | 60 | Não | — | — | Função/relação com a equipa |
| `contacto_equipa` | `principal` | BOOLEAN | — | Não | — | `false` | Contacto principal; 1 por equipa (índice parcial) |

Restrições:
- UNIQUE (equipa_id) WHERE principal — 1 contacto principal por equipa (RF-04.03)

## solicitacao_jogo

Pedidos de jogo (RF-05)

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `solicitacao_jogo` | `id` | UUID | — | Não | PK | `gen_random_uuid()` | Identificador |
| `solicitacao_jogo` | `equipa_desafiante_id` | UUID | — | Não | FK→equipa.id | — | Quem pede |
| `solicitacao_jogo` | `equipa_desafiada_id` | UUID | — | Não | FK→equipa.id | — | Quem recebe (≠ desafiante) |
| `solicitacao_jogo` | `data_hora` | TIMESTAMPTZ | — | Não | — | — | Data/hora proposta (UTC — RNF-034) |
| `solicitacao_jogo` | `local` | VARCHAR | 150 | Não | — | — | Campo/local proposto |
| `solicitacao_jogo` | `equipa_mandante_id` | UUID | — | Sim | FK→equipa.id | — | Mandante, se aplicável (RF-05.11) |
| `solicitacao_jogo` | `observacao` | TEXT | — | Sim | — | — | Observação opcional |
| `solicitacao_jogo` | `estado` | ENUM estado_solicitacao | — | Não | — | `'pendente'` | Estado da solicitação |
| `solicitacao_jogo` | `aguarda_resposta_de_id` | UUID | — | Sim | FK→equipa.id | — | Equipa que tem de responder (muda após alteração) |
| `solicitacao_jogo` | `motivo` | TEXT | — | Sim | — | — | Motivo de recusa/cancelamento |
| `solicitacao_jogo` | `criado_por` | UUID | — | Não | FK→utilizador.id | — | Utilizador que enviou |
| `solicitacao_jogo` | `criado_em` | TIMESTAMPTZ | — | Não | — | `now()` | Data de envio |
| `solicitacao_jogo` | `actualizado_em` | TIMESTAMPTZ | — | Não | — | `now()` | Última alteração |

Restrições:
- `equipa_desafiante_id <> equipa_desafiada_id`

## proposta_alteracao

Contra-propostas numa solicitação (RF-05.06)

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `proposta_alteracao` | `id` | UUID | — | Não | PK | `gen_random_uuid()` | Identificador |
| `proposta_alteracao` | `solicitacao_id` | UUID | — | Não | FK→solicitacao_jogo.id | — | Solicitação |
| `proposta_alteracao` | `proposta_por_equipa_id` | UUID | — | Não | FK→equipa.id | — | Equipa que propõe |
| `proposta_alteracao` | `data_hora` | TIMESTAMPTZ | — | Não | — | — | Nova data/hora |
| `proposta_alteracao` | `local` | VARCHAR | 150 | Não | — | — | Novo local |
| `proposta_alteracao` | `observacao` | TEXT | — | Sim | — | — | Observação |
| `proposta_alteracao` | `criado_em` | TIMESTAMPTZ | — | Não | — | `now()` | Data da proposta |

## jogo

Jogos agendados (RF-06)

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `jogo` | `id` | UUID | — | Não | PK | `gen_random_uuid()` | Identificador único do jogo (RF-06.01) |
| `jogo` | `codigo` | VARCHAR | 12 | Não | UK | — | Código curto legível, ex.: GB-2026-00042 |
| `jogo` | `solicitacao_id` | UUID | — | Não | FK→solicitacao_jogo.id, UK | — | Solicitação que o originou (RN-05) |
| `jogo` | `equipa_a_id` | UUID | — | Não | FK→equipa.id | — | Equipa A (mandante, ou desafiante por defeito) |
| `jogo` | `equipa_b_id` | UUID | — | Não | FK→equipa.id | — | Equipa B |
| `jogo` | `data_hora` | TIMESTAMPTZ | — | Não | — | — | Data/hora acordada (UTC) |
| `jogo` | `local` | VARCHAR | 150 | Não | — | — | Campo/local |
| `jogo` | `estado` | ENUM estado_jogo | — | Não | — | `'agendado'` | Estado do jogo |
| `jogo` | `estado_resultado` | ENUM estado_resultado | — | Não | — | `'nao_submetido'` | Estado do resultado oficial |
| `jogo` | `golos_a` | SMALLINT | — | Sim | — | — | Golos oficiais de A (só quando confirmado) |
| `jogo` | `golos_b` | SMALLINT | — | Sim | — | — | Golos oficiais de B (só quando confirmado) |
| `jogo` | `confirmado_em` | TIMESTAMPTZ | — | Sim | — | — | Quando o resultado foi confirmado |
| `jogo` | `divergente_desde` | TIMESTAMPTZ | — | Sim | — | — | Início do prazo de 72 h (RN-20) |
| `jogo` | `realizado_admin` | BOOLEAN | — | Não | — | `false` | Marcado como realizado pelo admin (RF-06.13) |
| `jogo` | `lembrete_enviado_em` | TIMESTAMPTZ | — | Sim | — | — | Lembrete (RF-10.04) |
| `jogo` | `cancelado_por_equipa_id` | UUID | — | Sim | FK→equipa.id | — | Quem cancelou |
| `jogo` | `motivo_cancelamento` | TEXT | — | Sim | — | — | Motivo (RF-05.09) |
| `jogo` | `cancelado_em` | TIMESTAMPTZ | — | Sim | — | — | Quando foi cancelado (RN-24) |
| `jogo` | `criado_em` | TIMESTAMPTZ | — | Não | — | `now()` | Data de criação |

Restrições:
- `equipa_a_id <> equipa_b_id`
- `(golos_a IS NULL) = (golos_b IS NULL) AND golos_a >= 0 AND golos_b >= 0`

## comparencia

Comparência declarada por cada equipa (RF-07)

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `comparencia` | `id` | UUID | — | Não | PK | `gen_random_uuid()` | Identificador |
| `comparencia` | `jogo_id` | UUID | — | Não | FK→jogo.id, UK(jogo_id,equipa_id) | — | Jogo |
| `comparencia` | `equipa_id` | UUID | — | Não | FK→equipa.id | — | Equipa a que a comparência se refere |
| `comparencia` | `estado` | ENUM estado_comparencia | — | Não | — | `'nao_registada'` | Estado da comparência desta equipa |
| `comparencia` | `declarou_adversaria` | ENUM declaracao_adversaria | — | Sim | — | — | O que esta equipa declarou sobre a adversária |
| `comparencia` | `observacao` | TEXT | — | Sim | — | — | Observação (TEL-16) |
| `comparencia` | `declarado_por` | UUID | — | Sim | FK→utilizador.id | — | Quem declarou |
| `comparencia` | `declarado_em` | TIMESTAMPTZ | — | Sim | — | — | Quando declarou |
| `comparencia` | `prazo_resposta_ate` | TIMESTAMPTZ | — | Sim | — | — | Fim das 48 h para responder a falta declarada (RN-16) |

## submissao_resultado

Versões do resultado submetido por equipa (RF-06.08, RF-08.08)

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `submissao_resultado` | `id` | UUID | — | Não | PK | `gen_random_uuid()` | Identificador |
| `submissao_resultado` | `jogo_id` | UUID | — | Não | FK→jogo.id | — | Jogo |
| `submissao_resultado` | `equipa_id` | UUID | — | Não | FK→equipa.id | — | Equipa que submeteu |
| `submissao_resultado` | `golos_a` | SMALLINT | — | Não | — | — | Golos da equipa A (≥ 0) |
| `submissao_resultado` | `golos_b` | SMALLINT | — | Não | — | — | Golos da equipa B (≥ 0) |
| `submissao_resultado` | `versao` | SMALLINT | — | Não | UK(jogo_id,equipa_id,versao) | `1` | Nº da versão (correcções — RF-06.11) |
| `submissao_resultado` | `actual` | BOOLEAN | — | Não | — | `true` | Última versão desta equipa |
| `submissao_resultado` | `submetido_por` | UUID | — | Não | FK→utilizador.id | — | Quem submeteu |
| `submissao_resultado` | `criado_em` | TIMESTAMPTZ | — | Não | — | `now()` | Quando submeteu |

Restrições:
- `golos_a >= 0 AND golos_b >= 0`
- `UNIQUE (jogo_id, equipa_id) WHERE actual`

## caso_analise

Casos para o administrador (RF-08.07, RF-11.03)

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `caso_analise` | `id` | UUID | — | Não | PK | `gen_random_uuid()` | Identificador |
| `caso_analise` | `jogo_id` | UUID | — | Não | FK→jogo.id | — | Jogo em causa |
| `caso_analise` | `tipo` | ENUM tipo_caso | — | Não | — | — | Tipo de caso |
| `caso_analise` | `estado` | ENUM estado_caso | — | Não | — | `'aberto'` | Estado do caso |
| `caso_analise` | `aberto_por_equipa_id` | UUID | — | Sim | FK→equipa.id | — | Equipa que pediu (nulo se automático) |
| `caso_analise` | `motivo` | TEXT | — | Sim | — | — | Motivo do pedido |
| `caso_analise` | `decisao` | JSONB | — | Sim | — | — | Decisão aplicada (ex.: {golos_a:2, golos_b:1}) |
| `caso_analise` | `justificacao` | TEXT | — | Sim | — | — | Justificação obrigatória ao resolver (RF-11.04) |
| `caso_analise` | `resolvido_por` | UUID | — | Sim | FK→utilizador.id | — | Administrador |
| `caso_analise` | `criado_em` | TIMESTAMPTZ | — | Não | — | `now()` | Abertura |
| `caso_analise` | `resolvido_em` | TIMESTAMPTZ | — | Sim | — | — | Resolução |

Restrições:
- `estado <> 'resolvido' OR (justificacao IS NOT NULL AND resolvido_por IS NOT NULL)`

## notificacao

Notificações internas (RF-10)

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `notificacao` | `id` | UUID | — | Não | PK | `gen_random_uuid()` | Identificador |
| `notificacao` | `utilizador_id` | UUID | — | Não | FK→utilizador.id | — | Destinatário |
| `notificacao` | `tipo` | ENUM tipo_notificacao | — | Não | — | — | Tipo de evento |
| `notificacao` | `mensagem` | VARCHAR | 255 | Não | — | — | Texto |
| `notificacao` | `jogo_id` | UUID | — | Sim | FK→jogo.id | — | Jogo relacionado |
| `notificacao` | `solicitacao_id` | UUID | — | Sim | FK→solicitacao_jogo.id | — | Solicitação relacionada |
| `notificacao` | `lida_em` | TIMESTAMPTZ | — | Sim | — | — | Quando foi lida (nulo = não lida) |
| `notificacao` | `criado_em` | TIMESTAMPTZ | — | Não | — | `now()` | Criação |

## registo_auditoria

Histórico imutável de alterações (RN-12, RF-11.05)

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `registo_auditoria` | `id` | BIGINT | — | Não | PK | `identity` | Identificador sequencial |
| `registo_auditoria` | `entidade` | VARCHAR | 40 | Não | — | — | Tabela afectada (ex.: jogo) |
| `registo_auditoria` | `entidade_id` | UUID | — | Não | — | — | Registo afectado |
| `registo_auditoria` | `accao` | ENUM accao_auditoria | — | Não | — | — | Tipo de acção |
| `registo_auditoria` | `valor_anterior` | JSONB | — | Sim | — | — | Estado antes |
| `registo_auditoria` | `valor_novo` | JSONB | — | Sim | — | — | Estado depois |
| `registo_auditoria` | `motivo` | TEXT | — | Sim | — | — | Justificação (obrigatória em decisao_admin) |
| `registo_auditoria` | `utilizador_id` | UUID | — | Sim | FK→utilizador.id | — | Autor (nulo = sistema) |
| `registo_auditoria` | `criado_em` | TIMESTAMPTZ | — | Não | — | `now()` | Momento da alteração |

Restrições:
- Sem UPDATE/DELETE: só INSERT (permissões da BD — RNF-031)
- `accao <> 'decisao_admin' OR motivo IS NOT NULL`

## estatistica_equipa

Cache derivada para ranking e indicadores (RN-11, RNF-005)

| Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição |
|--------|----------|------|---------|------|-------|---------|-----------|
| `estatistica_equipa` | `equipa_id` | UUID | — | Não | PK, FK→equipa.id | — | Equipa |
| `estatistica_equipa` | `jogos_confirmados` | INTEGER | — | Não | — | `0` | J |
| `estatistica_equipa` | `vitorias` | INTEGER | — | Não | — | `0` | V |
| `estatistica_equipa` | `empates` | INTEGER | — | Não | — | `0` | E |
| `estatistica_equipa` | `derrotas` | INTEGER | — | Não | — | `0` | D |
| `estatistica_equipa` | `pontos` | INTEGER | — | Não | — | `0` | Pts = 3V + E |
| `estatistica_equipa` | `golos_marcados` | INTEGER | — | Não | — | `0` | Golos marcados |
| `estatistica_equipa` | `golos_sofridos` | INTEGER | — | Não | — | `0` | Golos sofridos |
| `estatistica_equipa` | `jogos_agendados` | INTEGER | — | Não | — | `0` | G (RN-11 §3.1) |
| `estatistica_equipa` | `comparencias` | INTEGER | — | Não | — | `0` | C |
| `estatistica_equipa` | `faltas_confirmadas` | INTEGER | — | Não | — | `0` | Faltas confirmadas |
| `estatistica_equipa` | `indice` | NUMERIC | 4,3 | Não | — | `0` | I = 0,6·A + 0,4·Cp |
| `estatistica_equipa` | `estrelas` | SMALLINT | — | Sim | — | — | 1–5; nulo = 'Nova' (RN-14) |
| `estatistica_equipa` | `actualizado_em` | TIMESTAMPTZ | — | Não | — | `now()` | Último recálculo |

## Enumerações

| Enum | Valores |
|------|---------|
| `papel_utilizador` | `utilizador`, `admin` |
| `estado_conta` | `activa`, `suspensa` |
| `papel_membro` | `responsavel` |
| `posicao_jogador` | `guarda_redes`, `defesa`, `medio`, `avancado` |
| `visibilidade_plantel` | `publico`, `autenticados`, `privado` |
| `estado_solicitacao` | `pendente`, `alteracao_proposta`, `aceite`, `recusada`, `cancelada` |
| `estado_jogo` | `agendado`, `aguarda_comparencia`, `aguarda_resultado`, `resultado_pendente`, `divergencia`, `em_analise`, `concluido`, `cancelado` |
| `estado_resultado` | `nao_submetido`, `aguarda_adversaria`, `confirmado`, `divergente`, `em_analise` |
| `estado_comparencia` | `nao_registada`, `compareceu_declarado`, `falta_declarada`, `em_analise`, `validada`, `falta_confirmada` |
| `declaracao_adversaria` | `compareceu`, `faltou` |
| `tipo_caso` | `divergencia_resultado`, `comparencia_contestada`, `comparencia_contraditoria`, `reabertura_resultado`, `jogo_fora_de_prazo` |
| `estado_caso` | `aberto`, `em_analise`, `resolvido`, `rejeitado` |
| `tipo_notificacao` | `solicitacao_recebida`, `solicitacao_aceite`, `solicitacao_recusada`, `alteracao_proposta`, `jogo_cancelado`, `lembrete_jogo`, `comparencia_submetida`, `falta_declarada`, `resultado_submetido`, `resultado_confirmado`, `resultado_divergente`, `caso_resolvido` |
| `accao_auditoria` | `criar`, `actualizar`, `eliminar`, `decisao_admin`, `automatico` |

## Correspondência com os estados da especificação (§7)

| Especificação | Enum | Valores |
|---------------|------|---------|
| Solicitação de jogo | `estado_solicitacao` | Pendente → `pendente`; Aceite/Confirmada → `aceite`; Recusada → `recusada`; Alteração proposta → `alteracao_proposta`; Cancelada → `cancelada` |
| Jogo | `estado_jogo` | Agendado → `agendado`; Em aguardo de comparência → `aguarda_comparencia`; Em aguardo de resultado → `aguarda_resultado`; Resultado pendente de confirmação → `resultado_pendente`; Divergência → `divergencia`; Cancelado → `cancelado`; Concluído → `concluido`; Resultado confirmado ⇒ `concluido` + `estado_resultado=confirmado`; acrescentado `em_analise` |
| Comparência por equipa | `estado_comparencia` | Não registada → `nao_registada`; Compareceu (declarado) → `compareceu_declarado`; Falta de comparência (declarada) → `falta_declarada`; Em divergência/análise → `em_analise`; Validada → `validada`; acrescentado `falta_confirmada` (RN-16) |
| Resultado | `estado_resultado` | Não submetido → `nao_submetido`; Aguardando submissão adversária → `aguarda_adversaria`; Confirmado → `confirmado`; Divergente → `divergente`; Em análise administrativa → `em_analise` |
