# Versione 9 (21/11): tagli ai servizi di Aubay. Eliminati l'accesso a pista (OR14) e la consulenza su sicurezza
# funzionale e linee guida HMI (OR1, A1.2) e le licenze di dati cartografici, POI e routing (OR1: si usano
# Overture Maps, OpenStreetMap, Wikidata, Open Charge Map e PUN) e la licenza del simulatore (OR6: CARLA, SUMO,
# esmini, ns-3, con i modelli dei sensori multispettrali sviluppati in A6.2); licenza di dataset ridotta a
# 20.000 €; servizi di OR14 attribuiti alle attività; motivazioni dei servizi cloud con le attività.
# Uso: python3 struttura/aggiorna_v9_aubay.py struttura/economics_moovxr_v8_21nov.py struttura/economics_moovxr.py
import importlib.util, pprint, sys
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
VIA = {("OR14", "Accesso a pista o area di prova chiusa"),
       ("OR1", "Consulenza su sicurezza funzionale e linee guida HMI (ISO 26262, ISO 21448, linee guida sulla distrazione)"),
       ("OR1", "Licenze di dati cartografici e POI e servizi di routing con disponibilità delle colonnine"),
       ("OR6", "Licenza di software di simulazione di guida e di scena")}
DS = "Licenza di dataset di guida registrati per la verifica del motore"
NOME = {("OR1", DS): "Licenza di dataset di guida registrati per l'addestramento dei modelli del contesto e della "
                     "componente adattiva (A1.1, A1.3)"}
TASK = {("OR14", "Penetration test dell'applicazione e del flusso dei contenuti"): "A14.2",
        ("OR14", "Assessment di conformità a UNECE R155 e ISO/SAE 21434"): "A14.2",
        ("OR14", "Servizi cloud per le prove di carico del sistema"): "A14.4"}
MOT = {"OR1": "Capacità di calcolo GPU a consumo per A1.1, A1.3, A1.6 e A1.7, in luogo di un server dedicato",
       "OR6": "Capacità di calcolo GPU a consumo per le campagne di scenari di A6.5, in luogo di un server dedicato"}
IMPORTO = {("OR1", "Licenza di dataset di guida registrati per la verifica del motore"): 20000}
cons, tolti, ridotti = [], 0, 0
for c in C["consulenze"]:
    k = (c[2], c[1])
    if k in VIA:
        tolti += 1; continue
    if k in IMPORTO:
        c = c[:3] + (IMPORTO[k],) + tuple(c[4:]); ridotti += 1
    c = list(c)
    if k in NOME:
        c[1] = NOME[k]
    if k in TASK:
        c[6] = TASK[k]
    if c[1].startswith("Servizi cloud GPU") and c[2] in MOT:
        c[4] = MOT[c[2]]
    cons.append(tuple(c))
assert tolti == 4 and ridotti == 1, (tolti, ridotti)
C["consulenze"] = cons
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 8 (21/11/2026):", "Versione 9 (21/11/2026): tagli ai servizi di Aubay (aggiorna_v9_aubay.py).\nVersione 8 (21/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok")
