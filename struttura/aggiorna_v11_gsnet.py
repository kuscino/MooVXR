# Versione 11 (22/11): team di GSNet dal nuovo Excel (MooVXR_GSNet_costi GSNET 2.xlsx, Documenti RICEVUTI):
# fascia Media ridotta su A2.1, A2.2, A3.1, A3.3, A4.1, A4.4, A4.5, A5.1; costi ricalcolati dal foglio Team
# (il file di GSNet riporta ancora in A4.4 il personale di A4.3).
# Uso: python3 struttura/aggiorna_v11_gsnet.py struttura/economics_moovxr_v10_21nov.py struttura/economics_moovxr.py
import importlib.util, os, pprint, sys
import openpyxl
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
R = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), "..", "..", "Documenti RICEVUTI")
wb = openpyxl.load_workbook(os.path.join(R, "MooVXR_GSNet_costi GSNET 2.xlsx"), data_only=True)
T = {r[1]: r for r in wb["Team"].iter_rows(min_row=2, values_only=True) if r[0] and str(r[0]).startswith("OR") and r[1]}
att, n = [], 0
for a in C["attivita"]:
    if a[1] in T and a[0] in ("OR2", "OR3", "OR4", "OR5"):
        r = T[a[1]]
        nuovo = (r[3], r[4], r[6] or 0, r[7] or 0, r[8] or 0, float(r[9]))
        if nuovo != (a[3], a[4], a[6], a[7], a[8], a[9]):
            n += 1
        a = (a[0], a[1], a[2], nuovo[0], nuovo[1], a[5], nuovo[2], nuovo[3], nuovo[4], nuovo[5]) + tuple(a[10:])
    att.append(a)
assert n == 8, n
C["attivita"] = att
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 10 (21/11/2026):", "Versione 11 (22/11/2026): team di GSNet dal nuovo Excel (aggiorna_v11_gsnet.py).\nVersione 10 (21/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok, attività modificate:", n)
