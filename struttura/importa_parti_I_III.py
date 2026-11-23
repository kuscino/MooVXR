# -*- coding: utf-8 -*-
"""importa_parti_I_III.py - importa senza modifiche i testi delle Parti I e III dal documento
ricevuto (Allegato 4 MooVXR Parti I e III) in un modulo di dati usato da contenuti_moovxr.py.

Il testo resta quello del documento: si scartano solo i titoli e le istruzioni del template
ministeriale, che il generatore produce da se'. Le figure sono estratte in PNG.

Uso: python3 struttura/importa_parti_I_III.py <docx> <cartella struttura>
Produce: <struttura>/parti_I_III_moovxr.py e <struttura>/img/parti_I_III/figNN.png
"""
import io, pathlib, pprint, sys
import docx
from docx.oxml.ns import qn
from PIL import Image

SCARTA = {"Titolo", "Sottotitolomodulo", "Indiceragionato", "Titolosezioneministeriale",
          "Paragrafoministeriale", "Sottoparagrafoministeriale", "Istruzionimodello", "Riganota"}
LARGHEZZA = 9526          # twip, testo della pagina verticale del profilo
EMU_CM = 360000
NS_A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
NS_WP = "{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}"
NS_R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"

src, dest = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
D = docx.Document(str(src))
IMG = dest / "img" / "parti_I_III"
IMG.mkdir(parents=True, exist_ok=True)
nfig = [0]


def stile(p):
    pp = p.find(qn("w:pPr"))
    s = pp.find(qn("w:pStyle")) if pp is not None else None
    return s.get(qn("w:val")) if s is not None else ""


def _on(rpr, tag):
    if rpr is None or rpr.find(qn(tag)) is None:
        return False
    return rpr.find(qn(tag)).get(qn("w:val")) not in ("0", "false")


def runs(p):
    out = []
    for r in p.iter(qn("w:r")):
        t = ""
        for c in r.iterchildren():
            if c.tag == qn("w:t"):
                t += c.text or ""
            elif c.tag == qn("w:tab"):
                t += "\t"
            elif c.tag in (qn("w:br"), qn("w:cr")):
                t += "\n"
        if not t:
            continue
        rpr = r.find(qn("w:rPr"))
        f = (_on(rpr, "w:b"), _on(rpr, "w:i"))
        if out and out[-1][1:] == f:
            out[-1] = (out[-1][0] + t,) + f
        else:
            out.append((t,) + f)
    return out


def figura(p):
    dr = next(p.iter(qn("w:drawing")))
    ext = dr.find(".//" + NS_WP + "extent")
    blip = dr.find(".//" + NS_A + "blip")
    part = D.part.related_parts[blip.get(NS_R + "embed")]
    nfig[0] += 1
    nome = "fig%02d.png" % nfig[0]
    im = Image.open(io.BytesIO(part.blob))
    if im.mode not in ("RGB", "RGBA", "L", "LA", "P"):
        im = im.convert("RGB")
    im.save(IMG / nome, "PNG")
    cm = round(min(int(ext.get("cx")), LARGHEZZA * 635) / EMU_CM, 2)
    return ["img", "img/parti_I_III/" + nome, cm, None]


def cella(tc):
    righe, bold, al = [], [], "left"
    for p in tc.iter(qn("w:p")):
        rr = runs(p)
        righe.append("".join(r[0] for r in rr))
        bold += [r[1] for r in rr if r[0].strip()]
        jc = p.find(qn("w:pPr") + "/" + qn("w:jc")) if p.find(qn("w:pPr")) is not None else None
        if jc is not None and jc.get(qn("w:val")) in ("center", "right"):
            al = jc.get(qn("w:val"))
    c = {"t": "\n".join(righe).strip("\n")}
    if bold and all(bold) or any(stile(p) == "Intestazionetabella" for p in tc.iter(qn("w:p"))):
        c["b"] = True
    if al != "left":
        c["al"] = al
    tcpr = tc.find(qn("w:tcPr"))
    if tcpr is not None:
        gs = tcpr.find(qn("w:gridSpan"))
        if gs is not None and int(gs.get(qn("w:val"))) > 1:
            c["span"] = int(gs.get(qn("w:val")))
        vm = tcpr.find(qn("w:vMerge"))
        if vm is not None:
            c["vm"] = "restart" if vm.get(qn("w:val")) == "restart" else "cont"
            if c["vm"] == "cont":
                c["t"] = ""
    return c


def tabella(tbl):
    grid = [int(g.get(qn("w:w"))) for g in tbl.find(qn("w:tblGrid")).findall(qn("w:gridCol"))]
    w = [int(round(g * LARGHEZZA / sum(grid))) for g in grid]
    w[-1] += LARGHEZZA - sum(w)
    righe = [[cella(tc) for tc in tr.findall(qn("w:tc"))] for tr in tbl.findall(qn("w:tr"))]
    testa = 0
    for r in righe:
        if all(c.get("b") for c in r):
            testa += 1
        else:
            break
    return ["tab", {"larghezze": w, "righe": righe, "testa": testa}]


def visita(el, out):
    for c in el.iterchildren():
        if c.tag == qn("w:p"):
            s = stile(c)
            if s in SCARTA:
                continue
            if list(c.iter(qn("w:drawing"))):
                out.append(figura(c))
                continue
            rr = runs(c)
            t = "".join(r[0] for r in rr).strip()
            if not t:
                continue
            if out and out[-1][0] == "img" and out[-1][3] is None and s == "Cella" and t.startswith("Figura"):
                out[-1][3] = t                     # didascalia della figura
            elif s == "SezLv1":
                out.append(["proponente", t])
            elif s == "NomeproponenteIII":
                out.append(["sotto", t])
            elif t.startswith("•"):
                out.append(["punto", t.lstrip("•").strip()])
            elif all(r[1] for r in rr if r[0].strip()):
                out.append(["sotto", t])
            else:
                rr = [list(r) for r in rr]
                rr[0][0] = rr[0][0].lstrip()
                rr[-1][0] = rr[-1][0].rstrip()
                out.append(["testo", rr])
        elif c.tag == qn("w:tbl"):
            grid = c.find(qn("w:tblGrid")).findall(qn("w:gridCol"))
            trs = c.findall(qn("w:tr"))
            if len(grid) == 1 and len(trs) == 1:   # riquadro: contenitore di testo o di figura
                visita(trs[0].find(qn("w:tc")), out)
            else:
                out.append(tabella(c))


body = list(D.element.body.iterchildren())
def titolo(el):
    return stile(el) if el.tag == qn("w:p") else ""
# I nodi si riconoscono dai titoli ministeriali del documento
NODI, cur = {}, None
for el in body:
    t = "".join(x.text or "" for x in el.iter(qn("w:t"))) if el.tag == qn("w:p") else ""
    if titolo(el) == "Paragrafoministeriale" and t.startswith("1.STRUTTURA"):
        cur = "I.1"
    elif titolo(el) == "Paragrafoministeriale" and t.startswith("2.SETTORE"):
        cur = "I.2"
    elif titolo(el) == "Titolosezioneministeriale" and t.startswith("III"):
        cur = None
    elif titolo(el) == "Sottoparagrafoministeriale" and t.startswith("1.1"):
        cur = "III.1.1"
    elif titolo(el) == "Sottoparagrafoministeriale" and t.startswith("1.2"):
        cur = "III.1.2"
    elif cur and el.tag in (qn("w:p"), qn("w:tbl")):

        NODI.setdefault(cur, [])
        # visita un solo elemento: lo si avvolge in un contenitore temporaneo
        class _C:
            def __init__(s, e): s.e = e
            def iterchildren(s): return iter([s.e])
        visita(_C(el), NODI[cur])

with open(dest / "parti_I_III_moovxr.py", "w", encoding="utf8") as f:
    f.write("# -*- coding: utf-8 -*-\n# Generato da importa_parti_I_III.py da: %s\n"
            "# Non modificare a mano: rigenerare dal documento ricevuto.\n" % src.name)
    f.write("BLOCCHI = ")
    f.write(pprint.pformat(NODI, width=110, sort_dicts=False))
    f.write("\n")
for k, v in NODI.items():
    print(k, len(v), "blocchi", {t: sum(1 for b in v if b[0] == t) for t in ("proponente", "sotto", "testo", "punto", "tab", "img")})
print("figure:", nfig[0])
