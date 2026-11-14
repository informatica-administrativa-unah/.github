"""Logo original de la comunidad Informática Administrativa UNAH (no usa marcas oficiales).

Dibuja: fondo azul marino, anillo dorado, una base de datos (cilindro) con barras de gráfico
encima (datos + gestión) y las letras "IA" con "UNAH · COMUNIDAD" abajo.
Genera PNG 1024 (avatar), PNG 512 y un SVG equivalente.
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
AZUL = "#0B2E59"
AZUL2 = "#123F78"
DORADO = "#F2B705"
BLANCO = "#FFFFFF"
FUENTE = "C:/Windows/Fonts/bahnschrift.ttf"
FUENTE_B = "C:/Windows/Fonts/arialbd.ttf"

S = 1024
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
c = S // 2

# fondo y anillo
d.ellipse((0, 0, S - 1, S - 1), fill=AZUL)
d.ellipse((34, 34, S - 35, S - 35), outline=DORADO, width=22)
d.ellipse((78, 78, S - 79, S - 79), fill=AZUL2)

# base de datos (cilindro) centrada arriba
bw, bh = 300, 64           # ancho y alto de cada tapa elíptica
ancho_grupo = bw + 34 + 118          # cilindro + separación + 3 barras
x0 = c - ancho_grupo // 2
x1 = x0 + bw
cx_cil = x0 + bw // 2
ytop = 250
capas = 3
alto_capa = 70
for i in range(capas, -1, -1):
    y = ytop + i * alto_capa
    if i < capas:
        d.rectangle((x0, y + bh // 2, x1, y + alto_capa + bh // 2), fill=BLANCO)
    d.ellipse((x0, y, x1, y + bh), fill=BLANCO, outline=AZUL2, width=10)
d.ellipse((x0, ytop, x1, ytop + bh), fill=DORADO, outline=AZUL2, width=10)

# barras de gráfico al lado derecho del cilindro (gestión, indicadores)
bx = x1 + 34
base_y = ytop + capas * alto_capa + bh // 2 + 2
for k, h in enumerate((90, 150, 215)):
    d.rounded_rectangle((bx + k * 44, base_y - h, bx + k * 44 + 30, base_y), radius=6, fill=DORADO)

# texto
f_ia = ImageFont.truetype(FUENTE_B, 210)
f_sub = ImageFont.truetype(FUENTE, 62)
def centrar(texto, fuente, y, color):
    w = d.textlength(texto, font=fuente)
    d.text((c - w / 2, y), texto, font=fuente, fill=color)
centrar("IA", f_ia, 560, BLANCO)
centrar("UNAH · COMUNIDAD", f_sub, 790, DORADO)

img.save(OUT / "logo-1024.png")
img.resize((512, 512), Image.LANCZOS).save(OUT / "logo-512.png")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" role="img" aria-label="Comunidad Informática Administrativa UNAH">
  <circle cx="512" cy="512" r="511" fill="{AZUL}"/>
  <circle cx="512" cy="512" r="466" fill="none" stroke="{DORADO}" stroke-width="22"/>
  <circle cx="512" cy="512" r="433" fill="{AZUL2}"/>
  <g stroke="{AZUL2}" stroke-width="10">
    <rect x="{x0}" y="{ytop+bh//2}" width="{bw}" height="{capas*alto_capa}" fill="{BLANCO}" stroke="none"/>
    <ellipse cx="{cx_cil}" cy="{ytop+capas*alto_capa+bh//2}" rx="{bw//2}" ry="{bh//2}" fill="{BLANCO}"/>
    <ellipse cx="{cx_cil}" cy="{ytop+2*alto_capa+bh//2}" rx="{bw//2}" ry="{bh//2}" fill="{BLANCO}"/>
    <ellipse cx="{cx_cil}" cy="{ytop+alto_capa+bh//2}" rx="{bw//2}" ry="{bh//2}" fill="{BLANCO}"/>
    <ellipse cx="{cx_cil}" cy="{ytop+bh//2}" rx="{bw//2}" ry="{bh//2}" fill="{DORADO}"/>
  </g>
  <g fill="{DORADO}">
    <rect x="{bx}" y="{base_y-90}" width="30" height="90" rx="6"/>
    <rect x="{bx+44}" y="{base_y-150}" width="30" height="150" rx="6"/>
    <rect x="{bx+88}" y="{base_y-215}" width="30" height="215" rx="6"/>
  </g>
  <text x="512" y="760" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-weight="700" font-size="210" fill="{BLANCO}">IA</text>
  <text x="512" y="850" text-anchor="middle" font-family="Bahnschrift, Arial, sans-serif" font-size="62" fill="{DORADO}">UNAH · COMUNIDAD</text>
</svg>
'''
(OUT / "logo.svg").write_text(svg, encoding="utf-8")
print("ok", sorted(p.name for p in OUT.iterdir()))
