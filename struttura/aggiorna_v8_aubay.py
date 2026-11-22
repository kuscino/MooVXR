# Versione 8 (21/11): titoli di A1.5, A1.7, A6.5, A14.3 e A10.5 (Politecnico, da condividere); A14.4 (prove di
# carico) accorpata nell'integrazione del dimostratore; A14.5 e A14.6 rinumerate A14.4 e A14.5; team di Aubay
# ricalcolati (riequilibrio_aubay_v8.json) a ore per OR e fascia invariate.
# Uso: python3 struttura/aggiorna_v8_aubay.py struttura/economics_moovxr_v7_21nov.py struttura/riequilibrio_aubay_v8.json struttura/economics_moovxr.py
import importlib.util, json, math, pprint, sys
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
S = json.load(open(sys.argv[2])); IMP = 0.95
RX = lambda v: math.floor(v + 0.5)
ORE = lambda n, d: RX(n * (d * IMP) * 1720 / 12)
AUB = ("OR1", "OR6", "OR14")
H = {}
for a in C["attivita"]:
    if a[0] in AUB:
        h = H.setdefault(a[0], [0, 0, 0])
        for f in range(3):
            h[f] += RX(a[6 + f] * ((a[4] - a[3] + 1) * a[9]) * 1720 / 12)
T, X = S["T"], [list(x) for x in S["x"]]
for i, t in enumerate(T):
    for f in range(3):
        if 0 < X[i][f] < 0.05:
            j = max((k for k in range(len(T)) if T[k][0] == t[0] and k != i), key=lambda k: X[k][f])
            X[j][f] = round(X[j][f] + X[i][f] * (t[3] - t[2] + 1) / (T[j][3] - T[j][2] + 1), 4); X[i][f] = 0
for o in H:
    idx = [i for i, t in enumerate(T) if t[0] == o]
    for f in range(3):
        for _ in range(30):
            d = H[o][f] - sum(ORE(X[i][f], T[i][3] - T[i][2] + 1) for i in idx)
            if d == 0: break
            j = max(idx, key=lambda i: X[i][f]); n = T[j][3] - T[j][2] + 1
            X[j][f] = round(X[j][f] + d / (n * 1720 / 12 * IMP), 4)
        assert d == 0, (o, f, d)
nuovo = {t[1]: (t, x) for t, x in zip(T, X)}
RIN = {"A14.5": "A14.4", "A14.6": "A14.5"}
TIT = {
    "A1.5": "Verifica formale delle regole del content policy engine",
    "A1.7": "Apprendimento a bordo dei profili degli occupanti senza trasferimento di dati personali, con gestione del "
            "consenso tramite strumenti esistenti",
    "A6.5": "Campagna di verifica virtuale di policy, percezione e HMI sugli scenari del digital twin, prima delle "
            "prove su strada",
    "A14.3": "Gestione dei modelli AI in esercizio a bordo: criteri di rilascio e di ritorno alla versione precedente, "
             "monitoraggio della deriva e coerenza con le policy, con distribuzione tramite la piattaforma OTA di OR8",
    "A14.5": "Integrazione del dimostratore su veicolo, prove di carico e di continuità, protocollo di prova",
    "A10.5": "Verifica sperimentale con partecipanti delle regole adattive di OR1 sulla postazione di guida simulata, "
             "con gli scenari del digital twin (OR6)",
}
att = []
for a in C["attivita"]:
    if a[1] == "A14.4":
        continue
    if a[1] not in nuovo:
        if a[1] in TIT:
            a = (a[0], a[1], TIT[a[1]]) + tuple(a[3:])
        att.append(a); continue
    t, x = nuovo[a[1]]
    cod = RIN.get(a[1], a[1])
    att.append((a[0], cod, TIT.get(a[1], a[2]), t[2], t[3], a[5], x[0], x[1], x[2], IMP, "D" + cod[1:],
                (a[11] or "Responsabile tecnico: indirizzo, revisione e validazione") if x[0] else None,
                (a[12] or "Senior: progettazione e sviluppo") if x[1] else None,
                (a[13] or "Sviluppatore o tecnico: implementazione e prove") if x[2] else None))
for o in H:
    idx = [k for k, a in enumerate(att) if a[0] == o]
    cst = [sum(ORE(att[k][6 + f], att[k][4] - att[k][3] + 1) * r for f, r in enumerate((83, 47, 30))) for k in idx]
    p = [round(c / sum(cst), 2) for c in cst]; p[cst.index(max(cst))] = round(p[cst.index(max(cst))] + 1 - sum(p), 2)
    for k, v in zip(idx, p):
        a = list(att[k]); a[5] = v; att[k] = tuple(a)
C["attivita"] = att
DEL = {
    "D1.5": ("Rapporto di verifica formale delle regole",
             "Nessun caso raggiungibile in cui il guidatore riceva un contenuto vietato; tempo di decisione entro il "
             "valore obiettivo"),
    "D1.7": ("Profili costruiti a bordo",
             "Nessun dato personale grezzo trasferito fuori dal veicolo; consenso registrato per ogni occupante"),
    "D14.3": (None, "Rilasci dei modelli dei partner validati e monitorati sul veicolo di prova; ritorno alla versione "
                    "precedente verificato"),
    "D14.5": ("Dimostratore integrato e rapporto delle prove di carico",
              "Software e hardware di tutti gli OR in esecuzione sul veicolo di prova; latenza e continuità entro i "
              "valori obiettivo"),
}
RD = {"D14.5": "D14.4", "D14.6": "D14.5"}
fine = {a[10]: a[4] for a in att if a[0] in AUB}
dl = []
for d in C["deliverable"]:
    if d[1] == "D14.4":
        continue
    d = list(d)
    if d[1] in DEL:
        nome, crit = DEL[d[1]]
        d[2] = nome or d[2]; d[4] = crit
    d[1] = RD.get(d[1], d[1])
    d[3] = fine.get(d[1], d[3])
    dl.append(tuple(d))
C["deliverable"] = dl
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 7 (21/11/2026):", "Versione 8 (21/11/2026): verifiche distinte, A14.4 accorpata, titoli (aggiorna_v8_aubay.py).\nVersione 7 (21/11/2026):")
open(sys.argv[3], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok")
