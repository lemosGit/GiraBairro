#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exporta diagramas Mermaid (.mmd) para SVG e PNG (escala 2x) com o Google Chrome headless.
Não precisa de npm: o Mermaid é carregado do CDN jsDelivr.

Uso: python3 scripts/render_mermaid.py docs/01-requisitos/src/contexto.mmd [...]
     → gera docs/01-requisitos/img/contexto.svg e .png
Um .mmd que comece por `%% look: handDrawn` é desenhado em estilo à mão (equivalente Excalidraw).
"""
import html, os, re, subprocess, sys, tempfile

CHROME = os.environ.get("CHROME", "google-chrome")
TPL = """<!doctype html><html><head><meta charset="utf-8">
<script src="https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.min.js"></script></head>
<body style="margin:0;padding:10px;background:#fff"><pre class="mermaid" style="margin:0">{src}</pre>
<script>mermaid.initialize({{startOnLoad:true, look:"{look}", theme:"default",
  themeVariables:{{fontFamily:"Arial, sans-serif"}}}});</script></body></html>"""


def chrome(*args, tmp):
    return subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                           f"--user-data-dir={tmp}/profile", *args], capture_output=True, text=True, timeout=120)


def render(mmd):
    src = open(mmd, encoding="utf-8").read()
    look = "handDrawn" if "look: handDrawn" in src.splitlines()[0] else "classic"
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(mmd))), "img")
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, os.path.splitext(os.path.basename(mmd))[0])
    with tempfile.TemporaryDirectory() as tmp:
        page = os.path.join(tmp, "p.html")
        open(page, "w", encoding="utf-8").write(TPL.format(src=html.escape(src), look=look))
        dom = chrome("--virtual-time-budget=15000", "--dump-dom", f"file://{page}", tmp=tmp).stdout
        m = re.search(r"<svg[\s\S]*?</svg>(?![\s\S]*</svg>)", dom)
        if not m:
            raise SystemExit(f"falhou: {mmd}\n{dom[-500:]}")
        svg = m.group(0)
        vb = re.search(r'viewBox="([\d.\-]+) ([\d.\-]+) ([\d.]+) ([\d.]+)"', svg)
        w, h = int(float(vb.group(3))) + 20, int(float(vb.group(4))) + 20
        # o SVG do Mermaid repete xmlns/width: limpar para ser XML válido
        head_end = svg.index(">")
        head = svg[:head_end]
        head = re.sub(r'\s(xmlns|width|style)="[^"]*"', "", head)
        head += f' xmlns="http://www.w3.org/2000/svg" width="{w-20}" height="{h-20}"'
        svg = head + svg[head_end:]
        svg = re.sub(r"<br>", "<br/>", svg)
        open(base + ".svg", "w", encoding="utf-8").write(svg)
        # o Chrome headless devolve imagem em branco com janelas muito pequenas
        chrome(f"--screenshot={base}.png", f"--window-size={max(w, 500)},{max(h, 200)}",
               "--force-device-scale-factor=2", f"file://{os.path.abspath(base)}.svg", tmp=tmp)
    print(f"ok  {mmd} → {base}.png ({look})")


if __name__ == "__main__":
    for f in sys.argv[1:]:
        render(f)
