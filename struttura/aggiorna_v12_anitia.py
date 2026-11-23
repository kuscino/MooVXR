# Versione 12 (23/11): pianificazione rivista di Anitia (mail del 23/11). A7.2 mesi 4-13, A8.2 mesi 19-30, A8.3
# mesi 13-30, con i deliverable D7.2 al mese 13, D8.2 e D8.3 al mese 30. In attesa dell'Excel di Anitia con i
# team per task, le ore di ciascuna attività spostata restano quelle della rev1 (team riscalato sulla nuova
# durata). Addette donne di Anitia in Tab. 2: 1 in fascia Media, 3 in fascia Bassa.
# Uso: python3 struttura/aggiorna_v12_anitia.py struttura/economics_moovxr_v11_22nov.py struttura/economics_moovxr.py
import importlib.util, pprint, sys
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
NUOVE = {"A7.2": (4, 13), "A8.2": (19, 30), "A8.3": (13, 30)}
att, n = [], 0
for a in C["attivita"]:
    if a[1] in NUOVE:
        s, f = NUOVE[a[1]]
        k = (a[4] - a[3] + 1) / (f - s + 1)           # stesse ore: persone x durata invariato
        a = (a[0], a[1], a[2], s, f, a[5], round(a[6] * k, 4), round(a[7] * k, 4), round(a[8] * k, 4)) + tuple(a[9:])
        n += 1
    att.append(a)
assert n == 3
C["attivita"] = att
fine = {"D7.2": 13, "D8.2": 30, "D8.3": 30}
C["deliverable"] = [d[:3] + (fine.get(d[1], d[3]),) + tuple(d[4:]) for d in C["deliverable"]]
C.setdefault("donne", {})["Anitia"] = {"Medio": 1, "Basso": 3}
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 11 (22/11/2026):", "Versione 12 (23/11/2026): pianificazione rivista di Anitia (aggiorna_v12_anitia.py).\nVersione 11 (22/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok")
