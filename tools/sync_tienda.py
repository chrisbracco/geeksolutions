#!/usr/bin/env python3
"""Sincroniza el catálogo de ec.geeksolutions.com.ve dentro de este sitio.

La sección "Tienda" de index.html se dibuja con nuestro propio diseño a partir de
`productos.json`. Este script regenera ese archivo leyendo la tienda Odoo real.
El botón de cada producto enlaza a su ficha en la tienda, que es donde se cobra.

Uso:
    py tools/sync_tienda.py              # sincroniza y reescribe productos.json
    py tools/sync_tienda.py --dry        # muestra lo que encontró, sin escribir

Requiere: py -m pip install --user "scrapling[fetchers]"

Nota: la tienda vive detrás de Cloudflare y a veces devuelve 522 (origen caído).
En ese caso el script no toca productos.json y sale con código 1.
"""
import argparse
import json
import pathlib
import re
import sys
import time
from urllib.parse import urljoin

BASE = "https://ec.geeksolutions.com.ve"
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "productos.json"
MAX_PRODUCTS = 48


def clean(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"&nbsp;?", " ", s)
    s = re.sub(r"&amp;", "&", s)
    s = re.sub(r"&#?\w+;", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def fetch(url, tries=3):
    from scrapling.fetchers import DynamicFetcher
    for i in range(tries):
        try:
            r = DynamicFetcher.fetch(url, headless=True, network_idle=True, timeout=90000)
            if r.status == 200 and "Connection timed out" not in r.html_content[:3000]:
                return r.html_content
            print(f"  intento {i+1}: status {r.status}", file=sys.stderr)
        except Exception as e:
            print(f"  intento {i+1}: {type(e).__name__}: {str(e)[:90]}", file=sys.stderr)
        time.sleep(4)
    return None


def parse_products(html):
    """Extrae tarjetas de producto de una página /shop de Odoo."""
    items, seen = [], set()

    # Cada tarjeta de Odoo vive en un contenedor .oe_product; si cambia el tema,
    # caemos al barrido genérico de enlaces /shop/<slug>.
    blocks = re.findall(r'<(?:div|form)[^>]*class="[^"]*oe_product[^"]*".*?</(?:div|form)>\s*(?=<(?:div|form)|</)', html, re.S)
    if not blocks:
        blocks = [html]

    for b in blocks:
        m = re.search(r'href="(/shop/(?!category)([^"?#]+))"', b)
        if not m:
            continue
        href, slug = m.group(1), m.group(2)
        if href in seen:
            continue

        name = ""
        nm = re.search(r'<h6[^>]*>(.*?)</h6>|<h5[^>]*>(.*?)</h5>|itemprop="name"[^>]*>(.*?)<', b, re.S)
        if nm:
            name = clean(next(g for g in nm.groups() if g))
        if not name:
            am = re.search(r'href="' + re.escape(href) + r'"[^>]*>(.*?)</a>', b, re.S)
            name = clean(am.group(1)) if am else ""
        if not name or len(name) > 130:
            continue

        price = ""
        pm = re.search(r'oe_currency_value[^>]*>\s*([\d.,]+)', b)
        if pm:
            price = pm.group(1)
        cur = "USD" if "$" in b else ""

        img = ""
        im = re.search(r'(?:src|data-src)="(/web/image/product[^"\']+)"', b)
        if im:
            img = urljoin(BASE, im.group(1))

        seen.add(href)
        items.append({
            "nombre": name,
            "slug": slug,
            "precio": price,
            "moneda": cur,
            "imagen": img,
            "url": urljoin(BASE, href),
        })
        if len(items) >= MAX_PRODUCTS:
            break
    return items


def parse_categories(html):
    cats, seen = [], set()
    for m in re.finditer(r'href="(/shop/category/([^"?#]+))"[^>]*>(.*?)</a>', html, re.S):
        name = clean(m.group(3))
        if not name or m.group(1) in seen or len(name) > 60:
            continue
        seen.add(m.group(1))
        cats.append({"nombre": name, "slug": m.group(2), "url": urljoin(BASE, m.group(1))})
    return cats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true", help="no escribe productos.json")
    args = ap.parse_args()

    print(f"Leyendo {BASE}/shop ...")
    html = fetch(BASE + "/shop")
    if html is None:
        print("\nLa tienda no respondió (probablemente 522: origen caído).", file=sys.stderr)
        print("productos.json NO se modificó. Reintente más tarde.", file=sys.stderr)
        return 1

    productos = parse_products(html)
    categorias = parse_categories(html)
    print(f"  {len(productos)} productos · {len(categorias)} categorías")

    data = {
        "actualizado": time.strftime("%Y-%m-%d"),
        "origen": BASE + "/shop",
        "categorias": categorias,
        "productos": productos,
    }

    if args.dry:
        print(json.dumps(data, ensure_ascii=False, indent=2)[:4000])
        return 0

    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Escrito {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
