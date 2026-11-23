# Versione 21 (23/11): donne per fascia di nLight (2 Bassa), comunicate da Francesco; nessun effetto sui costi.
# Uso: python3 struttura/aggiorna_v21_donne.py struttura/economics_moovxr_v20_23nov.py struttura/economics_moovxr.py
import importlib.util, pprint, sys
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
C["donne"]["nLight"] = {"Basso": 2}
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 20 (23/11/2026):", "Versione 21 (23/11/2026): donne per fascia di nLight (aggiorna_v21_donne.py).\nVersione 20 (23/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok", C["donne"])
