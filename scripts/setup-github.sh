#!/usr/bin/env bash
# setup-github.sh — cria labels e milestones do roteiro
set -e

REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
echo "Repositório: $REPO"

# --- Remover labels por defeito (opcional) ---
for l in "bug" "documentation" "duplicate" "enhancement" "good first issue" \
         "help wanted" "invalid" "question" "wontfix"; do
  gh label delete "$l" --yes 2>/dev/null || true
done

# --- Labels: "nome|cor|descrição" ---
LABELS=(
  "tipo: feature|1D76DB|Nova funcionalidade"
  "tipo: docs|0075CA|Documentação / artefacto de engenharia"
  "tipo: bug|D73A4A|Erro a corrigir"
  "tipo: chore|C5DEF5|Configuração e manutenção"
  "tipo: refactor|BFD4F2|Melhoria sem mudar comportamento"
  "tipo: test|5319E7|Testes"
  "tipo: spike|F9D0C4|Investigação com tempo limitado"

  "area: gestão|EDEDED|Repositório, quadro, processos"
  "area: requisitos|FEF2C0|Levantamento e especificação"
  "area: modelagem|FBCA04|UML, MER, dicionário de dados"
  "area: arquitetura|E99695|Stack, ADRs, desenho técnico"
  "area: ux-ui|F9A8D4|Wireframes, protótipos"
  "area: backend|0E8A16|Servidor / API"
  "area: database|006B75|Base de dados"
  "area: frontend|7057FF|Web"
  "area: mobile|8B5CF6|App mobile"
  "area: devops|000000|CI/CD, infra, deploy"
  "area: qa|B60205|Qualidade e testes"

  "prioridade: must|B60205|MoSCoW — obrigatório"
  "prioridade: should|D93F0B|MoSCoW — importante"
  "prioridade: could|FBCA04|MoSCoW — desejável"
  "prioridade: wont|CCCCCC|MoSCoW — fora do âmbito"

  "estado: bloqueado|000000|Depende de algo não resolvido"
  "estado: precisa-info|D876E3|Falta informação"
  "estado: em-revisão|0052CC|Aguarda revisão"

  "tamanho: XS|C2E0C6|< 2 horas"
  "tamanho: S|A2EEEF|Meio dia"
  "tamanho: M|7DD3FC|1-2 dias"
  "tamanho: L|3B82F6|3-5 dias"
  "tamanho: XL|1E3A8A|> 1 semana — dividir"

  "ferramenta: excalidraw|6965DB|Diagrama informal / explicação de fluxo"
  "ferramenta: drawio|F08705|Diagrama formal UML / MER / arquitetura"
  "entrega: imagem|0E8A16|Exige PNG/SVG exportado em docs/"

  "persona: PER-01|FFFFFF|Visitante (sem conta)"
  "persona: PER-02|FFFFFF|Utilizador registado sem equipa"
  "persona: PER-03|FFFFFF|Responsável / Administrador da equipa"
  "persona: PER-04|FFFFFF|Responsável de contacto da equipa"
  "persona: PER-05|FFFFFF|Administrador da plataforma"
)

for entry in "${LABELS[@]}"; do
  IFS='|' read -r name color desc <<< "$entry"
  gh label create "$name" --color "$color" --description "$desc" --force
done

# --- Milestones: "título|descrição" ---
MILESTONES=(
  "M0 — Setup & Governança|Repositório, branches, labels, milestones, quadro e templates"
  "M1 — Levantamento de Requisitos|Visão, stakeholders, personas, RF, RNF, RN, MoSCoW, user stories"
  "M2 — Análise & Modelagem|Casos de uso, MER, dicionário de dados, classes, sequência"
  "M3 — Arquitetura & Stack|Stack, ADRs, arquitetura, contrato da API, segurança"
  "M4 — UX/UI Design|Fluxo de telas, wireframes, design system, protótipo"
  "M5 — Backend-1: Fundação|Projecto, BD, migrações, autenticação, autorização, CI"
  "M6 — Backend-2: Módulos de negócio|Implementação dos RF por prioridade"
  "M7 — Frontend-1: Telas primordiais|Interface web principal"
  "M8 — Frontend-2: Mobile|Aplicação mobile nativa — fora do MVP salvo decisão em M3-01"
  "M9 — Integração & QA|Testes E2E, RNF, correcções, homologação"
  "M10 — Deploy & Entrega|Produção, release, manuais"
)

for entry in "${MILESTONES[@]}"; do
  IFS='|' read -r title desc <<< "$entry"
  gh api "repos/$REPO/milestones" -f title="$title" -f description="$desc" -f state=open \
    >/dev/null 2>&1 && echo "Milestone criada: $title" || echo "Já existe: $title"
done

# --- Branch develop ---
git fetch origin
if ! git ls-remote --exit-code --heads origin develop >/dev/null 2>&1; then
  git checkout -b develop
  git push -u origin develop
fi

echo "✅ Configuração concluída."
