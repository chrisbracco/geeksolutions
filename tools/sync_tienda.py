#!/usr/bin/env python3
"""Trae productos nuevos de la tienda vieja (ec.geeksolutions.com.ve, nopCommerce).

La sección "Tienda" de index.html se dibuja con nuestro diseño a partir de
`productos.json`, con imágenes locales en assets/tienda/ y cada ficha abierta
hacia WhatsApp. La tienda vieja ya no se enlaza: sólo se usa como origen de fotos.

Este script NO reescribe productos.json (los nombres y fichas de ahí están
redactados a mano). Lo que hace:
  1. lee el sitemap de la tienda y detecta productos que aún no están en productos.json,
  2. descarga su foto a assets/tienda/,
  3. deja nombre y descripción originales en tools/tienda_nuevos.json para redactarlos.

Uso:
    py tools/sync_tienda.py

Sin dependencias externas. La tienda está detrás de Cloudflare y a veces cae (522):
en ese caso el script avisa y no toca nada.
"""
import html as H
import json
import pathlib
import re
import sys
import urllib.request

BASE = "https://ec.geeksolutions.com.ve"
ROOT = pathlib.Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "assets" / "tienda"
OUT = ROOT / "tools" / "tienda_nuevos.json"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126 Safari/537.36"}

# productos de ejemplo que trae nopCommerce de fábrica: no son de Geek
DEMO = {
    "sound-forge-pro-recurring", "microsoft-windows-os", "adobe-photoshop",
    "lenovo-thinkpad-carbon-laptop", "hp-envy-156-inch-sleekbook", "asus-laptop",
    "digital-storm-vanquish-custom-performance-pc", "switch-crs317-1g-16srm",
}
# slugs de la tienda que ya están en productos.json (con otro nombre de archivo)
KNOWN = {
    "monitor-touch-aon", "scanner-epson-workforce-es-50-wireless", "ups-cdp-3kva",
    "ups-it-salidas-ot2000va", "switch-mikrotik-crs317-1g-16srm", "epson-fx890ii",
    "cpu-intel-i5-9na16-gb-ram-512-ssd-refurbished-", "ups-1000-va600w", "teclado",
    "ssd-480-gb", "microfono-usb", "impresora-de-etiquetas", "etiquetas", "monitor-touch",
    "teclado-usb", "reconocimiento-qr", "router-mikrotik-ccr2004-16g-2s-16",
    "build-your-own-computer",
}


def get(url, binary=False):
    raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
    return raw if binary else raw.decode("utf-8", "replace")


def txt(s):
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def main():
    try:
        sitemap = get(BASE + "/sitemap.xml")
    except Exception as e:
        print(f"La tienda no respondió ({e}). No se tocó nada.", file=sys.stderr)
        return 1

    nuevos = []
    for slug in re.findall(r"<loc>https?://[^/]+/es/([^<]+)</loc>", sitemap):
        if slug in KNOWN or slug in DEMO:
            continue
        try:
            page = get(f"{BASE}/es/{slug}")
        except Exception:
            continue
        img = re.search(r'id="main-product-img-\d+"[^>]*src="([^"]+)"', page)
        if not img:
            continue                      # no es ficha de producto (categoría, marca, etiqueta…)
        name = re.search(r"<h1[^>]*>(.*?)</h1>", page, re.S)
        short = re.search(r'<div class="short-description">(.*?)</div>', page, re.S)
        src = img.group(1).replace("http://", "https://")
        dest = IMG_DIR / f"{slug.strip('-')}.{src.rsplit('.', 1)[-1]}"
        dest.write_bytes(get(src, binary=True))
        nuevos.append({
            "slug": slug,
            "nombre_original": txt(name.group(1)) if name else slug,
            "descripcion_original": txt(short.group(1)) if short else "",
            "imagen": dest.relative_to(ROOT).as_posix(),
        })
        print(f"  nuevo: {slug}")

    OUT.write_text(json.dumps(nuevos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(nuevos)} producto(s) nuevo(s) → {OUT.relative_to(ROOT)}")
    print("Redacte nombre, ficha y categoría y agréguelos a productos.json.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
