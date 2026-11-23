# Versione 20 (23/11): donne per fascia di GSNet (2 Media, 3 Bassa), comunicate da Francesco; nessun effetto sui costi.
# Uso: python3 struttura/aggiorna_v20_donne.py struttura/economics_moovxr_v19_23nov.py struttura/economics_moovxr.py
import importlib.util, pprint, sys
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
C["donne"]["GSNet"] = {"Medio": 2, "Basso": 3}
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 19 (23/11/2026):", "Versione 20 (23/11/2026): donne per fascia di GSNet (aggiorna_v20_donne.py).\nVersione 19 (23/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok", C["donne"])
