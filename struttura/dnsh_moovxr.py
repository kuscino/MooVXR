# -*- coding: utf-8 -*-
"""Allegato n. 4bis, Schede DNSH, del progetto MooVXR (Accordi per l'innovazione nella filiera automotive).

Dati confermati da Francesco il 23/11: risposte e motivazioni delle due schede, piano di monitoraggio,
legislazione applicabile. Gli stessi dati alimentano il paragrafo 5.BIS del Piano di Sviluppo.
Le domande riproducono il testo dell'Allegato 4bis (Documenti RICEVUTI).

Uso (da Area di Lavoro): python3 struttura/dnsh_moovxr.py [uscita.docx]
"""
import sys

TITOLO = "MooVXR"
CAPOFILA = "GS NET - ITALIA S.r.l."

# (domanda, risposta "Si"/"No", motivazione)
CONTRIBUTI = [
    ("Contributo sostanziale alla mitigazione dei cambiamenti climatici", "Descrizione delle motivazioni se è stata apposta una X nella casella «Si»", [
        ("Contribuisce alla produzione, la trasmissione, lo stoccaggio, la distribuzione o l’uso di energie rinnovabili conformemente alla direttiva (UE) 2018/2001, anche tramite tecnologie innovative potenzialmente in grado di ottenere risparmi significativi in futuro oppure tramite il necessario rafforzamento o ampliamento della rete?", "No", ""),
        ("Contribuisce al miglioramento dell’efficienza energetica, fatta eccezione per le attività di produzione di energia elettrica?", "No", ""),
        ("Contribuisce all’aumento della mobilità pulita o climaticamente neutra?", "Si",
         "Il sistema di bordo pianifica le soste di ricarica e raccomanda le colonnine disponibili lungo il percorso, "
         "facilitando l’uso dei veicoli elettrici (attività A1.6). La validazione virtuale del sistema nel digital twin "
         "(OR6) riduce i chilometri percorsi nelle prove su strada."),
        ("Contribuisce al passaggio all’uso di materiali rinnovabili di origine sostenibile?", "No", ""),
        ("Contribuisce all’aumento del ricorso alle tecnologie, non nocive per l’ambiente, di cattura e utilizzo del carbonio (carbon capture and utilisation — CCU) e di cattura e stoccaggio del carbonio (carbon capture and storage — CCS), che consentono una riduzione netta delle emissioni di gas a effetto serra?", "No", ""),
        ("Contribuisce al potenziamento dei pozzi di assorbimento del carbonio nel suolo, anche attraverso attività finalizzate a evitare la deforestazione e il degrado forestale, il ripristino delle foreste, la gestione sostenibile e il ripristino delle terre coltivate, delle praterie e delle zone umide, l’imboschimento e l’agricoltura rigenerative?", "No", ""),
        ("Contribuisce alla creazione dell’infrastruttura energetica necessaria per la decarbonizzazione dei sistemi energetici?", "No", ""),
        ("Contribuisce alla produzione di combustibili puliti ed efficienti da fonti rinnovabili o neutre in carbonio?", "No", ""),
        ("Presenta livelli di emissioni di gas a effetto serra che corrispondono alla migliore prestazione del settore o dell’industria?", "No", ""),
        ("Non ostacola lo sviluppo e la diffusione di alternative a basse emissioni di carbonio?", "Si",
         "Il software e i componenti sviluppati sono indipendenti dalla motorizzazione del veicolo e sono utilizzabili "
         "su veicoli elettrici e ibridi."),
        ("Non comporta una dipendenza da attività ad elevata intensità di carbonio, tenuto conto della vita economica di tali attività?", "Si",
         "Il progetto consiste in attività di ricerca e sviluppo di software e di prototipi di laboratorio, senza "
         "impianti produttivi né investimenti in attività ad elevata intensità di carbonio."),
    ]),
    ("Contributo sostanziale all’adattamento ai cambiamenti climatici", "In caso affermativo descrivere", [
        ("Comprende soluzioni di adattamento che riducono in modo sostanziale il rischio di effetti negativi del clima attuale e del clima previsto per il futuro sull’attività economica o riducono in modo sostanziale tali effetti negativi, senza accrescere il rischio di effetti negativi sulle persone, sulla natura e sulle attività?", "No", ""),
        ("Fornisce soluzioni di adattamento che contribuiscono in modo sostanziale a prevenire o ridurre il rischio di effetti negativi del clima attuale e del clima previsto per il futuro sulle persone, sulla natura o sugli attivi, senza accrescere il rischio di effetti negativi sulle altre persone, sulla natura o sugli attivi?", "No", ""),
        ("Le soluzioni di adattamento di cui al paragrafo 1, lettera a), sono valutate e classificate in ordine di priorità utilizzando le migliori proiezioni climatiche disponibili e prevengono e riducono, come minimo: a) gli effetti negativi, sull’attività economica, dei cambiamenti climatici legati a un luogo e contesto determinato; oppure b) i potenziali effetti negativi dei cambiamenti climatici sull’ambiente in cui si svolge l’attività economica?", "No", ""),
    ]),
    ("Contributo sostanziale all’uso sostenibile e alla protezione delle acque e delle risorse marine", "In caso affermativo descrivere", [
        ("Considera la protezione dell’ambiente dagli effetti negativi degli scarichi di acque reflue urbane e industriali, compresi i contaminanti che destano nuove preoccupazioni, quali i prodotti farmaceutici e le microplastiche, per esempio assicurando la raccolta, il trattamento e lo scarico adeguati delle acque reflue urbane e industriali?", "No", ""),
        ("Considera la protezione della salute umana dagli effetti negativi di eventuali contaminazioni delle acque destinate al consumo umano, provvedendo a che siano esenti da microorganismi, parassiti e sostanze potenzialmente pericolose per la salute umana e aumentando l’accesso delle persone ad acqua potabile pulita?", "No", ""),
        ("Considera il miglioramento della gestione e dell’efficienza idrica, anche proteggendo e migliorando lo stato degli ecosistemi acquatici, promuovendo l’uso sostenibile dell’acqua attraverso la protezione a lungo termine delle risorse idriche disponibili, anche mediante misure quali il riutilizzo dell’acqua, assicurando la progressiva riduzione delle emissioni inquinanti nelle acque sotterranee e di superficie, contribuendo a mitigare gli effetti di inondazioni e siccità, o mediante qualsiasi altra attività che protegga o migliori lo stato qualitativo e quantitativo dei corpi idrici?", "No", ""),
        ("Considera la garanzia di un uso sostenibile dei servizi ecosistemici marini o il contributo al buono stato ecologico delle acque marine, anche proteggendo, preservando o ripristinando l’ambiente marino e prevenendo o riducendo gli apporti nell’ambiente marino?", "No", ""),
    ]),
    ("Contributo sostanziale alla transizione verso un’economia circolare", "In caso affermativo descrivere", [
        ("Promuove l’utilizzo più efficiente delle risorse naturali, compresi i materiali a base biologica di origine sostenibile e altre materie prime, nella produzione, anche attraverso: la riduzione dell’uso di materie prime primarie o aumentando l’uso di sottoprodotti e materie prime secondarie; o misure di efficienza energetica e delle risorse?", "Si",
         "Il progetto ricorre al noleggio in luogo dell’acquisto per il veicolo di prova e per il sistema di acquisizione "
         "dei dati, e a servizi cloud a consumo in luogo di server dedicati, riducendo le apparecchiature acquistate e "
         "non più utilizzate a fine progetto."),
        ("Aumenta la durabilità, la riparabilità, la possibilità di miglioramento o della riutilizzabilità dei prodotti, in particolare nelle attività di progettazione e di fabbricazione?", "Si",
         "Il software di bordo e i modelli AI sono aggiornati tramite la piattaforma OTA (OR8) con criteri di rilascio e "
         "di ritorno alla versione precedente (A14.3): le funzioni evolvono nel tempo senza sostituire l’hardware del "
         "veicolo."),
        ("Aumenta la riciclabilità dei prodotti, compresa la riciclabilità dei singoli materiali ivi contenuti, anche sostituendo o riducendo l’impiego di prodotti e materiali non riciclabili, in particolare nelle attività di progettazione e di fabbricazione?", "No", ""),
        ("Riduce in misura sostanziale il contenuto di sostanze pericolose e sostituisce le sostanze estremamente preoccupanti in materiali e prodotti in tutto il ciclo di vita, in linea con gli obiettivi indicati nel diritto dell’Unione, anche rimpiazzando tali sostanze con alternative più sicure e assicurando la tracciabilità dei prodotti?", "No", ""),
        ("Prolunga l’uso dei prodotti, anche attraverso il riutilizzo, la progettazione per la longevità, il cambio di destinazione, lo smontaggio, la rifabbricazione, la possibilità di miglioramento e la riparazione, e la condivisione dei prodotti?", "Si",
         "L’aggiornamento OTA del software e dei modelli AI prolunga la vita utile del sistema di bordo; il kit di "
         "percezione (OR13) è progettato in forma modulare, con sensori sostituibili singolarmente."),
        ("Aumenta l’uso di materie prime secondarie e il miglioramento della loro qualità, anche attraverso un riciclaggio di alta qualità dei rifiuti?", "No", ""),
        ("Previene o riduce la produzione di rifiuti, anche la produzione di rifiuti derivante dall’estrazione di minerali e dalla costruzione e demolizione di edifici?", "Si",
         "La validazione virtuale del sistema nel digital twin (OR6) sostituisce parte delle prove fisiche e riduce il "
         "numero di prototipi e di iterazioni di prova necessari."),
        ("Aumenta la preparazione per il riutilizzo e il riciclaggio dei rifiuti?", "No", ""),
        ("Potenzia lo sviluppo delle infrastrutture di gestione dei rifiuti necessarie per la prevenzione, la preparazione per il riutilizzo e il riciclaggio, garantendo al contempo che i materiali di recupero siano riciclati nella produzione come apporto di materie prime secondarie di elevata qualità, evitando così il downcycling?", "No", ""),
        ("Riduce al minimo l’incenerimento dei rifiuti ed evita lo smaltimento dei rifiuti, compresa la messa in discarica, conformemente ai principi della gerarchia dei rifiuti?", "No", ""),
        ("Evita e riduce la dispersione di rifiuti?", "No", ""),
    ]),
    ("Contributo sostanziale alla prevenzione e alla riduzione dell’inquinamento", "In caso affermativo descrivere", [
        ("Prevenzione o, qualora ciò non sia possibile, promuove la riduzione delle emissioni inquinanti nell’aria, nell’acqua o nel suolo, diverse dai gas a effetto serra?", "No", ""),
        ("Promuove il miglioramento del livello di qualità dell’aria, dell’acqua o del suolo nelle zone in cui l’attività economica si svolge, riducendo contemporaneamente al minimo gli effetti negativi per la salute umana e l’ambiente o il relativo rischio?", "No", ""),
        ("Promuove la prevenzione o la riduzione al minimo di qualsiasi effetto negativo sulla salute umana e sull’ambiente legati alla produzione e all’uso o allo smaltimento di sostanze chimiche?", "No", ""),
        ("Abbatte la produzione dei rifiuti e di altre dispersioni inquinanti?", "No", ""),
    ]),
    ("Contributo sostanziale alla protezione e al ripristino della biodiversità e degli ecosistemi", "In caso affermativo descrivere", [
        ("Sostiene la conservazione della natura e della biodiversità, anche conseguendo uno stato di conservazione soddisfacente degli habitat e delle specie naturali e seminaturali, o prevenendone il deterioramento quando presentano già uno stato di conservazione soddisfacente, e proteggendo e ripristinando gli ecosistemi terrestri, marini e gli altri ecosistemi acquatici al fine di migliorarne la condizione nonché la capacità di fornire servizi ecosistemici?", "No", ""),
        ("Promuove l’uso e la gestione sostenibile del territorio, anche attraverso l’adeguata protezione della biodiversità del suolo, la neutralità in termini di degrado del suolo e la bonifica dei siti contaminati?", "No", ""),
        ("Sostiene le pratiche agricole sostenibili, comprese quelle che contribuiscono a migliorare la biodiversità oppure ad arrestare o prevenire il degrado del suolo e degli altri ecosistemi, la deforestazione e la perdita di habitat?", "No", ""),
        ("Promuove la gestione sostenibile delle foreste, compresi le pratiche e gli utilizzi delle foreste e delle superfici boschive che contribuiscono a migliorare la biodiversità o ad arrestare o prevenire il degrado degli ecosistemi, la deforestazione e la perdita di habitat?", "No", ""),
    ]),
]

# (obiettivo, risposta "Si"/"No"/"Non pertinente", motivazione)
IMPATTI = [
    ("Mitigazione dei cambiamenti climatici", "No",
     "I consumi energetici del progetto sono limitati alle postazioni di lavoro, alle apparecchiature di laboratorio e ai "
     "servizi cloud. I proponenti si impegnano ad acquistare apparecchiature elettriche ed elettroniche dotate di etichetta "
     "ambientale di tipo I (UNI EN ISO 14024) o di etichetta Energy Star o equivalente, e a selezionare fornitori di "
     "servizi cloud con data center ad alta efficienza energetica. Le prove su strada sono contenute grazie alla "
     "validazione virtuale nel digital twin e si svolgono con un veicolo a noleggio."),
    ("Adattamento ai cambiamenti climatici", "Non pertinente",
     "Le attività si svolgono in sedi e laboratori esistenti dei proponenti e non prevedono infrastrutture o beni fisici "
     "durevoli esposti a rischi climatici."),
    ("Uso sostenibile e protezione delle acque e delle risorse marine", "Non pertinente",
     "Il progetto non prevede prelievi né scarichi idrici di natura industriale; l’uso dell’acqua è limitato agli usi "
     "civili delle sedi."),
    ("Economia circolare, compresi la prevenzione e il riciclaggio dei rifiuti", "No",
     "Le apparecchiature elettriche ed elettroniche sono acquistate da produttori iscritti al registro RAEE e gestite a "
     "fine vita come RAEE ai sensi del D.Lgs. 14 marzo 2014, n. 49. Il progetto privilegia il noleggio e i servizi a "
     "consumo; i componenti dei prototipi sono riutilizzati nelle attività successive o conferiti come RAEE."),
    ("Prevenzione e riduzione dell’inquinamento dell’aria, dell’acqua o del suolo", "No",
     "Il progetto non genera emissioni in aria, acqua o suolo diverse da quelle degli usi civili. Le apparecchiature "
     "acquistate sono conformi alla direttiva 2011/65/UE (RoHS), recepita con il D.Lgs. 4 marzo 2014, n. 27, e al "
     "regolamento (CE) n. 1907/2006 (REACH). Le prove ambientali dei prototipi si svolgono presso laboratori esterni."),
    ("Protezione e ripristino della biodiversità e degli ecosistemi", "Non pertinente",
     "Le attività si svolgono in sedi esistenti in aree urbanizzate, senza consumo di suolo; le prove su strada usano la "
     "viabilità esistente."),
]

# (obiettivo, indicatore, frequenza, responsabile)
MONITORAGGIO = [
    ("Mitigazione dei cambiamenti climatici",
     "Consumo energetico dichiarato delle apparecchiature acquistate e dei servizi cloud; chilometri percorsi nelle prove su strada",
     "A ogni stato di avanzamento", "Ciascun proponente per le proprie spese; consolidamento a cura del capofila"),
    ("Economia circolare",
     "Quota di apparecchiature con etichetta ambientale di tipo I, Energy Star o equivalente; apparecchiature dismesse avviate a recupero come RAEE",
     "A ogni stato di avanzamento e a fine progetto", "Ciascun proponente per le proprie spese; consolidamento a cura del capofila"),
    ("Prevenzione e riduzione dell’inquinamento",
     "Dichiarazioni di conformità RoHS e REACH acquisite per il 100% delle apparecchiature",
     "All’acquisto, verifica a ogni stato di avanzamento", "Ciascun proponente per le proprie spese; consolidamento a cura del capofila"),
]

LEGISLAZIONE = [
    "Regolamento (UE) 2020/852, articolo 17 (principio di non arrecare un danno significativo);",
    "D.Lgs. 3 aprile 2006, n. 152, Norme in materia ambientale, con particolare riferimento alla parte IV sulla gestione dei rifiuti;",
    "D.Lgs. 14 marzo 2014, n. 49, attuazione della direttiva 2012/19/UE sui rifiuti di apparecchiature elettriche ed elettroniche (RAEE);",
    "D.Lgs. 4 marzo 2014, n. 27, attuazione della direttiva 2011/65/UE sulla restrizione dell’uso di determinate sostanze pericolose (RoHS);",
    "Regolamento (CE) n. 1907/2006 (REACH);",
    "Direttiva 2009/125/CE sulla progettazione ecocompatibile, recepita con il D.Lgs. 16 febbraio 2011, n. 15;",
    "Regolamento (UE) 2019/424 sulla progettazione ecocompatibile di server e prodotti di archiviazione dati.",
]

PROVE = [
    "Non sono presenti elementi di prova alla data della domanda, poiché le apparecchiature e i servizi non sono ancora "
    "stati acquistati. In fase di acquisto e di rendicontazione saranno acquisiti e conservati:",
    "dichiarazioni dei produttori sull’etichetta ambientale o energetica e sulla conformità RoHS e REACH;",
    "attestazione dell’iscrizione dei produttori al registro RAEE;",
    "contratti di noleggio e di servizio cloud, con le caratteristiche energetiche dichiarate dai fornitori.",
]


# ---------------------------------------------------------------- generazione del documento
def genera(uscita):
    from docx import Document
    from docx.enum.section import WD_ORIENT
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt

    d = Document()
    st = d.styles["Normal"]; st.font.name = "Arial"; st.font.size = Pt(9)
    sec = d.sections[0]
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width, sec.page_height = Cm(29.7), Cm(21.0)
    for m in ("left_margin", "right_margin"):
        setattr(sec, m, Cm(1.8))
    sec.top_margin = sec.bottom_margin = Cm(1.5)
    h = sec.header.paragraphs[0]
    h.text = "Allegato N. 4 BIS\nAccordi per l’innovazione nella filiera automotive"
    h.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    for r in h.runs:
        r.font.size = Pt(8)

    def par(t, bold=False, size=9, align=None, after=4, italic=False):
        p = d.add_paragraph(); r = p.add_run(t); r.bold = bold; r.italic = italic; r.font.size = Pt(size)
        p.paragraph_format.space_after = Pt(after)
        if align:
            p.alignment = align
        return p

    def ombra(cella, colore="D9D9D9"):
        sh = OxmlElement("w:shd"); sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), colore)
        cella._tc.get_or_add_tcPr().append(sh)

    def scrivi(cella, t, bold=False, center=False):
        cella.text = ""
        p = cella.paragraphs[0]; r = p.add_run(t); r.bold = bold; r.font.size = Pt(8.5)
        if center:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    def tabella(larghezze, intest, righe, titolo=None):
        t = d.add_table(rows=0, cols=len(larghezze)); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        if titolo:
            c = t.add_row().cells; m = c[0].merge(c[-1]); scrivi(m, titolo, bold=True, center=True); ombra(m, "BFBFBF")
        c = t.add_row().cells
        for i, x in enumerate(intest):
            scrivi(c[i], x, bold=True, center=True); ombra(c[i])
        for riga in righe:
            c = t.add_row().cells
            for i, (x, centro) in enumerate(riga):
                scrivi(c[i], x, bold=centro and x == "X", center=centro)
        lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); t._tbl.tblPr.append(lay)
        for i, w in enumerate(larghezze):
            t.columns[i].width = Cm(w)
        for row in t.rows:
            for i, w in enumerate(larghezze):
                row.cells[i].width = Cm(w)
        d.add_paragraph().paragraph_format.space_after = Pt(2)

    def firma():
        par("")
        par("Firma digitale del legale rappresentante dell’impresa unica proponente o, nel caso di progetto congiunto, "
            "dal legale rappresentante dell’impresa capofila", italic=True, size=8, align=WD_ALIGN_PARAGRAPH.CENTER)
        par("%s, legale rappresentante" % CAPOFILA, size=8, align=WD_ALIGN_PARAGRAPH.CENTER)

    # Scheda di autovalutazione dei contributi
    par("Scheda autovalutazione dei contributi relative ai sei obiettivi ambientali in cui si applica il principio DNSH",
        bold=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, after=6)
    par("Progetto %s. Soggetto capofila: %s." % (TITOLO, CAPOFILA), size=9, align=WD_ALIGN_PARAGRAPH.CENTER, after=8)
    par("Ai fini della valutazione del principio DNSH, il soggetto firmatario dichiara:")
    par("-    che il contributo positivo del progetto in relazione ai sei obiettivi ambientali è nel seguito esposto:", after=6)
    W = [10.0, 1.1, 1.1, 13.9]
    for titolo, col, voci in CONTRIBUTI:
        righe = [[(q, False), ("X" if r == "Si" else "", True), ("X" if r == "No" else "", True), (m, False)]
                 for q, r, m in voci]
        tabella(W, ["Contributo", "Si", "No", col], righe, titolo)
    firma()

    # Scheda dei possibili impatti
    d.add_page_break()
    par("Scheda dei possibili impatti relativi ai sei obiettivi ambientali in cui si applica il principio DNSH",
        bold=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, after=8)
    par("Ai fini della valutazione del principio DNSH, il soggetto firmatario dichiara:")
    par("-    che il progetto presenta i seguenti impatti, in relazione ai sei obiettivi ambientali:", after=6)
    righe = [[(o, False), ("X" if r == "Si" else "", True), ("X" if r == "No" else "", True),
              ("X" if r == "Non pertinente" else "", True), (m, False)] for o, r, m in IMPATTI]
    tabella([5.5, 1.1, 1.1, 2.4, 16.0], ["Obiettivi ambientali in cui si applica il principio DNSH", "Si", "No",
                                         "Non pertinente", "Motivazione"], righe)
    par("-    che è previsto l’allegato Piano di monitoraggio dei possibili impatti del progetto (solo per progetti di "
        "importo uguale o superiore a 10 milioni di euro);", after=6)
    par("-    che nell’ambito della realizzazione del progetto, sarà garantita la conformità giuridica dell’operazione, nel "
        "rispetto della legislazione ambientale applicabile nel seguito specificata:", after=4)
    for x in LEGISLAZIONE:
        p = d.add_paragraph(x, style="List Bullet"); p.paragraph_format.space_after = Pt(2)
    par("")
    par("-    allega, ove presenti, i seguenti elementi di prova della conformità giuridica dell’operazione:", after=4)
    par(PROVE[0])
    for x in PROVE[1:]:
        p = d.add_paragraph(x, style="List Bullet"); p.paragraph_format.space_after = Pt(2)
    firma()

    # Piano di monitoraggio
    d.add_page_break()
    par("Piano di monitoraggio dei possibili impatti del progetto", bold=True, size=11,
        align=WD_ALIGN_PARAGRAPH.CENTER, after=6)
    par("Il progetto, di importo superiore a 10 milioni di euro, prevede il monitoraggio degli obiettivi ambientali per i "
        "quali la scheda dei possibili impatti riporta una valutazione. Gli obiettivi valutati come non pertinenti non "
        "richiedono monitoraggio.", after=6)
    righe = [[(a, False), (b, False), (c, False), (e, False)] for a, b, c, e in MONITORAGGIO]
    tabella([5.5, 10.6, 4.5, 5.5], ["Obiettivo ambientale", "Indicatore", "Frequenza", "Responsabile"], righe)
    par("Gli esiti del monitoraggio sono riportati nei rapporti tecnici di stato di avanzamento e nella relazione tecnica "
        "finale.")
    firma()
    d.save(uscita)


if __name__ == "__main__":
    genera(sys.argv[1] if len(sys.argv) > 1 else "Allegato_4bis_DNSH_MooVXR.docx")
    print("scritto")
