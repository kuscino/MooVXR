# -*- coding: utf-8 -*-
"""matrice_moovxr.py - matrice di tracciabilita del Piano di Sviluppo MooVXR (Allegato n. 4,
Accordi per l'innovazione nella filiera automotive, DD 17/09/2026).

Una riga per nodo da redigere del template (profilo mimit_accordi_automotive), con fonte
puntuale nel bando, natura, chi redige e prescrizione di redazione. Il capitolo 0 raccoglie i
requisiti di ammissibilita': non entra nel documento ma va dimostrato.

Uso (da Area di Lavoro):
    python3 struttura/matrice_moovxr.py
Scrive Matrice_Tracciabilita.xlsx in Area di Lavoro e l'export struttura/matrice.csv.
"""
import csv, pathlib, sys
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "toolchain" / "toolchain"))
from profili import mimit_accordi_automotive as P

OE, VD, IN = "Obbligo esplicito", "Vincolo da dimostrare", "Iniziativa"
AU, TUTTI = "Aubay", "Aubay con i partner"

# requisiti di ammissibilita' (capitolo 0)
AMMISSIBILITA = [
    ("0.1", "Area di intervento unica (Area 2 dell'Allegato A)", "DD art. 3, c. 3, lett. c); All. A", OE, AU,
     "Collocare tutte le attivita' nell'Area 2; nessuna attivita' riconducibile ad altre aree."),
    ("0.2", "Costi ammissibili fra 5 e 40 M€", "DD art. 3, c. 3, lett. e); art. 7, c. 6", OE, AU,
     "Totale da modello economico; margine sopra i 5 M€ anche con tagli del 20%."),
    ("0.3", "Durata fra 18 e 36 mesi, avvio dopo la domanda", "DD art. 3, c. 3, lett. d); All. 4 Parte II par. 1", OE, AU,
     "36 mesi; avvio entro 3 mesi dal decreto di concessione."),
    ("0.4", "Massimo cinque co-proponenti, contratto di collaborazione con capofila", "DM 31/12/2021 art. 3, c. 2-3, richiamato da DD art. 3, c. 3, lett. a)", OE, AU,
     "Cinque proponenti; accordo di partenariato con Aubay capofila."),
    ("0.5", "Quota minima dei costi per proponente", "DM 31/12/2021 art. 4, c. 2, lett. f), richiamato da DD art. 3, c. 3, lett. b)", OE, AU,
     "Grandi imprese almeno 10%, altri soggetti almeno 5%: verifica nel modello economico."),
    ("0.6", "OR di un solo proponente e di un solo tipo (RI o SS), massimo 15", "All. 4 Parte II par. 7", OE, AU,
     "13 OR, ciascuno di un proponente e di un tipo."),
    ("0.7", "Rispetto del principio DNSH e degli ambiti di esclusione", "DD art. 3, c. 3, lett. f) e g); All. 4bis", OE, TUTTI,
     "Schede DNSH per proponente; nessuna attivita' negli ambiti esclusi."),
    ("0.8", "Soglie minime di punteggio per criterio e totale", "All. 8; DD art. 8", VD, AU,
     "a almeno 18, b almeno 25, c almeno 12; costruire i testi sui criteri."),
]

# nodi del template: (fonte nel bando, natura, chi redige, prescrizione)
PROGETTO = {
    "I.1": ("All. 8 criterio a.1", OE, TUTTI,
            "Una scheda per proponente: struttura organizzativa, management, struttura produttiva e di R&S, "
            "unita' locali del progetto. Dati forniti dai partner."),
    "I.2": ("All. 8 criterio c.1", OE, TUTTI,
            "Solo per le imprese: attivita', mercato con dati quantitativi, posizione e previsioni triennali, "
            "fatturato nel settore della ricerca, concorrenti, accordi, licenze e brevetti."),
    "II.1": ("DD art. 3, c. 3, lett. d)", OE, AU,
             "Titolo del progetto e durata di 36 mesi."),
    "II.2": ("DD art. 3, c. 3, lett. c); All. A, Area 2", OE, AU,
             "Area di intervento 2; linee generali dell'Allegato A citate alla lettera; motivare la linea "
             "generale prevalente."),
    "II.3": ("All. 4 Parte II par. 3", OE, AU,
             "Sintesi in una pagina: problema, soluzione, partenariato, risultato finale."),
    "II.4": ("DD art. 3, c. 2 (finalita' degli Accordi); All. 8 criterio c.1", OE, AU,
             "Finalita' rispetto allo scenario del settore automotive e alle direttrici di mercato."),
    "II.5": ("All. 8 criteri b.2 e b.3", OE, AU,
             "Obiettivo finale: caratteristiche e prestazioni del sistema, problematiche tecnico-scientifiche, "
             "soluzioni tecnologiche. Nessun rinvio numerato ad altri paragrafi."),
    "II.5BIS": ("DD art. 3, c. 3, lett. f) e g); All. 4bis", OE, TUTTI,
                "Elementi per la verifica DNSH sui sei obiettivi ambientali e sugli ambiti di esclusione, "
                "coerenti con le schede dell'Allegato 4bis."),
    "II.6": ("All. 4 Parte II par. 6", OE, AU,
             "Riferimenti del responsabile del progetto; CV europeo allegato con soli dati pertinenti."),
    "II.7": ("All. 4 Parte II par. 7; DD art. 1, definizioni di ricerca industriale (lett. o) e sviluppo "
             "sperimentale; All. 8 criterio b.1", OE, TUTTI,
             "Tabella degli OR e, per ogni OR, moduli 7.1-7.3. Ogni attivita' qualificata secondo i criteri "
             "del Manuale di Frascati (novita', creativita', incertezza, sistematicita', trasferibilita'); "
             "per ciascuna problemi, soluzioni, risorse umane e risultati; coerenza con Tabella 3 e modello "
             "economico."),
    "II.8": ("DM 31/12/2021 art. 13, c. 1; All. 4 Parte II par. 8", OE, AU,
             "Risultato intermedio al mese 18, verificabile, con parametri di valutazione e valori attesi."),
    "II.9": ("All. 4 Parte II par. 9", OE, AU,
             "Risultato finale: dimostratore validato su strada, parametri di valutazione e valori attesi."),
    "II.10": ("All. 4 Parte II par. 10", OE, AU,
              "Cronoprogramma degli OR e delle attivita' generato dal modello economico."),
    "II.11": ("All. 4 Parte II par. 11; All. 10 lett. b), c), e)", OE, TUTTI,
              "Per proponente: attrezzature (pertinenza, ammortamento, congruita'), consulenze e prestazioni "
              "(solo di dominio o forniture esterne), materiali nel forfait; costi per regione."),
    "III.1.1": ("All. 8 criterio a.1 (0-12)", OE, TUTTI,
                "Per proponente: competenze interne, personale qualificato, strutture di R&S, progetti e spese "
                "di R&S degli ultimi tre anni, capacita' di coordinare terzi."),
    "III.1.2": ("All. 8 criterio a.2 (0-3); DD art. 8, c. 1, lett. a), n. 2", OE, AU,
                "Competenze del Politecnico di Milano sulle tecnologie del progetto, attinenza alla ricerca "
                "industriale, necessita' delle attivita'; quota del Politecnico sui costi, sopra il 10%."),
    "III.2.1": ("All. 8 criterio b.1 (0-7)", OE, TUTTI,
                "Per proponente: risorse strumentali possedute e da acquistare, procedure di gestione della R&S, "
                "responsabile tecnico, congruita' di costi e tempi."),
    "III.2.2": ("All. 8 criterio b.2 (0-15)", OE, TUTTI,
                "Per proponente: risultati attesi, rilevanza e originalita' rispetto allo stato dell'arte "
                "internazionale (nazionale per le PMI), non incrementali; riferimenti verificabili."),
    "III.2.3": ("All. 8 criterio b.3 (0-12, nuovo prodotto)", OE, AU,
                "A livello di progetto: qualificare l'innovazione come nuovo prodotto e motivarlo."),
    "III.3.1": ("All. 8 criterio c.1 (0-12)", OE, TUTTI,
                "Per impresa: mercato nazionale ed estero, sistema competitivo, impatto economico (ricavi, "
                "export, margini), investimenti di industrializzazione, ricadute occupazionali."),
    "III.3.2": ("All. 8 criterio c.2 (0-12)", OE, TUTTI,
                "Per impresa: sviluppo del settore e ricadute in altri ambiti (trasporto turistico, veicoli "
                "per la sicurezza, ricognizione del territorio)."),
    "III.4": ("All. 4 Parte III par. 4; DD art. 7, c. 5", OE, TUTTI,
              "Per impresa: piano finanziario annuale con fabbisogno al netto del personale interno e del "
              "forfait, e fonti di copertura."),
    "TAB1": ("All. 4 Tab. 1; DD art. 10", OE, AU, "Dal modello economico, per proponente."),
    "TAB2": ("All. 4 Tab. 2; All. 10 lett. a)", OE, AU, "Dal modello economico, per proponente."),
    "TAB3": ("All. 4 Tab. 3; All. 10 lett. a)", OE, AU, "Dal modello economico, per proponente e OR."),
    "TAB4": ("All. 4 Tab. 4; All. 10 lett. b); DD art. 10, c. 1, lett. b)", OE, AU,
             "Dal modello economico, per proponente."),
}

COLONNE = ["Cap.", "Par.", "Titolo", "Fonte", "Natura", "Redazione", "Prescrizione di redazione"]
LARGHEZZE = [6, 10, 48, 40, 20, 18, 90]


def main():
    righe = [(0,) + r for r in AMMISSIBILITA] + P.righe_matrice(PROGETTO)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Matrice"
    ws.append(COLONNE)
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="1F3864")
    for r in righe:
        ws.append(list(r))
    for j, w in enumerate(LARGHEZZE, 1):
        ws.column_dimensions[openpyxl.utils.get_column_letter(j)].width = w
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "A2"
    wb.save(ROOT / "Matrice_Tracciabilita.xlsx")
    with open(ROOT / "struttura" / "matrice.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(COLONNE)
        w.writerows(righe)
    print("matrice scritta:", len(righe), "righe, di cui", len(AMMISSIBILITA), "requisiti di ammissibilita'")


if __name__ == "__main__":
    main()
