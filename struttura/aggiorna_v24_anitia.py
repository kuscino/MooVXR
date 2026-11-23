# Versione 24 (23/11): addetti di Anitia su A8.1-A8.4 dal file Modello_Economico_MooVXR_v20_Anitia-addetti.xlsx
# (impegno di OR8 da 0,65 a 0,75, persone ridotte in proporzione; ore e costi invariati; Tab. 2 Anitia 1/4/9).
# Dal file di Anitia si prendono solo queste quattro righe: il resto resta come nella v23.
# Uso: python3 struttura/aggiorna_v24_anitia.py struttura/economics_moovxr_v23_23nov.py struttura/economics_moovxr.py <Excel di Anitia>
import importlib.util, pprint, sys, openpyxl
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
A = {r[1]: r for r in openpyxl.load_workbook(sys.argv[3], data_only=True)["Attività"].iter_rows(min_row=2, values_only=True)
     if r[1] in ("A8.1", "A8.2", "A8.3", "A8.4")}
assert len(A) == 4 and all(r[11] == "Anitia" for r in A.values())
n = 0
for i, a in enumerate(C["attivita"]):
    if a[1] in A:
        r = A[a[1]]
        assert abs(a[9] - 0.65) < 1e-9 and abs(r[9] - 0.75) < 1e-9
        for k in (6, 7, 8):                         # stesse FTE: n x impegno invariato
            assert abs(a[k] * a[9] - r[k] * r[9]) < 1e-6, (a[1], k)
        x = list(a); x[6], x[7], x[8], x[9] = r[6], r[7], r[8], r[9]
        C["attivita"][i] = tuple(x); n += 1
assert n == 4
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 23 (23/11/2026):", "Versione 24 (23/11/2026): addetti di Anitia su A8.1-A8.4, impegno OR8 0,75 "
                      "(aggiorna_v24_anitia.py).\nVersione 23 (23/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok")
