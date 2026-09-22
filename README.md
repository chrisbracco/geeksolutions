# Geek Solutions — sitio web

Rediseño y unificación del sitio de **Geek Solutions** (Porlamar, Nueva Esparta, Venezuela).

Un solo archivo: `index.html` (~63 KB, HTML + CSS + JS inline) + `assets/` (~1 MB).
Sin build, sin dependencias de layout, sin framework.

**Vista previa:** https://chrisbracco.github.io/geeksolutions/
**Destino final:** https://www.geeksolutions.com.ve/

---

## Qué es esto

La fusión de tres fuentes, mapeadas en `docs/mapeo-auditoria.md`:

| Fuente | Qué aporta |
|---|---|
| **geeksolutions.com.ve** | Marca, catálogo real de servicios, 14 proyectos, 5 clientes con testimonio, equipo, trayectoria de 15 años |
| **CrGen** | Sistema de diseño (tokens monocromos, escala `clamp()`, single-file, GSAP), la oferta de arquitectura de datos y la regla de cero cifras sin respaldo |
| **castillo-company.kit.com** | La mecánica de conversión: una promesa con plazo, un bloque, una acción. Lenguaje de dueño de negocio, no de técnico |

---

## Sistema de diseño

**Tokens** — base monocroma con un solo acento de marca:

```
--black #0e1113   --ink #1c2226    --gray #5f6a70    --gray-lt #93a0a7
--gray-xlt #d5dbde  --off-white #f6f7f8  --white #ffffff
--accent #0e9f6e  --accent-bright #26d48c  --accent-dk #0a7c55
```

El verde sale del `style.css` original de Geek Solutions (`#26d48c`), atemperado a `#0e9f6e`
para que cumpla contraste sobre blanco. Los otros tres acentos sueltos del sitio viejo
(`#34a5ed`, `#20c997`, `#25d366`) se eliminaron; el verde de WhatsApp sobrevive **solo**
en los botones de WhatsApp.

**Tipografía** — `Inter` (texto, común a Geek y Castillo) + `JetBrains Mono` (etiquetas y
datos, firma de CrGen). Escala fluida con `clamp()` en 5 pasos.

**Movimiento** — GSAP 3.15.0 + ScrollTrigger por CDN (parallax del hero, entrada del meta).
Todo lo demás es CSS. Los `:hover` van dentro de `@media (hover:hover) and (pointer:fine)`
con equivalente táctil por `IntersectionObserver`, porque sin ese guard Android deja las
tarjetas pegadas en estado hover tras un toque.

**Accesibilidad y rendimiento** — `prefers-reduced-motion` respetado en todo,
`content-visibility:auto` por sección, `loading="lazy"` en todas las imágenes salvo el hero,
skip link, `:focus-visible`, `aria-expanded` en el menú, `role="status"` en los avisos de
formulario, listeners de scroll con rAF throttle y `passive:true`.

---

## Estructura

```
index.html              todo el sitio
assets/                 imágenes (recomprimidas, -80% vs. el original)
  project/              14 proyectos
docs/mapeo-auditoria.md el mapeo completo de las 3 fuentes + los 18 defectos detectados
.github/workflows/      deploy automático a GitHub Pages al hacer push a main
```

Secciones: `#top` · `#servicios` · `#arquitectura` · `#metodo` · `#proyectos` · `#clientes` · `#nosotros` · `#checklist` · `#contacto`

---

## Lo que se corrigió del sitio original

El detalle completo está en `docs/mapeo-auditoria.md`. Los de mayor impacto:

1. **Había cero formularios en todo el sitio.** La página "Contáctanos" no tenía formulario.
   Ahora hay dos, con honeypot anti-bot y validación.
2. **`mailto:info@example.com`** — placeholder de plantilla en la página de contacto.
   Todo lead por correo se perdía.
3. **Cuatro juegos de contadores contradictorios** (189/25/120/5 · 34/5/21/1 · 38/5/24/1 · 30/4/18/1),
   incluido **"1 Estrella de satisfacción"**. Eliminados: no se publican cifras sin respaldo.
4. **Enlace "Tienda" roto** en `about.html` y `contact.html` → `tienda.geeksolutions.com.ve`
   devuelve **HTTP 402 "Tienda no disponible"**. Todo apunta ahora a `ec.geeksolutions.com.ve`, que sí está viva.
5. Teléfono placeholder `+58 123 456 789` y correo mal escrito `info@geeksoutions.com.ve`.
6. Faltas de ortografía en los proyectos ("Comunicacionjes", "Instalaciond e", "Estructurdo", "ransonware").
7. Footer de plantilla ajena: "Designed By HTML GEEK Distributed By GEEK".
8. Se quitaron Bootstrap, jQuery, WOW.js, Owl Carousel, Font Awesome y AdSense.
9. Imágenes: **5,4 MB → 1,06 MB**. El hero solo pesaba 1,6 MB.
10. SEO que no existía: `og:*`, Twitter cards, `canonical`, JSON-LD `ProfessionalService`.

---

## Pendientes antes de poner esto en producción

| # | Qué | Quién |
|---|---|---|
| 1 | **Arreglar el DNS del ápex.** `geeksolutions.com.ve` **no tiene registro A** — solo funciona `www.`. Quien escriba el dominio sin `www` no llega a ninguna parte. Se arregla en Cloudflare con un CNAME de ápex hacia el host de Azure. | Amílcar |
| 2 | **Access key de Web3Forms.** En `index.html`, constante `WEB3FORMS_KEY` (vacía). Mientras esté vacía los formularios abren WhatsApp con el mensaje ya redactado — no se pierde ningún lead, pero no llega copia al correo. Son 30 segundos en web3forms.com. | — |
| 3 | **Escribir el checklist de 7 días.** La sección lo promete y hoy no existe el PDF. | Contenido |
| 4 | **GA4 `G-8Z63VGX2M4`** existe pero faltaba en el home del sitio viejo. No se incluyó aquí todavía: decidir si entra y con qué aviso de cookies. | Amílcar |
| 5 | Confirmar con Amílcar que los 5 clientes nombrados (NAVIBUS, LD HOTELES, BT TRAVEL, SAMBIL, GRUPO LEIROS) autorizan seguir apareciendo. | Amílcar |
| 6 | Foto propia para el hero. La actual es la `carousel-1.jpg` del sitio original. | Amílcar |

`canonical` y `og:url` apuntan a `www.geeksolutions.com.ve` a propósito: mientras esto viva
en GitHub Pages como vista previa, no debe competir en Google con el sitio real.

---

## Deploy

Push a `main` dispara el workflow de GitHub Pages. Nada que compilar.

```
git add -A
git commit -m "..."
git push
```
