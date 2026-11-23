# Versione 13 (23/11): costi del Politecnico dall'Excel del 22/11 (MooVXR_Politecnico_costi_CONSEGNA_20261122.xlsx,
# "v13" del Politecnico), acquisiti come sono: team dal gruppo nominativo di 18 posizioni (ore per fascia del
# foglio Team, impegno medio per attività), 20 attrezzature e 17 voci di servizi e consulenze. Totali per OR
# invariati; addetti della Tab. 2 pari alle persone distinte (5/2/11). Titolo di A10.5: resta la proposta del 21/11, in attesa di conferma del Politecnico.
# Uso: python3 struttura/aggiorna_v13_polimi.py struttura/economics_moovxr_v12_23nov.py struttura/economics_moovxr.py
import importlib.util, os, pprint, sys
import openpyxl
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
R = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), "..", "..", "Documenti RICEVUTI")
wb = openpyxl.load_workbook(os.path.join(R, "MooVXR_Politecnico_costi_CONSEGNA_20261122.xlsx"), data_only=True)
ORE = 1500
POLI = ("OR9", "OR10", "OR11")
T = {r[1]: r for r in wb["Team"].iter_rows(min_row=2, values_only=True) if r[0] in POLI and r[1]}
att, n = [], 0
for a in C["attivita"]:
    if a[0] in POLI:
        r = T[a[1]]
        s, f, imp = int(r[3]), int(r[4]), float(r[9])
        d = f - s + 1
        # persone equivalenti per fascia: riproducono le ore del Politecnico con l'impegno medio dell'attività
        nf = [round((r[10 + k] or 0) / (d * imp * ORE / 12), 4) for k in range(3)]
        a = (a[0], a[1], a[2], s, f, a[5], nf[0], nf[1], nf[2], round(imp, 4), a[10],
             "Responsabile scientifico e professori: indirizzo, revisione e validazione" if nf[0] else None,
             "Professori associati e ricercatori senior: progettazione e sperimentazione" if nf[1] else None,
             "Ricercatori, dottorandi e assegnisti: sviluppo, prove e analisi" if nf[2] else None)
        n += 1
    att.append(a)
assert n == 15, n
# ore intere per OR e fascia che riproducono esattamente il costo del personale del Politecnico
# (OR9 698.000 €, OR10 598.000 €, OR11 654.000 €); il file del Politecnico usa ore non intere
import math
RX = lambda v: math.floor(v + 0.5)
OBI = {"OR9": (4258, 1808, 7567), "OR10": (2820, 0, 10870), "OR11": (3566, 1816, 7909)}
for o, obi in OBI.items():
    assert obi[0] * 81 + obi[1] * 53 + obi[2] * 34 == {"OR9": 698000, "OR10": 598000, "OR11": 654000}[o]
    idx = [i for i, a in enumerate(att) if a[0] == o]
    for f in range(3):
        for _ in range(40):
            ore = sum(RX(att[i][6 + f] * ((att[i][4] - att[i][3] + 1) * att[i][9]) * ORE / 12) for i in idx)
            dlt = obi[f] - ore
            if dlt == 0:
                break
            j = max(idx, key=lambda i: att[i][6 + f])
            a = list(att[j]); dd = (a[4] - a[3] + 1) * a[9] * ORE / 12
            a[6 + f] = round(a[6 + f] + dlt / dd, 4); att[j] = tuple(a)
        assert dlt == 0, (o, f, dlt)
C["attivita"] = att
attr = [x for x in C["attrezzature"] if x[2] not in POLI]
for r in wb["Attrezzature"].iter_rows(min_row=2, values_only=True):
    if r[0] and r[2] in POLI:
        attr.append((r[0], r[1], r[2], r[3], r[4], 0.0, r[5], r[6], r[7], r[8]))
C["attrezzature"] = attr
cons = [c for c in C["consulenze"] if c[2] not in POLI]
for r in wb["Servizi"].iter_rows(min_row=2, values_only=True):
    if not (r[1] and r[2] in POLI):
        continue
    mot = str(r[6] or "")
    if str(r[4]).startswith("Altri servizi"):
        cat = "Altri servizi e licenze"
    elif "Consulenza di dominio" in mot or "Competenza di dominio" in mot:
        cat = "Consulenza"
    else:
        cat = "Ricerca contrattuale"
    ruolo = mot.split("|")[0].strip() if cat != "Altri servizi e licenze" else ""
    cons.append((r[0], r[1], r[2], r[5], mot, cat, r[3] or "", ruolo))
C["consulenze"] = cons
# Tab. 2: persone distinte per fascia del gruppo del Politecnico (conteggio dal loro Excel, senza nomi)
C.setdefault("addetti", {})["Politecnico di Milano"] = {"Alto": 5, "Medio": 2, "Basso": 11}
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 12 (23/11/2026):", "Versione 13 (23/11/2026): costi del Politecnico del 22/11 (aggiorna_v13_polimi.py).\nVersione 12 (23/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok")
