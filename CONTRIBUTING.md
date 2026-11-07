# Como contribuir — GiraBairro

Convenções da equipa, baseadas no [roteiro de engenharia](roteiro-engenharia-de-sistemas.md).

## 1. Branches (Git Flow simplificado)

| Branch | Origem | Destino | Uso |
|--------|--------|---------|-----|
| `master` | — | — | Código em produção (faz o papel de `main` do roteiro). **Protegida**: só recebe merge de `release/*` e `hotfix/*` |
| `develop` | `master` | — | Integração contínua. **Branch por defeito** do repositório. **Protegida**: só via PR |
| `feature/<nº-issue>-<slug>` | `develop` | `develop` | Nova funcionalidade. Ex.: `feature/58-modulo-equipas` |
| `docs/<nº-issue>-<slug>` | `develop` | `develop` | Documentação. Ex.: `docs/14-personas` |
| `fix/<nº-issue>-<slug>` | `develop` | `develop` | Correcção não urgente |
| `release/vX.Y.Z` | `develop` | `master` + `develop` | Preparação de versão |
| `hotfix/<slug>` | `master` | `master` + `develop` | Correcção urgente em produção |

Regras de protecção (`master` e `develop`): PR obrigatório, mínimo 1 aprovação, proibido push directo e force push. A partir do M5 o CI também tem de passar.

## 2. Commits (Conventional Commits)

```
<tipo>(<escopo>): <descrição curta>

feat(equipas): adiciona pesquisa por município
fix(resultados): corrige comparação de marcadores
docs(mer): adiciona entidade Comparencia
```

Tipos: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `style`, `ci`.

## 3. Issues

- Título: **`[Mx-NN] Verbo + objecto`** — ex.: `[M1-03] Definir personas (PER-01 a PER-05)`.
- Telas do frontend usam sub-código: `[M7-06.05] Implementar tela TEL-07 Lista de jogadores`.
- Cada issue tem: 1 `tipo:`, ≥1 `area:`, 1 `prioridade:`, 1 `tamanho:` e a **milestone** da fase.
- Dependências no corpo: `Depende de: #12 (M1-03)`.
- No PR, usar `Closes #N` para fechar a issue no merge.

## 4. Códigos usados em todos os artefactos

| Código | Significado | Onde está definido |
|--------|-------------|--------------------|
| `PER-0X` | Persona | `docs/01-requisitos/personas.md` |
| `RF-XX.YY` | Requisito funcional | `GiraBairro_MVP_Requisitos_Funcionais_Telas.md` → `docs/01-requisitos/requisitos-funcionais.md` |
| `RNF-NNN` | Requisito não funcional | `docs/01-requisitos/requisitos-nao-funcionais.md` |
| `RN-NN` | Regra de negócio | `docs/01-requisitos/regras-negocio.md` |
| `US-NNN` | User story | `docs/01-requisitos/user-stories.md` |
| `UCNN` | Caso de uso | `docs/02-modelagem/casos-de-uso/` |
| `TEL-NN` | Tela | Especificação, secção 5 |

Personas propostas (a confirmar em M1-03): **PER-01** Visitante · **PER-02** Utilizador registado sem equipa · **PER-03** Responsável da equipa · **PER-04** Responsável de contacto · **PER-05** Administrador da plataforma.

## 5. Quadro

Colunas: 📥 Backlog → 📌 Pronto → 🔨 Em curso → 👀 Em revisão → ✅ Feito. O estado normal fica nas colunas; as labels `estado:` são só para situações especiais (bloqueado, precisa-info, em-revisão).

## 6. Definition of Ready

- [ ] Título `[Mx-NN] Verbo + objecto`
- [ ] Labels de tipo, área, prioridade e tamanho
- [ ] Milestone atribuída
- [ ] Critérios de aceitação escritos
- [ ] Dependências concluídas (ou explicitamente não bloqueantes)
- [ ] Tamanho ≤ L (se XL, dividir)

## 7. Definition of Done

**Documentação (M1–M4):** ficheiro em `docs/` na pasta certa; diagramas com fonte (`src/`) + imagem (`img/`) feitos na ferramenta da label `ferramenta:`; imagem referenciada no `.md` e anexada à issue; códigos consistentes; PR aprovado.

**Código (M5–M10):** critérios de aceitação cumpridos; testes a passar no CI; conforme contrato da API / protótipo; PR com merge em `develop`; documentação actualizada.

## 8. Scripts de configuração

- `scripts/setup-github.sh` — cria labels e milestones (idempotente).
- `scripts/criar_issues.py` — cria/actualiza as issues do backlog definidas em `scripts/tarefas_mvp.py`.
