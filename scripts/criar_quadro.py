#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cria o quadro GitHub Projects do GiraBairro e coloca lá todas as issues.

Requer: gh autenticado com o scope `project`  (gh auth refresh -s project)
Uso:    python3 scripts/criar_quadro.py

- Cria (ou reutiliza) o projecto "GiraBairro — MVP" do utilizador lemosGit e liga-o ao repositório.
- Substitui as opções do campo Status por: Backlog, Pronto, Em curso, Em revisão, Feito.
- Cria os campos Início (data), Fim (data) e Estimativa (número).
- Adiciona todas as issues: abertas → Backlog, fechadas → Feito.
É idempotente.
"""
import json
import subprocess
import time

OWNER = "lemosGit"
REPO = "lemosGit/GiraBairro"
TITLE = "GiraBairro — MVP"
COLUNAS = [
    ("📥 Backlog", "GRAY", "Criada, ainda não está pronta para começar"),
    ("📌 Pronto", "BLUE", "Cumpre a Definition of Ready"),
    ("🔨 Em curso", "YELLOW", "Alguém está a trabalhar (tem responsável e branch)"),
    ("👀 Em revisão", "PURPLE", "PR aberto"),
    ("✅ Feito", "GREEN", "Merge em develop + DoD cumprida"),
]


def gh(*args, inp=None):
    for attempt in range(6):
        r = subprocess.run(["gh", *args], input=inp, capture_output=True, text=True)
        if r.returncode == 0:
            return r.stdout
        if any(k in r.stderr.lower() for k in ("rate limit", "secondary", "502", "503", "504", "timeout")):
            time.sleep(10 * (attempt + 1))
            continue
        raise RuntimeError(f"gh {' '.join(args)}\n{r.stderr}")
    raise RuntimeError("erro transitório persistente")


def graphql(query, **vars):
    args = ["api", "graphql", "-f", f"query={query}"]
    for k, v in vars.items():
        args += ["-F" if isinstance(v, int) else "-f", f"{k}={v}"]
    return json.loads(gh(*args))["data"]


def main():
    projects = json.loads(gh("project", "list", "--owner", OWNER, "--format", "json", "--limit", "100"))["projects"]
    proj = next((p for p in projects if p["title"] == TITLE), None)
    if not proj:
        proj = json.loads(gh("project", "create", "--owner", OWNER, "--title", TITLE, "--format", "json"))
        print(f"projecto criado: #{proj['number']}")
    num, pid = proj["number"], proj["id"]
    try:
        gh("project", "link", str(num), "--owner", OWNER, "--repo", REPO)
    except RuntimeError as e:
        if "already" not in str(e).lower():
            raise
    gh("project", "edit", str(num), "--owner", OWNER, "--visibility", "PUBLIC",
       "--description", "Backlog do MVP GiraBairro — fases M0 a M10 do roteiro de engenharia")

    # --- campo Status com as 5 colunas
    fields = json.loads(gh("project", "field-list", str(num), "--owner", OWNER, "--format", "json", "--limit", "50"))["fields"]
    status = next(f for f in fields if f["name"] == "Status")
    wanted = [c[0] for c in COLUNAS]
    if [o["name"] for o in status.get("options", [])] != wanted:
        opts = ", ".join(f'{{name: "{n}", color: {c}, description: "{d}"}}' for n, c, d in COLUNAS)
        graphql(f"""mutation($id: ID!) {{ updateProjectV2Field(input: {{fieldId: $id,
                 singleSelectOptions: [{opts}]}}) {{ projectV2Field {{ ... on ProjectV2SingleSelectField {{ id }} }} }} }}""",
                id=status["id"])
        print("colunas do Status definidas")
    fields = json.loads(gh("project", "field-list", str(num), "--owner", OWNER, "--format", "json", "--limit", "50"))["fields"]
    status = next(f for f in fields if f["name"] == "Status")
    opt = {o["name"]: o["id"] for o in status["options"]}

    # --- campos personalizados
    names = {f["name"] for f in fields}
    for name, dtype in [("Início", "DATE"), ("Fim", "DATE"), ("Estimativa", "NUMBER")]:
        if name not in names:
            gh("project", "field-create", str(num), "--owner", OWNER, "--name", name, "--data-type", dtype)
            print(f"campo criado: {name}")

    # --- itens
    items = json.loads(gh("project", "item-list", str(num), "--owner", OWNER, "--format", "json", "--limit", "1000"))["items"]
    in_board = {i["content"].get("number"): i for i in items if i.get("content", {}).get("type") == "Issue"}
    issues = json.loads(gh("issue", "list", "--repo", REPO, "--state", "all", "--limit", "500",
                           "--json", "number,url,state"))
    for iss in sorted(issues, key=lambda x: x["number"]):
        col = "✅ Feito" if iss["state"] == "CLOSED" else "📥 Backlog"
        item = in_board.get(iss["number"])
        # não mexe em itens que a equipa já moveu para uma coluna válida
        if item and item.get("status") in opt and not (iss["state"] == "CLOSED" and item["status"] != col):
            continue
        if not item:
            item = json.loads(gh("project", "item-add", str(num), "--owner", OWNER, "--url", iss["url"], "--format", "json"))
            time.sleep(0.4)
        gh("project", "item-edit", "--id", item["id"], "--project-id", pid,
           "--field-id", status["id"], "--single-select-option-id", opt[col])
        time.sleep(0.4)
        print(f"#{iss['number']:>3} → {col}", flush=True)

    url = json.loads(gh("project", "view", str(num), "--owner", OWNER, "--format", "json"))["url"]
    print(f"quadro pronto: {url}")


if __name__ == "__main__":
    main()
