# Versione 26 (24/11): finanziamento agevolato al 20% dei costi per GSNet, Anitia e nLight, come nei piani
# finanziari del documento "Prospetti finanziari.docx" (24/11, fa fede); Aubay solo contributo diretto.
# Uso: python3 struttura/aggiorna_v26_finanziamento.py struttura/economics_moovxr_v25_24nov.py struttura/economics_moovxr.py
import importlib.util, pprint, sys
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
n = 0
for i, p in enumerate(C["proponenti"]):
    if p[0] in ("GSNet", "Anitia", "nLight"):
        assert p[9] == 0
        C["proponenti"][i] = tuple(p[:9]) + (0.2,) + tuple(p[10:]); n += 1
assert n == 3
C["nota_agevolazioni"] = C["nota_agevolazioni"].replace(
    "Finanziamento agevolato non richiesto in questa ipotesi.",
    "Finanziamento agevolato richiesto da GSNet, Anitia e nLight per il 20% dei costi, come nei piani finanziari "
    "del 24/11; Aubay richiede solo il contributo diretto.")
assert "20% dei costi" in C["nota_agevolazioni"]
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 25 (24/11/2026):", "Versione 26 (24/11/2026): finanziamento agevolato al 20% per GSNet, "
                      "Anitia e nLight (aggiorna_v26_finanziamento.py).\nVersione 25 (24/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok")
