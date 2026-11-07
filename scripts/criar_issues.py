#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cria (ou actualiza) no GitHub as issues do backlog do MVP definidas em tarefas_mvp.py.

Uso (na raiz do repositório, com `gh` autenticado):
    python3 scripts/criar_issues.py

1.ª passagem: cria as issues que ainda não existem (procura pelo código [Mx-NN] no título).
2.ª passagem: reescreve o corpo de todas com as dependências ligadas por número (#N)
              e a lista "Bloqueia" calculada automaticamente.
É idempotente: pode ser executado várias vezes.
"""
import json
import os
import re
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tarefas_mvp import MILESTONES, TASKS  # noqa: E402


TRANSIENT = ("rate limit", "secondary", "http 502", "http 503", "http 504", "timeout", "eof")


def gh(*args, inp=None, retry=True):
    for attempt in range(6):
        r = subprocess.run(["gh", *args], input=inp, capture_output=True, text=True)
        if r.returncode == 0:
            return r.stdout
        if retry and any(k in r.stderr.lower() for k in TRANSIENT):
            time.sleep(10 * (attempt + 1))
            continue
        raise RuntimeError(f"gh {' '.join(args)}\n{r.stderr}")
    raise RuntimeError("erro transitório persistente")


def existing_numbers():
    nums = {}
    data = json.loads(gh("issue", "list", "--state", "all", "--limit", "500", "--json", "number,title"))
    for i in data:
        m = re.match(r"\[(M\d+-[\w.]+)\]", i["title"])
        if m:
            nums[m.group(1)] = i["number"]
    return nums


def create_issue(args, body, code):
    """Cria sem repetir às cegas: após um erro, verifica se a issue já existe (um 504 pode ter criado)."""
    for attempt in range(6):
        try:
            url = gh(*args, inp=body, retry=False).strip()
            return int(url.rstrip("/").split("/")[-1])
        except RuntimeError as e:
            if not any(k in str(e).lower() for k in TRANSIENT):
                raise
            time.sleep(10 * (attempt + 1))
            found = existing_numbers().get(code)
            if found:
                return found
    raise RuntimeError(f"não foi possível criar {code}")


def milestone_of(code):
    return MILESTONES[code.split("-")[0]]


def labels_of(t):
    ls = [f"tipo: {t['t']}"] + [f"area: {a}" for a in t["a"]] + [f"prioridade: {t['p']}", f"tamanho: {t['s']}"]
    ls += t["extra"] + [f"persona: {p}" for p in t["per"]]
    return list(dict.fromkeys(ls))


def ref(code, nums):
    return f"#{nums[code]} ({code})" if code in nums else code


def body_of(t, nums, blocks):
    L = ["## Objectivo", t["obj"] or f"{t['title']}.", ""]
    L += ["## Referências"]
    if t["refs"]:
        L.append(f"- Requisitos/Telas: {t['refs']}")
    if t["per"]:
        L.append(f"- Persona: {', '.join(t['per'])}")
    L.append("- Roteiro: `roteiro-engenharia-de-sistemas.md`")
    L.append("- Especificação: `GiraBairro_MVP_Requisitos_Funcionais_Telas.md`")
    L += ["", "## Critérios de aceitação"]
    L += [f"- [ ] {a}" for a in (t["ac"] or [f"Entregável produzido: {t['ent'] or t['title']}", "Revisto por pelo menos 1 membro (PR aprovado)"])]
    L += ["", "## Dependências"]
    L.append("- Depende de: " + (", ".join(ref(d, nums) for d in t["deps"]) if t["deps"] else "—"))
    L.append("- Bloqueia: " + (", ".join(ref(b, nums) for b in blocks) if blocks else "—"))
    L += ["", "## Entregável", t["ent"] or "—", ""]
    return "\n".join(L)


def main():
    codes = [t["code"] for t in TASKS]
    assert len(codes) == len(set(codes)), "códigos duplicados"
    for t in TASKS:
        for d in t["deps"]:
            assert d in codes, f"{t['code']} depende de {d} inexistente"

    blocks = {c: [] for c in codes}
    for t in TASKS:
        for d in t["deps"]:
            blocks[d].append(t["code"])

    nums = existing_numbers()

    # 1.ª passagem — criar
    for t in TASKS:
        if t["code"] in nums:
            continue
        args = ["issue", "create", "--title", f"[{t['code']}] {t['title']}", "--body-file", "-",
                "--milestone", milestone_of(t["code"])]
        for l in labels_of(t):
            args += ["--label", l]
        nums[t["code"]] = create_issue(args, body_of(t, nums, blocks[t["code"]]), t["code"])
        print(f"criada  #{nums[t['code']]:>3} {t['code']}", flush=True)
        time.sleep(1.2)

    # 2.ª passagem — ligar dependências
    for t in TASKS:
        gh("issue", "edit", str(nums[t["code"]]), "--body-file", "-", inp=body_of(t, nums, blocks[t["code"]]))
        time.sleep(0.6)
    print("dependências ligadas", flush=True)

    out = os.environ.get("ISSUES_MAP", "issues_map.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump({t["code"]: {"n": nums[t["code"]], "title": t["title"], "p": t["p"], "s": t["s"]} for t in TASKS},
                  f, ensure_ascii=False, indent=1)
    print(f"{len(TASKS)} tarefas — mapa em {out}")


if __name__ == "__main__":
    main()
