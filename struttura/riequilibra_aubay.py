# Riequilibrio del team di Aubay (20/11): date e team delle attività da struttura/riequilibrio_aubay.json,
# ore per OR e per fascia invariate.
# Uso: python3 struttura/riequilibra_aubay.py struttura/economics_moovxr_v4_20nov.py struttura/riequilibrio_aubay.json struttura/economics_moovxr.py
# (poi va riapplicata la riformulazione del criterio di D1.2)
import importlib.util, json, pprint, sys
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
S = json.load(open(sys.argv[2])); IMP = 0.95
import math
RX = lambda v: math.floor(v + 0.5)                 # ROUND di Excel (metà per eccesso)
ORE = lambda n, d: RX(n * (d * IMP) * 1720 / 12)
# ore per OR e fascia da conservare
H = {}
for a in C["attivita"]:
    if a[0] in ("OR1", "OR6", "OR14"):
        h = H.setdefault(a[0], [0, 0, 0])
        for f in range(3):
            h[f] += RX(a[6 + f] * ((a[4] - a[3] + 1) * a[9]) * 1720 / 12)
T, X = S["T"], [list(x) for x in S["x"]]
for i, t in enumerate(T):                       # quote trascurabili spostate sull'attività maggiore dello stesso OR
    for f in range(3):
        if 0 < X[i][f] < 0.05:
            j = max((k for k in range(len(T)) if T[k][0] == t[0] and k != i), key=lambda k: X[k][f])
            X[j][f] = round(X[j][f] + X[i][f] * (t[3] - t[2] + 1) / (T[j][3] - T[j][2] + 1), 4); X[i][f] = 0
for o in H:                                     # quadratura esatta delle ore per OR e fascia
    idx = [i for i, t in enumerate(T) if t[0] == o]
    for f in range(3):
        for _ in range(30):
            d = H[o][f] - sum(ORE(X[i][f], T[i][3] - T[i][2] + 1) for i in idx)
            if d == 0: break
            j = max(idx, key=lambda i: X[i][f]); n = T[j][3] - T[j][2] + 1
            X[j][f] = round(X[j][f] + d / (n * 1720 / 12 * IMP), 4)
        assert d == 0, (o, f, d)
nuovo = {t[1]: (t, x) for t, x in zip(T, X)}
att = []
for a in C["attivita"]:
    if a[1] not in nuovo:
        att.append(a); continue
    t, x = nuovo[a[1]]
    att.append((a[0], a[1], a[2], t[2], t[3], a[5], x[0], x[1], x[2], IMP, a[10],
                a[11] or "Responsabile tecnico: indirizzo, revisione e validazione" if x[0] else None,
                a[12] or "Senior: progettazione e sviluppo" if x[1] else None,
                a[13] or "Sviluppatore o tecnico: implementazione e prove" if x[2] else None))
# pesi delle attività sul costo del personale dell'OR
for o in H:
    idx = [k for k, a in enumerate(att) if a[0] == o]
    cst = [sum(ORE(att[k][6 + f], att[k][4] - att[k][3] + 1) * r for f, r in enumerate((83, 47, 30))) for k in idx]
    p = [round(c / sum(cst), 2) for c in cst]; p[cst.index(max(cst))] = round(p[cst.index(max(cst))] + 1 - sum(p), 2)
    for k, v in zip(idx, p):
        a = list(att[k]); a[5] = v; att[k] = tuple(a)
C["attivita"] = att
fine = {a[10]: a[4] for a in att if a[0] in H}
C["deliverable"] = [tuple(d[:3]) + (fine.get(d[1], d[3]),) + tuple(d[4:]) for d in C["deliverable"]]
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
open(sys.argv[3], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
for k in nuovo: print(k, [round(v, 3) for v in X[[t[1] for t in T].index(k)]])
