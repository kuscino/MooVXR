# Versione 25 (24/11): revisione del Politecnico del 24/11 (registro di tracciabilità Rev. 8 e
# 20261124_Modello_Economico_MooVXR_v24_ALLINEATO_PoliMI.xlsx): titoli di D9.1, D9.2, D9.3, D10.3, D10.5, D11.4 come
# nel loro file; criterio di D10.5 nella forma di compromesso (misura documentata, esito non vincolante);
# D2.5 al mese 20 (fine di A2.5); titolo di CAT-04 senza "agentica" (Cognitive Mesh deterministica). Costi invariati.
# Uso: python3 struttura/aggiorna_v25_polimi.py struttura/economics_moovxr_v24_24nov.py struttura/economics_moovxr.py
import importlib.util, pprint, sys
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
TIT = {
    "D9.1": "Algoritmi, dataset e rapporto riproducibile di localizzazione; verifica di accuratezza, affidabilità e "
            "robustezza in condizioni diverse.",
    "D9.2": "Algoritmi di ancoraggio e specifiche dei riferimenti; verifica della stabilità geometrica e temporale.",
    "D9.3": "Stimatore di affidabilità e schema comune per livelli di servizio; valutazione dell’incertezza e delle "
            "condizioni degradate.",
    "D10.3": "Dati sperimentali su passeggeri e cinetosi; valutazione comparativa del comfort nelle diverse condizioni "
             "di prova.",
    "D10.5": "Rapporto di verifica delle regole adattive, completo di metodologia, risultati anche negativi e limiti "
             "della sperimentazione.",
    "D11.4": "Prototipo di laboratorio dell'HUD per il passeggero, con sintetica documentazione tecnica e delle "
             "verifiche eseguite.",
}
CRIT_D105 = ("Rapporto sperimentale completo e riproducibile, con la misura degli indicatori di attenzione rispetto alle "
             "regole fisse; metodologia, risultati anche negativi e limiti documentati.")
n = 0
for i, d in enumerate(C["deliverable"]):
    x = list(d)
    if x[1] in TIT:
        x[2] = TIT[x[1]]; n += 1
    if x[1] == "D10.5":
        assert x[4] == "Indicatori di attenzione non peggiorati rispetto alle regole fisse"; x[4] = CRIT_D105
    if x[1] == "D2.5":
        assert x[3] == 24; x[3] = 20
    C["deliverable"][i] = tuple(x)
assert n == 6
m = 0
for i, s in enumerate(C["consulenze"]):
    if isinstance(s, tuple) and any(isinstance(v, str) and v.startswith("CAT-04: Prove di resilienza agentica") for v in s):
        C["consulenze"][i] = tuple(v.replace("CAT-04: Prove di resilienza agentica:", "CAT-04: Prove di resilienza "
                                "dell'orchestrazione:") if isinstance(v, str) else v for v in s); m += 1
assert m == 1, m
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 24 (23/11/2026):", "Versione 25 (24/11/2026): revisione del Politecnico del 24/11, D2.5 al "
                      "mese 20, titolo di CAT-04 (aggiorna_v25_polimi.py).\nVersione 24 (23/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok")
