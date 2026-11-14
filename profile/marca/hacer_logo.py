"""Logo v2 de la comunidad: estilo sello (fondo azul noche, anillos azules, texto en arco).

Texto: "INFORMÁTICA ADMINISTRATIVA" en arco arriba y "UNAH - CU" abajo.
Centro: ícono propio de línea blanca (base de datos con barras de gráfico), no el símbolo de otra organización.
"""
import math
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
FONDO = (10, 18, 56)
AZUL = (59, 155, 240)
BLANCO = (255, 255, 255)
F_ARCO = "C:/Windows/Fonts/arialbd.ttf"
F_ABAJO = "C:/Windows/Fonts/bahnschrift.ttf"

S = 2048                       # se dibuja grande y se reduce para suavizar
c = S / 2
img = Image.new("RGB", (S, S), FONDO)
d = ImageDraw.Draw(img)

def anillo(r, ancho):
    d.ellipse((c - r, c - r, c + r, c + r), outline=AZUL, width=ancho)

anillo(860, 40)                # anillo exterior
anillo(560, 40)                # anillo interior

def texto_en_arco(texto, radio, centro_grados, fuente, color, arriba=True, espacio=1.0):
    """Coloca cada letra rotada sobre un arco. centro_grados: 90 = arriba (sentido matemático)."""
    anchos = [d.textlength(ch, font=fuente) * espacio for ch in texto]
    total = sum(anchos)
    ang_total = total / radio            # radianes que ocupa el texto
    ang = math.radians(centro_grados) + (ang_total / 2 if arriba else -ang_total / 2)
    for ch, w in zip(texto, anchos):
        paso = w / radio
        a = ang - paso / 2 if arriba else ang + paso / 2
        x = c + radio * math.cos(a)
        y = c - radio * math.sin(a)
        caja = fuente.getbbox(ch)
        cw, chh = caja[2] - caja[0] + 8, caja[3] - caja[1] + 8
        letra = Image.new("RGBA", (int(cw * 1.6) + 20, int(chh * 1.6) + 20), (0, 0, 0, 0))
        ld = ImageDraw.Draw(letra)
        ld.text((letra.width / 2, letra.height / 2), ch, font=fuente, fill=color, anchor="mm")
        rot = math.degrees(a) - 90 if arriba else math.degrees(a) + 90
        letra = letra.rotate(rot, resample=Image.BICUBIC, expand=True)
        img.paste(letra, (int(x - letra.width / 2), int(y - letra.height / 2)), letra)
        ang = ang - paso if arriba else ang + paso

texto_en_arco("INFORMÁTICA ADMINISTRATIVA", 712, 90, ImageFont.truetype(F_ARCO, 112), BLANCO, arriba=True, espacio=1.08)
texto_en_arco("UNAH - CU", 712, 270, ImageFont.truetype(F_ABAJO, 104), BLANCO, arriba=False, espacio=1.35)

# ícono central de línea blanca: cilindro (base de datos) + barras con puntas redondeadas
G = 30                                   # grosor del trazo
cx, cy = c - 122, c + 20
rw, rh = 190, 64                         # radios de la elipse de las tapas
alto = 300
top = cy - alto / 2
def elipse(yc, completa=True):
    caja = (cx - rw, yc - rh, cx + rw, yc + rh)
    if completa:
        d.ellipse(caja, outline=BLANCO, width=G)
    else:
        d.arc(caja, 0, 180, fill=BLANCO, width=G)   # solo la mitad de abajo
elipse(top)                               # tapa superior
elipse(top + alto / 3, False)             # divisiones
elipse(top + 2 * alto / 3, False)
elipse(top + alto, False)                 # base
d.line((cx - rw + G / 2 - 1, top, cx - rw + G / 2 - 1, top + alto), fill=BLANCO, width=G)
d.line((cx + rw - G / 2, top, cx + rw - G / 2, top + alto), fill=BLANCO, width=G)
# barras a la derecha, con puntas redondeadas como el estilo de la referencia
bx = cx + rw + 70
base = top + alto + 20
for k, h in enumerate((150, 250, 360)):
    x = bx + k * 78
    d.line((x, base, x, base - h), fill=BLANCO, width=G + 6)
    r = (G + 6) / 2
    d.ellipse((x - r, base - h - r, x + r, base - h + r), fill=BLANCO)
    d.ellipse((x - r, base - r, x + r, base + r), fill=BLANCO)
# punto con anillo arriba de la barra más alta (guiño a los nodos del estilo)
px, py = bx + 2 * 78, base - 360 - 70
d.ellipse((px - 34, py - 34, px + 34, py + 34), outline=BLANCO, width=G - 6)

for tam in (1024, 512):
    img.resize((tam, tam), Image.LANCZOS).save(OUT / f"logo-{tam}.png")
print("ok")
