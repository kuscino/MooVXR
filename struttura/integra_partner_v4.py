# Costruisce la configurazione v4 del modello economico MooVXR (struttura/economics_moovxr.py) dalla v3
# (economics_moovxr_v3_20nov.py) e dagli Excel dei costi dei partner del 20/11 in Documenti RICEVUTI.
# Uso: python3 struttura/integra_partner_v4.py struttura/economics_moovxr.py
import importlib.util, os, pprint, sys
import openpyxl
W = os.path.expanduser("~/mnt/MooVXR/Area di Lavoro")
R = os.path.expanduser("~/mnt/MooVXR/Documenti RICEVUTI")
spec = importlib.util.spec_from_file_location("eco", W + "/struttura/economics_moovxr_v3_20nov.py")
eco = importlib.util.module_from_spec(spec); spec.loader.exec_module(eco)
C = eco.CONFIG
FILES = {"GSNet": "MooVXR_GSNet_costi GSNET1.xlsx", "Anitia": "MooVXR_Anitia_costi_rev1.xlsx",
         "nLight": "MooVXR_nLight_costi v2.xlsx", "Politecnico di Milano": "MooVXR_Politecnico_costi_CONSEGNA_20261120.xlsx"}
ORS = {"GSNet": ["OR2", "OR3", "OR4", "OR5"], "Anitia": ["OR7", "OR8"], "nLight": ["OR12", "OR13"],
       "Politecnico di Milano": ["OR9", "OR10", "OR11"]}
TIPO_OR = {o[0]: o[3] for o in C["or"]}
RUOLI = ("Responsabile tecnico: indirizzo, revisione e validazione", "Senior: progettazione e sviluppo",
         "Sviluppatore o tecnico: implementazione e prove")
vecchie = {a[1]: a for a in C["attivita"]}
# rinumerazione di OR4 nella revisione GSNet: nuova A4.4, ex A4.4-A4.8 -> A4.5-A4.9
RINUM = {"A4.5": "A4.4", "A4.6": "A4.5", "A4.7": "A4.6", "A4.8": "A4.7", "A4.9": "A4.8"}

def num(v):
    return 0 if v in (None, "") else v

def team(nome):
    wb = openpyxl.load_workbook(os.path.join(R, FILES[nome]), data_only=True)
    titoli = {}
    for r in wb["Costi per task"].iter_rows(min_row=2, values_only=True):
        if r[0] and str(r[0]).startswith("OR") and r[1]:
            titoli[r[1]] = str(r[2]).strip()
    righe = []
    for r in wb["Team"].iter_rows(min_row=2, values_only=True):
        if not (r[0] and str(r[0]).startswith("OR") and r[1]):
            continue
        righe.append(dict(OR=r[0], id=r[1], titolo=titoli.get(r[1], str(r[2]).strip()), da=int(r[3]), a=int(r[4]),
                          nA=num(r[6]), nM=num(r[7]), nB=num(r[8]), imp=float(r[9])))
    par = {r[0]: r[1] for r in wb["Parametri"].iter_rows(min_row=2, values_only=True) if r[0]}
    attr = [r for r in wb["Attrezzature"].iter_rows(min_row=2, values_only=True) if r[0] and r[2]]
    serv = [r for r in wb["Servizi"].iter_rows(min_row=2, values_only=True) if r[1] and r[2]]
    return righe, par, attr, serv

nuove_att, nuove_attr, nuove_cons = [], [], []
for nome, ors in ORS.items():
    righe, par, attr, serv = team(nome)
    assert {r["OR"] for r in righe} == set(ors), (nome, {r["OR"] for r in righe})
    ore = par["Ore annue"]; tar = (par["€/h Alto"], par["€/h Medio"], par["€/h Basso"])
    for o in ors:
        rr = [r for r in righe if r["OR"] == o]
        costi = [sum(round(n * (r["a"] - r["da"] + 1) / 12 * ore * r["imp"]) * t
                     for n, t in zip((r["nA"], r["nM"], r["nB"]), tar)) for r in rr]
        pesi = [round(c / sum(costi), 2) for c in costi]
        pesi[costi.index(max(costi))] += round(1 - sum(pesi), 2)
        for r, p in zip(rr, pesi):
            old = vecchie.get(RINUM.get(r["id"], r["id"])) if not (nome == "GSNet" and r["id"] == "A4.4") else None
            d = "D" + r["id"][1:]
            nuove_att.append((o, r["id"], r["titolo"], r["da"], r["a"], round(p, 2), r["nA"], r["nM"], r["nB"],
                              r["imp"], d, RUOLI[0] if r["nA"] else None, RUOLI[1] if r["nM"] else None,
                              RUOLI[2] if r["nB"] else None))
    for a in attr:
        voce, mod, o, q, pu, amm, uso, imp, vita = a[:9]
        nuove_attr.append((voce, mod, o, q, pu, 1.0 if TIPO_OR[o] == "SS" else 0.0, amm, uso, imp, vita))
    vec_cons = {(c[2], c[1]): c for c in C["consulenze"]}
    vec_task = {(c[2], c[6]): c for c in C["consulenze"] if c[6]}
    for s in serv:
        sog, ogg, o, task, cat, imp, mot = s[:7]
        task = task or ""
        old = vec_cons.get((o, ogg)) or (vec_task.get((o, task)) if task else None)
        ruolo = old[7] if old else ""
        nuove_cons.append((sog, ogg, o, imp, mot, cat, task, ruolo))

PARTNER_OR = {o for v in ORS.values() for o in v}
C["attivita"] = sorted([a for a in C["attivita"] if a[0] not in PARTNER_OR] + nuove_att,
                       key=lambda a: (int(a[0][2:]), [int(x) for x in a[1][1:].split(".")]))
C["attrezzature"] = [a for a in C["attrezzature"] if a[2] not in PARTNER_OR] + nuove_attr
C["consulenze"] = [c for c in C["consulenze"] if c[2] not in PARTNER_OR] + nuove_cons

# deliverable: nuovi D2.6 e D4.4, rinumerazione D4.4-D4.8, titoli nuovi di nLight, rinvii a OR6 superati
dl = []
for d in C["deliverable"]:
    d = list(d)
    if d[0] == "OR4" and d[1] in ("D4.4", "D4.5", "D4.6", "D4.7", "D4.8"):
        d[1] = "D4.%d" % (int(d[1][3:]) + 1)
    if d[1] == "D4.3":
        d[4] = d[4].replace("tramite OR3 e OR6", "tramite OR3 e le applicazioni XR di OR4")
    if d[1] == "D12.3":
        d[2], d[4] = "Modulo di stabilizzazione inerziale", "Tremolio delle immagini ed errore di posizione ridotti rispetto al modulo non stabilizzato"
    if d[1] == "D12.4":
        d[2] = "Modulo di percezione in bassa visibilità e di fusione multisensore"
        d[4] = "Prestazioni di rilevamento misurate di notte e con visibilità ridotta; errore di distanza entro obiettivo"
    dl.append(tuple(d))
dl.append(("OR2", "D2.6", "Studio per la realizzazione di una IMU", 24, "Da definire con GSNet"))
dl.append(("OR4", "D4.4", "Applicazione di bordo per acquisizione sincronizzata dei dati GNSS, inerziali e altimetrici", 27,
           "Da definire con GSNet"))
C["deliverable"] = sorted(dl, key=lambda d: (int(d[0][2:]), [int(x) for x in d[1][1:].split(".")]))
C["or"] = [tuple(x.replace("veicolo di prova da OR6", "veicolo di prova da OR4") if isinstance(x, str) else x for x in o)
           for o in C["or"]]
C["kpi"] = [tuple(x.replace("(OR10, OR6)", "(OR10, OR4)") if isinstance(x, str) else x for x in k) for k in C["kpi"]]

# proponenti: regione e fatturato medio (ricavi delle vendite, documento Parti I e III e ritorni dei partner)
FATT = {"Aubay Italia": (105000000, "Lazio"), "GSNet": (round((5671268 + 6434150) / 2), "Lazio"),
        "nLight": (round((2268356 + 1907259) / 2), "Piemonte"), "Anitia": (round((1806475 + 2509805) / 2), "Veneto")}
C["proponenti"] = [tuple(list(p[:4]) + [FATT[p[0]][1], FATT[p[0]][0]] + list(p[6:])) if p[0] in FATT else p
                   for p in C["proponenti"]]
r = dict(C["regole"])
nuove_regole = {}
for k, v in r.items():
    nuove_regole[k] = v
    if k == "Quota minima per proponente":
        nuove_regole[k] = (0.05, "DM 31/12/2021, art. 4, c. 2, lett. f), richiamato da DD art. 3, c. 3, lett. b): "
                                 "5% per i proponenti diversi dalle grandi imprese; da verificare sul testo ufficiale")
        nuove_regole["Quota minima per le grandi imprese"] = (0.10, "DM 31/12/2021, art. 4, c. 2, lett. f): 10% per le "
                                                                    "grandi imprese; da verificare sul testo ufficiale")
C["regole"] = nuove_regole
C["nota_tariffe"] = ("Costi standard da Allegato 10, Tab. 1. Ore annue: 1500 per il personale universitario (Allegato 10); "
                     "1720 per le imprese: confermate da Anitia (CCNL Terziario, Commercio), assunzione da verificare "
                     "per gli altri partner.")
testa = open(W + "/struttura/economics_moovxr_v3_20nov.py", encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Generata da uno script di calibrazione: i team e le quote di impegno sono dimensionati sugli importi degli OR\nconcordati (forfait del 20% incluso). Attrezzature e servizi sono ipotesi da confermare con i partner.",
                      "Versione 4 (20/11/2026): OR di Aubay dalla calibrazione del 20/11; OR di GSNet, Anitia, nLight e\nPolitecnico dagli Excel dei costi restituiti dai partner il 20/11 (team, attrezzature e servizi).")
open(sys.argv[1], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("attivita", len(C["attivita"]), "attrezzature", len(C["attrezzature"]), "consulenze", len(C["consulenze"]),
      "deliverable", len(C["deliverable"]))
