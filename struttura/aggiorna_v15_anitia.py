# Versione 15 (23/11): team di Anitia dal modello v14 rivisto da Anitia (Modello_Economico_MooVXR_v14_Anitia-rev2.xlsx,
# Documenti RICEVUTI): persone per fascia e peso nell'OR delle attività A7.1-A8.4; date e quote di impegno invariate.
# Capofila: GSNet (deciso il 23/11), al posto di Aubay; il flag non entra nei calcoli.
# Uso: python3 struttura/aggiorna_v15_anitia.py struttura/economics_moovxr_v14_23nov.py struttura/economics_moovxr.py
import importlib.util, os, pprint, sys
import openpyxl
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
R = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), "..", "..", "Documenti RICEVUTI")
ws = openpyxl.load_workbook(os.path.join(R, "Modello_Economico_MooVXR_v14_Anitia-rev2.xlsx"))["Attività"]
T = {r[1]: r for r in ws.iter_rows(min_row=2, values_only=True) if r[0] in ("OR7", "OR8") and r[1]}
assert len(T) == 8, sorted(T)
att, n = [], 0
for a in C["attivita"]:
    if a[1] in T:
        r = T[a[1]]
        assert (r[3], r[4], r[9]) == (a[3], a[4], a[9]), (a[1], "date o impegno diversi")
        nuovo = (r[5], r[6], r[7], r[8])
        if nuovo != tuple(a[5:9]):
            n += 1
        a = tuple(a[:5]) + nuovo + tuple(a[9:])
    att.append(a)
assert n == 8, n
C["attivita"] = att
C["proponenti"] = [tuple(p[:6]) + (("Sì" if p[0] == "GSNet" else "No"),) + tuple(p[7:]) for p in C["proponenti"]]
assert [p[6] for p in C["proponenti"]].count("Sì") == 1
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 14 (23/11/2026):", "Versione 15 (23/11/2026): team di Anitia (rev2), capofila GSNet (aggiorna_v15_anitia.py).\nVersione 14 (23/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok, attività modificate:", n)
