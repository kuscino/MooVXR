# Versione 6 (21/11): attrezzature e servizi di Aubay. Server GPU sostituiti da servizi cloud a costo
# invariato; workstation GPU per il digital twin; sistema di acquisizione dati a noleggio; titolo di A14.3.
# Uso: python3 struttura/aggiorna_v6_aubay.py struttura/economics_moovxr_v5_20nov.py struttura/economics_moovxr.py
import importlib.util, pprint, sys
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
VIA = {("OR1", "Server GPU per addestramento e simulazione"), ("OR6", "Server GPU per la simulazione")}
SOST = {
    ("OR6", "Workstation di simulazione"):
        ("Workstation GPU per il digital twin", "Da definire", "OR6", 6, 9000, 0.0, 60, 27, 1.0, "No"),
    ("OR14", "Sistema di acquisizione dati sincronizzata per le prove su strada"):
        ("Noleggio del sistema di acquisizione dati sincronizzata (canoni per 14 mesi: mesi 20-24 e 27-35)",
         "Da definire", "OR14", 1, 16800, 1.0, 14, 14, 1.0, "Sì"),
}
att = []
for a in C["attrezzature"]:
    k = (a[2], a[0])
    if k in VIA:
        continue
    att.append(SOST.get(k, a))
assert len(att) == len(C["attrezzature"]) - 2
C["attrezzature"] = att
C["consulenze"] += [
    ("Fornitore di servizi cloud da individuare",
     "Servizi cloud GPU per addestramento e sperimentazione dei modelli (content policy engine, personalizzazione, "
     "apprendimento a bordo)", "OR1", 36000, "Capacità di calcolo GPU a consumo, in luogo di un server dedicato",
     "Altri servizi e licenze", "", ""),
    ("Fornitore di servizi cloud da individuare",
     "Servizi cloud GPU per l'esecuzione degli scenari del digital twin (simulazione e verifica virtuale su larga scala)",
     "OR6", 36000, "Capacità di calcolo GPU a consumo per le campagne di scenari, in luogo di un server dedicato",
     "Altri servizi e licenze", "", ""),
]
n = 0
for i, a in enumerate(C["attivita"]):
    if a[1] == "A14.3":
        a = list(a); a[2] = ("Ciclo di vita dei modelli AI a bordo: validazione dei rilasci, monitoraggio e criteri di "
                             "aggiornamento, con distribuzione tramite la piattaforma OTA di OR8")
        C["attivita"][i] = tuple(a); n += 1
assert n == 1
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 5 (20/11/2026):", "Versione 6 (21/11/2026): attrezzature e servizi di Aubay (aggiorna_v6_aubay.py).\nVersione 5 (20/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok")
