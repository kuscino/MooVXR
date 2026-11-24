# -*- coding: utf-8 -*-
"""Importa la revisione di Anitia del 24/11 (Piano_di_Sviluppo_scheletro_v15_Anitia.docx, revisioni tracciate
accettate) e scrive struttura/testi_anitia_24nov.py con:
- I_1, I_2, III_1_1: i blocchi di Anitia delle Parti I e III, nel formato di parti_I_III_moovxr.py;
- OR78: le coppie (testo precedente, testo nuovo) dei paragrafi modificati in OR7 e OR8;
- III_2_1, III_2_2, III_3_1, III_4: i paragrafi nuovi della Parte III, come liste (tipo, testo) e tabelle grezze.
Uso: python3 struttura/importa_anitia_24nov.py "<docx di Anitia>" struttura/testi_anitia_24nov.py"""
import pprint, re, sys, zipfile
from lxml import etree

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
body = etree.fromstring(zipfile.ZipFile(sys.argv[1]).read("word/document.xml")).find(W + "body")
EL = list(body)


def runs(p, keep="new"):
    out = []
    for r in p.iter(W + "r"):
        anc = [a.tag for a in r.iterancestors()]
        if keep == "new" and W + "del" in anc:
            continue
        if keep == "old" and W + "ins" in anc:
            continue
        s = "".join((x.text or "") for x in r.iter(W + "t", W + "delText"))
        if s:
            out.append([s, r.find(W + "rPr/" + W + "b") is not None, r.find(W + "rPr/" + W + "i") is not None])
    return out


def testo(p, keep="new"):
    return "".join(x[0] for x in runs(p, keep))


def stile(p):
    s = p.find(W + "pPr/" + W + "pStyle")
    return s.get(W + "val") if s is not None else ""


def righe(tbl):
    out = []
    for tr in tbl.iter(W + "tr"):
        out.append(["\n".join(testo(pp) for pp in tc.iter(W + "p")).strip() for tc in tr.iter(W + "tc")])
    return out


ETICHETTE = ["Competenze.", "Maturità tecnologica.", "Coordinamento con soggetti terzi.",
             "Risorse strumentali possedute.", "Risorse strumentali da acquistare.", "Procedure di gestione della R&S.",
             "Qualificazione dei dati da strada e infrastruttura (OR7).",
             "Piattaforma di accesso ai dati del veicolo e di aggiornamento coordinato del software di bordo (OR8).",
             "Settore di destinazione.", "Dimensione del mercato.", "Sistema competitivo.", "Posizionamento.",
             "Impatto economico.", "Investimenti per l'industrializzazione.", "Ricadute occupazionali."]


def blocchi_parti(a, b):
    """Blocchi nel formato di parti_I_III_moovxr.py (testo, sotto, punto, tab grezza, img segnaposto)."""
    out = []
    for el in EL[a:b + 1]:
        if el.tag == W + "tbl":
            out.append(["tab_grezza", righe(el)]); continue
        if el.find(".//" + W + "drawing") is not None:
            out.append(["img_originale"]); continue
        rr = runs(el); t = "".join(x[0] for x in rr).strip()
        if not t:
            continue
        if stile(el) == "Paragrafoelenco":
            out.append(["punto", t])
        elif all(x[1] for x in rr) and len(t) < 120:
            out.append(["sotto", t])
        else:
            et = next((e for e in ETICHETTE if t.startswith(e + " ")), None)
            if et:
                out.append(["testo", [[et, True, False], [t[len(et):], False, False]]])
            else:
                out.append(["testo", [[t, False, False]]])
    return out


def spec(a, b):
    out = []
    for el in EL[a:b + 1]:
        if el.tag == W + "tbl":
            out.append(("tab", righe(el))); continue
        t = testo(el).strip()
        if not t:
            continue
        if stile(el) == "Paragrafoelenco":
            out.append(("p", t)); continue
        et = next((e for e in ETICHETTE if t.startswith(e + " ")), None)
        out.append(("e", (et, t[len(et) + 1:])) if et else ("t", t))
    return out


coppie = []
for el in EL[1061:1333]:
    if el.tag == W + "p" and (el.find(".//" + W + "ins") is not None or el.find(".//" + W + "del") is not None):
        v, n = testo(el, "old").strip(), testo(el).strip()
        if v != n:
            coppie.append((v, n))

D = dict(I_1=blocchi_parti(87, 103), I_2=blocchi_parti(201, 225), III_1_1=blocchi_parti(2151, 2162), OR78=coppie,
         III_2_1=spec(2192, 2198), III_2_2=spec(2220, 2234), III_3_1=spec(2255, 2267), III_4=spec(2282, 2284))
with open(sys.argv[2], "w", encoding="utf8") as f:
    f.write("# -*- coding: utf-8 -*-\n# Generato da importa_anitia_24nov.py da %s. Non modificare a mano.\n"
            % sys.argv[1].split("/")[-1])
    for k, v in D.items():
        f.write("%s = %s\n\n" % (k, pprint.pformat(v, width=120)))
print({k: len(v) for k, v in D.items()})
