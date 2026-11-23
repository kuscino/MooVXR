# Versione 23 (23/11): addetti del Politecnico per attività dal roster v13 del 22/11 (foglio "Piano personale",
# righe 71-89: 18 posizioni, ore per task), impegno distinto per fascia ricavato dalle ore già nel modello, così
# ore e costi restano invariati; profilo mensile per fascia dai carichi del roster (righe 94-111), senza nomi.
# Uso: python3 struttura/aggiorna_v23_polimi_roster.py struttura/economics_moovxr_v22_23nov.py \
#        struttura/economics_moovxr.py <Excel del Politecnico> <modello v22 ricalcolato>
import importlib.util, pprint, sys, openpyxl
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
P = openpyxl.load_workbook(sys.argv[3], data_only=True)
M = openpyxl.load_workbook(sys.argv[4], data_only=True)
PROP = "Politecnico di Milano"
ore_mod = {r[1]: (r[20], r[21], r[22], r[14], r[19]) for r in M["Attività"].iter_rows(min_row=2, values_only=True)
           if r[11] == PROP}
ws = P["Piano personale"]
assert ws.cell(71, 6).value == "A9.1" and ws.cell(93, 1).value == "Risorsa"
task = [ws.cell(71, c).value for c in range(6, 21)]
roster = [r for r in ws.iter_rows(min_row=72, max_row=89, values_only=True) if r[0]]
assert len(roster) == 18
F = ("Alto", "Medio", "Basso")
n = {t: tuple(sum(1 for r in roster if r[2] == f and (r[5 + j] or 0) > 0.01) for f in F) for j, t in enumerate(task)}
team = {r[1]: tuple(r[6:9]) for r in P["Team"].iter_rows(min_row=2, values_only=True) if r[1] and str(r[1]).startswith("A")}
assert all(n[t] == team[t] for t in task), "roster e foglio Team non coincidono"
cambiate = 0
for i, a in enumerate(C["attivita"]):
    if a[1] not in ore_mod:
        continue
    oA, oM, oB, dur, oa = ore_mod[a[1]]
    nn = n[a[1]]
    imp = tuple((o / (k * dur * oa / 12) if k else 0.0) for o, k in zip((oA, oM, oB), nn))
    for o, k, im in zip((oA, oM, oB), nn, imp):
        assert round(k * dur * im * oa / 12) == o
    x = list(a); x[6], x[7], x[8] = nn; x[9] = tuple(round(v, 10) for v in imp)
    C["attivita"][i] = tuple(x); cambiate += 1
assert cambiate == 15
prof = {f: [0.0] * 30 for f in F}
for r in ws.iter_rows(min_row=94, max_row=111, values_only=True):
    if r[0]:
        for m, v in enumerate(r[2:32]):
            prof[r[1]][m] += v or 0
C["profilo_mensile"] = {PROP: {f: [round(v, 2) for v in prof[f]] for f in F}}
print("ore roster", round(sum(map(sum, prof.values()))), "ore modello", sum(sum(v[:3]) for v in ore_mod.values()))
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 22 (23/11/2026):", "Versione 23 (23/11/2026): addetti del Politecnico dal roster, impegno per fascia, "
                      "profilo mensile (aggiorna_v23_polimi_roster.py).\nVersione 22 (23/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok")
