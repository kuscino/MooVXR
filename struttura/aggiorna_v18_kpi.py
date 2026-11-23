# Versione 18 (23/11): valori obiettivo dei KPI dai testi del Piano di Sviluppo confermati il 23/11:
# K1 15% (A1.3, A10.5), K3 5 mrad (A9.2, A11.3), K4 2% (A11.2, A11.5), K5 30% (A10.3), K7 50 ms (A1.2, A1.5).
# Nessun effetto sui costi.
# Uso: python3 struttura/aggiorna_v18_kpi.py struttura/economics_moovxr_v17_23nov.py struttura/economics_moovxr.py
import importlib.util, pprint, sys
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
NUOVI = {"K1": (15, "Piano di Sviluppo, A1.3 e A10.5 (23/11/2026): riduzione di almeno il 15%"),
         "K3": (5, "Piano di Sviluppo, A9.2 e A11.3 (23/11/2026): errore inferiore a 5 mrad al 95° percentile"),
         "K4": (2, "Piano di Sviluppo, A11.2 e A11.5 (23/11/2026): non superiore al 2% della luminanza nominale"),
         "K5": (30, "Piano di Sviluppo, A10.3 (23/11/2026): riduzione dell'incidenza di almeno il 30%"),
         "K7": (50, "Piano di Sviluppo, A1.2 e A1.5 (23/11/2026): inferiore a 50 ms nel 95% dei casi")}
kpi = []
for k in C["kpi"]:
    if k[0] in NUOVI:
        k = tuple(k[:7]) + NUOVI[k[0]] + tuple(k[9:])
    kpi.append(k)
assert sum(1 for k in kpi if k[0] in NUOVI) == 5
C["kpi"] = kpi
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 17 (23/11/2026):", "Versione 18 (23/11/2026): valori obiettivo dei KPI (aggiorna_v18_kpi.py).\nVersione 17 (23/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok")
