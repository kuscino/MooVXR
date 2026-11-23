# Versione 17 (23/11): donne del Politecnico (1 Alta, 1 Bassa); valore obiettivo di K6 (≤ 10%, testo di A6.4 nel Piano
# di Sviluppo); titolo di A14.3 con "drift" al posto di "deriva". Nessun effetto sui costi.
# Uso: python3 struttura/aggiorna_v17.py struttura/economics_moovxr_v16_23nov.py struttura/economics_moovxr.py
import importlib.util, pprint, sys
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
C["donne"]["Politecnico di Milano"] = {"Alto": 1, "Basso": 1}
k = [i for i, x in enumerate(C["kpi"]) if x[0] == "K6"]; assert len(k) == 1
x = list(C["kpi"][k[0]]); x[7] = 10; x[8] = "Piano di Sviluppo, A6.4 (23/11/2026): scarto non superiore al 10%"
C["kpi"][k[0]] = tuple(x)
n = 0
att = []
for a in C["attivita"]:
    if a[1] == "A14.3":
        assert "monitoraggio della deriva" in a[2]
        a = (a[0], a[1], a[2].replace("monitoraggio della deriva", "monitoraggio del drift")) + tuple(a[3:]); n += 1
    att.append(a)
assert n == 1
C["attivita"] = att
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 16 (23/11/2026):", "Versione 17 (23/11/2026): donne del Politecnico, K6, titolo di A14.3 (aggiorna_v17.py).\nVersione 16 (23/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok")
