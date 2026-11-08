# -*- coding: utf-8 -*-
"""
Backlog do MVP GiraBairro, organizado segundo o roteiro de engenharia
(roteiro-engenharia-de-sistemas.md) e a especificação funcional
(GiraBairro_MVP_Requisitos_Funcionais_Telas.md).

Cada tarefa: dict com
  code   — código Mx-NN (vai para o título)
  title  — verbo + objecto
  t, a   — tipo e área(s) (lista ou str)
  p      — prioridade MoSCoW
  s      — tamanho
  deps   — códigos de que depende
  ent    — entregável
  obj    — objectivo
  refs   — requisitos / regras / telas relacionados
  per    — personas afectadas (PER-0X)
  ac     — critérios de aceitação
  extra  — labels adicionais (ferramenta, entrega, estado)
"""

MILESTONES = {
    "M0": "M0 — Setup & Governança",
    "M1": "M1 — Levantamento de Requisitos",
    "M2": "M2 — Análise & Modelagem",
    "M3": "M3 — Arquitetura & Stack",
    "M4": "M4 — UX/UI Design",
    "M5": "M5 — Backend-1: Fundação",
    "M6": "M6 — Backend-2: Módulos de negócio",
    "M7": "M7 — Frontend-1: Telas primordiais",
    "M8": "M8 — Frontend-2: Mobile",
    "M9": "M9 — Integração & QA",
    "M10": "M10 — Deploy & Entrega",
}

DOC = "GiraBairro_MVP_Requisitos_Funcionais_Telas.md"
EXC = ["ferramenta: excalidraw", "entrega: imagem"]
DIO = ["ferramenta: drawio", "entrega: imagem"]

T = []


def task(code, title, t, a, p, s, deps=(), ent="", obj="", refs="", per=(), ac=(), extra=()):
    T.append(dict(code=code, title=title, t=t, a=a if isinstance(a, list) else [a], p=p, s=s,
                  deps=list(deps), ent=ent, obj=obj, refs=refs, per=list(per), ac=list(ac),
                  extra=list(extra)))


# ---------------------------------------------------------------- M0
task("M0-01", "Criar repositório no GitHub (README, .gitignore, licença)", "chore", "gestão", "must", "XS",
     ent="Repositório `lemosGit/GiraBairro`",
     obj="Ter o repositório central do projecto com README, `.gitignore` e licença.",
     ac=["Repositório acessível pela equipa", "README descreve o GiraBairro e aponta para `docs/`",
         "`.gitignore` adequado", "Licença escolhida e adicionada (`LICENSE`)"])
task("M0-02", "Definir branches master e develop + regras de protecção", "chore", "gestão", "must", "XS", ["M0-01"],
     ent="Branches `master` e `develop` protegidas",
     obj="Aplicar o Git Flow simplificado (o `master` do repositório faz o papel de `main` do roteiro).",
     ac=["`develop` criada a partir de `master`", "PR obrigatório + 1 aprovação em `master` e `develop`",
         "Push directo e force push proibidos"])
task("M0-03", "Configurar labels", "chore", "gestão", "must", "XS", ["M0-01"],
     ent="Labels da secção 4 do roteiro + labels de persona PER-01..PER-05",
     ac=["Labels por defeito do GitHub removidas", "Labels tipo/área/prioridade/estado/tamanho/ferramenta/persona criadas"])
task("M0-04", "Configurar milestones das fases", "chore", "gestão", "must", "XS", ["M0-01"],
     ent="Milestones M0–M10", ac=["11 milestones criadas", "Cada issue atribuída a uma milestone", "Datas-limite definidas pela equipa"])
task("M0-05", "Criar quadro no GitHub Projects (colunas + vistas)", "chore", "gestão", "must", "S", ["M0-03", "M0-04"],
     ent="Quadro activo ligado ao repositório",
     obj="Acompanhar o fluxo Backlog → Pronto → Em curso → Em revisão → Feito.",
     ac=["Colunas: Backlog, Pronto, Em curso, Em revisão, Feito", "Vistas: por milestone, roadmap, por responsável, bloqueados",
         "Campos: Início, Fim, Estimativa", "Todas as issues do repositório adicionadas ao quadro"])
task("M0-06", "Criar templates de issue e PR", "chore", "gestão", "should", "XS", ["M0-01"],
     ent="`.github/ISSUE_TEMPLATE/` e `.github/pull_request_template.md`",
     ac=["Template Task", "Template Bug", "Template de PR"])
task("M0-07", "Criar estrutura de pastas docs/", "docs", "gestão", "should", "XS", ["M0-01"],
     ent="Estrutura `docs/00-gestao` … `docs/06-entrega` (secção 6 do roteiro)",
     ac=["Pastas criadas com README curto", "Pastas `img/` e `src/` para diagramas"])
task("M0-08", "Documentar convenções (CONTRIBUTING.md)", "docs", "gestão", "should", "S", ["M0-02"],
     ent="`CONTRIBUTING.md`", ac=["Branches", "Conventional Commits", "Nomenclatura `[Mx-NN]`", "Códigos PER/RF/RNF/RN/US/UC/TEL", "DoR / DoD"])
task("M0-09", "Definir papéis da equipa e rituais (daily, revisão semanal)", "docs", "gestão", "could", "S",
     ent="`docs/00-gestao/equipa-e-papeis.md`", ac=["Tabela de responsáveis por área", "Calendário de rituais"])
task("M0-10", "Ligar os conectores MCP do Excalidraw e do draw.io", "chore", "gestão", "must", "XS",
     ent="Ambos respondem a um diagrama de teste (secção 11.2 do roteiro)",
     ac=["Excalidraw: desenha `Utilizador → Login → Dashboard`", "draw.io: gera diagrama de sequência Mermaid de login"])
task("M0-11", "Instalar draw.io Desktop (exportação PNG/SVG por CLI)", "chore", "gestão", "should", "XS", ["M0-10"],
     ent="`drawio --version` funciona", ac=["draw.io Desktop instalado em cada máquina que exporta diagramas"])

# ---------------------------------------------------------------- M1
task("M1-01", "Elaborar documento de visão do GiraBairro", "docs", "requisitos", "must", "S", ["M0-07"],
     ent="`docs/01-requisitos/visao.md`",
     obj="Descrever o problema (marcação informal de jogos entre equipas de bairro, resultados sem registo, falta de seriedade nas comparências), objectivos, âmbito e fora de âmbito do MVP.",
     refs=f"{DOC} — secções 1, 8 e 10",
     ac=["Problema e público-alvo descritos", "Objectivos do MVP listados", "Fora de âmbito (secção 8) explícito",
         "Princípio central: registo auditável de quem marcou, quem compareceu e que resultado foi confirmado"])
task("M1-01a", "Desenhar diagrama de contexto do sistema", "docs", "requisitos", "must", "S", ["M1-01"],
     ent="`docs/01-requisitos/src/contexto.excalidraw` + `img/contexto.png`",
     obj="Mostrar o GiraBairro ao centro com os actores (visitante, responsável de equipa, responsável de contacto, administrador da plataforma) e sistemas externos (SMS/WhatsApp para notificações e recuperação de palavra-passe, armazenamento de emblemas).",
     refs=f"{DOC} — secção 2", extra=EXC, ac=["Setas rotuladas com o que cada actor troca com o sistema", "PNG referenciado em `visao.md`"])
task("M1-02", "Identificar stakeholders", "docs", "requisitos", "must", "S", ["M1-01"],
     ent="`docs/01-requisitos/stakeholders.md`",
     obj="Listar stakeholders: responsáveis de equipas, jogadores, comunidade/bairro, administradores da plataforma, eventuais parceiros locais (administração municipal, associações), equipa de desenvolvimento, orientador.",
     ac=["Tabela com interesse, influência e expectativa de cada stakeholder"])
task("M1-02a", "Desenhar mapa de stakeholders (influência × interesse)", "docs", "requisitos", "should", "XS", ["M1-02"],
     ent="`img/stakeholders.png`", extra=EXC, ac=["Quadrantes influência × interesse preenchidos"])
task("M1-02b", "Modelar processo AS-IS e TO-BE em BPMN", "docs", "requisitos", "must", "M", ["M1-02"],
     ent="`img/processo-as-is.png`, `img/processo-to-be.png` + fontes `.drawio`",
     obj="AS-IS: marcação por telefone/WhatsApp, resultados sem registo, faltas sem consequência. TO-BE: solicitação → aceitação → jogo agendado → comparência por equipa → resultado bilateral → confirmação/divergência → ranking.",
     refs="RF-05, RF-06, RF-07, RF-08, RF-09", extra=DIO,
     ac=["Raias: Equipa desafiante, Equipa desafiada, Sistema, Administrador da plataforma", "Gateways para aceitar/recusar/propor alteração e resultado igual/divergente"])
task("M1-03", "Definir personas (PER-01 a PER-05)", "docs", "requisitos", "must", "S", ["M1-02"],
     ent="`docs/01-requisitos/personas.md`",
     obj="Proposta: PER-01 Visitante; PER-02 Utilizador registado sem equipa; PER-03 Responsável/Administrador da equipa; PER-04 Responsável de contacto; PER-05 Administrador da plataforma.",
     refs=f"{DOC} — secção 2 (Atores)", per=["PER-01", "PER-02", "PER-03", "PER-04", "PER-05"],
     ac=["Cada persona com objectivos, dores, contexto de uso (dispositivo, rede) e permissões", "Códigos usados em todos os artefactos seguintes"])
task("M1-03a", "Desenhar jornada do utilizador por persona", "docs", "requisitos", "should", "M", ["M1-03"],
     ent="`img/jornada-PER-0X.png`", extra=EXC, per=["PER-03", "PER-05"],
     ac=["Jornada do PER-03: criar conta → registar equipa → plantel → marcar jogo → comparência → resultado → ranking", "Acção, dor e oportunidade em cada etapa"])
task("M1-04", "Consolidar requisitos funcionais (RF-01 a RF-11) com persona", "docs", "requisitos", "must", "M", ["M1-03"],
     ent="`docs/01-requisitos/requisitos-funcionais.md`",
     obj="Migrar os RF da especificação existente para o formato do roteiro, mantendo os códigos RF-XX.YY e associando a persona de cada um.",
     refs=f"{DOC} — secção 3",
     ac=["Tabela: Código | Descrição | Persona | Prioridade | Origem", "Todos os RF-01.01 … RF-11.06 presentes"])
task("M1-05", "Levantar requisitos não funcionais por persona (RNF)", "docs", "requisitos", "must", "M", ["M1-03"],
     ent="`docs/01-requisitos/requisitos-nao-funcionais.md`",
     obj="Ex.: web responsiva mobile-first; uso em redes móveis lentas; interface em português; privacidade dos telefones dos contactos; auditoria de alterações (RN-12); disponibilidade; segurança das palavras-passe.",
     ac=["Cada RNF com código RNF-NNN, persona e métrica verificável"])
task("M1-06", "Consolidar regras de negócio (RN-01 a RN-13)", "docs", "requisitos", "must", "S", ["M1-04"],
     ent="`docs/01-requisitos/regras-negocio.md`", refs=f"{DOC} — secção 4",
     ac=["Todas as RN com código e RF relacionados", "Regras resultantes de M1-11 e M1-12 acrescentadas"])
task("M1-11", "Fechar as decisões pendentes do MVP", "docs", "requisitos", "must", "S", ["M1-03"],
     ent="`docs/00-gestao/actas/decisoes-mvp.md`",
     obj="Responder às 10 decisões da secção 9 da especificação antes da priorização.",
     refs=f"{DOC} — secção 9", extra=["estado: precisa-info"],
     ac=["1. Estrelas e ranking (ver M1-12)", "2. Falta de comparência: declaração basta ou exige confirmação/validação?",
         "3. Contactos públicos para todos ou só para autenticados?", "4. Um responsável pode administrar mais de uma equipa?",
         "5. Jogos só entre equipas registadas?", "6. Quem decide o resultado divergente?",
         "7. Reabrir resultado confirmado: possível? quem?", "8. Ranking: bairro, município, província e geral?",
         "9. Plantel público no perfil da equipa?", "10. Notificações só internas ou também SMS/WhatsApp?"])
task("M1-12", "Especificar a fórmula de ranking e estrelas", "docs", "requisitos", "must", "S", ["M1-11"],
     ent="Secção em `regras-negocio.md` (RN-11) com fórmula e exemplos",
     obj="Definir quantas estrelas existem, como são calculadas (vitórias, comparência, pontos) e os critérios de desempate do ranking.",
     refs="RF-09, RF-09.11, RN-09, RN-10, RN-11", extra=["estado: precisa-info"],
     ac=["Fórmula explícita e transparente", "Critérios de desempate definidos", "3 exemplos numéricos resolvidos", "Texto pronto para a explicação pública (TEL-19)"])
task("M1-07", "Priorizar requisitos (MoSCoW)", "docs", "requisitos", "must", "S", ["M1-04", "M1-05", "M1-11"],
     ent="Coluna de prioridade nos RF/RNF", ac=["Todos os RF e RNF com Must/Should/Could/Won't", "Justificação para cada Won't"])
task("M1-07a", "Desenhar quadro MoSCoW visual", "docs", "requisitos", "could", "XS", ["M1-07"],
     ent="`img/moscow.png`", extra=EXC, ac=["4 colunas com os códigos RF/RNF"])
task("M1-08", "Escrever user stories com critérios de aceitação", "docs", "requisitos", "should", "L", ["M1-07"],
     ent="`docs/01-requisitos/user-stories.md`",
     ac=["US-NNN para cada RF Must/Should", "Critérios de aceitação no formato Dado/Quando/Então"])
task("M1-09", "Construir matriz de rastreabilidade (RF ↔ Persona ↔ US ↔ TEL)", "docs", "requisitos", "could", "S", ["M1-08"],
     ent="`docs/01-requisitos/rastreabilidade.md`", ac=["Cada RF ligado a persona, US e tela (TEL-01..TEL-22)"])
task("M1-10", "Validar requisitos com o cliente/orientador", "docs", "requisitos", "must", "S", ["M1-07", "M1-12"],
     ent="Acta de aprovação em `docs/00-gestao/actas/`", ac=["Requisitos e decisões aprovados", "Alterações registadas"])

# ---------------------------------------------------------------- M2
UCS = ("UC01 Criar conta (RF-01) · UC02 Iniciar/terminar sessão · UC03 Recuperar palavra-passe · UC04 Registar equipa (RF-02) · "
       "UC05 Gerir jogadores (RF-03) · UC06 Gerir contactos (RF-04) · UC07 Pesquisar equipas (RF-02.08, RF-05.01/02) · "
       "UC08 Solicitar jogo (RF-05.03/04) · UC09 Responder a solicitação: aceitar/recusar/propor alteração (RF-05.05/06) · "
       "UC10 Cancelar jogo (RF-05.09) · UC11 Registar comparência (RF-07) · UC12 Submeter resultado (RF-06.06–06.11) · "
       "UC13 Resolver divergência / solicitar análise (RF-08) · UC14 Consultar ranking (RF-09) · UC15 Consultar notificações (RF-10) · "
       "UC16 Moderar contas e equipas (RF-11.02) · UC17 Analisar divergência e corrigir registo (RF-11.03/04)")
task("M2-01", "Elaborar diagrama de casos de uso", "docs", "modelagem", "must", "M", ["M1-10"],
     ent="`docs/02-modelagem/src/casos-de-uso.drawio` + `img/casos-de-uso.png`",
     obj="Actores = personas PER-01..PER-05. Casos de uso propostos: " + UCS, extra=DIO,
     ac=["Fronteira do sistema GiraBairro", "<<include>>/<<extend>> onde fizer sentido (ex.: UC13 estende UC12)"])
task("M2-02", "Especificar os casos de uso principais", "docs", "modelagem", "should", "L", ["M2-01"],
     ent="`docs/02-modelagem/casos-de-uso/especificacao-casos-uso.md`",
     obj="Fluxo principal, alternativos, pré/pós-condições para UC04, UC08, UC09, UC11, UC12, UC13, UC14.",
     ac=["Cada UC Must especificado", "Regras RN referenciadas em cada passo"])
task("M2-03", "Elaborar Modelo Entidade-Relacionamento (MER) conceptual", "docs", ["modelagem", "database"], "must", "M", ["M1-10"],
     ent="`mer-conceptual.drawio` + `.mmd` + `.png`",
     obj="Entidades previstas: Utilizador, Equipa, Jogador, ContactoEquipa, Localização (Província › Município › Bairro), SolicitacaoJogo, PropostaAlteracao, Jogo, Comparencia (por equipa), SubmissaoResultado (por equipa), CasoAnalise/Divergência, Notificação, HistoricoAlteracao (auditoria).",
     extra=DIO, ac=["Cardinalidades correctas (ex.: Jogo 1—2 Comparencia, Jogo 1—N SubmissaoResultado)", "Código Mermaid `erDiagram` versionado"])
task("M2-04", "Elaborar modelo lógico/físico", "docs", "database", "must", "M", ["M2-03"],
     ent="`mer-logico.drawio` + `.png`", extra=DIO,
     ac=["Tabelas, PK, FK, UK (ex.: telefone único — RF-01.03; nº camisola único por equipa activa — RN-04)"])
task("M2-05", "Elaborar dicionário de dados", "docs", "database", "must", "M", ["M2-04"],
     ent="`docs/02-modelagem/dicionario-dados.md`",
     ac=["Formato: Tabela | Atributo | Tipo | Tamanho | Nulo | Chave | Default | Descrição", "Enums dos estados da secção 7 da especificação"])
task("M2-06", "Elaborar diagrama de classes", "docs", "modelagem", "must", "M", ["M2-03", "M2-01"],
     ent="`classes.drawio` + `.mmd` + `.png`", extra=DIO,
     ac=["Atributos com tipo, métodos principais, visibilidade", "Regras RN-04, RN-07, RN-08 reflectidas nos métodos"])
task("M2-07", "Elaborar diagramas de sequência dos casos de uso críticos", "docs", "modelagem", "must", "L", ["M2-02", "M2-06"],
     ent="`sequencia-UC0X.mmd` + `.drawio` + `.png`",
     obj="UC02 login, UC08+UC09 solicitação/aceitação, UC11 comparência, UC12 resultado bilateral, UC13 divergência e análise.",
     extra=DIO, ac=["Participantes: PER-03, Frontend Web, API, BD, Serviço de notificações", "Blocos `alt` para divergência e recusa", "Códigos HTTP indicados"])
task("M2-08", "Elaborar diagramas de estados (solicitação, jogo, comparência, resultado)", "docs", "modelagem", "should", "M", ["M2-02"],
     ent="`estados-*.drawio` + `.png`",
     obj="Os estados são o núcleo do GiraBairro (secção 7 da especificação); por isso a prioridade sobe de Could para Should.",
     extra=DIO, ac=["4 máquinas de estados com transições e eventos", "Consistentes com o dicionário de dados"])
task("M2-09", "Rever consistência da modelagem (MER ↔ classes ↔ dicionário)", "docs", "modelagem", "must", "S", ["M2-05", "M2-06", "M2-07"],
     ent="Checklist de revisão", ac=["Nomes iguais em todos os artefactos", "Todos os diagramas com fonte + PNG em `docs/`"])

# ---------------------------------------------------------------- M3
task("M3-01", "Definir stack e tecnologias", "docs", "arquitetura", "must", "M", ["M1-07"],
     ent="`docs/03-arquitetura/stack.md` com justificação por RNF",
     obj="Stack decidida pelo dono do produto: Next.js (web), FastAPI (API), React Native (app), PostgreSQL. Justificar por RNF e detalhar bibliotecas, alojamento e ferramentas.",
     ac=["Cada escolha justificada por RNF", "Decisão sobre mobile registada"])
task("M3-02", "Registar decisões em ADRs", "docs", "arquitetura", "should", "S", ["M3-01"],
     ent="`docs/03-arquitetura/adr/ADR-001-*.md`", ac=["ADR por decisão: stack, mobile, autenticação, cálculo do ranking"])
task("M3-03", "Elaborar diagrama de arquitetura (C4: contexto e contentores)", "docs", "arquitetura", "must", "S", ["M3-01"],
     ent="`arquitetura-c4.drawio` + `.png`", extra=DIO, ac=["Protocolos nas setas", "Versão simplificada para o cliente (Excalidraw)"])
task("M3-04", "Definir padrão arquitectural do backend", "docs", "arquitetura", "must", "S", ["M3-01", "M2-06"],
     ent="Estrutura de pastas do código", ac=["Camadas definidas", "Módulos: auth, equipas, jogadores, contactos, jogos, comparência, resultados, ranking, notificações, admin"])
task("M3-05", "Elaborar contrato da API (OpenAPI)", "docs", ["arquitetura", "backend"], "must", "L", ["M2-07", "M3-01"],
     ent="`docs/03-arquitetura/openapi.yaml`", ac=["Endpoints de todos os RF Must", "Esquemas de erro padrão", "Exemplos de pedido/resposta"])
task("M3-06", "Definir estratégia de segurança", "docs", "arquitetura", "must", "M", ["M3-01", "M1-05"],
     ent="`docs/03-arquitetura/seguranca.md`",
     obj="Autenticação por telefone + palavra-passe, recuperação (OTP/SMS), RBAC (PER-03 só gere a sua equipa — RN-13; PER-05 admin), privacidade dos contactos (decisão 3), auditoria (RF-11.05, RN-12).",
     ac=["Matriz persona × permissão", "Política de palavras-passe e tokens", "Tratamento de dados pessoais (telefones)"])
task("M3-07", "Definir ambientes (dev, staging, prod) e variáveis", "docs", "devops", "should", "S", ["M3-01"],
     ent="`docs/03-arquitetura/ambientes.md`", ac=["Lista de variáveis de ambiente por ambiente"])
task("M3-08", "Investigar envio de SMS/OTP e WhatsApp em Angola", "spike", "arquitetura", "could", "S", ["M3-01"],
     ent="Relatório curto", obj="Avaliar fornecedores, custo e fiabilidade para recuperação de palavra-passe e notificações externas (decisão 10).",
     ac=["2–3 fornecedores comparados", "Recomendação"])

# ---------------------------------------------------------------- M4
task("M4-01", "Elaborar mapa de navegação / fluxo de telas por persona", "docs", "ux-ui", "must", "S", ["M2-01"],
     ent="Esboço `.excalidraw` → final `.drawio` em `docs/04-ux-ui/`",
     refs=f"{DOC} — secções 5 e 6", extra=["ferramenta: excalidraw", "ferramenta: drawio", "entrega: imagem"],
     ac=["Navegação do PER-03, do PER-01/02 e do PER-05", "TEL-01..TEL-22 todas ligadas"])
task("M4-02", "Desenhar wireframes web (baixa fidelidade)", "docs", "ux-ui", "must", "L", ["M4-01"],
     ent="`docs/04-ux-ui/wireframes/`", ac=["Uma wireframe por tela TEL-01..TEL-22", "Estados vazios e de erro nas telas de jogos"])
task("M4-03", "Desenhar wireframes mobile / responsivo (baixa fidelidade)", "docs", "ux-ui", "must", "M", ["M4-01"],
     ent="`docs/04-ux-ui/wireframes/mobile/`", obj="A maioria dos responsáveis usará o telemóvel: desenhar mobile-first.",
     ac=["Telas Must em largura de telemóvel"])
task("M4-04", "Criar design system (cores, tipografia, componentes)", "docs", "ux-ui", "should", "M", ["M4-02"],
     ent="Guia de estilos", ac=["Identidade visual GiraBairro", "Componentes: estrela, badge de estado, cartão de equipa, cartão de jogo"])
task("M4-05", "Construir protótipo de alta fidelidade (Figma)", "docs", "ux-ui", "should", "L", ["M4-04"],
     ent="Link do protótipo", ac=["Fluxo completo: marcar jogo → comparência → resultado → ranking"])
task("M4-06", "Validar protótipo com responsáveis de equipas", "docs", "ux-ui", "should", "S", ["M4-05"],
     ent="Feedback registado", ac=["Testado com pelo menos 3 responsáveis de equipas reais"])

# ---------------------------------------------------------------- M5
task("M5-01", "Inicializar projecto backend com a estrutura definida", "chore", "backend", "must", "S", ["M3-04"], ent="Projecto a correr localmente")
task("M5-02", "Configurar Docker / docker-compose (app + BD)", "chore", "devops", "should", "S", ["M5-01"], ent="`docker-compose.yml`")
task("M5-03", "Criar migrações da BD a partir do dicionário de dados", "feature", "database", "must", "M", ["M2-05", "M5-01"],
     ent="Migrações", ac=["Restrições UK: telefone (RF-01.03), camisola por equipa activa (RN-04), equipa+bairro (RF-02.09)"])
task("M5-04", "Criar seeds (localizações, posições, admin, equipas de teste)", "chore", "database", "should", "S", ["M5-03"],
     ent="Scripts de seed", ac=["Províncias, municípios e bairros", "Posições: guarda-redes, defesa, médio, avançado", "Utilizador administrador", "Equipas e jogos de exemplo"])
task("M5-05", "Implementar autenticação por telefone e palavra-passe", "feature", "backend", "must", "M", ["M3-06", "M5-03"],
     ent="Endpoints auth", refs="RF-01.01–RF-01.05", per=["PER-02", "PER-03"],
     ac=["Registo com nome, telefone e palavra-passe", "Telefone único", "Login e logout com tokens"])
task("M5-06", "Implementar recuperação/redefinição de palavra-passe", "feature", "backend", "must", "M", ["M5-05"],
     ent="Endpoints de recuperação", refs="RF-01.07", ac=["Fluxo de código de verificação com expiração"])
task("M5-07", "Implementar autorização por perfil (RBAC)", "feature", "backend", "must", "M", ["M5-05"],
     ent="Middleware de permissões", refs="RN-02, RN-13",
     ac=["Responsável só altera a sua equipa e os seus jogos", "Rotas de administração só para PER-05", "Contas/equipas suspensas bloqueadas"])
task("M5-08", "Implementar tratamento de erros, logs e validação padrão", "feature", "backend", "must", "S", ["M5-01"], ent="Middleware global")
task("M5-09", "Implementar trilha de auditoria (histórico de alterações)", "feature", ["backend", "database"], "must", "M", ["M5-03"],
     ent="Serviço de auditoria reutilizável", refs="RN-12, RF-08.08, RF-11.05",
     ac=["Guarda utilizador, data, entidade, valor anterior/novo e motivo", "Usado por jogos, comparências e resultados"])
task("M5-10", "Configurar pipeline CI (lint + testes em cada PR)", "chore", "devops", "must", "S", ["M5-01"], ent="GitHub Actions")
task("M5-11", "Servir documentação Swagger pela API", "docs", "backend", "should", "XS", ["M3-05", "M5-01"], ent="`/docs` acessível")

# ---------------------------------------------------------------- M6
task("M6-01", "Implementar módulo Utilizador — perfil", "feature", "backend", "must", "S", ["M5-07"],
     ent="Endpoints + testes", refs="RF-01.06", per=["PER-02", "PER-03"], ac=["Consultar/editar dados básicos", "Alterar palavra-passe"])
task("M6-02", "Implementar módulo Equipas", "feature", "backend", "must", "L", ["M5-07"],
     ent="Endpoints + testes", refs="RF-02.01–RF-02.09, RN-01, RN-02", per=["PER-03"],
     ac=["Criador fica como responsável", "Upload de emblema", "Perfil público", "Pesquisa por nome e localização", "Bloqueio de duplicados (nome + bairro)"])
task("M6-03", "Implementar módulo Jogadores", "feature", "backend", "must", "M", ["M6-02"],
     ent="Endpoints + testes", refs="RF-03, RN-03, RN-04", per=["PER-03"],
     ac=["CRUD com desactivação", "Nº de camisola único no plantel activo", "Posições pré-definidas"])
task("M6-04", "Implementar módulo Contactos da equipa", "feature", "backend", "must", "S", ["M6-02"],
     ent="Endpoints + testes", refs="RF-04", per=["PER-03", "PER-04"],
     ac=["Vários contactos, um principal", "Visibilidade conforme decisão 3 (M1-11)"])
task("M6-05", "Implementar módulo Solicitações de jogo", "feature", "backend", "must", "L", ["M6-02"],
     ent="Endpoints + testes", refs="RF-05.01–RF-05.08, RN-05", per=["PER-03"],
     ac=["Estados: pendente, aceite, recusada, alteração proposta, cancelada", "Propor nova data/hora/local", "Jogo criado apenas após aceitação"])
task("M6-06", "Implementar módulo Jogos (agenda, cancelamento, histórico)", "feature", "backend", "must", "M", ["M6-05", "M5-09"],
     ent="Endpoints + testes", refs="RF-05.09–RF-05.11, RF-06.01, RF-06.02, RF-06.12, RF-06.13",
     ac=["Identificador único", "Mandante/visitante", "Cancelamento com motivo", "Listagem por estado", "Histórico por equipa"])
task("M6-07", "Implementar módulo Comparência e seriedade", "feature", "backend", "must", "L", ["M6-06"],
     ent="Endpoints + testes", refs="RF-06.03–RF-06.05, RF-07, RN-06, RN-07",
     ac=["Comparência declarada separadamente por equipa, só após a data do jogo", "Declaração unilateral de falta não confirma falta da adversária",
         "Contradições sinalizadas", "Indicadores: agendados, compareceu, faltas"])
task("M6-08", "Implementar módulo Resultados e confirmação bilateral", "feature", "backend", "must", "L", ["M6-06", "M5-09"],
     ent="Endpoints + testes", refs="RF-06.06–RF-06.11, RF-08, RN-08, RN-09",
     ac=["Submissão separada por equipa", "Confirmado quando iguais; divergente quando diferentes", "Correcção antes da confirmação",
         "Encaminhar para análise do admin", "Histórico de submissões"])
task("M6-09", "Implementar módulo Ranking e estrelas", "feature", "backend", "must", "L", ["M6-07", "M6-08", "M1-12"],
     ent="Endpoints + testes", refs="RF-09, RN-10, RN-11",
     ac=["Ranking geral, por bairro, município e província", "V/E/D apenas de resultados confirmados", "Estrelas pela fórmula de M1-12",
         "Recalculado quando resultado/comparência é confirmado", "Endpoint público com os critérios"])
task("M6-10", "Implementar módulo Notificações internas", "feature", "backend", "must", "M", ["M6-05"],
     ent="Endpoints + testes", refs="RF-10",
     ac=["Eventos: solicitação recebida/aceite/recusada, alteração/cancelamento, lembrete de jogo, comparência/resultado submetido, divergência",
         "Estado lida/não lida", "Tarefa agendada para lembretes (RF-10.04)"])
task("M6-11", "Implementar módulo Administração da plataforma", "feature", "backend", "must", "M", ["M6-08", "M5-09"],
     ent="Endpoints + testes", refs="RF-11, RF-08.07", per=["PER-05"],
     ac=["Consultar utilizadores e equipas", "Suspender/reactivar", "Analisar divergências e corrigir com justificação (auditado)", "Indicadores gerais"])
task("M6-12", "Implementar endpoint agregado do dashboard do responsável", "feature", "backend", "should", "S", ["M6-09", "M6-10"],
     ent="Endpoint + testes", refs="TEL-05", per=["PER-03"],
     ac=["Próximos jogos, solicitações pendentes, jogos por confirmar, total de jogadores, V/E/D, posição no ranking, estrelas"])
task("M6-13", "Escrever testes unitários e de integração do backend", "test", "backend", "must", "L", ["M5-10"],
     ent="Relatório de cobertura", obj="Contínuo ao longo de M6; foco nas regras RN-04, RN-05, RN-07, RN-08, RN-09.",
     ac=["Cobertura mínima acordada pela equipa", "Testes das máquinas de estados"])
task("M6-14", "Integrar notificações externas (SMS/WhatsApp)", "feature", "backend", "could", "M", ["M6-10", "M3-08"],
     ent="Integração + testes", refs="RF-10, decisão 10", ac=["Só se a decisão 10 (M1-11) o incluir no MVP"])

# ---------------------------------------------------------------- M7
task("M7-01", "Inicializar projecto web + estrutura de pastas", "chore", "frontend", "must", "S", ["M3-01"], ent="Projecto a correr")
task("M7-02", "Implementar design system (componentes base)", "feature", "frontend", "must", "M", ["M4-04", "M7-01"],
     ent="Botões, inputs, tabelas, layout, estrelas, badges de estado")
task("M7-03", "Implementar camada de comunicação com a API", "feature", "frontend", "must", "S", ["M3-05", "M7-01"], ent="Serviço de API com interceptors")
task("M7-04", "Implementar telas de autenticação e gestão de sessão (TEL-02, TEL-03)", "feature", "frontend", "must", "M", ["M5-05", "M5-06", "M7-03"],
     ent="Registo, login e recuperação de palavra-passe", refs="RF-01, TEL-02, TEL-03", per=["PER-02"])
task("M7-05", "Implementar layout principal (menu por persona, rotas protegidas)", "feature", "frontend", "must", "S", ["M7-04"],
     ent="Navegação", refs=f"{DOC} — secção 6", ac=["Menus distintos para visitante, responsável e admin"])

SCREENS = [
    ("01", "TEL-01 Página inicial / apresentação", ["M7-05", "M6-09"], "must", "PER-01"),
    ("02", "TEL-04 Registo da equipa", ["M7-05", "M6-02"], "must", "PER-02"),
    ("03", "TEL-05 Dashboard do responsável da equipa", ["M7-05", "M6-12"], "must", "PER-03"),
    ("04", "TEL-06 Perfil e gestão da equipa", ["M7-05", "M6-02"], "must", "PER-03"),
    ("05", "TEL-07 Lista de jogadores", ["M7-05", "M6-03"], "must", "PER-03"),
    ("06", "TEL-08 Cadastro/edição de jogador", ["M7-05", "M6-03"], "must", "PER-03"),
    ("07", "TEL-09 Gestão de contactos da equipa", ["M7-05", "M6-04"], "must", "PER-03"),
    ("08", "TEL-10 Pesquisa/listagem de equipas", ["M7-05", "M6-02"], "must", "PER-01"),
    ("09", "TEL-11 Perfil público de equipa", ["M7-05", "M6-02", "M6-09"], "must", "PER-01"),
    ("10", "TEL-12 Solicitar/marcar jogo", ["M7-05", "M6-05"], "must", "PER-03"),
    ("11", "TEL-13 Solicitações de jogos", ["M7-05", "M6-05"], "must", "PER-03"),
    ("12", "TEL-14 Agenda/lista de jogos", ["M7-05", "M6-06"], "must", "PER-03"),
    ("13", "TEL-15 Detalhes do jogo", ["M7-05", "M6-06"], "must", "PER-03"),
    ("14", "TEL-16 Registo de comparência", ["M7-05", "M6-07"], "must", "PER-03"),
    ("15", "TEL-17 Registo de resultado", ["M7-05", "M6-08"], "must", "PER-03"),
    ("16", "TEL-18 Confirmação/divergência de resultado", ["M7-05", "M6-08"], "must", "PER-03"),
    ("17", "TEL-19 Ranking de equipas", ["M7-05", "M6-09"], "must", "PER-01"),
    ("18", "TEL-20 Notificações", ["M7-05", "M6-10"], "must", "PER-03"),
    ("19", "TEL-21 Perfil do utilizador", ["M7-05", "M6-01"], "must", "PER-02"),
]
for n, name, deps, prio, per in SCREENS:
    tel = name.split()[0]
    task(f"M7-06.{n}", f"Implementar tela {name}", "feature", "frontend", prio, "M", deps,
         ent="Tela ligada à API", refs=f"{tel} ({DOC} — secção 5)", per=[per],
         ac=[f"Todos os elementos listados em {tel} presentes", "Conforme wireframe/protótipo (M4)", "Estados de carregamento, vazio e erro", "Funciona em largura de telemóvel"])
task("M7-07", "Implementar painel administrativo (TEL-22)", "feature", "frontend", "should", "L", ["M7-05", "M6-11"],
     ent="Telas de administração", refs="TEL-22, RF-11", per=["PER-05"],
     ac=["Totais", "Casos pendentes/divergentes", "Suspensão/reactivação", "Análise e correcção de divergências com justificação"])
task("M7-08", "Garantir responsividade e acessibilidade básica", "feature", "frontend", "should", "M", ["M7-06.18"],
     ent="Checklist", ac=["Mobile-first", "Contraste e tamanhos de toque adequados", "Bom desempenho em rede móvel lenta"])

# ---------------------------------------------------------------- M8 (no MVP — decisão M3-01: React Native)
MOB = "App mobile em **React Native** (decisão do dono do produto em M3-01, ADR-003). Consome a mesma API FastAPI que a web; foco no PER-03 (responsável de equipa) e no dia do jogo."
for code, title, t, p, s, deps, ac in [
    ("M8-01", "Inicializar projecto mobile React Native (Expo)", "chore", "must", "S", ["M3-01"],
     ["Projecto Expo + TypeScript a correr em emulador Android e dispositivo", "Estrutura de pastas definida em M3-04"]),
    ("M8-02", "Criar componentes base / tema mobile", "feature", "must", "M", ["M4-04", "M8-01"],
     ["Tema partilhado com o design system (cores, tipografia)", "Componentes: botão, input, cartão de jogo, badge de estado, estrelas"]),
    ("M8-03", "Implementar cliente da API + armazenamento seguro do token", "feature", "must", "S", ["M3-05", "M8-01"],
     ["Cliente gerado/tipado a partir do OpenAPI", "Token em SecureStore", "Renovação automática do token"]),
    ("M8-04", "Implementar login e navegação mobile", "feature", "must", "M", ["M8-03"],
     ["Registo, login, recuperação de palavra-passe", "Navegação por separadores: Início, Jogos, Ranking, Notificações, Perfil"]),
    ("M8-05", "Implementar telas Must do responsável no mobile", "feature", "must", "L", ["M8-04", "M6-09"],
     ["Dashboard, solicitações, agenda, detalhe do jogo, comparência, resultado, divergência, ranking", "Registo de comparência e resultado em ≤ 3 toques (RNF-012)"]),
    ("M8-06", "Implementar funcionalidades nativas (notificações push, rede fraca)", "feature", "should", "M", ["M8-05"],
     ["Notificações push (Expo Notifications) para os eventos de RF-10", "Fila local para submeter comparência/resultado quando a rede falha"]),
    ("M8-07", "Gerar build de teste (APK)", "chore", "must", "S", ["M8-05"],
     ["APK instalável distribuído aos testers do piloto (EAS Build)"]),
]:
    task(code, title, t, "mobile", p, s, deps, obj=MOB, ac=ac, per=["PER-03"])

# ---------------------------------------------------------------- M9
task("M9-01", "Elaborar plano de testes a partir dos critérios de aceitação", "test", "qa", "must", "M", ["M1-08"],
     ent="`docs/05-qa/plano-testes.md`")
task("M9-02", "Implementar testes E2E dos fluxos críticos", "test", "qa", "must", "L", ["M9-01", "M7-06.16"],
     ent="Testes automatizados",
     ac=["Criar conta → registar equipa → plantel → contactos", "Solicitar → aceitar / propor alteração → jogo agendado",
         "Comparência das duas equipas → resultado igual → ranking actualizado", "Resultado divergente → análise do admin → correcção auditada"])
task("M9-03", "Executar testes de RNF (desempenho, segurança, usabilidade)", "test", "qa", "should", "M", ["M9-01"], ent="Relatório")
task("M9-04", "Corrigir bugs encontrados", "bug", "qa", "must", "L", ["M9-02"], ent="Issues de bug fechadas")
task("M9-05", "Realizar homologação/UAT com equipas piloto", "test", "qa", "must", "M", ["M9-04"],
     ent="Aceite formal", obj="Piloto com equipas reais de um bairro: marcar e jogar pelo menos 3 jogos de ponta a ponta.")
task("M9-06", "Verificar matriz de rastreabilidade (RF Must cobertos)", "docs", "qa", "must", "S", ["M9-05", "M1-09"], ent="Matriz actualizada")

# ---------------------------------------------------------------- M10
task("M10-01", "Configurar pipeline CD (deploy automático para staging)", "chore", "devops", "must", "M", ["M5-10"], ent="Workflow de deploy")
task("M10-02", "Configurar ambiente de produção (servidor, domínio, HTTPS, BD)", "chore", "devops", "must", "M", ["M3-07"], ent="Produção pronta")
task("M10-03", "Configurar backups e monitorização", "chore", "devops", "should", "S", ["M10-02"], ent="Rotina de backup + alertas")
task("M10-04", "Criar release v1.0.0 (merge em master + tag)", "chore", "gestão", "must", "XS", ["M9-05"], ent="Release no GitHub")
task("M10-05", "Publicar app mobile (Google Play)", "chore", "mobile", "should", "S", ["M8-07", "M9-05"], ent="App publicada", obj=MOB,
     ac=["Ficha da loja em português", "Política de privacidade publicada (RNF-026)", "Versão 1.0.0 disponível"])
task("M10-06", "Escrever manual do utilizador por persona", "docs", "gestão", "should", "M", ["M9-05"],
     ent="`docs/06-entrega/manual-utilizador.md`", ac=["Manual do responsável de equipa", "Manual do administrador da plataforma"])
task("M10-07", "Escrever manual técnico / guia de instalação", "docs", "devops", "must", "M", ["M10-02"], ent="`docs/06-entrega/manual-tecnico.md`")
task("M10-08", "Realizar retrospectiva do projecto", "docs", "gestão", "could", "S", ["M10-04"], ent="Lições aprendidas")

TASKS = T
