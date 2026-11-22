# Versione 7 (21/11): A1.7 (percorsi a minor consumo) accorpata in A1.6 come uso di servizi di routing
# esistenti; A1.8 rinumerata A1.7; KPI K6 eliminato; team di Aubay ricalcolati (riequilibrio_aubay_v7.json)
# a ore per OR e fascia invariate; motivazioni dei servizi di Aubay precisate.
# Uso: python3 struttura/aggiorna_v7_aubay.py struttura/economics_moovxr_v6_21nov.py struttura/riequilibrio_aubay_v7.json struttura/economics_moovxr.py
import importlib.util, json, math, pprint, sys
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
S = json.load(open(sys.argv[2])); IMP = 0.95
RX = lambda v: math.floor(v + 0.5)
ORE = lambda n, d: RX(n * (d * IMP) * 1720 / 12)
AUB = ("OR1", "OR6", "OR14")
H = {}
for a in C["attivita"]:                                   # ore per OR e fascia della v6, A1.7 compresa
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
RIN = {"A1.8": "A1.7"}
TIT = {"A1.6": "Raccomandazione personalizzata per occupante di contenuti, POI e soste di ricarica, con pianificazione "
               "delle soste tramite servizi di routing esistenti"}
att = []
for a in C["attivita"]:
    if a[1] == "A1.7":
        continue
    if a[1] not in nuovo:
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
fine = {a[10]: a[4] for a in att if a[0] in AUB}
dl = []
for d in C["deliverable"]:
    if d[1] == "D1.7":
        continue
    d = list(d)
    if d[1] == "D1.8":
        d[1] = "D1.7"
    d[3] = fine.get(d[1], d[3])
    dl.append(tuple(d))
C["deliverable"] = dl
C["kpi"] = [k for k in C["kpi"] if k[0] != "K6"]
MOT = {
    "Licenze di dati cartografici, POI e disponibilità delle colonnine":
        ("Licenze di dati cartografici e POI e servizi di routing con disponibilità delle colonnine",
         "Dati e servizi di terzi usati dalla raccomandazione personalizzata (A1.6)"),
    "Licenza di software di simulazione di guida e di scena":
        (None, "Modelli fisici dei sensori, scenari conformi a OpenSCENARIO e supporto del produttore, non disponibili "
               "negli strumenti open source"),
    "Accesso a pista o area di prova chiusa":
        (None, "Prove del dimostratore in sicurezza prima della circolazione su strada aperta (A14.6)"),
}
cons = []
for c in C["consulenze"]:
    if c[1] in MOT and c[2] in AUB:
        nome, mot = MOT[c[1]]
        c = (c[0], nome or c[1], c[2], c[3], mot) + tuple(c[5:])
    cons.append(c)
C["consulenze"] = cons
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 6 (21/11/2026):", "Versione 7 (21/11/2026): A1.7 accorpata in A1.6, team di Aubay ricalcolati (aggiorna_v7_aubay.py).\nVersione 6 (21/11/2026):")
open(sys.argv[3], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
for t in sorted(nuovo, key=lambda k: (int(k.split('.')[0][1:]), int(k.split('.')[1]))):
    tt, x = nuovo[t]; print("%-5s %2d-%2d  A%.2f M%.2f B%.2f" % (RIN.get(t, t), tt[2], tt[3], *x))
