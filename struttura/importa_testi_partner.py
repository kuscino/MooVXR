# -*- coding: utf-8 -*-
"""importa_testi_partner.py - legge un documento di revisione di un partner (docx, revisioni tracciate accettate
con pandoc) e ne estrae, per ogni OR, la descrizione (7.1) e le attività (7.2) come liste (tipo, testo) nel formato
di contenuti_moovxr.py: t paragrafo, p punto, s sottotitolo, e paragrafo con etichetta (Problema., Soluzione
proposta., Novità e incertezza., Metodo., Risultati misurabili.). Esclude risorse umane e tabelle di costo.
Uso: python3 importa_testi_partner.py <docx> <uscita.py> <nome variabile>
"""
import re, subprocess, sys, pprint
ETI = ("Problema.", "Soluzione proposta.", "Novità e incertezza.", "Metodo.", "Risultati misurabili.")
txt = subprocess.run(["pandoc", "--track-changes=accept", "-t", "plain", "--wrap=none", sys.argv[1]],
                     capture_output=True, text=True, check=True).stdout
righe = [r.rstrip() for r in txt.splitlines()]
OR, cur, sez = {}, None, None
for r in righe:
    s = r.strip()
    if not s or re.fullmatch(r"[-+ ]+", s):
        continue
    m = re.match(r"^(OR\d+), ", s)
    if m:
        cur = m.group(1); OR[cur] = {"7.1": [], "7.2": []}; sez = "testa"; continue
    if cur is None:
        continue
    if s.startswith("Descrizione dell'obiettivo realizzativo"):
        sez = "7.1"; continue
    if s.startswith("Task e abstract"):
        sez = "7.2"; continue
    if s.startswith(("Risorse umane", "Ipotesi di costo", "Tabella ", "Totale indicativo", "4. Ipotesi")) or \
            re.match(r"^Task\s+Titolo", s) or re.match(r"^A\d+\.\d+\s{2,}", s) or s.startswith("Totale OR"):
        sez = "salta" if not s.startswith("Totale indicativo") else None
        if s.startswith("Totale indicativo") or s.startswith("4. Ipotesi"):
            cur = None
        continue
    if sez not in ("7.1", "7.2"):
        continue
    if re.match(r"^A\d+\.\d+ ", s) and sez == "7.2":
        OR[cur]["7.2"].append(("s", s)); continue
    if r.startswith("-   "):
        OR[cur][sez].append(("p", s[1:].strip())); continue
    m = re.match(r"^(\d+)\. (.*)", s)
    if m and r.startswith("  "):
        OR[cur][sez].append(("t", "%s. %s" % (m.group(1), m.group(2)))); continue
    for e in ETI:
        if s.startswith(e):
            OR[cur][sez].append(("e", (e, s[len(e):].strip()))); break
    else:
        OR[cur][sez].append(("t", s))
open(sys.argv[2], "w", encoding="utf8").write(
    "# -*- coding: utf-8 -*-\n# Generato da importa_testi_partner.py da %s. Non modificare a mano.\n%s = %s\n"
    % (sys.argv[1].split("/")[-1], sys.argv[3], pprint.pformat(OR, width=120)))
for o, d in OR.items():
    print(o, "7.1:", len(d["7.1"]), "blocchi | 7.2:", len(d["7.2"]), "blocchi |", [v for k, v in d["7.2"] if k == "s"])
