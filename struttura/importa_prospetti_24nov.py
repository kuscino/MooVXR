# -*- coding: utf-8 -*-
"""Importa il paragrafo III.4 dal documento "Prospetti finanziari.docx" (24/11, fa fede per i piani finanziari delle
quattro imprese) e scrive struttura/testi_prospetti_iii4.py con INTRO (paragrafi introduttivi) e PIANI
(intestazione, righe della tabella, nota).
Uso: python3 struttura/importa_prospetti_24nov.py "<Prospetti finanziari.docx>" struttura/testi_prospetti_iii4.py"""
import pprint, sys, zipfile
from lxml import etree

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
EL = list(etree.fromstring(zipfile.ZipFile(sys.argv[1]).read("word/document.xml")).find(W + "body"))


def t(el):
    return "".join(x.text or "" for x in el.iter(W + "t")).strip()


i0 = next(i for i, e in enumerate(EL) if t(e).startswith("4. RISORSE FINANZIARIE"))
i1 = next(i for i, e in enumerate(EL) if i > i0 and t(e).startswith("SINTESI NUMERICA"))
INTRO, PIANI, cur = [], [], None
for e in EL[i0 + 1:i1]:
    if e.tag == W + "tbl":
        cur["righe"] = [[" ".join(t(p) for p in tc.iter(W + "p") if t(p)).replace("Anno (", "Anno (")
                         for tc in tr.iter(W + "tc")] for tr in e.iter(W + "tr")]
        continue
    st = e.find(W + "pPr/" + W + "pStyle")
    if st is not None and st.get(W + "val", "").startswith("Istruzione"):
        continue
    x = t(e)
    if not x:
        continue
    runs = [r for r in e.iter(W + "r") if "".join(y.text or "" for y in r.iter(W + "t")).strip()]
    if runs and all(r.find(W + "rPr/" + W + "b") is not None for r in runs) and len(x) < 60:
        cur = {"titolo": x, "righe": None, "nota": None}; PIANI.append(cur)
    elif cur is None:
        INTRO.append(x)
    else:
        cur["nota"] = x
assert len(PIANI) == 4 and all(p["righe"] and p["nota"] for p in PIANI)
for p in PIANI:                                   # intestazioni degli anni: "Anno (2027)"
    p["righe"][1] = [p["righe"][1][0]] + [c.replace("Anno(", "Anno (").replace("Anno (", "Anno (") for c in p["righe"][1][1:]]
with open(sys.argv[2], "w", encoding="utf8") as f:
    f.write("# -*- coding: utf-8 -*-\n# Generato da importa_prospetti_24nov.py da Prospetti finanziari.docx. "
            "Non modificare a mano.\n")
    f.write("INTRO = %s\n\nPIANI = %s\n" % (pprint.pformat(INTRO, width=120), pprint.pformat(PIANI, width=120)))
print(len(INTRO), [p["titolo"] for p in PIANI], PIANI[0]["righe"][1])
