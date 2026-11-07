# Última actualização — GiraBairro

<!-- ESTADO:INICIO -->
## 📍 Estado actual

| | Tarefa | Issue | Entregável |
|---|--------|-------|------------|
| ✅ **Última tarefa feita** | M1-01a Diagrama de contexto do sistema | #13 | `img/contexto.png` + `src/contexto.mmd` |
| ⏭️ **Próxima tarefa** | M1-02 Identificar stakeholders | #14 | `docs/01-requisitos/stakeholders.md` |
<!-- ESTADO:FIM -->

## 🗒️ Registo de progresso — M1 Levantamento de Requisitos

| Data | Código | Issue | Tarefa | Entregáveis |
|------|--------|-------|--------|-------------|
| 2026-11-08 | M1-01 | #12 | Elaborar documento de visão | `docs/01-requisitos/visao.md` |
| 2026-11-08 | M1-01a | #13 | Diagrama de contexto do sistema | `img/contexto.png` + `src/contexto.mmd` |
<!-- REGISTO:FIM -->

> Notas do M1: os diagramas são escritos em **Mermaid** (`docs/01-requisitos/src/*.mmd`) e exportados para SVG/PNG com `python3 scripts/render_mermaid.py <ficheiro.mmd>` (Chrome headless). Os de estilo "Excalidraw" usam `look: handDrawn`. O `.mmd` pode ser importado no Excalidraw (*Mermaid to Excalidraw*) e no draw.io (*Arrange → Insert → Mermaid*) para acabamento. Motivo: o draw.io MCP ainda não está ligado (M0-10) e o disco do sistema está cheio, impedindo instalar ferramentas.

---

# Histórico — Configuração do repositório e backlog do MVP (M0)

**Data:** 2026-11-08 (actualizado)
**Repositório:** <https://github.com/lemosGit/GiraBairro>
**Base:** [`roteiro-engenharia-de-sistemas.md`](roteiro-engenharia-de-sistemas.md) + [`GiraBairro_MVP_Requisitos_Funcionais_Telas.md`](GiraBairro_MVP_Requisitos_Funcionais_Telas.md)

---

## 1. Resumo

| Item | Estado |
|------|--------|
| Repositório `lemosGit/GiraBairro` | ✅ Já existia (público); README reescrito |
| Labels (secção 4 do roteiro + personas) | ✅ 38 labels; labels por defeito do GitHub removidas |
| Milestones M0–M10 | ✅ 11 milestones |
| Issues do backlog do MVP | ✅ **123 issues**, todas com milestone, labels e dependências ligadas por número |
| Branch `develop` | ✅ Criada a partir de `master` e definida como **branch por defeito** |
| Protecção de `master` e `develop` | ✅ PR obrigatório, 1 aprovação, sem push directo/force push |
| Templates de issue e PR | ✅ `.github/` |
| Estrutura `docs/` | ✅ Pastas `00-gestao` … `06-entrega` com `img/` e `src/` |
| `CONTRIBUTING.md` | ✅ Branches, commits, códigos, DoR/DoD |
| Scripts reutilizáveis | ✅ `scripts/setup-github.sh`, `scripts/criar_issues.py`, `scripts/tarefas_mvp.py` |
| Quadro GitHub Projects (M0-05) | ✅ [GiraBairro — MVP](https://github.com/users/lemosGit/projects/6) — colunas 📥 Backlog → 📌 Pronto → 🔨 Em curso → 👀 Em revisão → ✅ Feito, 123 issues, campos Início/Fim/Estimativa |
| PR de configuração | ✅ #124 com merge em `master` |

**Distribuição por prioridade:** 86 *must* · 23 *should* · 6 *could* · 8 *won't* (app nativa, M8/M10-05).

---

## 2. Decisões tomadas na adaptação do roteiro ao GiraBairro

| Decisão | Motivo |
|---------|--------|
| `master` faz o papel de `main` | O repositório já usava `master`; evita renomear e partir clones existentes |
| `develop` como branch por defeito | Os PR abrem contra `develop` por defeito e o `Closes #N` fecha a issue no merge em `develop` — coincide com a coluna "Feito" da DoD |
| Proteção com `enforce_admins = false` | Com 1 aprovação obrigatória, um autor sozinho não consegue aprovar o próprio PR; o administrador pode fazer merge em caso de necessidade |
| Personas propostas **PER-01 a PER-05** | Derivadas da secção 2 (Atores): Visitante, Utilizador sem equipa, Responsável da equipa, Responsável de contacto, Administrador da plataforma. A confirmar em M1-03 |
| Nova task **M1-11 — Fechar decisões pendentes** | A secção 9 da especificação lista 10 decisões que condicionam RF, MER e segurança; ficam com `estado: precisa-info` |
| Nova task **M1-12 — Fórmula de ranking e estrelas** | A especificação marca a regra de estrelas como "por definir" (RN-11); bloqueia M6-09 |
| M2-08 (diagramas de estados) subiu de *could* para *should* | Os estados de solicitação, jogo, comparência e resultado são o núcleo do sistema |
| M5 ganhou **M5-06 Recuperação de palavra-passe** e **M5-09 Trilha de auditoria** | RF-01.07 e RN-12 / RF-08.08 / RF-11.05 são transversais e devem existir antes dos módulos |
| M6 dividido por módulo de RF (M6-01 … M6-14) | "1 issue por módulo/RF" (roteiro, M6) |
| M7-06 dividido em **1 issue por tela** (M7-06.01 … M7-06.19) | "1 issue por tela" (roteiro, M7); TEL-02/03 ficam em M7-04, TEL-22 (admin) em M7-07 |
| M8 e M10-05 com prioridade **won't** | A secção 8 da especificação põe a app nativa fora do MVP se a 1.ª versão for web responsiva. A decisão final é tomada em M3-01; se mudar, basta reclassificar |
| M3-08 (spike) concretizado: **SMS/OTP e WhatsApp em Angola** | Tecnologia de risco: recuperação de palavra-passe e decisão 10 (canal de notificações) |

---

## 3. Labels criadas

- **tipo:** feature, docs, bug, chore, refactor, test, spike
- **area:** gestão, requisitos, modelagem, arquitetura, ux-ui, backend, database, frontend, mobile, devops, qa
- **prioridade:** must, should, could, wont
- **estado:** bloqueado, precisa-info, em-revisão
- **tamanho:** XS, S, M, L, XL
- **ferramenta / entrega:** ferramenta: excalidraw, ferramenta: drawio, entrega: imagem
- **persona:** PER-01 … PER-05

Cada issue tem pelo menos 1 tipo, 1 área, 1 prioridade e 1 tamanho; as tasks de diagrama têm `ferramenta:` + `entrega: imagem` conforme a matriz 11.3 do roteiro.

---

## 4. Estrutura de cada issue

Título `[Mx-NN] Verbo + objecto` e corpo segundo o template de task:

- **Objectivo** — adaptado ao GiraBairro
- **Referências** — RF / RN / TEL da especificação e personas
- **Critérios de aceitação** — checklist
- **Dependências** — `Depende de: #N (Mx-NN)` e `Bloqueia: #N (Mx-NN)` (calculado automaticamente)
- **Entregável** — ficheiro em `docs/`, endpoint, tela…

---

## 5. Backlog criado por milestone

#### M0 — Setup & Governança (11 issues)

| Issue | Código | Tarefa | Prioridade | Tamanho |
|---|---|---|---|---|
| #1 | M0-01 | Criar repositório no GitHub (README, .gitignore, licença) | must | XS |
| #2 | M0-02 | Definir branches master e develop + regras de protecção | must | XS |
| #3 | M0-03 | Configurar labels | must | XS |
| #4 | M0-04 | Configurar milestones das fases | must | XS |
| #5 | M0-05 | Criar quadro no GitHub Projects (colunas + vistas) | must | S |
| #6 | M0-06 | Criar templates de issue e PR | should | XS |
| #7 | M0-07 | Criar estrutura de pastas docs/ | should | XS |
| #8 | M0-08 | Documentar convenções (CONTRIBUTING.md) | should | S |
| #9 | M0-09 | Definir papéis da equipa e rituais (daily, revisão semanal) | could | S |
| #10 | M0-10 | Ligar os conectores MCP do Excalidraw e do draw.io | must | XS |
| #11 | M0-11 | Instalar draw.io Desktop (exportação PNG/SVG por CLI) | should | XS |

#### M1 — Levantamento de Requisitos (17 issues)

| Issue | Código | Tarefa | Prioridade | Tamanho |
|---|---|---|---|---|
| #12 | M1-01 | Elaborar documento de visão do GiraBairro | must | S |
| #13 | M1-01a | Desenhar diagrama de contexto do sistema | must | S |
| #14 | M1-02 | Identificar stakeholders | must | S |
| #15 | M1-02a | Desenhar mapa de stakeholders (influência × interesse) | should | XS |
| #16 | M1-02b | Modelar processo AS-IS e TO-BE em BPMN | must | M |
| #17 | M1-03 | Definir personas (PER-01 a PER-05) | must | S |
| #18 | M1-03a | Desenhar jornada do utilizador por persona | should | M |
| #19 | M1-04 | Consolidar requisitos funcionais (RF-01 a RF-11) com persona | must | M |
| #20 | M1-05 | Levantar requisitos não funcionais por persona (RNF) | must | M |
| #21 | M1-06 | Consolidar regras de negócio (RN-01 a RN-13) | must | S |
| #22 | M1-11 | Fechar as decisões pendentes do MVP | must | S |
| #23 | M1-12 | Especificar a fórmula de ranking e estrelas | must | S |
| #24 | M1-07 | Priorizar requisitos (MoSCoW) | must | S |
| #25 | M1-07a | Desenhar quadro MoSCoW visual | could | XS |
| #26 | M1-08 | Escrever user stories com critérios de aceitação | should | L |
| #27 | M1-09 | Construir matriz de rastreabilidade (RF ↔ Persona ↔ US ↔ TEL) | could | S |
| #28 | M1-10 | Validar requisitos com o cliente/orientador | must | S |

#### M2 — Análise & Modelagem (9 issues)

| Issue | Código | Tarefa | Prioridade | Tamanho |
|---|---|---|---|---|
| #29 | M2-01 | Elaborar diagrama de casos de uso | must | M |
| #30 | M2-02 | Especificar os casos de uso principais | should | L |
| #31 | M2-03 | Elaborar Modelo Entidade-Relacionamento (MER) conceptual | must | M |
| #32 | M2-04 | Elaborar modelo lógico/físico | must | M |
| #33 | M2-05 | Elaborar dicionário de dados | must | M |
| #34 | M2-06 | Elaborar diagrama de classes | must | M |
| #35 | M2-07 | Elaborar diagramas de sequência dos casos de uso críticos | must | L |
| #36 | M2-08 | Elaborar diagramas de estados (solicitação, jogo, comparência, resultado) | should | M |
| #37 | M2-09 | Rever consistência da modelagem (MER ↔ classes ↔ dicionário) | must | S |

#### M3 — Arquitetura & Stack (8 issues)

| Issue | Código | Tarefa | Prioridade | Tamanho |
|---|---|---|---|---|
| #38 | M3-01 | Definir stack e tecnologias | must | M |
| #39 | M3-02 | Registar decisões em ADRs | should | S |
| #40 | M3-03 | Elaborar diagrama de arquitetura (C4: contexto e contentores) | must | S |
| #41 | M3-04 | Definir padrão arquitectural do backend | must | S |
| #42 | M3-05 | Elaborar contrato da API (OpenAPI) | must | L |
| #43 | M3-06 | Definir estratégia de segurança | must | M |
| #44 | M3-07 | Definir ambientes (dev, staging, prod) e variáveis | should | S |
| #45 | M3-08 | Investigar envio de SMS/OTP e WhatsApp em Angola | could | S |

#### M4 — UX/UI Design (6 issues)

| Issue | Código | Tarefa | Prioridade | Tamanho |
|---|---|---|---|---|
| #46 | M4-01 | Elaborar mapa de navegação / fluxo de telas por persona | must | S |
| #47 | M4-02 | Desenhar wireframes web (baixa fidelidade) | must | L |
| #48 | M4-03 | Desenhar wireframes mobile / responsivo (baixa fidelidade) | must | M |
| #49 | M4-04 | Criar design system (cores, tipografia, componentes) | should | M |
| #50 | M4-05 | Construir protótipo de alta fidelidade (Figma) | should | L |
| #51 | M4-06 | Validar protótipo com responsáveis de equipas | should | S |

#### M5 — Backend-1: Fundação (11 issues)

| Issue | Código | Tarefa | Prioridade | Tamanho |
|---|---|---|---|---|
| #52 | M5-01 | Inicializar projecto backend com a estrutura definida | must | S |
| #53 | M5-02 | Configurar Docker / docker-compose (app + BD) | should | S |
| #54 | M5-03 | Criar migrações da BD a partir do dicionário de dados | must | M |
| #55 | M5-04 | Criar seeds (localizações, posições, admin, equipas de teste) | should | S |
| #56 | M5-05 | Implementar autenticação por telefone e palavra-passe | must | M |
| #57 | M5-06 | Implementar recuperação/redefinição de palavra-passe | must | M |
| #58 | M5-07 | Implementar autorização por perfil (RBAC) | must | M |
| #59 | M5-08 | Implementar tratamento de erros, logs e validação padrão | must | S |
| #60 | M5-09 | Implementar trilha de auditoria (histórico de alterações) | must | M |
| #61 | M5-10 | Configurar pipeline CI (lint + testes em cada PR) | must | S |
| #62 | M5-11 | Servir documentação Swagger pela API | should | XS |

#### M6 — Backend-2: Módulos de negócio (14 issues)

| Issue | Código | Tarefa | Prioridade | Tamanho |
|---|---|---|---|---|
| #63 | M6-01 | Implementar módulo Utilizador — perfil | must | S |
| #64 | M6-02 | Implementar módulo Equipas | must | L |
| #65 | M6-03 | Implementar módulo Jogadores | must | M |
| #66 | M6-04 | Implementar módulo Contactos da equipa | must | S |
| #67 | M6-05 | Implementar módulo Solicitações de jogo | must | L |
| #68 | M6-06 | Implementar módulo Jogos (agenda, cancelamento, histórico) | must | M |
| #69 | M6-07 | Implementar módulo Comparência e seriedade | must | L |
| #70 | M6-08 | Implementar módulo Resultados e confirmação bilateral | must | L |
| #71 | M6-09 | Implementar módulo Ranking e estrelas | must | L |
| #72 | M6-10 | Implementar módulo Notificações internas | must | M |
| #73 | M6-11 | Implementar módulo Administração da plataforma | must | M |
| #74 | M6-12 | Implementar endpoint agregado do dashboard do responsável | should | S |
| #75 | M6-13 | Escrever testes unitários e de integração do backend | must | L |
| #76 | M6-14 | Integrar notificações externas (SMS/WhatsApp) | could | M |

#### M7 — Frontend-1: Telas primordiais (26 issues)

| Issue | Código | Tarefa | Prioridade | Tamanho |
|---|---|---|---|---|
| #77 | M7-01 | Inicializar projecto web + estrutura de pastas | must | S |
| #78 | M7-02 | Implementar design system (componentes base) | must | M |
| #79 | M7-03 | Implementar camada de comunicação com a API | must | S |
| #80 | M7-04 | Implementar telas de autenticação e gestão de sessão (TEL-02, TEL-03) | must | M |
| #81 | M7-05 | Implementar layout principal (menu por persona, rotas protegidas) | must | S |
| #82 | M7-06.01 | Implementar tela TEL-01 Página inicial / apresentação | must | M |
| #83 | M7-06.02 | Implementar tela TEL-04 Registo da equipa | must | M |
| #84 | M7-06.03 | Implementar tela TEL-05 Dashboard do responsável da equipa | must | M |
| #85 | M7-06.04 | Implementar tela TEL-06 Perfil e gestão da equipa | must | M |
| #86 | M7-06.05 | Implementar tela TEL-07 Lista de jogadores | must | M |
| #87 | M7-06.06 | Implementar tela TEL-08 Cadastro/edição de jogador | must | M |
| #88 | M7-06.07 | Implementar tela TEL-09 Gestão de contactos da equipa | must | M |
| #89 | M7-06.08 | Implementar tela TEL-10 Pesquisa/listagem de equipas | must | M |
| #90 | M7-06.09 | Implementar tela TEL-11 Perfil público de equipa | must | M |
| #91 | M7-06.10 | Implementar tela TEL-12 Solicitar/marcar jogo | must | M |
| #92 | M7-06.11 | Implementar tela TEL-13 Solicitações de jogos | must | M |
| #93 | M7-06.12 | Implementar tela TEL-14 Agenda/lista de jogos | must | M |
| #94 | M7-06.13 | Implementar tela TEL-15 Detalhes do jogo | must | M |
| #95 | M7-06.14 | Implementar tela TEL-16 Registo de comparência | must | M |
| #96 | M7-06.15 | Implementar tela TEL-17 Registo de resultado | must | M |
| #97 | M7-06.16 | Implementar tela TEL-18 Confirmação/divergência de resultado | must | M |
| #98 | M7-06.17 | Implementar tela TEL-19 Ranking de equipas | must | M |
| #99 | M7-06.18 | Implementar tela TEL-20 Notificações | must | M |
| #100 | M7-06.19 | Implementar tela TEL-21 Perfil do utilizador | must | M |
| #101 | M7-07 | Implementar painel administrativo (TEL-22) | should | L |
| #102 | M7-08 | Garantir responsividade e acessibilidade básica | should | M |

#### M8 — Frontend-2: Mobile (7 issues)

| Issue | Código | Tarefa | Prioridade | Tamanho |
|---|---|---|---|---|
| #103 | M8-01 | Inicializar projecto mobile | wont | S |
| #104 | M8-02 | Criar componentes base / tema mobile | wont | M |
| #105 | M8-03 | Implementar cliente da API + armazenamento seguro do token | wont | S |
| #106 | M8-04 | Implementar login e navegação mobile | wont | M |
| #107 | M8-05 | Implementar telas Must do responsável no mobile | wont | L |
| #108 | M8-06 | Implementar funcionalidades nativas (notificações push, offline) | wont | M |
| #109 | M8-07 | Gerar build de teste (APK) | wont | S |

#### M9 — Integração & QA (6 issues)

| Issue | Código | Tarefa | Prioridade | Tamanho |
|---|---|---|---|---|
| #110 | M9-01 | Elaborar plano de testes a partir dos critérios de aceitação | must | M |
| #111 | M9-02 | Implementar testes E2E dos fluxos críticos | must | L |
| #112 | M9-03 | Executar testes de RNF (desempenho, segurança, usabilidade) | should | M |
| #113 | M9-04 | Corrigir bugs encontrados | must | L |
| #114 | M9-05 | Realizar homologação/UAT com equipas piloto | must | M |
| #115 | M9-06 | Verificar matriz de rastreabilidade (RF Must cobertos) | must | S |

#### M10 — Deploy & Entrega (8 issues)

| Issue | Código | Tarefa | Prioridade | Tamanho |
|---|---|---|---|---|
| #116 | M10-01 | Configurar pipeline CD (deploy automático para staging) | must | M |
| #117 | M10-02 | Configurar ambiente de produção (servidor, domínio, HTTPS, BD) | must | M |
| #118 | M10-03 | Configurar backups e monitorização | should | S |
| #119 | M10-04 | Criar release v1.0.0 (merge em master + tag) | must | XS |
| #120 | M10-05 | Publicar app mobile | wont | S |
| #121 | M10-06 | Escrever manual do utilizador por persona | should | M |
| #122 | M10-07 | Escrever manual técnico / guia de instalação | must | M |
| #123 | M10-08 | Realizar retrospectiva do projecto | could | S |

---

## 6. Estado das tasks do M0

| Issue | Task | Estado |
|-------|------|--------|
| #1 M0-01 | Repositório, README, `.gitignore`, licença | 🟡 Aberta — falta escolher e adicionar a **licença** |
| #2 M0-02 | Branches + protecção | ✅ Fechada |
| #3 M0-03 | Labels | ✅ Fechada |
| #4 M0-04 | Milestones | ✅ Fechada (falta só definir datas-limite, opcional) |
| #5 M0-05 | Quadro GitHub Projects | ✅ Fechada (PR deste quadro) — falta só configurar as vistas na interface |
| #6 M0-06 | Templates de issue e PR | ✅ Fechada |
| #7 M0-07 | Estrutura `docs/` | ✅ Fechada |
| #8 M0-08 | `CONTRIBUTING.md` | ✅ Fechada |
| #9 M0-09 | Papéis da equipa e rituais | ⬜ Aberta — depende da equipa |
| #10 M0-10 | Conectores MCP Excalidraw + draw.io | ⬜ Aberta — Excalidraw já disponível no Claude; falta draw.io (`claude mcp add --transport http drawio https://mcp.draw.io/mcp`) |
| #11 M0-11 | draw.io Desktop | ⬜ Aberta |

### Quadro GitHub Projects (M0-05)

**Link:** <https://github.com/users/lemosGit/projects/6> (ligado ao repositório, público)

| Coluna (campo *Status*) | Significado | Issues iniciais |
|--------|-------------|-----------------|
| 📥 Backlog | Criada, ainda não está pronta para começar | todas as abertas |
| 📌 Pronto | Cumpre a *Definition of Ready* | — |
| 🔨 Em curso | Alguém está a trabalhar (tem responsável e branch) | — |
| 👀 Em revisão | PR aberto | — |
| ✅ Feito | Merge em `develop` + DoD cumprida | as fechadas do M0 |

Campos personalizados: **Início** (data), **Fim** (data), **Estimativa** (número). A milestone e as labels de cada issue aparecem automaticamente.

**Falta fazer à mão (a API do GitHub não permite criar vistas):** na interface do projecto, mudar o layout da vista para **Board** e criar as vistas *Por milestone* (agrupar por Milestone), *Roadmap* (layout Roadmap com Início/Fim), *Por responsável* (agrupar por Assignees) e *Bloqueados* (filtro `label:"estado: bloqueado"`).

Recriar/sincronizar: `python3 scripts/criar_quadro.py` (idempotente; adiciona issues novas em Backlog e move as fechadas para Feito, sem mexer nas que a equipa já moveu).

---

## 7. Próximos passos recomendados

1. Concluir M0-01 (licença), as vistas do quadro e M0-10/M0-11 (draw.io).
2. Definir **datas-limite** das milestones (`gh api -X PATCH repos/lemosGit/GiraBairro/milestones/<n> -f due_on=...`).
3. Arrancar o **M1** por M1-01 (visão) → M1-03 (personas) → **M1-11 (decisões pendentes)** e **M1-12 (ranking/estrelas)**, que bloqueiam a priorização e o módulo de ranking.
4. Trabalhar sempre a partir de `develop`: `git switch develop && git pull && git switch -c docs/<nº>-<slug>`.

---

## 8. Ficheiros adicionados/alterados nesta actualização

```
.github/ISSUE_TEMPLATE/task.md
.github/ISSUE_TEMPLATE/bug.md
.github/ISSUE_TEMPLATE/config.yml
.github/pull_request_template.md
CONTRIBUTING.md
README.md                          (reescrito)
docs/README.md + estrutura 00-gestao … 06-entrega
roteiro-engenharia-de-sistemas.md  (passa a estar versionado)
scripts/setup-github.sh            (labels + milestones, idempotente)
scripts/tarefas_mvp.py             (definição das 123 tarefas)
scripts/criar_issues.py            (cria/actualiza as issues, idempotente)
scripts/criar_quadro.py            (cria/sincroniza o quadro GitHub Projects)
ultima_atualizacao.md              (este relatório)
```
