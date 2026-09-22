# Mapeo completo — Geek Solutions + Castillo Company + CrGen

Fecha del scrape: 2026-09-21 · Método: Scrapling 0.4.7 (DynamicFetcher, render JS completo)

---

## 1. geeksolutions.com.ve (Amílcar Roa)

### Infraestructura

| Dato | Valor |
|---|---|
| Hosting | **Azure Static Web Apps** (`green-mushroom-04d5ccb1e.2.azurestaticapps.net` → 52.167.15.22) |
| DNS | Cloudflare (`desi.ns` / `terin.ns.cloudflare.com`) |
| Ápex `geeksolutions.com.ve` | 🔴 **SIN REGISTRO A** — no resuelve. Sólo funciona `www.` |
| Stack | HTML estático + Bootstrap 5.0.0 + jQuery 3.6.4 + WOW.js + Owl Carousel + Font Awesome 5.10 |
| Plantilla | Comercial de terceros — footer "Designed By **HTML GEEK** Distributed By **GEEK**" |
| Analítica | GA4 `G-8Z63VGX2M4` (sólo en about/project/contact, **falta en el home**) · GTM `GTM-MSTF4HSL` (sólo project) · AdSense `ca-pub-5259661431095344` |
| Tipografías | Inter (400/500/600) + Saira (500/600/700) |

### Páginas (5)

`index.html` · `about.html` · `service.html` · `project.html` · `contact.html`

### Navegación

Inicio · Nosotros · Servicios · Proyectos · Contactos · **Tienda** (externa)

### Identidad y contacto

- Nombre: oscila entre **"Geek Solution"**, **"GeekSolution"** y **"Geek Solutions"** (sin criterio fijo)
- Tagline: *"Evoluciona con la Tecnología"*
- Ubicación: Porlamar, Isla de Margarita, Nueva Esparta, Venezuela
- WhatsApp: **+58 412-2721953** (también `wa.link/35jnn0`)
- Email: `info@geeksolutions.com.ve`
- Maps: `goo.gl/maps/Zd4BCynmTb98ivUJ6`
- Antigüedad declarada: **"más de 15 años"**

### Equipo (about.html)

- **Amilcar Roa** (`img/team-1.jpg`)
- **Jesús Medina** (`img/team-3.jpg`)

### Servicios (service.html) — los reales y vendibles

1. **Cloud Computing** — arquitectura AWS y Azure, SES, WAF, gestión de secretos
2. **Administración de Servidores** — Windows Server y Linux (Ubuntu/CentOS), Active Directory, Exchange
3. **Infraestructura de Correo** — Zimbra Collaboration, Postfix, problemas críticos de MTA
4. **Redes y Conectividad** — certificaciones **CCNP** y **MTCRE**, MikroTik, Cisco
5. **Office 365** — migración e implementación completa
6. **Optimización de Bases de Datos** — SQL Server, optimización de consultas, alta disponibilidad

Del home, además: **Licencias** (digitales), **Desarrollo web**, **CCTV**, **Cyber Security**, **Infraestructura IT**.
Del carrusel: **Facturación AWS/Azure** ("Ahorra dinero optimizando tu facturación"), **Correos Corporativos**.

### Proyectos / casos (project.html) — 14 tarjetas

Power BI · Data Center · Sistema CCTV · Cableado Estructurado · Comunicaciones · Servidores ·
Arquitectura AWS · Telefonía IP · BACKUPS · Arquitectura AZURE · Racks · **Implementación de Odoo** · CCTV

### Clientes nombrados (con logo)

**NAVIBUS · LD HOTELES · BT TRAVEL · SAMBIL · GRUPO LEIROS**

Testimonios asociados:
- *"Soporte técnico excepcional. Soluciones rápidas y efectivas para nuestras necesidades IT."*
- *"Implementación de Dominio. Recuperación de Virtual"*
- *"Recuperación de Archivos por ataque de ransomware, implementación de sistema de Backup"*
- *"Instalación y Normalización en Sistema CCTV. Excelente servicio y profesionalismo."*
- *"Implementación de sistema de Monitoreo para su infraestructura. Totalmente recomendados."*

### 🔴 Defectos detectados (18)

**Credibilidad**

1. **Contadores contradictorios en las 4 páginas.** Home `189 / 25 / 120 / 5` · About `34 / 5 / 21 / 1` · Project `38 / 5 / 24 / 1` · Contact `30 / 4 / 18 / 1`. Son cifras de plantilla nunca editadas.
2. **"1 Estrella de satisfacción"** en about/project/contact. Literalmente anuncia calificación de 1 estrella.
3. Home dice "189 Clientes Satisfechos" pero "120 Clientes Totales" — más satisfechos que totales.
4. Footer de plantilla ajeno: "Designed By HTML GEEK Distributed By GEEK".

**Conversión**

5. 🔴 **CERO formularios en todo el sitio.** `forms=0 inputs=0` en las 5 páginas. La página "Contáctanos" **no tiene formulario de contacto**.
6. 🔴 `contact.html`: el email enlaza a **`mailto:info@example.com`** — placeholder de plantilla. Todo lead por email se pierde.
7. `service.html` footer: teléfono **"+58 123 456 789"** — placeholder.
8. `service.html` footer: email **`info@geeksoutions.com.ve`** — falta la "l", dominio inexistente.
9. Único canal vivo: WhatsApp. Sin captura de correo, sin lista, sin lead magnet.

**Infraestructura**

10. 🔴 Ápex sin registro A: quien escriba `geeksolutions.com.ve` sin `www` no llega.
11. 🔴 **Enlace "Tienda" roto en 2 de 4 páginas.** `about.html` y `contact.html` → `tienda.geeksolutions.com.ve` = **HTTP 402 "Tienda no disponible"** (impago). `index.html` y `service.html` → `ec.geeksolutions.com.ve` = ✅ viva (Odoo eCommerce).
12. GA4 ausente en el home — la página más visitada no mide nada.
13. Sin `<meta og:*>`, sin Twitter cards, sin canonical, sin JSON-LD.
14. `project.html` sin meta description ni keywords; `<title>` distinto al resto.

**Contenido**

15. Faltas de ortografía visibles: "Comunicacionjes", "Instalaciond e Sistema CCTV", "Cableado Estructurdo", "Instlación", "Recupercaión", "ransonware".
16. Los 14 proyectos enlazan todos a `#` — no hay caso de estudio detrás de ninguno.
17. CSS de emergencia pegado inline en `service.html` y `contact.html` ("CSS CRÍTICO - ELIMINAR FRANJA GRIS") — parche sobre plantilla rota.
18. Paleta sin sistema: `#26d48c` (verde CSS) + `#34a5ed` (azul inline) + `#20c997` (teal) + `#25d366` (verde WhatsApp) conviviendo sin jerarquía.

---

## 2. castillo-company.kit.com/checklist (Juan Matute)

### Infraestructura

| Dato | Valor |
|---|---|
| Plataforma | **Kit (ex-ConvertKit)** — landing hospedada, plantilla "Hyde" |
| Form ID | `9328874` → `app.kit.com/forms/9328874/subscriptions` |
| Stack | React 16.14 + plantillas ConvertKit |
| Tipografías | **Playfair Display** (display) + **Inter** (texto) |
| Paleta | `#1e1e1e` tinta · `#fffbf5` crema · `#c9922f` oro · `#8c7b6b` topo · `#f5f5f5` |

### Copy completo

- **H1:** "Recupera el control de tu negocio en 7 días"
- **Sub:** "7 acciones concretas — una por día — para pasar del caos operativo a una estructura. Diseñado para dueños de negocio cuya operación creció más rápido que sus procesos. Sin herramientas complicadas. Sin jerga técnica. Solo claridad, una semana."
- **CTA:** botón **"Quiero el Checklist"**, único campo: Correo Electrónico
- **Micro-copy de confianza:** "Respeto tu privacidad. Cancelas cuando quieras."

**3 bloques de beneficio:**

1. **Visibilidad total** — "Vas a mapear toda tu operación en menos de una hora. Por primera vez, vas a ver en un solo lugar qué hace tu equipo, dónde se registran los datos y qué procesos te están drenando tiempo a mano."
2. **Los 3 KPIs que sí importan** — "Vas a definir las 3 métricas que reflejan la salud real de tu negocio y a saber dónde mirarlas cada mañana antes de tomar cualquier decisión. Nada de tableros con 30 números que no usas."
3. **Una rutina que sostiene el orden** — "15 minutos al día. Esa es la rutina de cierre que separa a los negocios que mantienen el control de los que vuelven al caos en dos semanas. Te muestro exactamente cómo armarla."

### Lo que hace bien (y hay que robarle)

- **Una sola acción en toda la página.** Un campo, un botón. Cero distracción.
- **Promesa con plazo concreto** ("7 días", "menos de una hora", "15 minutos al día").
- **Habla del dolor del dueño, no de tecnología.** Cero jerga. "Sin jerga técnica" es literalmente parte del copy.
- **Beneficio en segunda persona futura** ("Vas a mapear", "Vas a definir") — el lector se ve haciéndolo.
- Tipografía editorial serif + crema: se lee como carta, no como folleto corporativo.

### Defectos

- Footer "© 2020 All rights reserved" — 6 años desactualizado.
- `meta description` vacía; `og:description` vacío.
- Sin nombre ni cara del autor en la página: nadie sabe quién es Juan Matute.
- Dependencia total de Kit: la lista y la página no son suyas.

---

## 3. CrGen — el sistema fuerte (base del rediseño)

| Dato | Valor |
|---|---|
| Arquitectura | **Single-file**: 1.693 líneas, ~93 KB, todo HTML+CSS+JS inline |
| Tipografía | JetBrains Mono (mono/datos) + SF Pro / system sans (texto) |
| Paleta | Monocroma disciplinada: `--white #ffffff` · `--off-white #f5f5f7` · `--black #1d1d1f` · `--ink #2b2b30` · `--gray #6e6e73` · `--gray-lt #a1a1a6` · `--gray-xlt #d2d2d7` · `--rule rgba(0,0,0,.08)` · **un solo acento** `--accent-warn #c44536` |
| Escala tipográfica | `clamp()` en 5 pasos: 5.4rem → 3.4rem → 2.1rem → 1.28rem → 1.2rem |
| Movimiento | GSAP 3.15.0 + ScrollTrigger por CDN cdnjs. Hover 100 % CSS dentro de `@media (hover:hover) and (pointer:fine)` |
| Secciones | `#hero` `#pilares` `#caso` `#publico` `#metodo` `#planes` `#lead` |
| Conversión | Modal de leads con nombre de plan dinámico + WhatsApp + 6 CTAs |
| Rendimiento | `content-visibility:auto`, guards `prefers-reduced-motion`, backdrop-filter off <900px, listeners con rAF throttle |

### Reglas de marca heredadas (no negociables)

- Cero cifras sin respaldo. Si un dato es estimado, se dice que es estimado.
- Cero urgencia falsa, cero descuentos no verificables.
- Nunca vender reducción de nómina como beneficio.
- No listar capacidades que no existen.

---

## 4. Diagnóstico de la unificación

| Dimensión | Geek Solutions | Castillo | CrGen | Gana |
|---|---|---|---|---|
| Diseño / sistema visual | Plantilla genérica, 4 acentos sin jerarquía | Editorial limpio pero de plantilla | **Sistema de tokens disciplinado** | 🏆 **CrGen** |
| Arquitectura técnica | Bootstrap + jQuery + 4 librerías | React alquilado | **Single-file, 0 dependencias de layout** | 🏆 **CrGen** |
| Credibilidad del dato | 4 contadores contradictorios | Sin datos | **Honestidad radical + cifras del CoE** | 🏆 **CrGen** |
| Conversión | 🔴 Cero formularios | **1 acción, 1 campo, 1 botón** | Modal + WhatsApp | 🏆 **Castillo** |
| Copy / voz | Genérico ("soluciones innovadoras") | **Dolor del dueño, plazo concreto** | Autoridad + ROI | 🏆 **Castillo + CrGen** |
| Catálogo real de servicios | **6 servicios técnicos + 14 proyectos** | Ninguno | 3 niveles de arquitectura de datos | 🏆 **Geek Solutions** |
| Prueba social | **5 clientes con nombre y logo** | Ninguna | 1 caso anónimo + Viceconsulado | 🏆 **Geek Solutions** |
| Trayectoria | **15 años, 2 personas con nombre** | Anónimo | Fundador + CoE | 🏆 **Geek Solutions** |

### Fórmula del sitio nuevo

**Marca y catálogo de Geek Solutions** (nombre, 15 años, equipo, clientes reales, 6 servicios IT)
**+ sistema de diseño y honestidad de CrGen** (tokens, single-file, GSAP, cero cifras inventadas)
**+ mecánica de conversión de Castillo** (una promesa con plazo, un campo, un botón, lenguaje de dueño)

### Qué se elimina de entrada

- Los 4 juegos de contadores contradictorios y el "1 estrella".
- El footer "Designed By HTML GEEK".
- `mailto:info@example.com`, `+58 123 456 789`, `info@geeksoutions.com.ve`.
- El enlace a `tienda.geeksolutions.com.ve` (402) → apunta todo a `ec.geeksolutions.com.ve`.
- Bootstrap, jQuery, WOW.js, Owl Carousel, Font Awesome, AdSense.
- Las faltas de ortografía de los 14 proyectos.
