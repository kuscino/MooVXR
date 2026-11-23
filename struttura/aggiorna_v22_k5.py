# Versione 22 (23/11): K5 (cinetosi) marcato "Finale": si misura in A10.3, che si chiude al mese 22, dopo la verifica
# intermedia del mese 18. Nessun effetto sui costi.
# Uso: python3 struttura/aggiorna_v22_k5.py struttura/economics_moovxr_v21_23nov.py struttura/economics_moovxr.py
import importlib.util, pprint, sys
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
k = [i for i, x in enumerate(C["kpi"]) if x[0] == "K5"]; assert len(k) == 1 and C["kpi"][k[0]][4] == "Intermedio"
x = list(C["kpi"][k[0]]); x[4] = "Finale"; C["kpi"][k[0]] = tuple(x)
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 21 (23/11/2026):", "Versione 22 (23/11/2026): K5 finale (aggiorna_v22_k5.py).\nVersione 21 (23/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok")
