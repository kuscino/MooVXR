# Versione 14 (23/11): servizi di Aubay. Licenza dei sorgenti della soluzione Wiki-RAG di 42Rows per la base di
# conoscenza tecnica del progetto (OR14, A14.1); servizi LLM a consumo e licenze di strumenti di sviluppo basati
# su LLM, 80.000 € ripartiti sugli OR di Aubay in proporzione al costo del personale (OR1 32.000, OR6 22.000,
# OR14 26.000).
# Uso: python3 struttura/aggiorna_v14_aubay.py struttura/economics_moovxr_v13_23nov.py struttura/economics_moovxr.py
import importlib.util, pprint, sys
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
LLM = ("Servizi di modelli linguistici di grandi dimensioni (LLM) a consumo e licenze di strumenti di sviluppo basati "
       "su LLM per il team del progetto, per la durata delle attività")
MOT = ("Consumo dei modelli LLM nelle attività dell'OR e strumenti di sviluppo assistito riservati al team del "
       "progetto")
C["consulenze"] += [
    ("42Rows",
     "Licenza dei sorgenti della soluzione Wiki-RAG per la base di conoscenza tecnica del progetto (requisiti, "
     "interfacce, configurazioni, evidenze di prova)", "OR14", 90000,
     "Base di conoscenza tecnica dell'integrazione: tracciabilità fra requisiti, interfacce dei partner e prove del "
     "dimostratore", "Altri servizi e licenze", "A14.1", ""),
    ("Fornitori da individuare", LLM, "OR1", 32000, MOT, "Altri servizi e licenze", "", ""),
    ("Fornitori da individuare", LLM, "OR6", 22000, MOT, "Altri servizi e licenze", "", ""),
    ("Fornitori da individuare", LLM, "OR14", 26000, MOT, "Altri servizi e licenze", "", ""),
]
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 13 (23/11/2026):", "Versione 14 (23/11/2026): Wiki-RAG e servizi LLM di Aubay (aggiorna_v14_aubay.py).\nVersione 13 (23/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok")
