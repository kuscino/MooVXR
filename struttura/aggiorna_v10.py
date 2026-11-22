# Versione 10 (21/11): validazione del digital twin in due tempi (percorsi registrati da nLight in A12.5, poi
# registrazioni del dimostratore), noleggio del sistema di acquisizione ai mesi 26-35; KPI con sedi di misura
# aggiornate, K3 ristretto ai prototipi, nuovi K6 e K7, valori obiettivo di K2 e K7.
# Uso: python3 struttura/aggiorna_v10.py struttura/economics_moovxr_v9_21nov.py struttura/economics_moovxr.py
import importlib.util, pprint, sys
spec = importlib.util.spec_from_file_location("eco", sys.argv[1]); eco = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eco); C = eco.CONFIG
n = 0
for i, a in enumerate(C["attrezzature"]):
    if a[2] == "OR14" and a[0].startswith("Noleggio del sistema di acquisizione"):
        C["attrezzature"][i] = ("Noleggio del sistema di acquisizione dati sincronizzata (canoni per 10 mesi: mesi 26-35)",
                                "Da definire", "OR14", 1, 12000, 1.0, 10, 10, 1.0, "Sì"); n += 1
assert n == 1
C["or"] = [tuple(x.replace("Modelli e dati da OR1, OR9, OR10, OR12; dati registrati da OR14",
                           "Modelli e dati da OR1, OR9, OR10, OR12; percorsi registrati con i sensori di sviluppo da "
                           "OR12 (A12.5); dati del dimostratore registrati da OR14")
                 if isinstance(x, str) else x for x in o) for o in C["or"]]
assert any("A12.5" in str(o[6]) for o in C["or"] if o[0] == "OR6")
dl = []
for d in C["deliverable"]:
    if d[1] == "D6.4":
        d = d[:4] + ("Scarto fra simulazione e misura entro il valore obiettivo, prima sui percorsi registrati da nLight "
                     "(A12.5), poi sulle registrazioni del dimostratore",)
    dl.append(d)
C["deliverable"] = dl
K = {k[0]: list(k) for k in C["kpi"]}
K["K1"][5] = "Ambienti simulati (OR10) e prove su strada (OR14)"
K["K2"][5] = "Percorsi di prova (OR3, OR14)"
K["K2"][7] = 95
K["K2"][8] = "Bozza di A3.2 (20/11/2026): almeno il 95% dei contenuti disponibili nel momento utile"
K["K3"][1] = "Errore di allineamento dei contenuti AR"
K["K3"][2] = "Errore angolare fra contenuto e oggetto reale su HUD del passeggero (OR11) e occhiali AR (OR5)"
K["K3"][5] = "Banco ottico (OR11) e veicolo di prova (OR14)"
K["K3"][8] = "Da definire con il Politecnico e con GSNet"
K["K4"][5] = "Veicolo di prova (OR14)"
kpi = [tuple(K[c]) for c in ("K1", "K2", "K3", "K4", "K5")]
kpi.append(("K6", "Scarto fra digital twin e prove reali",
            "Differenza fra indicatori simulati e misurati sugli stessi percorsi (percezione, consegna dei contenuti, "
            "attenzione degli occupanti)", "%", "Finale", "Digital twin (OR6) e prove su strada (OR14)",
            "Indicatori misurati su strada", None, "Da definire"))
kpi.append(("K7", "Tempo di decisione del content policy engine",
            "95° percentile del tempo di valutazione delle regole per singola decisione", "ms", "Intermedio",
            "Scenari simulati e registrati (OR1, OR6)", "Specifica di progetto", 20,
            "Testo di OR1 nel Piano di Sviluppo: inferiore a 20 ms nel 95% dei casi"))
C["kpi"] = kpi
testa = open(sys.argv[1], encoding="utf8").read().split("CONFIG = ")[0]
testa = testa.replace("Versione 9 (21/11/2026):", "Versione 10 (21/11/2026): digital twin in due tempi, KPI (aggiorna_v10.py).\nVersione 9 (21/11/2026):")
open(sys.argv[2], "w", encoding="utf8").write(testa + "CONFIG = " + pprint.pformat(C, width=120, sort_dicts=False) + "\n")
print("ok")
