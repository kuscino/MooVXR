# Versione 19 (23/11): team di nLight dal file MooVXR_nLight_costi_rev2.xlsx (Documenti RICEVUTI): persone per fascia e
# impegno di A12.1-A13.5 (nessuna fascia Alta; impegno OR12 95%, OR13 66%); servizio "Realizzazione, schede
# elettroniche, meccaniche e ottiche prototipali per selezione fornitori" (OR12) da 75.000 a 120.000 €.
# Tab. 2 di nLight fissata sugli addetti dichiarati (0/1/5). Date, attrezzature e altri servizi invariati.
# Uso: python3 struttura/aggiorna_v19_nlight.py struttura/economics_moovxr_v18_23nov.py struttura/economics_moovxr.py
import importlib.util, os, pprint, sys
import openpyxl
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
R = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), "..", "..", "Documenti RICEVUTI")
wb = openpyxl.load_workbook(os.path.join(R, "MooVXR_nLight_costi_rev2.xlsx"))
T = {r[1]: r for r in wb["Team"].iter_rows(min_row=2, values_only=True) if r[0] in ("OR12", "OR13") and r[1]}
assert len(T) == 10, sorted(T)
att, n = [], 0
for a in C["attivita"]:
    if a[1] in T:
        r = T[a[1]]
        assert (r[3], r[4]) == (a[3], a[4]), (a[1], "date diverse")
        nuovo = (r[6] or 0, r[7] or 0, r[8] or 0, float(r[9]))
        if nuovo != tuple(a[6:10]):
            n += 1
        a = tuple(a[:6]) + nuovo + tuple(a[10:])
    att.append(a)
assert n == 10, n
C["attivita"] = att
VECCHIO = "Realizzazione meccaniche e ottiche prototipali per selezione fornitori"
NUOVO = "Realizzazione, schede elettroniche, meccaniche e ottiche prototipali per selezione fornitori"
k = [i for i, c in enumerate(C["consulenze"]) if c[1] == VECCHIO and c[2] == "OR12"]
assert len(k) == 1
c = list(C["consulenze"][k[0]]); c[1] = NUOVO; c[3] = 120000; C["consulenze"][k[0]] = tuple(c)
# Tab. 2: addetti dichiarati da nLight nel file rev2 (le persone sono le stesse sulle diverse attività)
C["addetti"]["nLight"] = {"Alto": 0, "Medio": 1, "Basso": 5}
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 18 (23/11/2026):", "Versione 19 (23/11/2026): team e servizi di nLight, rev2 (aggiorna_v19_nlight.py).\nVersione 18 (23/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok, attività modificate:", n)
