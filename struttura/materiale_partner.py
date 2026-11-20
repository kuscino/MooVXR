# -*- coding: utf-8 -*-
"""materiale_partner.py - genera, per ciascun partner, il documento di revisione (docx) con OR,
descrizioni e abstract dei task approvati per il Piano di Sviluppo, costi per task e dati richiesti,
e l'estratto del modello economico (xlsx con formule) con team, attrezzature, servizi e costi.

Fonti: struttura/economics_moovxr.py (struttura e ipotesi di costo) e struttura/contenuti_moovxr.py
(testi approvati). Nessun testo e' scritto a mano nei file generati.

Uso (da Area di Lavoro):
    python3 struttura/materiale_partner.py
Uscita: partner/MooVXR_<partner>_revisione.docx e partner/MooVXR_<partner>_costi.xlsx
"""
import importlib.util, pathlib, sys
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter as L

QUI = pathlib.Path(__file__).resolve().parent
ROOT = QUI.parent
sys.path.insert(0, str(ROOT / "toolchain" / "toolchain"))
import docx_core as D


def carica(nome, file):
    spec = importlib.util.spec_from_file_location(nome, QUI / file)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


CFG = carica("economics_moovxr", "economics_moovxr.py").CONFIG
CONT = carica("contenuti_moovxr", "contenuti_moovxr.py").CONTENUTI
OUT = ROOT / "partner"
OUT.mkdir(exist_ok=True)

SCADENZA = "venerdì 20 novembre 2026 alle 12:00"
FORFAIT = CFG["regole"]["Forfait spese generali e materiali"][0]
TARIFFE = {}
for tipo, fascia, _liv, eur, ore in CFG["tariffe"]:
    TARIFFE.setdefault(tipo, {})[fascia] = (eur, ore)
PROP = {p[0]: p for p in CFG["proponenti"]}
SIGLA = {"Aubay Italia": "Aubay", "Politecnico di Milano": "Politecnico", "GSNet": "GSNet",
         "Anitia": "Anitia", "nLight": "nLight"}


def costo_attr(a):
    q, p, amm, uso, imp, vu = a[3], a[4], a[6], a[7], a[8], a[9]
    return q * p * imp if vu == "Sì" else q * p * imp * min(1, uso / amm)


def costi_task(oid, tipo_tariffa):
    """Costi per task con la stessa regola del modello: ore intere per fascia, quote di OR ripartite
    in proporzione al personale, forfait sul totale."""
    att = [a for a in CFG["attivita"] if a[0] == oid]
    pers = {}
    for a in att:
        mesi = a[4] - a[3] + 1
        tot = 0
        for n, fascia in ((a[6], "Alto"), (a[7], "Medio"), (a[8], "Basso")):
            eur, ore = TARIFFE[tipo_tariffa][fascia]
            tot += round(n * mesi / 12 * ore * a[9]) * eur
        pers[a[1]] = tot
    p_or = sum(pers.values()) or 1
    q_or = (sum(costo_attr(x) for x in CFG["attrezzature"] if x[2] == oid)
            + sum(c[3] for c in CFG["consulenze"] if c[2] == oid and not c[6]))
    righe = []
    for a in att:
        serv = sum(c[3] for c in CFG["consulenze"] if c[2] == oid and c[6] == a[1])
        quota = q_or * pers[a[1]] / p_or
        dir_ = pers[a[1]] + serv + quota
        righe.append((a, pers[a[1]], serv, quota, dir_ * FORFAIT, dir_ * (1 + FORFAIT)))
    return righe


def keur(v):
    return "{:,.0f}".format(v / 1000).replace(",", ".")


def meur(v):
    return "{:,.2f}".format(v / 1e6).replace(",", "X").replace(".", ",").replace("X", ".")


# ---------------------------------------------------------------- documento di revisione
def documento(nome):
    ors = [o for o in CFG["or"] if o[2] == nome]
    tipo_t = PROP[nome][1]
    c = []
    c.append(D.heading(1, "MooVXR, proposta di obiettivi realizzativi e task: %s" % SIGLA[nome]))
    c.append(D.testo("Bozza per la revisione del partner, 19 novembre 2026. Accordi per l'innovazione nella "
                     "filiera automotive, DD 17 settembre 2026."))

    c.append(D.heading(2, "1. Istruzioni per la revisione"))
    for t in [
        "Ampliare gli abstract dei task: problema tecnico, soluzione proposta, elementi di novità e di "
        "incertezza secondo il Manuale di Frascati, metodo, risultati misurabili.",
        "Verificare nel file Excel allegato il team di ciascun task (numero di persone per fascia Alta, "
        "Media e Bassa, quota di impegno) e i costi conseguenti. Sono ammesse correzioni anche importanti, "
        "purché ogni costo sia giustificato e coerente con le finalità del progetto.",
        "Consulenze: solo di dominio, non tecniche. Restano ammesse come forniture le prestazioni esecutive di "
        "terzi, le licenze e le prove affidate a soggetti esterni (per esempio penetration test o laboratori "
        "accreditati). Non è ammessa la fatturazione fra partner del raggruppamento (Allegato 10, lett. c).",
        "Materiali e componenti rientrano nel forfait del 20% per spese generali e materiali e non si "
        "espongono a parte (DD, art. 10, c. 2).",
        "Attrezzature: è ammissibile la sola quota di ammortamento per il periodo di utilizzo nel progetto, "
        "oppure i canoni di noleggio (DD, art. 10, c. 1, lett. b; Allegato 10).",
        "Quota minima dei costi del progetto a carico di ciascun proponente: 10% per le grandi imprese, 5% per "
        "gli altri soggetti (DM 31/12/2021, art. 4, c. 2, lett. f).",
        "Restituire il documento con le revisioni tracciate e il file Excel aggiornato entro %s." % SCADENZA,
    ]:
        c.append(D.punto(t))

    c.append(D.heading(2, "2. Il progetto"))
    c.append(D.testo("MooVXR sviluppa una piattaforma per l'abitacolo del veicolo connesso che decide quali "
                     "contenuti mostrare a ciascun occupante, in quale forma e su quale superficie, in funzione "
                     "della situazione di guida, della scena rilevata e dell'attenzione del guidatore. Il "
                     "progetto dura 36 mesi ed è articolato in %d obiettivi realizzativi:" % len(CFG["or"])))
    righe = [(o[0], SIGLA[o[2]], o[3], o[1]) for o in CFG["or"]]
    c.append(D.tabella(["OR", "Proponente", "Tipo", "Titolo"], righe, [900, 1700, 800, 6935]))

    c.append(D.heading(2, "3. Obiettivi realizzativi di %s" % SIGLA[nome]))
    tot_p = 0
    for o in ors:
        rt = costi_task(o[0], tipo_t)
        tot_or = sum(r[5] for r in rt)
        tot_p += tot_or
        c.append(D.heading(3, "%s, %s" % (o[0], o[1])))
        c.append(D.testo("Tipo: %s. Mesi %d-%d. Budget indicativo: %s M€, forfait incluso."
                         % ("ricerca industriale" if o[3] == "RI" else "sviluppo sperimentale", o[4], o[5],
                            meur(tot_or))))
        c.append(D.sottotitolo("Descrizione dell'obiettivo realizzativo"))
        if "II.7.1/%s" % o[0] in CONT:
            c.append(CONT["II.7.1/%s" % o[0]]())
        else:
            c.append(D.testo("[Descrizione dell'obiettivo realizzativo da redigere in forma Frascati per la nuova "
                             "struttura.]"))
        c.append(D.sottotitolo("Task e abstract"))
        testo_72 = CONT["II.7.2/%s" % o[0]]() if "II.7.2/%s" % o[0] in CONT else ""
        c.append(testo_72)
        mancanti = [a for a in CFG["attivita"] if a[0] == o[0] and a[1] + " " not in testo_72]
        if mancanti:
            if testo_72:
                c.append(D.sottotitolo("Task aggiunti con la nuova struttura, da redigere"))
            for a in mancanti:
                c.append(D.sottotitolo("%s %s (mesi %d-%d)" % (a[1], a[2], a[3], a[4])))
                c.append(D.testo("[Abstract da redigere in forma Frascati: Problema, Soluzione proposta, Novità e "
                                 "incertezza, Metodo, Risultati misurabili con valori obiettivo.]"))
        if testo_72 and (mancanti or "Risorse umane" not in testo_72):
            c.append(D.testo("[Il paragrafo Risorse umane sarà aggiornato sul team ricalcolato, riportato nella "
                             "sezione Ipotesi da confermare.]"))
        c.append(D.sottotitolo("Ipotesi di costo per task (k€)"))
        righe = [(r[0][1], r[0][2], keur(r[1]), keur(r[2] + r[3]), keur(r[4]), keur(r[5])) for r in rt]
        righe.append(("", "Totale %s" % o[0], keur(sum(r[1] for r in rt)), keur(sum(r[2] + r[3] for r in rt)),
                      keur(sum(r[4] for r in rt)), keur(tot_or)))
        c.append(D.tabella(["Task", "Titolo", "Personale", "Attrezzature e servizi", "Forfait 20%", "Totale"],
                           righe, [800, 4535, 1200, 1500, 1100, 1200]))
    c.append(D.testo("Totale indicativo di %s: %s M€." % (SIGLA[nome], meur(tot_p))))

    c.append(D.heading(2, "4. Ipotesi da confermare"))
    c.append(D.sottotitolo("Team per task"))
    righe = []
    for a in CFG["attivita"]:
        if any(a[0] == o[0] for o in ors):
            righe.append((a[1], a[3], a[4], a[6], a[7], a[8], "%d%%" % round(a[9] * 100)))
    c.append(D.tabella(["Task", "Da mese", "A mese", "Alto", "Medio", "Basso", "Impegno"], righe,
                       [1335, 1500, 1500, 1500, 1500, 1500, 1500]))
    att = [a for a in CFG["attrezzature"] if any(a[2] == o[0] for o in ors)]
    if att:
        c.append(D.sottotitolo("Attrezzature"))
        righe = [(a[0], a[2], a[3], "{:,.0f}".format(a[4]).replace(",", "."),
                  a[6], a[7], keur(costo_attr(a))) for a in att]
        c.append(D.tabella(["Voce", "OR", "Q.tà", "Prezzo unitario (€)", "Ammortamento (mesi)", "Utilizzo (mesi)",
                            "Costo ammissibile (k€)"], righe, [3335, 700, 700, 1500, 1400, 1300, 1400]))
    srv = [s for s in CFG["consulenze"] if any(s[2] == o[0] for o in ors)]
    if srv:
        c.append(D.sottotitolo("Consulenze e servizi"))
        righe = [(s[1], s[2], s[6] or "intero OR", s[5], keur(s[3])) for s in srv]
        c.append(D.tabella(["Oggetto", "OR", "Task", "Categoria", "Importo (k€)"], righe,
                           [5035, 700, 900, 2400, 1300]))

    c.append(D.heading(2, "5. Dati richiesti"))
    dati = [
        "Ragione sociale, dimensione d'impresa e sede operativa con regione in cui si svolgono le attività.",
        "Valore della produzione degli ultimi due esercizi e bilanci approvati, per il modello economico e per "
        "gli indicatori di solidità finanziaria dell'Allegato 8.",
        "Organico, personale dedicato alla ricerca e sviluppo, progetti di ricerca e sviluppo degli ultimi tre "
        "anni e relative spese.",
        "Ore annue contrattuali per categoria di personale (CCNL applicato), che sostituiscono le 1.720 ore "
        "assunte nel modello (Allegato 10, lett. a).",
        "Nominativo e CV del referente tecnico del partner.",
        "Valori obiettivo degli indicatori di ciascun OR.",
        "Eventuale certificazione della parità di genere e rating di legalità (maggiorazioni dell'Allegato 8).",
    ]
    if PROP[nome][2] == "Organismo di ricerca":
        dati[0] = "Struttura di afferenza, sede in cui si svolgono le attività e requisiti di Organismo di ricerca."
        dati[1] = "Dati richiesti per la dichiarazione dei requisiti degli Organismi di ricerca (Allegato 6b)."
    for t in dati:
        c.append(D.punto(t))

    out = OUT / ("MooVXR_%s_revisione.docx" % SIGLA[nome])
    D.scrivi(D.accenti("".join(c)), out)
    return out, tot_p


# ---------------------------------------------------------------- estratto del modello economico
GIALLO = PatternFill("solid", fgColor="FFF2CC")
TESTA = PatternFill("solid", fgColor="1F3864")
EUR = '#,##0" €"'


def testa(ws, intest, larg):
    ws.append(intest)
    for j, cl in enumerate(ws[1], 1):
        cl.font = Font(bold=True, color="FFFFFF")
        cl.fill = TESTA
        cl.alignment = Alignment(wrap_text=True, vertical="center")
        ws.column_dimensions[L(j)].width = larg[j - 1]
    ws.freeze_panes = "A2"


def excel(nome):
    ors = [o for o in CFG["or"] if o[2] == nome]
    ids = [o[0] for o in ors]
    tipo_t = PROP[nome][1]
    wb = openpyxl.Workbook()

    ws = wb.active
    ws.title = "Parametri"
    testa(ws, ["Parametro", "Valore", "Nota"], [40, 14, 70])
    par = [("€/h Alto", TARIFFE[tipo_t]["Alto"][0], "Costi standard, Allegato 10, Tab. 1"),
           ("€/h Medio", TARIFFE[tipo_t]["Medio"][0], "Costi standard, Allegato 10, Tab. 1"),
           ("€/h Basso", TARIFFE[tipo_t]["Basso"][0], "Costi standard, Allegato 10, Tab. 1"),
           ("Ore annue", TARIFFE[tipo_t]["Alto"][1],
            "Allegato 10, lett. a): 1500 per il personale universitario; per le imprese ore del CCNL applicato "
            "(1720 in attesa del dato del partner)"),
           ("Forfait spese generali e materiali", FORFAIT, "DD art. 10, c. 2")]
    for r in par:
        ws.append(list(r))
        ws.cell(ws.max_row, 2).fill = GIALLO
    P = {"A": "Parametri!$B$2", "M": "Parametri!$B$3", "B": "Parametri!$B$4", "H": "Parametri!$B$5",
         "F": "Parametri!$B$6"}

    ws = wb.create_sheet("Team")
    testa(ws, ["OR", "Task", "Titolo", "Da mese", "A mese", "Mesi", "n. Alto", "n. Medio", "n. Basso", "Impegno",
               "Ore Alto", "Ore Medio", "Ore Basso", "Costo personale"],
          [7, 7, 60, 8, 8, 7, 8, 8, 8, 9, 10, 10, 10, 16])
    for a in CFG["attivita"]:
        if a[0] not in ids:
            continue
        ws.append([a[0], a[1], a[2], a[3], a[4]])
        r = ws.max_row
        ws.cell(r, 6, "=E%d-D%d+1" % (r, r))
        for j, v in zip((7, 8, 9, 10), (a[6], a[7], a[8], a[9])):
            ws.cell(r, j, v).fill = GIALLO
        ws.cell(r, 10).number_format = "0%"
        for j, col in ((11, "G"), (12, "H"), (13, "I")):
            ws.cell(r, j, "=ROUND(%s%d*F%d/12*%s*J%d,0)" % (col, r, r, P["H"], r))
        ws.cell(r, 14, "=K%d*%s+L%d*%s+M%d*%s" % (r, P["A"], r, P["M"], r, P["B"])).number_format = EUR
    nt = ws.max_row

    ws = wb.create_sheet("Attrezzature")
    testa(ws, ["Voce", "Modello", "OR", "Q.tà", "Prezzo unitario", "Ammortamento (mesi)", "Utilizzo (mesi)",
               "% imputazione", "Vita utile ≤ durata", "Costo ammissibile"], [50, 14, 7, 7, 14, 12, 12, 11, 11, 16])
    for a in CFG["attrezzature"]:
        if a[2] not in ids:
            continue
        ws.append([a[0], a[1], a[2], a[3], a[4], a[6], a[7], a[8], a[9]])
        r = ws.max_row
        for j in range(4, 10):
            ws.cell(r, j).fill = GIALLO
        ws.cell(r, 5).number_format = EUR
        ws.cell(r, 8).number_format = "0%"
        ws.cell(r, 10, '=IF(I%d="Sì",D%d*E%d*H%d,D%d*E%d*H%d*MIN(1,G%d/F%d))'
                % (r, r, r, r, r, r, r, r, r)).number_format = EUR
    na = max(ws.max_row, 2)

    ws = wb.create_sheet("Servizi")
    testa(ws, ["Soggetto", "Oggetto", "OR", "Task (vuoto = intero OR)", "Categoria", "Importo", "Motivazione"],
          [24, 60, 7, 12, 22, 14, 50])
    for s in CFG["consulenze"]:
        if s[2] not in ids:
            continue
        ws.append([s[0], s[1], s[2], s[6] or None, s[5], s[3], s[4]])
        r = ws.max_row
        ws.cell(r, 6).fill = GIALLO
        ws.cell(r, 6).number_format = EUR
    ns = max(ws.max_row, 2)

    ws = wb.create_sheet("Costi per task", 0)
    testa(ws, ["OR", "Task", "Titolo", "Personale", "Servizi del task", "Quota di attrezzature e servizi dell'OR",
               "Forfait", "Totale"], [7, 7, 60, 16, 16, 18, 14, 16])
    for k, a in enumerate([a for a in CFG["attivita"] if a[0] in ids], 2):
        ws.append([a[0], a[1], a[2]])
        r = ws.max_row
        ws.cell(r, 4, "=Team!N%d" % k)
        ws.cell(r, 5, "=SUMIFS(Servizi!$F$2:$F$%d,Servizi!$C$2:$C$%d,A%d,Servizi!$D$2:$D$%d,B%d)"
                % (ns, ns, r, ns, r))
        ws.cell(r, 6, '=IFERROR((SUMIF(Attrezzature!$C$2:$C$%d,A%d,Attrezzature!$J$2:$J$%d)'
                      '+SUMIFS(Servizi!$F$2:$F$%d,Servizi!$C$2:$C$%d,A%d,Servizi!$D$2:$D$%d,""))'
                      '*D%d/SUMIF(Team!$A$2:$A$%d,A%d,Team!$N$2:$N$%d),0)'
                % (na, r, na, ns, ns, r, ns, r, nt, r, nt))
        ws.cell(r, 7, "=(D%d+E%d+F%d)*%s" % (r, r, r, P["F"]))
        ws.cell(r, 8, "=D%d+E%d+F%d+G%d" % (r, r, r, r))
        for j in range(4, 9):
            ws.cell(r, j).number_format = EUR
    n = ws.max_row
    ws.append([])
    ws.append(["", "", "TOTALE"] + ["=SUM(%s2:%s%d)" % (L(j), L(j), n) for j in range(4, 9)])
    for j in range(3, 9):
        ws.cell(ws.max_row, j).font = Font(bold=True)
        ws.cell(ws.max_row, j).number_format = EUR
    r0 = ws.max_row + 2
    ws.cell(r0, 1, "Totale per OR").font = Font(bold=True)
    for i, o in enumerate(ids, 1):
        ws.cell(r0 + i, 1, o)
        ws.cell(r0 + i, 3, [x[1] for x in ors if x[0] == o][0])
        ws.cell(r0 + i, 8, "=SUMIF($A$2:$A$%d,A%d,$H$2:$H$%d)" % (n, r0 + i, n)).number_format = EUR
    ws.cell(r0 + len(ids) + 2, 1, "Celle gialle: ipotesi da confermare o correggere. Le altre celle sono formule.").font = Font(italic=True)

    out = OUT / ("MooVXR_%s_costi.xlsx" % SIGLA[nome])
    wb.save(out)
    return out


if __name__ == "__main__":
    # uso: materiale_partner.py [--solo-excel] [sigla ...]   (sigle: Aubay, GSNet, Anitia, Politecnico, nLight)
    argv = sys.argv[1:]
    solo_excel = "--solo-excel" in argv
    scelti = [a for a in argv if not a.startswith("--")]
    for p in CFG["proponenti"]:
        if scelti and SIGLA[p[0]] not in scelti:
            continue
        x = excel(p[0])
        if solo_excel:
            tot = sum(sum(r[5] for r in costi_task(o[0], p[1])) for o in CFG["or"] if o[2] == p[0])
            print("%-22s %8s M€  %s" % (p[0], meur(tot), x.name))
        else:
            d, tot = documento(p[0])
            print("%-22s %8s M€  %s  %s" % (p[0], meur(tot), d.name, x.name))
