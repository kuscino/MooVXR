# Versione 16 (23/11): donne per fascia di Aubay (3 Media, 6 Bassa), comunicate da Francesco; nessun effetto sui costi.
# Uso: python3 struttura/aggiorna_v16_donne.py struttura/economics_moovxr_v15_23nov.py struttura/economics_moovxr.py
import importlib.util, pprint, sys
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
C["donne"] = {"Aubay Italia": {"Medio": 3, "Basso": 6}, **C["donne"]}
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 15 (23/11/2026):", "Versione 16 (23/11/2026): donne per fascia di Aubay (aggiorna_v16_donne.py).\nVersione 15 (23/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok", C["donne"])
