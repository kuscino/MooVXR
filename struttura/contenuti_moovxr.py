# -*- coding: utf-8 -*-
"""contenuti_moovxr.py - testi redatti del Piano di Sviluppo MooVXR.

OBIETTIVI e i tempi degli OR (moduli 7.3) derivano dalla configurazione del modello economico
(struttura/economics_moovxr.py), cosi' tabella degli OR, cronoprogramma e costi restano
allineati per costruzione. I testi dei moduli 7.1 e 7.2 entrano qui solo dopo l'approvazione in
chat, un OR alla volta.

Uso (da Area di Lavoro):
    ROOT="$PWD" PROFILO=mimit_accordi_automotive CONTENUTI=struttura/contenuti_moovxr.py \
        python3 toolchain/toolchain/build_finanziato.py
"""
import importlib.util, pathlib, sys

QUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(QUI.parent / "toolchain" / "toolchain"))
from docx_core import testo, sottotitolo, punto, para, run

_spec = importlib.util.spec_from_file_location("economics_moovxr", QUI / "economics_moovxr.py")
_eco = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_eco)
CFG = _eco.CONFIG

# (id, proponente, tipo, titolo) per la tabella degli OR del par. 7
OBIETTIVI = [{"id": o[0], "proponente": o[2], "tipo": o[3], "titolo": o[1]} for o in CFG["or"]]

CONTENUTI = {}


def _tempi(inizio, fine):
    durata = fine - inizio + 1
    return lambda: testo("Durata: %d mesi, dal mese %d al mese %d del progetto." % (durata, inizio, fine))


for o in CFG["or"]:
    CONTENUTI["II.7.3/%s" % o[0]] = _tempi(o[4], o[5])


# ---------------------------------------------------------------- helper per i moduli degli OR
def _etichetta(coppia):
    """Paragrafo con etichetta in grassetto (forma Frascati: Problema, Soluzione proposta, ...)."""
    eti, resto = coppia
    return para(run(eti + " ", bold=True) + run(resto), spacing='<w:spacing w:before="60" w:after="60"/>')


def _blocchi(spec):
    """spec: lista di (tipo, testo), tipo t = paragrafo, p = punto elenco, s = sottotitolo,
    e = paragrafo con etichetta in grassetto (testo = (etichetta, resto))."""
    f = {"t": testo, "p": punto, "s": sottotitolo, "e": _etichetta}
    return lambda: "".join(f[k](v) for k, v in spec)


def _intestazione(titolo, proponente, tipo, luogo="[sede operativa da confermare]"):
    return ("t", "Titolo: %s. Soggetto proponente: %s. Tipologia: %s. Luogo di svolgimento: %s."
            % (titolo, proponente, tipo, luogo))


# ---------------------------------------------------------------- OR2 (approvato il 19/11)
CONTENUTI["II.7.1/OR2"] = _blocchi([
    _intestazione("Storytelling geo-temporale generativo", "Aubay Italia", "ricerca industriale"),
    ("t", "L'obiettivo realizzativo riguarda i metodi con cui informazioni storiche e culturali sui luoghi si "
          "trasformano in racconti generati da modelli di AI generativa. I racconti sono calibrati su percorso, "
          "velocità, tempo disponibile e interessi degli occupanti, e restano ancorati a fonti verificate."),
    ("t", "Le attività sono ricerca industriale ai sensi dell'art. 1, lett. o), del DD: acquisiscono nuove "
          "conoscenze su generazione controllata dei contenuti e valutazione della loro attendibilità, verificate "
          "su territori pilota senza realizzazione in condizioni operative reali."),
])
CONTENUTI["II.7.2/OR2"] = _blocchi([
    ("s", "A2.1 Knowledge graph culturale dei luoghi (mesi 1-10)"),
    ("t", "L'attività definisce e popola per i territori pilota un knowledge graph di entità, periodi, eventi, "
          "fonti, licenze d'uso e livello di attendibilità. Il problema è rappresentare in un modello unico "
          "informazioni disperse fra archivi, formati e regimi di licenza diversi, con l'indicazione esplicita "
          "della provenienza. La novità è il legame fra dimensione geografica, dimensione temporale e "
          "attendibilità della fonte. Il metodo prevede un'ontologia di riferimento, procedure di acquisizione "
          "documentate e controlli di qualità sui dati. Risultato: modello e prima popolazione del knowledge "
          "graph (D2.1)."),
    ("s", "A2.2 Generazione dei racconti ancorata alle fonti (mesi 6-18)"),
    ("t", "L'attività sviluppa un motore di generazione basato su retrieval-augmented generation sul knowledge "
          "graph. Ogni affermazione del racconto è collegata alla fonte, e il motore distingue ciò che è "
          "documentato da ciò che è interpretazione. L'incertezza principale è il controllo delle allucinazioni "
          "dei modelli generativi su domini con fonti scarse o contraddittorie. Il metodo prevede vincoli di "
          "generazione, verifica automatica della corrispondenza con le fonti e misura sistematica degli errori "
          "fattuali. Risultato: prima release del motore di storytelling (D2.2)."),
    ("s", "A2.3 Adattamento al contesto di viaggio e agli occupanti (mesi 12-22)"),
    ("t", "L'attività adatta lunghezza, lingua, registro e contenuto del racconto al tempo che separa il veicolo "
          "dal luogo, all'età e agli interessi dei passeggeri. Per il guidatore il racconto è solo audio, nei "
          "limiti fissati dal content policy engine. Il problema è sincronizzare la narrazione con il movimento "
          "del veicolo, con tempi di arrivo incerti. La soluzione combina stima del tempo di arrivo e composizione "
          "modulare del racconto. Risultato: moduli di adattamento al contesto (D2.3), misurati sulla coerenza fra "
          "racconto e posizione del veicolo."),
    ("s", "A2.4 Attendibilità e provenienza dei contributi (mesi 10-20)"),
    ("t", "L'attività definisce i metodi per integrare nel knowledge graph i contributi della piattaforma "
          "collaborativa, stimandone l'attendibilità in base a provenienza, coerenza con le fonti esistenti e "
          "storico del contributore. L'incertezza riguarda la stima dell'attendibilità di contenuti nuovi, privi "
          "di riscontri. Il metodo prevede modelli di punteggio verificati su campioni valutati da esperti. "
          "Risultato: metodo di valutazione dell'attendibilità dei contributi (D2.4)."),
    ("s", "A2.5 Valutazione della qualità sui territori pilota (mesi 18-24)"),
    ("t", "L'attività valuta i racconti generati sui territori pilota con un protocollo ripetibile: correttezza "
          "fattuale verificata da esperti di dominio, coerenza con la posizione, gradimento di campioni di utenti. "
          "La valutazione si avvale di una consulenza di dominio culturale. Il protocollo e i dataset di "
          "valutazione sono risultati trasferibili ad altri territori. Risultato: rapporto di valutazione dello "
          "storytelling (D2.5)."),
    ("s", "Risorse umane"),
    ("t", "Un responsabile tecnico, impegnato nelle attività A2.1 e A2.2, 6 profili senior e 8 sviluppatori, con "
          "un impegno dell'81%. Il dettaglio per fascia di costo è riportato nella Tabella 3."),
])

# ---------------------------------------------------------------- OR3 (approvato il 19/11)
CONTENUTI["II.7.1/OR3"] = _blocchi([
    _intestazione("Erogazione dei contenuti, applicazione di bordo e dimostratore su veicolo", "Aubay Italia",
                  "sviluppo sperimentale", "[sede operativa da confermare]; prove su pista e su strada"),
    ("t", "L'obiettivo realizzativo sviluppa la filiera software che porta i contenuti dentro il veicolo:"),
    ("p", "piattaforma di erogazione edge-cloud;"),
    ("p", "applicazione di bordo multi-display, con integrazione verso l'HUD di serie del guidatore;"),
    ("p", "protezione dei contenuti;"),
    ("p", "integrazione del dimostratore su veicolo e prove su strada."),
    ("t", "I dati del veicolo arrivano dalla piattaforma IoT, che è l'unico punto di accesso al veicolo. Le "
          "attività sono sviluppo sperimentale ai sensi dell'art. 1 del DD: comprendono costruzione del "
          "prototipo, dimostrazione, test e convalida in un ambiente che riproduce le condizioni operative reali."),
])
CONTENUTI["II.7.2/OR3"] = _blocchi([
    ("s", "A3.1 Architettura edge-cloud della piattaforma di erogazione (mesi 7-15)"),
    ("t", "L'attività definisce l'architettura distribuita fra cloud centrale e nodi edge vicini alla rete mobile, "
          "allocando i requisiti di latenza fra i livelli. Il problema è garantire tempi di consegna compatibili "
          "con contenuti legati al luogo, con connettività variabile e molti veicoli contemporanei. Risultato: "
          "documento di architettura approvato (D3.1)."),
    ("s", "A3.2 Streaming adattivo e prefetch predittivo (mesi 10-27)"),
    ("t", "L'attività sviluppa il prefetch dei contenuti sulla cache di bordo, basato sulla stima del percorso e "
          "del tempo di arrivo, con adattamento della qualità alla banda e funzionamento offline. L'incertezza "
          "riguarda l'accuratezza della previsione su percorsi non pianificati e in zone a copertura scarsa. Il "
          "metodo prevede misure su percorsi di prova rappresentativi. Risultato: servizi di streaming e prefetch "
          "(D3.2), misurati sulla quota di contenuti disponibili nel momento utile."),
    ("s", "A3.3 Applicazione di bordo e HMI multi-display (mesi 13-33)"),
    ("t", "L'attività sviluppa l'applicazione di bordo che presenta i contenuti sulle superfici del veicolo: "
          "schermo centrale, HUD di serie del guidatore, HUD del passeggero, dispositivi dei passeggeri. "
          "L'applicazione esegue le decisioni del content policy engine e usa i dati del veicolo resi disponibili "
          "dalla piattaforma IoT. Il problema è integrarsi con sistemi infotainment e HUD esistenti, con "
          "interfacce diverse fra costruttori, senza modificarne l'hardware. Risultato: applicazione di bordo "
          "integrata (D3.3)."),
    ("s", "A3.4 Sicurezza dei contenuti e dell'applicazione (mesi 13-30)"),
    ("t", "L'attività realizza cifratura e protezione dei contenuti e l'analisi dei rischi del flusso dei "
          "contenuti secondo UNECE R155 e ISO/SAE 21434. Penetration test e assessment di conformità sono "
          "affidati a fornitori esterni, come da prassi del settore. Risultato: analisi dei rischi e misure di "
          "protezione verificate (D3.4)."),
    ("s", "A3.5 Prove di carico e continuità del servizio (mesi 22-30)"),
    ("t", "L'attività verifica la piattaforma con carichi rappresentativi di flotte numerose e con guasti "
          "simulati dei nodi edge, misurando latenza, disponibilità e tempi di ripristino. Risultato: rapporto "
          "delle prove di carico (D3.5)."),
    ("s", "A3.6 Integrazione del dimostratore su veicolo e protocollo di prova (mesi 24-32)"),
    ("t", "L'attività integra sul veicolo di prova il software e l'hardware di tutti gli OR:"),
    ("p", "kit di percezione e unità di calcolo;"),
    ("p", "HUD del passeggero;"),
    ("p", "applicazioni per occhiali e visori;"),
    ("p", "piattaforma IoT."),
    ("t", "Definisce inoltre il protocollo di prova con scenari, percorsi, condizioni e indicatori. Le prove in "
          "ambiente controllato si svolgono su pista o area chiusa. Il problema è verificare l'interazione fra "
          "componenti sviluppati separatamente. Risultato: dimostratore integrato e protocollo di prova (D3.6)."),
    ("s", "A3.7 Prove su strada e rapporto di sperimentazione (mesi 30-36)"),
    ("t", "L'attività esegue le prove su strada nelle aree pilota secondo il protocollo e verifica i valori "
          "obiettivo di tutti gli OR. Risultato: rapporto di sperimentazione con risultati, limiti e condizioni "
          "di impiego (D3.7)."),
    ("s", "Risorse umane"),
    ("t", "Due profili di responsabilità tecnica, uno per la piattaforma (A3.1 e A3.3) e uno per il dimostratore "
          "(A3.6 e A3.7), 11 profili senior e 17 sviluppatori, con un impegno del 75%. Il dettaglio per fascia di "
          "costo è riportato nella Tabella 3."),
])

# ---------------------------------------------------------------- OR4 (approvato il 19/11)
CONTENUTI["II.7.1/OR4"] = _blocchi([
    _intestazione("Servizi di contenuto: piattaforma collaborativa, marketplace, POI", "Aubay Italia",
                  "sviluppo sperimentale"),
    ("t", "L'obiettivo realizzativo sviluppa i servizi che alimentano l'esperienza a bordo dei passeggeri:"),
    ("p", "piattaforma collaborativa di contenuti georeferenziati (Open Heritage Cloud);"),
    ("p", "marketplace di esperienze immersive;"),
    ("p", "servizio di POI commerciali e di ricarica;"),
    ("p", "percorsi a minor consumo."),
    ("t", "I servizi sono convalidati con utenti e veicoli reali sui territori pilota. Per questo le attività sono "
          "sviluppo sperimentale ai sensi dell'art. 1 del DD."),
])
CONTENUTI["II.7.2/OR4"] = _blocchi([
    ("s", "A4.1 Piattaforma collaborativa Open Heritage Cloud (mesi 10-24)"),
    ("t", "L'attività sviluppa la piattaforma in cui cittadini, istituzioni e operatori pubblicano fotografie, "
          "racconti, audio, video e modelli 3D associati ai luoghi, con metadati su posizione, periodo, fonte, "
          "autore, licenza e attendibilità. Il problema è garantire qualità e struttura dei metadati con "
          "contributori eterogenei. Risultato: prima release della piattaforma (D4.1)."),
    ("s", "A4.2 Moderazione, diritti e consenso (mesi 13-27)"),
    ("t", "L'attività sviluppa i servizi di moderazione, verifica, versionamento e gestione dei diritti e del "
          "consenso, distinguendo il livello aperto dal livello professionale per musei ed enti. Le regole sono "
          "definite con una consulenza legale di dominio su diritto d'autore e protezione dei dati. Risultato: "
          "servizi di moderazione e gestione dei diritti (D4.2)."),
    ("s", "A4.3 Marketplace di esperienze immersive (mesi 19-33)"),
    ("t", "L'attività sviluppa il marketplace delle esperienze fruibili a bordo, con regole trasparenti sui "
          "diritti e sulla remunerazione dei contributori. Il problema è adattare la distribuzione delle "
          "esperienze ai vincoli del viaggio: durata, posizione, dispositivo disponibile. Risultato: marketplace "
          "di esperienze (D4.3)."),
    ("s", "A4.4 POI commerciali e ricarica con regole per ruolo (mesi 19-33)"),
    ("t", "L'attività sviluppa il servizio di raccomandazione di POI commerciali e colonnine di ricarica. Le "
          "proposte al guidatore compaiono solo a veicolo fermo o come breve messaggio audio, quelle ai passeggeri "
          "in forma interattiva, sempre con il consenso dell'utente. Risultato: servizio di raccomandazione "
          "(D4.4), misurato sul tasso di accettazione e sul rispetto delle regole di consenso."),
    ("s", "A4.5 Percorsi a minor consumo (mesi 25-36)"),
    ("t", "L'attività sviluppa il calcolo di percorsi e profili di marcia a minor consumo, integrati con le soste "
          "di ricarica. Il consumo è misurato su missioni comparabili rispetto a un percorso di riferimento, con "
          "un protocollo ripetibile. Risultato: servizio e rapporto di misura dei consumi (D4.5)."),
    ("s", "Risorse umane"),
    ("t", "Un responsabile tecnico, impegnato nell'attività A4.1, 5 profili senior e 14 sviluppatori, con un "
          "impegno dell'82%. Il dettaglio per fascia di costo è riportato nella Tabella 3."),
])

# ---------------------------------------------------------------- OR5 (approvato il 19/11)
CONTENUTI["II.7.1/OR5"] = _blocchi([
    _intestazione("Occhiali AR in un veicolo in movimento", "GSNet", "ricerca industriale"),
    ("t", "L'obiettivo realizzativo riguarda i metodi per l'uso di occhiali AR da parte dei passeggeri di un "
          "veicolo in movimento. I contenuti devono restare agganciati agli oggetti reali fuori dal finestrino "
          "oppure all'abitacolo."),
    ("t", "Le attività sono ricerca industriale ai sensi dell'art. 1, lett. o), del DD: affrontano un problema "
          "aperto, la separazione del moto della testa dal moto del veicolo. Le verifiche si svolgono in "
          "laboratorio e su percorsi di prova, senza realizzazione in condizioni operative reali."),
])
CONTENUTI["II.7.2/OR5"] = _blocchi([
    ("s", "A5.1 Separazione del moto della testa dal moto del veicolo (mesi 1-12)"),
    ("t", "I sensori inerziali degli occhiali registrano insieme il movimento della testa e quello del veicolo. "
          "Accelerazioni, frenate e curve vengono così scambiate per movimenti della testa e il contenuto scivola "
          "o trema. L'attività studia la fusione fra sensori degli occhiali e dati di moto del veicolo per "
          "isolare il moto relativo della testa. La novità è l'uso del veicolo come riferimento inerziale noto. "
          "L'incertezza riguarda latenze e sincronizzazione fra le due fonti di dati. Il metodo prevede modelli "
          "di stima verificati su banco con traiettorie note. Risultato: algoritmo di tracking in veicolo (D5.1)."),
    ("s", "A5.2 Ancoraggio nel riferimento abitacolo e nel riferimento mondo esterno (mesi 5-15)"),
    ("t", "L'attività sviluppa le due modalità di ancoraggio dei contenuti: solidali all'abitacolo, come un "
          "pannello informativo, o solidali al mondo esterno, come un'etichetta su un monumento. Il problema è "
          "passare dall'una all'altra senza discontinuità percepibili. Risultato: modulo di ancoraggio per "
          "occhiali AR (D5.2)."),
    ("s", "A5.3 Integrazione con la localizzazione di precisione (mesi 9-16)"),
    ("t", "L'attività collega il tracking degli occhiali alla localizzazione di precisione del veicolo e ai dati "
          "di percezione della scena, così da agganciare i contenuti ai luoghi reali. Risultato: integrazione con "
          "la localizzazione (D5.3)."),
    ("s", "A5.4 Prove in veicolo su percorsi differenziati (mesi 13-18)"),
    ("t", "L'attività verifica gli algoritmi su percorsi urbani, extraurbani, con curve e con fondo irregolare. "
          "Misura l'errore di posizionamento, la stabilità in accelerazione e in curva e il ritardo fra movimento "
          "e aggiornamento dell'immagine (motion-to-photon). Come riferimento si usa un ground truth acquisito con "
          "motion capture. Risultato: rapporto delle prove (D5.4)."),
    ("s", "Risorse umane"),
    ("t", "Un responsabile tecnico, impegnato nell'attività A5.1, 4 profili senior e 5 sviluppatori, con un "
          "impegno dell'84%. Il dettaglio per fascia di costo è riportato nella Tabella 3."),
])

# ---------------------------------------------------------------- OR6 (approvato il 19/11)
CONTENUTI["II.7.1/OR6"] = _blocchi([
    _intestazione("Esperienze AR e XR per i passeggeri adattate alla scena", "GSNet", "sviluppo sperimentale",
                  "[sede operativa da confermare]; prove sul veicolo di prova"),
    ("t", "L'obiettivo realizzativo sviluppa le applicazioni per occhiali e visori dei passeggeri: informazioni "
          "sovrapposte al paesaggio, ricostruzioni, esperienze del marketplace. La presentazione dei contenuti si "
          "adatta alla scena rilevata dal kit di percezione."),
    ("t", "GSNet mette a disposizione il veicolo di prova, a noleggio, usato anche per le prove degli altri OR. "
          "Le attività sono sviluppo sperimentale ai sensi dell'art. 1 del DD: prototipi su dispositivi "
          "commerciali, convalidati con passeggeri in condizioni operative reali."),
])
CONTENUTI["II.7.2/OR6"] = _blocchi([
    ("s", "A6.1 Applicazione per occhiali AR (mesi 13-27)"),
    ("t", "L'attività sviluppa l'applicazione che mostra etichette e informazioni ancorate ai luoghi, integrate "
          "con i racconti e con i contenuti della piattaforma collaborativa. Usa il tracking in veicolo sviluppato "
          "nella ricerca industriale. Risultato: prototipo funzionante su dispositivo commerciale (D6.1)."),
    ("s", "A6.2 Applicazione per visori sincronizzata con il moto del veicolo (mesi 16-30)"),
    ("t", "L'attività sviluppa esperienze immersive su visore sincronizzate con accelerazioni e curve del "
          "veicolo, per ridurre la cinetosi secondo le indicazioni sperimentali del Politecnico. Il problema è "
          "mantenere la coerenza fra movimento percepito e movimento visto con i limiti di calcolo e batteria dei "
          "dispositivi. Risultato: applicazione per visori (D6.2)."),
    ("s", "A6.3 Adattamento dei contenuti alla scena rilevata (mesi 19-30)"),
    ("t", "L'attività usa gli oggetti rilevati e tracciati dal kit di percezione per riposizionare, filtrare o "
          "mettere in evidenza i contenuti: per esempio un'etichetta che segue un monumento in avvicinamento, "
          "oppure un contenuto spostato quando un oggetto lo coprirebbe. È la parte meno consolidata dell'OR, "
          "perché dipende dalla qualità della percezione in condizioni reali. Risultato: modulo di adattamento "
          "alla scena (D6.3)."),
    ("s", "A6.4 Integrazione con l'erogazione e con il content policy engine (mesi 22-33)"),
    ("t", "L'attività integra le applicazioni con la piattaforma di erogazione e con il content policy engine, "
          "che può sospendere o ridurre i contenuti in particolari situazioni di guida. Risultato: integrazione "
          "delle applicazioni XR (D6.4)."),
    ("s", "A6.5 Prove con i passeggeri sul veicolo di prova (mesi 28-36)"),
    ("t", "L'attività svolge prove con campioni di passeggeri, misurando gradimento, incidenza della cinetosi e "
          "durata della batteria in uso continuo. Risultato: rapporto delle prove (D6.5)."),
    ("s", "Risorse umane"),
    ("t", "Un responsabile tecnico, impegnato nell'attività A6.1, 5 profili senior e 5 sviluppatori, con un "
          "impegno del 53%. Il dettaglio per fascia di costo è riportato nella Tabella 3."),
])

# ---------------------------------------------------------------- OR7 (approvato il 19/11)
CONTENUTI["II.7.1/OR7"] = _blocchi([
    _intestazione("Integrazione di dati da strada e infrastruttura", "Anitia", "ricerca industriale"),
    ("t", "L'obiettivo realizzativo riguarda i metodi per arricchire le informazioni a disposizione del veicolo "
          "con dati esterni (semafori, cantieri, incidenti, traffico, disponibilità delle colonnine) attraverso la "
          "comunicazione V2X e le piattaforme dei gestori."),
    ("t", "Le attività sono ricerca industriale ai sensi dell'art. 1, lett. o), del DD: il criterio con cui un "
          "dato esterno diventa abbastanza affidabile e tempestivo da essere mostrato al guidatore non è definito "
          "dallo stato dell'arte."),
])
CONTENUTI["II.7.2/OR7"] = _blocchi([
    ("s", "A7.1 Censimento delle fonti esterne (mesi 1-5)"),
    ("t", "L'attività censisce le fonti disponibili nelle aree pilota, con formato, latenza, copertura e "
          "condizioni d'uso, in un catalogo strutturato e aggiornabile. Risultato: catalogo delle fonti esterne "
          "(D7.1)."),
    ("s", "A7.2 Fusione dei dati esterni con i dati di bordo (mesi 4-14)"),
    ("t", "L'attività sviluppa i metodi di fusione fra dati esterni e dati del veicolo, con una stima "
          "dell'affidabilità e dell'attualità di ogni informazione. L'incertezza riguarda la combinazione di fonti "
          "con ritardi e accuratezze molto diversi, spesso senza metadati di qualità. Il metodo prevede modelli "
          "probabilistici verificati su dati storici delle aree pilota. Risultato: modulo di fusione (D7.2)."),
    ("s", "A7.3 Criteri di promozione di un dato ad avviso per il guidatore (mesi 9-16)"),
    ("t", "L'attività definisce le soglie di affidabilità, anticipo e pertinenza oltre le quali un dato esterno "
          "diventa un avviso, coerenti con gli standard C-ITS e con le regole del content policy engine. "
          "L'allineamento agli standard si avvale di una consulenza di dominio. Risultato: criteri di promozione "
          "ad avviso (D7.3)."),
    ("s", "A7.4 Prove su area pilota (mesi 14-18)"),
    ("t", "L'attività misura sull'area pilota l'anticipo con cui un evento è noto rispetto alla sola percezione "
          "di bordo, la percentuale di segnalazioni corrette e il ritardo di propagazione. Risultato: rapporto "
          "delle prove (D7.4)."),
    ("s", "Risorse umane"),
    ("t", "Un responsabile tecnico, impegnato nell'attività A7.1, 4 profili senior e 6 sviluppatori, con un "
          "impegno dell'80%. Il dettaglio per fascia di costo è riportato nella Tabella 3."),
])

# ---------------------------------------------------------------- OR8 (approvato il 19/11)
CONTENUTI["II.7.1/OR8"] = _blocchi([
    _intestazione("Piattaforma IoT: accesso ai dati del veicolo, device management e OTA", "Anitia",
                  "sviluppo sperimentale"),
    ("t", "L'obiettivo realizzativo sviluppa la piattaforma che costituisce l'unico punto di accesso al veicolo "
          "per tutti i componenti del sistema. La piattaforma copre:"),
    ("p", "lettura dei dati del veicolo, compresi i segnali ADAS e DMS di serie;"),
    ("p", "raccolta e governance dei dati in cloud;"),
    ("p", "gestione dei dispositivi di bordo e aggiornamento OTA di tutto il software installato."),
    ("t", "Le attività sono sviluppo sperimentale ai sensi dell'art. 1 del DD: la piattaforma è convalidata sui "
          "veicoli di prova in condizioni operative reali."),
])
CONTENUTI["II.7.2/OR8"] = _blocchi([
    ("s", "A8.1 Accesso ai dati del veicolo tramite modello dati standard (mesi 7-18)"),
    ("t", "L'attività sviluppa il servizio che legge i dati del veicolo attraverso un modello dati standard e li "
          "espone tramite API agli altri componenti. Comprende i segnali dei sistemi ADAS e DMS di serie, che non "
          "si sviluppano ma si usano. Il problema è l'eterogeneità delle interfacce fra costruttori. Risultato: "
          "servizio di accesso ai dati del veicolo (D8.1)."),
    ("s", "A8.2 Raccolta, archiviazione e governance dei dati in cloud (mesi 10-24)"),
    ("t", "L'attività sviluppa la raccolta e l'archiviazione dei dati in cloud, con regole di conservazione e di "
          "accesso per ciascun componente e per ciascuna finalità. Risultato: piattaforma dati in cloud (D8.2), "
          "misurata sulla percentuale di dati raccolti senza perdite e sul ritardo fra evento a bordo e "
          "disponibilità in cloud."),
    ("s", "A8.3 Device management e aggiornamento OTA (mesi 13-28)"),
    ("t", "L'attività sviluppa registrazione, monitoraggio, configurazione e aggiornamento a distanza dei "
          "dispositivi e del software di bordo di tutti i partner. Gli aggiornamenti sono gestiti secondo UNECE "
          "R156; il penetration test del canale OTA è affidato a un fornitore esterno. Risultato: servizio di "
          "device management e OTA (D8.3)."),
    ("s", "A8.4 Fonti esterne, affidabilità e scalabilità (mesi 22-33)"),
    ("t", "L'attività integra le fonti esterne individuate nella ricerca industriale e verifica affidabilità e "
          "scalabilità della piattaforma su flotte simulate. Risultato: rapporto delle prove (D8.4), con il numero "
          "di veicoli gestibili."),
    ("s", "Risorse umane"),
    ("t", "Un responsabile tecnico, impegnato nell'attività A8.1, 4 profili senior e 8 sviluppatori, con un "
          "impegno del 68%. Il dettaglio per fascia di costo è riportato nella Tabella 3."),
])

# ---------------------------------------------------------------- OR9 (approvato il 19/11)
CONTENUTI["II.7.1/OR9"] = _blocchi([
    _intestazione("Localizzazione di precisione, ancoraggio dei contenuti e calcolo a bordo",
                  "Politecnico di Milano", "ricerca industriale", "[sede del Politecnico di Milano da confermare]"),
    ("t", "L'obiettivo realizzativo riguarda i metodi per posizionare con precisione i contenuti sulla scena reale, "
          "sia sugli HUD sia sugli occhiali, riconoscendo quando la precisione non è sufficiente. Comprende anche "
          "le specifiche dell'unità di calcolo di bordo su cui eseguire gli algoritmi."),
    ("t", "Le attività sono ricerca industriale ai sensi dell'art. 1, lett. o), del DD: producono nuove conoscenze "
          "su localizzazione e registrazione dei contenuti per un componente di un sistema complesso, verificate "
          "su dati registrati e su percorsi di prova."),
])
CONTENUTI["II.7.2/OR9"] = _blocchi([
    ("s", "A9.1 Localizzazione di precisione (mesi 1-14)"),
    ("t", "L'attività sviluppa algoritmi di localizzazione che combinano GNSS RTK, sensori inerziali e visione. I "
          "sistemi di serie localizzano il veicolo per la navigazione, non per sovrapporre contenuti agli oggetti "
          "reali, e la realtà aumentata richiede una precisione di un ordine di grandezza superiore. L'incertezza "
          "riguarda il mantenimento di questa precisione in condizioni di segnale GNSS degradato. Il metodo prevede "
          "la valutazione su percorsi rilevati con riferimento di precisione. Risultato: algoritmi di "
          "localizzazione di precisione (D9.1)."),
    ("s", "A9.2 Ancoraggio dei contenuti alla scena (mesi 6-18)"),
    ("t", "L'attività ricostruisce la geometria della scena utile all'ancoraggio dei contenuti dal punto di vista "
          "del guidatore, del passeggero e di chi indossa occhiali, usando i dati di percezione del kit "
          "multisensore. Il problema è un ancoraggio stabile con punti di vista diversi e con un veicolo in "
          "movimento. Risultato: algoritmi di ancoraggio (D9.2), misurati sulla stabilità dell'ancoraggio."),
    ("s", "A9.3 Stima dell'affidabilità e riduzione dei contenuti (mesi 10-20)"),
    ("t", "L'attività sviluppa uno stimatore dell'affidabilità della localizzazione in tempo reale, insieme ai "
          "criteri con cui il content policy engine riduce i contenuti quando l'affidabilità è insufficiente, per "
          "esempio con nebbia, buio o segnale degradato. La novità è trattare l'affidabilità come grandezza "
          "esplicita che governa la presentazione. Risultato: stimatore di affidabilità (D9.3)."),
    ("s", "A9.4 Specifiche dell'unità di calcolo di bordo (mesi 4-12)"),
    ("t", "L'attività definisce l'architettura di calcolo: cosa elaborare sul veicolo e cosa in cloud, con "
          "prestazioni, latenze e consumi richiesti. Le specifiche sono la base del prototipo realizzato da nLight. "
          "Risultato: specifiche dell'unità di calcolo di bordo (D9.4)."),
    ("s", "A9.5 Ottimizzazione degli algoritmi per l'esecuzione a bordo (mesi 16-24)"),
    ("t", "L'attività adatta gli algoritmi alle risorse dell'unità di bordo, misurandone tempi di calcolo e "
          "consumi. Risultato: algoritmi ottimizzati (D9.5)."),
    ("s", "Risorse umane"),
    ("t", "Un responsabile scientifico, impegnato nelle attività A9.1 e A9.4, 5 profili di fascia Media e 12 "
          "ricercatori, con un impegno dell'84%. Il dettaglio per fascia di costo è riportato nella Tabella 3."),
])

# ---------------------------------------------------------------- OR10 (approvato il 19/11)
CONTENUTI["II.7.1/OR10"] = _blocchi([
    _intestazione("Contenuti a bordo, attenzione degli occupanti e cinetosi", "Politecnico di Milano",
                  "ricerca industriale", "[sede del Politecnico di Milano da confermare]"),
    ("t", "L'obiettivo realizzativo stabilisce su basi sperimentali quali contenuti, in quale forma e su quale "
          "superficie sono compatibili con una guida sicura, e come ridurre la cinetosi dei passeggeri che usano "
          "HUD, schermi e visori."),
    ("t", "Le attività sono ricerca industriale ai sensi dell'art. 1, lett. o), del DD: sono indagini "
          "sperimentali svolte in ambienti simulati, su un abitacolo con più superfici di visualizzazione che la "
          "letteratura non ha ancora studiato."),
])
CONTENUTI["II.7.2/OR10"] = _blocchi([
    ("s", "A10.1 Disegno sperimentale e scenari di guida (mesi 1-6)"),
    ("t", "L'attività definisce ipotesi, scenari di guida di complessità crescente, campioni, misure e "
          "protocollo, compresi gli aspetti etici e di protezione dei dati. Risultato: protocollo sperimentale "
          "(D10.1)."),
    ("s", "A10.2 Prove sui guidatori in ambienti simulati (mesi 5-18)"),
    ("t", "L'attività misura attenzione e prestazioni di guida in presenza di contenuti diversi sulle varie "
          "superfici: HUD del guidatore, schermo centrale, HUD del passeggero, contenuti audio. Usa eye tracking e "
          "i segnali dei sistemi di monitoraggio del guidatore. L'incertezza riguarda gli effetti di superfici mai "
          "studiate insieme, come un contenuto proiettato sul finestrino del passeggero. Risultato: dati "
          "sperimentali sull'attenzione dei guidatori (D10.2)."),
    ("s", "A10.3 Prove sui passeggeri e cinetosi (mesi 10-22)"),
    ("t", "L'attività misura incidenza e intensità della cinetosi nei passeggeri che usano HUD, schermi e "
          "visori, con e senza sincronizzazione dei contenuti con il moto del veicolo. Risultato: dati "
          "sperimentali su passeggeri e cinetosi (D10.3)."),
    ("s", "A10.4 Linee guida e regole per il content policy engine (mesi 16-24)"),
    ("t", "L'attività sintetizza i risultati in linee guida e in regole trasferibili al content policy engine, "
          "in forma codificabile. Il risultato è trasferibile anche oltre il progetto, come riferimento per la "
          "progettazione di abitacoli multi-display. Risultato: linee guida per i contenuti a bordo (D10.4)."),
    ("s", "A10.5 Verifica delle regole adattive in ambienti simulati (mesi 22-30)"),
    ("t", "L'attività verifica in ambienti simulati che il content policy engine adattivo non peggiori gli "
          "indicatori di attenzione rispetto alle regole fisse. Verifica inoltre la visibilità dell'HUD del "
          "passeggero dal posto di guida. Risultato: rapporto di verifica (D10.5)."),
    ("s", "Risorse umane"),
    ("t", "Un responsabile scientifico, impegnato nelle attività A10.1 e A10.4, 5 profili di fascia Media e 11 "
          "ricercatori, con un impegno dell'84%. Il dettaglio per fascia di costo è riportato nella Tabella 3."),
])

# ---------------------------------------------------------------- OR11 (approvato il 19/11)
CONTENUTI["II.7.1/OR11"] = _blocchi([
    _intestazione("HUD per il passeggero a proiezione sul finestrino", "Politecnico di Milano",
                  "ricerca industriale",
                  "[sede del Politecnico di Milano da confermare]; verifiche sul veicolo di prova"),
    ("t", "L'obiettivo realizzativo riguarda la progettazione e la costruzione di un prototipo di laboratorio di "
          "HUD per il passeggero. Il dispositivo proietta i contenuti su una porzione definita del finestrino "
          "laterale, agganciati al paesaggio esterno e invisibili dal posto di guida. Oggi non esistono veicoli né "
          "prototipi noti che offrano un HUD dedicato ai passeggeri."),
    ("t", "Le attività sono ricerca industriale ai sensi dell'art. 1, lett. o), del DD, che vi comprende "
          "espressamente la costruzione di prototipi in ambiente di laboratorio. Il prototipo è installabile sul "
          "veicolo di prova per le verifiche, senza integrazione nell'abitacolo di serie."),
])
CONTENUTI["II.7.2/OR11"] = _blocchi([
    ("s", "A11.1 Stato dell'arte e requisiti (mesi 1-6)"),
    ("t", "L'attività analizza lo stato dell'arte di HUD e display trasparenti e definisce i requisiti: superfici "
          "utilizzabili, visibilità residua dal posto di guida, condizioni di luce, vincoli dell'abitacolo come gli "
          "airbag laterali e i rivestimenti. I vincoli di sicurezza passiva sono verificati con una consulenza di "
          "dominio automotive. Risultato: requisiti dell'HUD per il passeggero (D11.1)."),
    ("s", "A11.2 Architettura ottica del proiettore (mesi 4-16)"),
    ("t", "L'attività progetta l'architettura ottica: porzione di proiezione, distanza focale dell'immagine, "
          "contrasto rispetto al paesaggio esterno, alloggiamento del proiettore sopra il poggiabraccio. La novità "
          "è l'uso del finestrino laterale come superficie di proiezione per un passeggero libero di muovere la "
          "testa. L'incertezza riguarda la leggibilità in pieno sole e la visibilità residua dal posto di guida. "
          "Risultato: progetto ottico (D11.2)."),
    ("s", "A11.3 Correzione prospettica e registrazione sulla scena (mesi 8-20)"),
    ("t", "L'attività sviluppa gli algoritmi che correggono la prospettiva dell'immagine proiettata sul "
          "finestrino inclinato e la allineano agli oggetti esterni. Usa la posizione stimata della testa del "
          "passeggero e i dati di ancoraggio. Risultato: algoritmi di correzione prospettica e registrazione "
          "(D11.3), misurati sull'errore di allineamento."),
    ("s", "A11.4 Prototipo di laboratorio installabile su veicolo (mesi 14-26)"),
    ("t", "L'attività realizza il prototipo, affidando a fornitori esterni ottiche, proiettore e supporti, e lo "
          "verifica su banco ottico. Il prototipo non è un componente pronto per la produzione: dimostra la "
          "fattibilità dei principi ottici e algoritmici. Risultato: prototipo dell'HUD per il passeggero (D11.4)."),
    ("s", "A11.5 Verifiche di visibilità e leggibilità (mesi 22-30)"),
    ("t", "L'attività misura contrasto, leggibilità e visibilità residua dal posto di guida, su banco e sul "
          "veicolo di prova, con un protocollo ripetibile. Se i requisiti sono raggiunti solo in parte, il "
          "rapporto documenta i limiti e le condizioni d'impiego. Risultato: rapporto delle verifiche (D11.5)."),
    ("s", "Risorse umane"),
    ("t", "Un responsabile scientifico, impegnato nelle attività A11.1 e A11.2, 5 profili di fascia Media e 12 "
          "ricercatori, con un impegno dell'82%. Il dettaglio per fascia di costo è riportato nella Tabella 3."),
])

# ---------------------------------------------------------------- OR12 (approvato il 19/11)
CONTENUTI["II.7.1/OR12"] = _blocchi([
    _intestazione("Percezione della scena multispettrale e LiDAR, tracking dei punti di interesse", "nLight",
                  "ricerca industriale", "[sede di Torino da confermare]"),
    ("t", "L'obiettivo realizzativo riguarda i metodi per rilevare e seguire nella scena attorno al veicolo i "
          "punti di interesse su cui agganciare i contenuti, come monumenti, edifici ed elementi del paesaggio. "
          "La percezione combina:"),
    ("p", "video nel visibile su quattro lati;"),
    ("p", "infrarosso e termico;"),
    ("p", "LiDAR."),
    ("t", "Il kit di percezione è dedicato all'esperienza degli occupanti, non alla guida, e non si sovrappone ai "
          "sistemi ADAS di serie. Le attività sono ricerca industriale ai sensi dell'art. 1, lett. o), del DD: "
          "sviluppano metodi di percezione multisensore per una finalità nuova, verificati su banco e su percorsi "
          "registrati."),
])
CONTENUTI["II.7.2/OR12"] = _blocchi([
    ("s", "A12.1 Configurazione sensoriale (mesi 1-6)"),
    ("t", "L'attività definisce numero, posizione, campo visivo e caratteristiche dei sensori: telecamere "
          "grandangolari su quattro lati, telecamere infrarosse e termiche, LiDAR. Il problema è coprire la scena "
          "laterale vista dai passeggeri, che i sistemi di serie, orientati all'avanti, non coprono con questo "
          "scopo. Risultato: specifica della configurazione sensoriale (D12.1)."),
    ("s", "A12.2 Rilevamento e tracking dei punti di interesse su video (mesi 4-15)"),
    ("t", "L'attività sviluppa algoritmi di rilevamento e tracking di punti di interesse statici, osservati da un "
          "veicolo in movimento a distanze e angolazioni variabili. L'incertezza riguarda la continuità del "
          "tracking con occlusioni e variazioni di luce. Il metodo prevede l'addestramento su dataset annotati e la "
          "valutazione su metriche standard di rilevamento e tracking. Risultato: algoritmi di rilevamento e "
          "tracking (D12.2)."),
    ("s", "A12.3 Fusione di video, infrarosso e LiDAR (mesi 6-16)"),
    ("t", "L'attività sviluppa la fusione multisensore per stimare distanza e geometria dei punti di interesse, "
          "necessarie all'ancoraggio preciso dei contenuti. Risultato: modulo di fusione multisensore (D12.3), "
          "misurato sull'errore di distanza."),
    ("s", "A12.4 Percezione notturna e con bassa visibilità (mesi 10-18)"),
    ("t", "L'attività estende rilevamento e tracking alla notte e alla visibilità ridotta, sfruttando infrarosso "
          "e termico. Rende disponibili esperienze che altrimenti si interromperebbero. Risultato: modulo di "
          "percezione in bassa visibilità (D12.4)."),
    ("s", "A12.5 Verifiche su banco e su percorsi registrati (mesi 14-18)"),
    ("t", "L'attività verifica gli algoritmi su dataset di prova e su percorsi registrati, con indicatori di "
          "precisione, continuità del tracking ed errore di distanza. Risultato: rapporto delle verifiche (D12.5)."),
    ("s", "Risorse umane"),
    ("t", "Un responsabile tecnico, impegnato nelle attività A12.1 e A12.2, 5 profili senior e 13 tecnici, con un "
          "impegno dell'84%. Il dettaglio per fascia di costo è riportato nella Tabella 3."),
])

# ---------------------------------------------------------------- OR13 (approvato il 19/11)
CONTENUTI["II.7.1/OR13"] = _blocchi([
    _intestazione("Prototipo del kit di percezione e dell'unità di calcolo di bordo, validazione su veicolo",
                  "nLight", "sviluppo sperimentale", "[sede di Torino da confermare]; prove sul veicolo di prova"),
    ("t", "L'obiettivo realizzativo realizza il prototipo del kit di percezione multisensore e dell'unità di "
          "calcolo di bordo, lo installa e lo calibra sul veicolo di prova e ne valida le prestazioni su strada."),
    ("t", "Le attività sono sviluppo sperimentale ai sensi dell'art. 1 del DD: costruzione di prototipi, test e "
          "convalida in condizioni operative reali."),
])
CONTENUTI["II.7.2/OR13"] = _blocchi([
    ("s", "A13.1 Progetto del kit e dell'unità di calcolo (mesi 13-18)"),
    ("t", "L'attività progetta kit e unità di calcolo sulle specifiche del Politecnico: alimentazione da veicolo, "
          "cablaggi, contenitori, dissipazione. Risultato: progetto conforme alle specifiche (D13.1)."),
    ("s", "A13.2 Prototipo del kit di percezione (mesi 16-27)"),
    ("t", "L'attività realizza il prototipo del kit. Le lavorazioni meccaniche e i cablaggi sono affidati a "
          "fornitori esterni, i componenti rientrano nei materiali. Il problema è garantire allineamento e "
          "sincronizzazione dei sensori con le vibrazioni del veicolo. Risultato: kit funzionante su banco con "
          "alimentazione da veicolo (D13.2)."),
    ("s", "A13.3 Prototipo dell'unità di calcolo e prove ambientali (mesi 16-28)"),
    ("t", "L'attività realizza il prototipo dell'unità di calcolo, con la scheda prodotta da un fornitore esterno. "
          "Le prove di vibrazione, temperatura e compatibilità elettromagnetica si svolgono in un laboratorio "
          "accreditato. Risultato: prototipo dell'unità di calcolo (D13.3)."),
    ("s", "A13.4 Installazione e calibrazione sul veicolo di prova (mesi 25-31)"),
    ("t", "L'attività installa kit e unità di calcolo sul veicolo di prova e ne calibra i sensori. Risultato: kit "
          "installato e calibrato (D13.4), misurato sull'errore di calibrazione."),
    ("s", "A13.5 Validazione su strada della percezione (mesi 30-36)"),
    ("t", "L'attività verifica su strada, nelle prove del dimostratore, che gli indicatori di percezione misurati "
          "nella ricerca industriale siano confermati in condizioni reali. Risultato: rapporto di validazione "
          "(D13.5)."),
    ("s", "Risorse umane"),
    ("t", "Due profili di responsabilità tecnica, uno per il progetto e il prototipo del kit (A13.1 e A13.2) e uno "
          "per la validazione (A13.5), 7 profili senior e 19 tecnici, con un impegno dell'83%. Il dettaglio per "
          "fascia di costo è riportato nella Tabella 3."),
])


# ---------------------------------------------------------------- OR1, forma Frascati (approvato il 20/11)
CONTENUTI["II.7.1/OR1"] = _blocchi([
    _intestazione("Content policy engine adattivo e personalizzazione dei contenuti", "Aubay Italia",
                  "ricerca industriale", "Roma (Lazio)"),
    ("t", "L'obiettivo realizzativo studia i metodi e i modelli con cui un content policy engine stabilisce, "
          "istante per istante, quali contenuti presentare a ciascun occupante del veicolo, in quale forma e su "
          "quale superficie di visualizzazione. La decisione tiene conto della situazione di guida, della scena "
          "rilevata e dell'attenzione del singolo guidatore."),
    ("t", "Lo stato dell'arte regola i contenuti di bordo con criteri statici pensati per un solo display e per il "
          "solo guidatore: lo European Statement of Principles on HMI (Raccomandazione 2008/653/CE) e le linee "
          "guida NHTSA sulla distrazione visivo-manuale, con limiti come 2 secondi per singolo sguardo e 12 secondi "
          "complessivi fuori strada per compito. Le soglie sono fisse: la riproduzione di video si blocca oltre una "
          "velocità, i menu si riducono in marcia. I sistemi di monitoraggio del guidatore (DMS) previsti dal "
          "Regolamento (UE) 2019/2144 producono avvisi ma non governano i contenuti. Non esiste un criterio per "
          "arbitrare fra più superfici e più occupanti, né per adattarsi al singolo guidatore."),
    ("t", "L'obiettivo produce cinque risultati, usati dall'applicazione di bordo (OR3) e dalle esperienze per i "
          "passeggeri (OR4):"),
    ("p", "un modello del contesto con previsione a breve termine;"),
    ("p", "un insieme di policy eseguibili, verificate formalmente;"),
    ("p", "una componente adattiva che può solo restringere le policy validate;"),
    ("p", "raccomandazioni personalizzate per ciascun occupante, entro i limiti decisi dalle policy;"),
    ("p", "profili degli occupanti costruiti a bordo, senza trasferimento di dati personali."),
    ("t", "Le attività sono ricerca industriale ai sensi dell'art. 1, lett. o), del DD: acquisiscono nuove "
          "conoscenze per un componente di un sistema complesso, verificato in ambiente di simulazione e su dati "
          "registrati, senza realizzazione in condizioni operative reali."),
])
CONTENUTI["II.7.2/OR1"] = _blocchi([
    ("s", "A1.1 Modello del contesto di guida e degli occupanti (mesi 1-8)"),
    ("e", ("Problema.", "Per decidere cosa mostrare, a chi e dove, il motore deve conoscere in ogni istante:")),
    ("p", "la dinamica del veicolo;"),
    ("p", "la complessità del contesto stradale;"),
    ("p", "la scena rilevata dal kit di percezione;"),
    ("p", "la presenza e la posizione degli occupanti;"),
    ("p", "l'attenzione del guidatore stimata dai segnali DMS di serie;"),
    ("p", "gli eventi esterni."),
    ("t", "Questi dati arrivano da fonti diverse, con frequenze, latenze e affidabilità diverse, e possono mancare. "
          "Le regole statiche usano una sola variabile, come la velocità o la marcia inserita."),
    ("e", ("Soluzione proposta.", "Un modello formale del contesto, cioè un insieme di variabili che descrivono la "
           "situazione, ciascuna con significato, unità di misura, frequenza di aggiornamento e grado di "
           "affidabilità, alimentato dalla piattaforma IoT (OR8), dalla percezione della scena (OR12) e dai dati "
           "esterni (OR7). Al modello si affiancano modelli predittivi che stimano l'evoluzione della situazione di "
           "guida nei secondi successivi, per esempio l'ingresso in un incrocio o una manovra. Così la riduzione dei "
           "contenuti può essere anticipata anziché arrivare in ritardo.")),
    ("e", ("Novità e incertezza.", "La novità è la rappresentazione unificata di grandezze eterogenee, con "
           "affidabilità esplicita, usata per decisioni in tempo reale su più superfici. L'incertezza riguarda due "
           "punti:")),
    ("p", "quale orizzonte di previsione sia raggiungibile con accuratezza sufficiente su dati parziali;"),
    ("p", "quali variabili siano davvero predittive del carico di guida."),
    ("e", ("Metodo.", "")),
    ("t", "1. Analisi dei segnali disponibili da OR7, OR8 e OR12 e dei requisiti delle superfici di visualizzazione."),
    ("t", "2. Specifica formale del modello."),
    ("t", "3. Addestramento e confronto di modelli predittivi su dataset di guida registrati, con dati di sviluppo e "
          "di prova separati per percorso e periodo."),
    ("t", "4. Valutazione dell'errore predittivo per orizzonte temporale."),
    ("e", ("Risultati misurabili.", "Specifica del modello del contesto e modelli predittivi (D1.1). Indicatori:")),
    ("p", "previsione delle situazioni ad alto carico con anticipo di almeno 3 secondi e riconoscimento di almeno "
          "l'85% delle situazioni ad alto carico sui dati di prova;"),
    ("p", "copertura del 100% dei segnali concordati con OR8."),
    ("t", "Il modello è indipendente dal veicolo ed è riusato dall'applicazione di bordo e dalle esperienze per i "
          "passeggeri."),

    ("s", "A1.2 Traduzione delle linee guida in policy eseguibili (mesi 6-16)"),
    ("e", ("Problema.", "Le linee guida di settore, come lo European Statement of Principles on HMI e le linee "
           "guida NHTSA, sono descrittive e pensate per un display e per il solo guidatore. Tradotte in regole per "
           "più superfici e più occupanti producono conflitti e lacune. Per esempio, uno stesso contenuto può "
           "risultare ammesso sul display del passeggero e vietato su una superficie visibile dal guidatore.")),
    ("e", ("Soluzione proposta.", "Un linguaggio in cui le regole descrivono cosa è ammesso e in quali condizioni, "
           "con tre classi (sempre vietato, ammesso a condizioni, sempre consentito), condizioni sulle variabili del "
           "modello del contesto, priorità e una regola di default prudente. Un controllo automatico segnala, già in "
           "fase di codifica, le regole in conflitto e i casi non coperti. Le regole sperimentali dell'OR dedicato "
           "all'attenzione degli occupanti (OR10), disponibili più avanti nel progetto, sono recepite nella verifica "
           "formale del motore (A1.5).")),
    ("e", ("Novità e incertezza.", "La novità è un linguaggio di regole HMI per più superfici e più occupanti, "
           "con controllo automatico di conflitti e lacune. L'incertezza riguarda due punti:")),
    ("p", "se il controllo resti eseguibile in tempi ragionevoli quando crescono regole e superfici;"),
    ("p", "se il linguaggio sia abbastanza espressivo da codificare tutte le linee guida senza eccezioni gestite a mano."),
    ("e", ("Metodo.", "")),
    ("t", "1. Censimento e normalizzazione delle linee guida."),
    ("t", "2. Progetto del linguaggio e dello strumento di verifica."),
    ("t", "3. Codifica delle regole."),
    ("t", "4. Verifica su casi di prova generati in modo sistematico, combinando contesto, superficie e occupante."),
    ("e", ("Risultati misurabili.", "Prima release del motore con regole codificate (D1.2). Indicatori:")),
    ("p", "100% delle linee guida codificate o escluse con motivazione;"),
    ("p", "nessun conflitto residuo;"),
    ("p", "tempo di valutazione dell'insieme di regole inferiore a 50 ms nel 95% dei casi (K7)."),

    ("s", "A1.3 Componente adattiva calibrata sul singolo guidatore (mesi 9-22)"),
    ("e", ("Problema.", "Le soglie fisse sono tarate su un guidatore medio. Sono troppo restrittive per chi gestisce "
           "bene il carico e troppo permissive per chi si distrae facilmente. Il DMS di serie misura l'attenzione, "
           "ma non come il singolo guidatore reagisce ai contenuti.")),
    ("e", ("Soluzione proposta.", "Una componente che osserva le reazioni del singolo guidatore ai contenuti "
           "presentati e calibra quantità e forma delle informazioni, riducendole o semplificandole quando "
           "l'attenzione cala. Le reazioni osservate sono sguardi fuori strada, tempi di risposta e variazioni dei "
           "comandi di guida, rilevate dai segnali della piattaforma IoT. Il vincolo è garantito per costruzione: la "
           "componente può solo aggiungere restrizioni a quelle delle policy validate, mai toglierne.")),
    ("e", ("Novità e incertezza.", "La novità è la personalizzazione dei contenuti di bordo sull'attenzione del "
           "singolo guidatore, con garanzia formale di non allargare mai le regole validate. L'incertezza riguarda "
           "tre punti:")),
    ("p", "la separazione fra tratti individuali stabili e rumore dei segnali, con pochi episodi per guidatore;"),
    ("p", "il tempo di convergenza del profilo;"),
    ("p", "l'assenza di oscillazioni nel comportamento."),
    ("e", ("Metodo.", "")),
    ("t", "1. Definizione degli indicatori di reazione."),
    ("t", "2. Modelli del singolo guidatore che si aggiornano a ogni sessione di guida."),
    ("t", "3. Dimostrazione formale del vincolo e prove automatiche che lo controllano su un gran numero di casi "
          "generati."),
    ("t", "4. Valutazione su dati di guida registrati e in simulazione; la verifica sperimentale con partecipanti è "
          "svolta dall'OR dedicato all'attenzione degli occupanti (A10.5)."),
    ("e", ("Risultati misurabili.", "Componente adattiva e rapporto di prova (D1.3). Indicatori:")),
    ("p", "nessuna decisione più permissiva delle policy validate su tutti i casi di prova;"),
    ("p", "riduzione degli sguardi fuori strada di almeno il 15% rispetto alle regole fisse, a parità di "
          "informazioni utili consegnate;"),
    ("p", "convergenza del profilo entro 10 sessioni di guida."),

    ("s", "A1.4 Gestione delle condizioni degradate (mesi 12-20)"),
    ("e", ("Problema.", "I dati possono mancare, arrivare in ritardo o essere poco affidabili: perdita di "
           "connessione, sensori degradati, localizzazione imprecisa, DMS non disponibile. Un motore che decide su "
           "dati errati può mostrare contenuti in situazioni non sicure; uno che si blocca a ogni disturbo è "
           "inutilizzabile.")),
    ("e", ("Soluzione proposta.", "Livelli di funzionamento progressivamente più prudenti, attivati "
           "dall'affidabilità dei dati del modello del contesto. A ogni livello corrisponde un insieme di regole più "
           "restrittivo: per esempio, al primo livello degradato sono esclusi i video sulle superfici visibili dal "
           "guidatore, all'ultimo livello restano solo i messaggi audio essenziali. Il passaggio a un livello più "
           "prudente è immediato. Il ritorno al livello precedente avviene solo dopo che i dati sono rimasti "
           "affidabili per un tempo minimo, così i contenuti non compaiono e scompaiono in continuazione quando un "
           "dato oscilla intorno alla soglia.")),
    ("e", ("Novità e incertezza.", "La novità è una degradazione graduale guidata dall'affidabilità dei dati, "
           "applicata ai contenuti di bordo su più superfici. L'incertezza riguarda la scelta di soglie che "
           "garantiscano prudenza senza ridurre il servizio troppo spesso.")),
    ("e", ("Metodo.", "")),
    ("t", "1. Per ciascuna fonte di dati (localizzazione, DMS, connessione, percezione, dati del veicolo), censimento "
          "dei modi in cui il dato può venire meno (assente, in ritardo, bloccato sull'ultimo valore, errato ma "
          "plausibile), dei loro effetti sulle decisioni e dei criteri per riconoscerli."),
    ("t", "2. Definizione dei livelli e delle transizioni."),
    ("t", "3. Iniezione sistematica di guasti in simulazione."),
    ("t", "4. Taratura delle soglie."),
    ("e", ("Risultati misurabili.", "Specifica e implementazione dei comportamenti degradati (D1.4). Indicatori:")),
    ("p", "100% degli scenari degradati gestiti con comportamento prudente;"),
    ("p", "passaggio al livello prudente entro 200 ms dall'evento;"),
    ("p", "funzionamento in modalità degradata per meno del 5% del tempo in condizioni nominali."),

    ("s", "A1.5 Verifica formale delle regole del content policy engine"),
    ("e", ("Problema.", "Il content policy engine combina regole codificate, livelli di funzionamento degradato e una "
           "componente adattiva. Le prove su casi di esempio mostrano che il motore si comporta correttamente nei casi "
           "provati, ma non che un contenuto vietato non possa mai raggiungere il guidatore. Le regole sperimentali "
           "dell'OR dedicato all'attenzione degli occupanti (OR10) arrivano inoltre quando il motore è già in "
           "sviluppo, e vanno recepite senza introdurre conflitti.")),
    ("e", ("Soluzione proposta.", "Una verifica formale del motore completo. Le regole, i livelli degradati e i vincoli "
           "della componente adattiva sono tradotti in un modello su cui uno strumento di model checking dimostra "
           "proprietà di sicurezza. La prima è che nessuno stato raggiungibile porti un contenuto vietato su una "
           "superficie visibile dal guidatore. Quando una proprietà non è soddisfatta, lo strumento restituisce un "
           "controesempio, cioè la sequenza di situazioni che porta alla violazione, e il controesempio serve a "
           "correggere le regole. Nella stessa attività si misura il tempo di decisione sull'unità di calcolo di "
           "riferimento. La verifica su scenari simulati del sistema completo è svolta nel digital twin (A6.5).")),
    ("e", ("Novità e incertezza.", "La novità è la verifica formale di proprietà di sicurezza dei contenuti per più "
           "superfici e più occupanti, sull'insieme delle regole e sui loro cambi di stato. L'incertezza riguarda due "
           "punti:")),
    ("p", "se la verifica resti trattabile al crescere di regole, superfici e livelli di funzionamento (state space "
          "explosion);"),
    ("p", "quale astrazione della componente adattiva consenta di verificarla senza perdere le proprietà da "
          "dimostrare."),
    ("e", ("Metodo.", "")),
    ("t", "1. Formalizzazione delle proprietà di sicurezza dei contenuti."),
    ("t", "2. Traduzione di regole, livelli degradati e vincoli della componente adattiva nel modello verificabile."),
    ("t", "3. Recepimento delle regole di OR10 e nuova verifica."),
    ("t", "4. Analisi dei controesempi e correzione delle regole."),
    ("t", "5. Misura del tempo di decisione sull'unità di calcolo di riferimento."),
    ("e", ("Risultati misurabili.", "Rapporto di verifica formale delle regole (D1.5). Indicatori:")),
    ("p", "nessuno stato raggiungibile in cui il guidatore riceva un contenuto vietato;"),
    ("p", "100% delle regole di OR10 recepite e verificate;"),
    ("p", "tempo di decisione completo, comprensivo del modello del contesto e della componente adattiva, inferiore a "
          "250 ms nel 95% dei casi sull'unità di calcolo di riferimento (K7 per la sola valutazione delle regole)."),

    ("s", "A1.6 Raccomandazione personalizzata"),
    ("e", ("Problema.", "A bordo viaggiano più occupanti con interessi diversi, e il guidatore non può essere coinvolto "
           "come i passeggeri. I sistemi di raccomandazione esistenti propongono contenuti a un singolo utente, senza "
           "tenere conto dei limiti imposti dalla situazione di guida né del percorso. Per i veicoli elettrici le soste "
           "di ricarica sono un'occasione per proporre contenuti e punti di interesse, ma nei dati aperti la "
           "disponibilità delle colonnine non è nota in anticipo.")),
    ("e", ("Soluzione proposta.", "Un motore di raccomandazione per occupante, che propone contenuti, punti di "
           "interesse (POI) e soste lungo il percorso:")),
    ("p", "le raccomandazioni tengono conto del profilo dell'occupante (A1.7), della posizione, del percorso e del tempo "
          "disponibile;"),
    ("p", "ogni raccomandazione passa dal content policy engine, che ne decide l'ammissibilità e la superficie di "
          "presentazione;"),
    ("p", "le soste di ricarica sono pianificate con servizi di routing esistenti, alimentati da dati aperti sulle "
          "colonnine (Open Charge Map) e sui punti di interesse (OpenStreetMap, Overture Maps, Wikidata); la "
          "disponibilità delle colonnine è stimata dai dati statici disponibili."),
    ("e", ("Novità e incertezza.", "La novità è raccomandare insieme a più occupanti dello stesso veicolo, entro le "
           "policy sui contenuti e in funzione del percorso e delle soste. L'incertezza riguarda due punti:")),
    ("p", "come combinare le preferenze dei diversi occupanti in proposte condivise, come una sosta, senza "
          "penalizzarne nessuno;"),
    ("p", "quale accuratezza abbia la stima della disponibilità delle colonnine ricavata da dati statici."),
    ("e", ("Metodo.", "")),
    ("t", "1. Integrazione dei contenuti generati in OR2 e della piattaforma collaborativa di OR4 con i dati aperti su "
          "POI e colonnine."),
    ("t", "2. Modelli di raccomandazione per singolo occupante e per gruppo."),
    ("t", "3. Integrazione con i servizi di routing e con il content policy engine."),
    ("t", "4. Valutazione su percorsi registrati e in simulazione."),
    ("e", ("Risultati misurabili.", "Motore di raccomandazione personalizzata (D1.6). Indicatori:")),
    ("p", "100% delle raccomandazioni presentate entro i limiti decisi dal content policy engine;"),
    ("p", "stima della disponibilità delle colonnine corretta in almeno l'80% dei casi sui dati di prova."),

    ("s", "A1.7 Apprendimento a bordo dei profili degli occupanti"),
    ("e", ("Problema.", "La personalizzazione richiede profili degli occupanti, ma i dati che li alimentano (preferenze, "
           "abitudini, posizione, comportamento a bordo) sono dati personali. Trasferirli al cloud per costruire i "
           "profili espone gli occupanti a rischi per la riservatezza e richiede le basi giuridiche e le misure di "
           "protezione previste dal Regolamento (UE) 2016/679. In un veicolo condiviso, inoltre, ogni occupante deve "
           "poter dare o negare il consenso in modo indipendente.")),
    ("e", ("Soluzione proposta.", "")),
    ("p", "Profili a bordo: i profili sono costruiti e aggiornati sull'unità di calcolo del veicolo, e i dati grezzi non "
          "lasciano il veicolo."),
    ("p", "Modelli comuni: migliorano con tecniche di federated learning, che trasferiscono solo aggiornamenti "
          "aggregati dei parametri."),
    ("p", "Consenso: il consenso di ciascun occupante è gestito con strumenti esistenti di consent management. Il "
          "motore di raccomandazione (A1.6) usa un profilo solo se il relativo consenso è registrato."),
    ("e", ("Novità e incertezza.", "La novità è costruire interamente a bordo, con risorse di calcolo limitate, i "
           "profili di più occupanti dello stesso veicolo. L'incertezza riguarda due punti:")),
    ("p", "se i profili costruiti con i soli dati di bordo diano raccomandazioni di qualità comparabile a quelle dei "
          "profili costruiti in cloud;"),
    ("p", "se i profili restino separati e corretti quando cambiano gli occupanti a bordo."),
    ("e", ("Metodo.", "")),
    ("t", "1. Definizione dei dati di profilo e delle regole di consenso."),
    ("t", "2. Algoritmi di apprendimento a bordo e aggiornamento federato dei modelli comuni."),
    ("t", "3. Integrazione con gli strumenti di consent management e con il motore di raccomandazione."),
    ("t", "4. Verifica dei flussi di dati in uscita dal veicolo."),
    ("e", ("Risultati misurabili.", "Profili costruiti a bordo (D1.7). Indicatori:")),
    ("p", "nessun dato personale grezzo trasferito fuori dal veicolo, verificato sui flussi in uscita;"),
    ("p", "consenso registrato per il 100% degli occupanti profilati."),

    ("s", "Risorse umane"),
    ("t", "Un responsabile tecnico, impegnato nelle attività A1.1 e A1.3, 8 profili senior e 11 sviluppatori, con "
          "un impegno dell'83%. Il dettaglio per fascia di costo è riportato nella Tabella 3."),
])


# ---------------------------------------------------------------- riallineamento alla struttura del 20/11
# GSNet prende OR2, OR3 (ex A3.1-A3.3) e OR4 (ex A4.1-A4.3 + ex OR6, ora A4.4-A4.8); Aubay ha OR1, OR6
# (validazione virtuale) e OR14 (integrazione). I testi approvati il 19/11 si riusano task per task;
# le descrizioni degli OR cambiati restano da redigere e le chiavi superate si eliminano.
import re as _re


def _spec(chiave):
    """Lista (tipo, testo) di un contenuto costruito con _blocchi."""
    fn = CONTENUTI[chiave]
    return list(fn.__closure__[fn.__code__.co_freevars.index("spec")].cell_contents)


def _estrai(spec, codici, rinomina=None):
    """Segmenti dei task indicati (dal sottotitolo del task al successivo), con i codici rinominati."""
    rinomina = rinomina or {}
    out, dentro = [], False
    for k, v in spec:
        if k == "s":
            cod = v.split(" ", 1)[0]
            dentro = cod in codici
        if dentro:
            for vecchio, nuovo in rinomina.items():
                cv, cn = vecchio[1:], nuovo[1:]          # A6.1 -> A4.4 vale anche per D6.1 -> D4.4
                if isinstance(v, tuple):
                    v = tuple(_re.sub(r"\b([AD])%s\b" % _re.escape(cv), lambda m: m.group(1) + cn, x) for x in v)
                else:
                    v = _re.sub(r"\b([AD])%s\b" % _re.escape(cv), lambda m: m.group(1) + cn, v)
            out.append((k, v))
    return out


_or2 = _spec("II.7.1/OR2")
_or2[0] = _intestazione("Storytelling geo-temporale generativo", "GSNet", "ricerca industriale")
CONTENUTI["II.7.1/OR2"] = _blocchi(_or2)
CONTENUTI["II.7.2/OR3"] = _blocchi(_estrai(_spec("II.7.2/OR3"), {"A3.1", "A3.2", "A3.3"}))
CONTENUTI["II.7.2/OR4"] = _blocchi(
    _estrai(_spec("II.7.2/OR4"), {"A4.1", "A4.2", "A4.3"})
    + _estrai(_spec("II.7.2/OR6"), {"A6.1", "A6.2", "A6.3", "A6.4", "A6.5"},
              {"A6.1": "A4.5", "A6.2": "A4.6", "A6.3": "A4.7", "A6.4": "A4.8", "A6.5": "A4.9"}))
for _k in ("II.7.1/OR3", "II.7.1/OR4", "II.7.1/OR6", "II.7.2/OR6"):
    CONTENUTI.pop(_k, None)


# ---------------------------------------------------------------- Parti I e III
# Testi del documento ricevuto "Allegato 4 MooVXR Parti I e III" (20/11), importati senza
# modifiche con importa_parti_I_III.py nel modulo di dati parti_I_III_moovxr.py.
from docx_core import immagine

_sp = importlib.util.spec_from_file_location("parti_I_III_moovxr", QUI / "parti_I_III_moovxr.py")
_pm = importlib.util.module_from_spec(_sp)
_sp.loader.exec_module(_pm)
PARTI_I_III = _pm.BLOCCHI


def _proponente(t):
    return para(run(t, bold=True, size=22), spacing='<w:spacing w:before="240" w:after="80"/>')


def _paragrafo(rr):
    return para("".join(run(t, bold=b, italic=i) for t, b, i in rr),
                spacing='<w:spacing w:before="60" w:after="60"/>')


def _parte(chiave):
    def f():
        out = []
        for b in PARTI_I_III[chiave]:
            if b[0] == "proponente":
                out.append(_proponente(b[1]))
            elif b[0] == "sotto":
                out.append(sottotitolo(b[1]))
            elif b[0] == "punto":
                out.append(punto(b[1]))
            elif b[0] == "testo":
                out.append(_paragrafo(b[1]))
            elif b[0] == "img":
                out.append(immagine(QUI / b[1], b[2], b[3]))
            elif b[0] == "tab":
                out.append(b[1])                    # specifica di tabella, resa da build_finanziato
        return out
    return f


for _k in PARTI_I_III:
    CONTENUTI[_k] = _parte(_k)


# III.1.2: la tabella dei costi del documento ricevuto (20 M€, quote superate) si sostituisce con
# quella generata dal modello economico corrente (foglio Riepilogo) e dagli OR della configurazione.
MODELLO = QUI.parent / "Modello_Economico_MooVXR_v17.xlsx"


def _euro(v):
    return "€ " + format(round(v), ",d").replace(",", ".")


def _tabella_costi():
    import openpyxl
    ws = openpyxl.load_workbook(MODELLO, data_only=True)["Riepilogo"]
    righe, tot = [], None
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[0] == "TOTALE PROGETTO":
            tot = r[4]
            break
        righe.append((r[0], r[4], r[5]))
    assert tot and all(isinstance(c, (int, float)) for _, c, _ in righe), "modello non ricalcolato: " + str(MODELLO)
    assert {p for p, _, _ in righe} == {o[2] for o in CFG["or"]}, "proponenti del modello diversi dalla configurazione"
    assert round(sum(c for _, c, _ in righe), 2) == round(tot, 2)
    W = [2002, 1719, 857, 4948]
    testa = [{"t": t, "b": True} for t in ("Proponente", "Costo a carico", "Quota", "Obiettivi realizzativi di competenza")]
    corpo = []
    for p, c, q in righe:
        ors = ", ".join(o[0] for o in CFG["or"] if o[2] == p)
        corpo.append([{"t": p}, {"t": _euro(c), "al": "right"},
                      {"t": ("%.2f%%" % (q * 100)).replace(".", ","), "al": "right"}, {"t": ors}])
    corpo.append([{"t": "Totale", "b": True}, {"t": _euro(tot), "al": "right", "b": True},
                  {"t": "100,00%", "al": "right", "b": True}, {"t": ""}])
    return {"larghezze": W, "righe": [testa] + corpo, "testa": 1}


PARTI_I_III["III.1.2"] = [("tab", _tabella_costi()) if b[0] == "tab" else b for b in PARTI_I_III["III.1.2"]]
assert sum(1 for b in PARTI_I_III["III.1.2"] if b[0] == "tab") == 1


# Correzioni confermate il 23/11 ai testi importati: costo e quota del Politecnico letti dal modello.
def _quota_proponente(nome):
    import openpyxl
    ws = openpyxl.load_workbook(MODELLO, data_only=True)["Riepilogo"]
    righe = {r[0]: r for r in ws.iter_rows(min_row=2, values_only=True) if r[0]}
    return righe[nome][4], righe[nome][5], righe["TOTALE PROGETTO"][4]


def _sostituisci(chiave, vecchio, nuovo):
    n = 0
    for b in PARTI_I_III[chiave]:
        if b[0] == "testo":
            for j, (t, bo, it) in enumerate(b[1]):
                if vecchio in t:
                    b[1][j] = (t.replace(vecchio, nuovo), bo, it)
                    n += 1
    assert n == 1, (chiave, vecchio, n)


_c, _q, _t = _quota_proponente("Politecnico di Milano")
_qs = ("%.2f%%" % (_q * 100)).replace(".", ",")
_sostituisci("III.1.2", "Sostiene € 3.000.000 sul costo complessivo di € 20.000.000, pari al 15,00%",
             "Sostiene %s sul costo complessivo di %s, pari al %s" % (_euro(_c), _euro(_t), _qs))
_sostituisci("III.1.1", "spettante all’Ateneo è di € 3.000.000, pari al 15% del totale",
             "spettante all’Ateneo è di %s, pari al %s del totale" % (_euro(_c), _qs))


# Correzione confermata il 23/11: la tabella dei profili di GSNet in III.1.1 non riporta i nomi del
# personale; la prima colonna indica se la risorsa è in organico o da individuare.
_tab_gsnet = [b for b in PARTI_I_III["III.1.1"] if b[0] == "tab" and b[1]["righe"][0][0]["t"] == "Risorsa"]
assert len(_tab_gsnet) == 1
_righe = _tab_gsnet[0][1]["righe"]
_righe[0][0]["t"] = "Disponibilità"
for _r in _righe[1:]:
    if _r[0]["t"] != "Da individuare":
        _r[0]["t"] = "In organico"


# ---------------------------------------------------------------- OR6 e OR14 (Aubay), testi in forma Frascati (23/11)
# I sottotitoli delle attività (codice, titolo, mesi) si generano dalla configurazione del modello.
def _sotto_task(cod):
    a = next(x for x in CFG["attivita"] if x[1] == cod)
    return ("s", "%s %s (mesi %d-%d)" % (cod, a[2], a[3], a[4]))


CONTENUTI["II.7.1/OR6"] = _blocchi([
    _intestazione("Validazione virtuale del sistema di bordo (digital twin)", "Aubay Italia", "ricerca industriale",
                  "Roma (Lazio)"),
    ("t", "L'obiettivo realizzativo sviluppa un digital twin del sistema di bordo, cioè un modello eseguibile del "
          "veicolo, del percorso, degli occupanti, delle superfici di visualizzazione, dei sensori e della "
          "connettività. Il digital twin serve a verificare in simulazione il comportamento del content policy "
          "engine, della percezione della scena e dell'HMI prima delle prove su strada."),
    ("t", "Gli strumenti di simulazione disponibili sono nati per lo sviluppo di ADAS e della guida autonoma: CARLA "
          "simula veicolo, scena e sensori, SUMO il traffico, esmini esegue scenari descritti nello standard ASAM "
          "OpenSCENARIO, ns-3 le reti di comunicazione. Nessuno modella gli occupanti, le superfici di "
          "visualizzazione multiple o la consegna dei contenuti. Non esiste inoltre un metodo consolidato per "
          "misurare lo scarto fra indicatori simulati e misurati su strada per l'esperienza a bordo."),
    ("t", "L'obiettivo produce tre risultati:"),
    ("p", "un ambiente di co-simulazione che collega scena, traffico, rete, occupanti e superfici su una base "
          "temporale comune;"),
    ("p", "modelli validati sui dati reali, con lo scarto rispetto alle prove misurato per ciascun indicatore;"),
    ("p", "una campagna di verifica virtuale su scenari parametrici, compresi i casi rari difficili da riprodurre su "
          "strada."),
    ("t", "I risultati sono usati dal content policy engine (OR1) per verificare le policy sugli scenari e "
          "dall'integrazione di sistema (OR14) per concentrare le prove su strada sui casi non verificabili in "
          "simulazione."),
    ("t", "Le attività sono ricerca industriale ai sensi dell'art. 1, lett. o), del DD: acquisiscono nuove "
          "conoscenze tramite interfacce di simulazione e dati registrati in altri obiettivi realizzativi, senza "
          "realizzazione in condizioni operative reali."),
])

_OR6 = [
    _sotto_task("A6.1"),
    ("e", ("Problema.", "Il digital twin riceve modelli e dati da quattro obiettivi realizzativi:")),
    ("p", "il modello del contesto e le policy (OR1);"),
    ("p", "la localizzazione (OR9);"),
    ("p", "le linee guida sull'attenzione degli occupanti (OR10);"),
    ("p", "la percezione della scena (OR12)."),
    ("t", "Questi arrivano con formati, frequenze e granularità diversi. Nessun simulatore disponibile copre insieme "
          "scena, traffico, rete, occupanti e superfici. Combinare più simulatori introduce errori di "
          "sincronizzazione che, alle scale di tempo dell'HMI, possono falsare gli indicatori."),
    ("e", ("Soluzione proposta.", "Un'architettura di co-simulazione in cui i simulatori di scena, traffico e rete e "
           "i modelli di occupanti e superfici avanzano su una base temporale comune, con interfacce definite per lo "
           "scambio dei dati. Gli scenari sono descritti in ASAM OpenSCENARIO, così gli stessi casi si eseguono in "
           "simulazione e si riproducono su strada. La specifica fissa, per ciascun indicatore richiesto dai "
           "partner, le grandezze da simulare e la loro accuratezza.")),
    ("e", ("Novità e incertezza.", "La novità è l'integrazione in un unico ambiente dei domini della guida e "
           "dell'esperienza degli occupanti, finora simulati separatamente. L'incertezza riguarda due punti:")),
    ("p", "se la sincronizzazione fra simulatori eterogenei raggiunga l'accuratezza richiesta dagli indicatori di HMI;"),
    ("p", "se il costo di calcolo consenta campagne con migliaia di varianti di scenario."),
    ("e", ("Metodo.", "")),
    ("t", "1. Raccolta dei requisiti dei partner che usano il digital twin e degli indicatori da calcolare."),
    ("t", "2. Confronto degli strumenti di simulazione disponibili e scelta dell'architettura."),
    ("t", "3. Prototipo di co-simulazione su uno scenario di riferimento."),
    ("t", "4. Misura della deriva di sincronizzazione e del costo di calcolo."),
    ("t", "5. Specifica del digital twin."),
    ("e", ("Risultati misurabili.", "Specifica del digital twin (D6.1). Indicatori:")),
    ("p", "100% degli indicatori richiesti da OR1, OR10 e OR12 associati a grandezze simulate;"),
    ("p", "deriva di sincronizzazione fra simulatori non superiore a 10 ms sullo scenario di riferimento."),
]
CONTENUTI["II.7.2/OR6"] = _blocchi(_OR6)

_OR6 += [
    _sotto_task("A6.2"),
    ("e", ("Problema.", "I simulatori disponibili offrono modelli di camere nel visibile e di LiDAR generici. Il kit "
           "di percezione del progetto (OR12) combina visibile, infrarosso, termico e LiDAR. Le sue prestazioni "
           "dipendono da illuminazione, condizioni meteo e temperatura delle superfici, che i modelli generici non "
           "rappresentano. Anche la connettività incide sull'esperienza a bordo: perdite e ritardi della rete lungo "
           "il percorso determinano se un contenuto arriva prima del punto di fruizione.")),
    ("e", ("Soluzione proposta.", "")),
    ("p", "Sensori: modelli dei sensori multispettrali tarati sui dati di caratterizzazione dei sensori di sviluppo "
          "forniti da OR12, che riproducono rumore, risoluzione e degrado per condizione ambientale."),
    ("p", "Connettività: un modello del canale basato su ns-3, alimentato dai profili di copertura misurati lungo i "
          "percorsi di prova."),
    ("p", "Scene: ricostruite dai dati di localizzazione (OR9) e dai percorsi registrati in A12.5."),
    ("e", ("Novità e incertezza.", "La novità è simulare sulla stessa scena i sensori termici e infrarossi insieme "
           "alla consegna dei contenuti. L'incertezza riguarda due punti:")),
    ("p", "quale fedeltà sia raggiungibile, in condizioni di scarsa visibilità, per le classi di oggetti a cui si "
          "agganciano i contenuti, come edifici, monumenti e segnaletica;"),
    ("p", "se i profili di copertura misurati rappresentino la variabilità della rete nel tempo."),
    ("e", ("Metodo.", "")),
    ("t", "1. Raccolta dei dati di caratterizzazione dei sensori e dei profili di copertura."),
    ("t", "2. Sviluppo dei modelli dei sensori e del canale."),
    ("t", "3. Ricostruzione delle scene dei percorsi registrati."),
    ("t", "4. Confronto fra rilevazioni simulate e registrate, per classe di oggetto e condizione ambientale."),
    ("e", ("Risultati misurabili.", "Modelli di scena, sensori e connettività eseguibili nell'ambiente di "
           "simulazione (D6.2). Indicatori:")),
    ("p", "scarto di recall fra rilevazioni simulate e registrate non superiore a 10 punti percentuali sui percorsi "
          "di A12.5, per ciascuna classe di oggetto;"),
    ("p", "tutte e quattro le modalità del kit di percezione modellate: visibile, infrarosso, termico e LiDAR."),
]
CONTENUTI["II.7.2/OR6"] = _blocchi(_OR6)

_OR6 += [
    _sotto_task("A6.3"),
    ("e", ("Problema.", "Per valutare l'HMI in simulazione occorre sapere cosa vede ciascun occupante, dove e quando. I "
           "simulatori disponibili rappresentano il veicolo come un corpo con sensori, senza occupanti né superfici di "
           "visualizzazione. Il progetto usa superfici con geometrie e luminanze diverse:")),
    ("p", "l'HUD di serie del guidatore;"),
    ("p", "l'HUD del passeggero a proiezione sul finestrino (OR11);"),
    ("p", "gli occhiali AR (OR5)."),
    ("t", "Che un contenuto destinato al passeggero non sia visibile dal posto di guida è un requisito di sicurezza "
          "(K4)."),
    ("e", ("Soluzione proposta.", "")),
    ("p", "Occupanti: modelli parametrici con posizione, direzione dello sguardo e stato di attenzione, derivati dai "
          "dati e dalle linee guida dell'obiettivo sull'attenzione degli occupanti (OR10)."),
    ("p", "Superfici: modelli geometrici e fotometrici che calcolano, per ciascun occupante, l'area visibile e la "
          "luminanza percepita di ogni contenuto, compresa la visibilità residua dell'HUD del passeggero dal posto di "
          "guida."),
    ("e", ("Novità e incertezza.", "La novità è rappresentare in simulazione più occupanti e più superfici, calcolando "
           "cosa vede ciascuno. L'incertezza riguarda due punti:")),
    ("p", "se i modelli di sguardo e attenzione, derivati da prove controllate, rappresentino il comportamento in marcia;"),
    ("p", "quale accuratezza fotometrica sia raggiungibile per la proiezione sul finestrino al variare della luce esterna."),
    ("e", ("Metodo.", "")),
    ("t", "1. Definizione dei parametri degli occupanti con OR10."),
    ("t", "2. Acquisizione delle geometrie e delle caratteristiche ottiche delle superfici da OR5 e OR11."),
    ("t", "3. Sviluppo dei modelli e integrazione nella co-simulazione."),
    ("t", "4. Confronto della visibilità stimata con le misure su banco di OR11."),
    ("e", ("Risultati misurabili.", "Modelli di occupanti e superfici eseguibili nell'ambiente di simulazione (D6.3). "
           "Indicatori:")),
    ("p", "errore della visibilità stimata dal posto di guida non superiore al 15% rispetto alle misure su banco di OR11;"),
    ("p", "tutte le superfici del progetto modellate: HUD del guidatore, HUD del passeggero e occhiali AR."),
]
CONTENUTI["II.7.2/OR6"] = _blocchi(_OR6)

_OR6 += [
    _sotto_task("A6.4"),
    ("e", ("Problema.", "Un digital twin è utile solo se lo scarto fra ciò che simula e ciò che accade su strada è noto. "
           "Per gli indicatori del progetto (percezione della scena, consegna dei contenuti, attenzione degli "
           "occupanti) non esistono metriche consolidate di confronto fra simulazione e prova reale. I dati reali "
           "arrivano in due momenti: i percorsi registrati con i sensori di sviluppo (A12.5) entro il mese 18 e le "
           "registrazioni del dimostratore (OR14) dal mese 26.")),
    ("e", ("Soluzione proposta.", "Una validazione in due tempi sugli stessi percorsi:")),
    ("p", "prima sui percorsi registrati da nLight con i sensori di sviluppo;"),
    ("p", "poi sulle registrazioni sincronizzate del dimostratore."),
    ("t", "Per ogni percorso il digital twin riproduce le condizioni registrate (traiettoria, illuminazione, meteo, "
          "copertura di rete), calcola gli indicatori e li confronta con quelli misurati. Lo scarto è scomposto per "
          "modello (scena, sensori, rete, occupanti), per capire dove intervenire nella calibrazione."),
    ("e", ("Novità e incertezza.", "La novità è un protocollo che misura lo scarto fra simulazione e realtà sugli "
           "indicatori dell'esperienza a bordo, cioè la consegna dei contenuti e l'attenzione degli occupanti, oltre "
           "che sulla percezione della scena. L'incertezza riguarda due punti:")),
    ("p", "se la calibrazione dei modelli basti a riportare lo scarto entro il valore obiettivo, o se servano modelli "
          "di fedeltà superiore;"),
    ("p", "se la validazione resti valida nelle condizioni non coperte dalle registrazioni."),
    ("e", ("Metodo.", "")),
    ("t", "1. Definizione delle metriche di confronto per ciascun indicatore."),
    ("t", "2. Riproduzione nel digital twin dei percorsi registrati in A12.5 e calcolo dello scarto."),
    ("t", "3. Calibrazione dei modelli."),
    ("t", "4. Ripetizione del confronto sulle registrazioni del dimostratore."),
    ("t", "5. Rapporto di validazione con lo scarto residuo per indicatore e per condizione."),
    ("e", ("Risultati misurabili.", "Rapporto di validazione del digital twin (D6.4). Indicatori:")),
    ("p", "scarto fra indicatori simulati e misurati sugli stessi percorsi non superiore al 10% (K6);"),
    ("p", "scarto riportato separatamente per percezione, consegna dei contenuti e attenzione degli occupanti."),
]
CONTENUTI["II.7.2/OR6"] = _blocchi(_OR6)

_OR6 += [
    _sotto_task("A6.5"),
    ("e", ("Problema.", "Le prove su strada sono costose e poco ripetibili, e non possono riprodurre in sicurezza i casi "
           "rari. Esempi sono l'ingresso in galleria con perdita del segnale, un evento improvviso mentre un occupante "
           "fruisce di un contenuto, o traffico intenso con scarsa visibilità. Sono proprio questi i casi in cui il "
           "content policy engine, la percezione della scena e l'HMI devono dimostrare un comportamento corretto.")),
    ("e", ("Soluzione proposta.", "Una campagna sistematica di scenari parametrici nel digital twin validato. Da "
           "ciascuno scenario di riferimento si generano varianti combinando traffico, illuminazione, meteo, copertura "
           "di rete, occupanti e contenuti in fruizione. Per ogni variante si verifica che:")),
    ("p", "il guidatore non riceva contenuti vietati dalle policy (OR1);"),
    ("p", "la percezione mantenga gli oggetti di interesse entro i valori obiettivo di OR12;"),
    ("p", "i contenuti destinati al passeggero restino non visibili dal posto di guida."),
    ("t", "Gli scenari sono eseguiti su servizi cloud GPU a consumo. La campagna è distinta da altre due verifiche:"),
    ("p", "la verifica formale delle regole (A1.5), che lavora sul modello delle regole;"),
    ("p", "la verifica sperimentale con partecipanti (A10.5), che usa gli scenari del digital twin sulla postazione di "
          "guida simulata."),
    ("e", ("Novità e incertezza.", "La novità è verificare insieme policy, percezione e HMI su più superfici, sullo "
           "stesso insieme di scenari. L'incertezza riguarda due punti:")),
    ("p", "quale copertura dei casi critici sia raggiungibile con il calcolo disponibile;"),
    ("p", "come scegliere le varianti più informative senza doverle eseguire tutte."),
    ("e", ("Metodo.", "")),
    ("t", "1. Definizione con i partner degli scenari critici e dei criteri di esito."),
    ("t", "2. Generazione delle varianti parametriche."),
    ("t", "3. Esecuzione su servizi cloud GPU."),
    ("t", "4. Analisi delle violazioni e restituzione ai partner per la correzione."),
    ("t", "5. Selezione dei casi da confermare su strada nell'integrazione di sistema (OR14)."),
    ("e", ("Risultati misurabili.", "Rapporto delle verifiche virtuali (D6.5). Indicatori:")),
    ("p", "100% degli scenari critici concordati con i partner eseguiti;"),
    ("p", "nessuna violazione residua delle policy al termine della campagna;"),
    ("p", "almeno 1.000 varianti di scenario eseguite."),
]
CONTENUTI["II.7.2/OR6"] = _blocchi(_OR6)


CONTENUTI["II.7.1/OR14"] = _blocchi([
    _intestazione("Integrazione di sistema, sicurezza e dimostratore su veicolo", "Aubay Italia",
                  "sviluppo sperimentale", "Roma (Lazio)"),
    ("t", "L'obiettivo realizzativo integra in un dimostratore su veicolo i componenti sviluppati da tutti i partner:"),
    ("p", "il content policy engine e la personalizzazione (OR1);"),
    ("p", "i contenuti generativi e la piattaforma di erogazione (OR2, OR3);"),
    ("p", "le esperienze AR e XR e gli occhiali per i passeggeri (OR4, OR5);"),
    ("p", "i dati esterni e la piattaforma IoT (OR7, OR8);"),
    ("p", "la localizzazione, l'attenzione degli occupanti e l'HUD del passeggero (OR9, OR10, OR11);"),
    ("p", "il kit di percezione (OR12, OR13)."),
    ("t", "Il dimostratore è installato sul veicolo di prova di OR4 e verificato su strada."),
    ("t", "Quando un sistema di bordo coinvolge più fornitori, i componenti nascono con interfacce, cicli di rilascio e "
          "livelli di maturità diversi. Il Regolamento UNECE n. 155 richiede, per i veicoli omologati, un sistema di "
          "gestione della cybersecurity, e la norma ISO/SAE 21434 ne definisce il processo di ingegneria. I modelli AI "
          "in esercizio a bordo richiedono inoltre criteri di rilascio, monitoraggio e ritorno alla versione "
          "precedente, adattati ai vincoli dei dispositivi del veicolo: connettività intermittente, risorse di calcolo "
          "limitate, aggiornamento tramite OTA."),
    ("t", "L'obiettivo produce quattro risultati:"),
    ("p", "l'architettura di sistema e la matrice delle interfacce approvate dai partner;"),
    ("p", "l'analisi dei rischi di sicurezza informatica e le misure di protezione dei contenuti, verificate da "
          "penetration test indipendenti;"),
    ("p", "un servizio di gestione dei modelli AI in esercizio, con distribuzione tramite la piattaforma OTA (OR8);"),
    ("p", "il dimostratore integrato, verificato con prove di carico e prove su strada."),
    ("t", "Le attività sono sviluppo sperimentale ai sensi dell'art. 1 del DD: comprendono la realizzazione di un "
          "prototipo, la dimostrazione, il test e la convalida in un ambiente che riproduce le condizioni operative "
          "reali."),
])

_OR14 = [
    _sotto_task("A14.1"),
    ("e", ("Problema.", "I componenti del dimostratore sono sviluppati da cinque soggetti in tredici obiettivi "
           "realizzativi, con tecnologie, formati dei dati e cicli di rilascio diversi. Senza un'architettura comune e "
           "interfacce specificate prima dell'integrazione, le incompatibilità emergono solo sul veicolo, quando "
           "correggerle costa di più. La tracciabilità fra requisiti, interfacce e prove, che serve anche all'analisi "
           "dei rischi di sicurezza, si disperde fra i documenti dei partner.")),
    ("e", ("Soluzione proposta.", "")),
    ("p", "Architettura: un'architettura di sistema che assegna le funzioni ai componenti e ai dispositivi di bordo e "
          "di terra."),
    ("p", "Interfacce: una matrice che, per ciascun flusso, fissa formato, frequenza, latenza ammessa e responsabile."),
    ("p", "Base di conoscenza tecnica: costruita su una soluzione Wiki-RAG che collega requisiti, specifiche di "
          "interfaccia, configurazioni ed evidenze di prova, e che i team dei partner interrogano in linguaggio "
          "naturale."),
    ("e", ("Novità e incertezza.", "La novità è usare una base di conoscenza interrogabile come strumento di "
           "integrazione, che tiene allineati requisiti, interfacce e prove mentre i componenti evolvono. "
           "L'incertezza riguarda due punti:")),
    ("p", "se le interfacce specificate a metà progetto reggano l'evoluzione dei componenti di ricerca industriale "
          "senza revisioni sostanziali;"),
    ("p", "se la base di conoscenza resti affidabile al crescere dei documenti, cioè restituisca sempre la versione "
          "corretta di una specifica."),
    ("e", ("Metodo.", "")),
    ("t", "1. Raccolta delle funzioni e dei vincoli dei componenti dei partner."),
    ("t", "2. Definizione dell'architettura e allocazione delle funzioni."),
    ("t", "3. Specifica delle interfacce e revisione con i partner."),
    ("t", "4. Configurazione della base di conoscenza tecnica e caricamento di requisiti e specifiche."),
    ("t", "5. Approvazione della matrice delle interfacce."),
    ("e", ("Risultati misurabili.", "Architettura di sistema e matrice delle interfacce (D14.1). Indicatori:")),
    ("p", "100% delle interfacce specificate e approvate da tutti i partner;"),
    ("p", "100% dei requisiti del dimostratore tracciati verso almeno una prova."),
]
CONTENUTI["II.7.2/OR14"] = _blocchi(_OR14)

_OR14 += [
    _sotto_task("A14.2"),
    ("e", ("Problema.", "Il dimostratore collega al veicolo componenti di cinque soggetti, servizi cloud, la piattaforma "
           "OTA e dispositivi personali come gli occhiali AR. Ogni interfaccia è un possibile punto di attacco:")),
    ("p", "un contenuto manipolato potrebbe raggiungere il guidatore aggirando le policy;"),
    ("p", "un aggiornamento non autorizzato potrebbe alterare il software di bordo;"),
    ("p", "i dati degli occupanti potrebbero essere esposti."),
    ("t", "L'analisi dei rischi dei singoli componenti non copre gli scenari che nascono dalla loro combinazione."),
    ("e", ("Soluzione proposta.", "Un'analisi dei rischi del sistema completo (TARA, threat analysis and risk "
           "assessment) secondo la ISO/SAE 21434, condotta sull'architettura e sulla matrice delle interfacce di "
           "A14.1. Ne derivano misure di protezione per i flussi critici:")),
    ("p", "autenticazione e integrità dei contenuti lungo tutta la catena, dalla piattaforma di erogazione alle "
          "superfici di visualizzazione;"),
    ("p", "garanzia che nessun contenuto raggiunga una superficie visibile dal guidatore senza la decisione del "
          "content policy engine;"),
    ("p", "protezione degli aggiornamenti distribuiti tramite OTA e dei dati degli occupanti."),
    ("t", "Le misure sono verificate da un penetration test indipendente dell'applicazione e del flusso dei contenuti. "
          "Un assessment esterno ne verifica l'allineamento ai requisiti del Regolamento UNECE n. 155 e della ISO/SAE "
          "21434."),
    ("e", ("Novità e incertezza.", "La novità è estendere l'analisi dei rischi al flusso dei contenuti generati e "
           "personalizzati, che entra nel veicolo da fonti esterne e da più fornitori. L'incertezza riguarda due "
           "punti:")),
    ("p", "se le misure di protezione rispettino i vincoli di latenza della consegna dei contenuti;"),
    ("p", "se restino efficaci quando i componenti dei partner vengono aggiornati in modo indipendente."),
    ("e", ("Metodo.", "")),
    ("t", "1. Identificazione dei beni da proteggere e degli scenari di minaccia sull'architettura di A14.1."),
    ("t", "2. Valutazione dei rischi e definizione degli obiettivi di sicurezza."),
    ("t", "3. Progetto e realizzazione delle misure di protezione con i partner."),
    ("t", "4. Penetration test indipendente e assessment esterno."),
    ("t", "5. Correzione delle vulnerabilità e nuova verifica."),
    ("e", ("Risultati misurabili.", "Analisi dei rischi e misure di protezione dei contenuti (D14.2). Indicatori:")),
    ("p", "analisi dei rischi estesa al 100% delle interfacce della matrice di A14.1;"),
    ("p", "nessuna vulnerabilità critica o alta aperta a fine progetto."),
]
CONTENUTI["II.7.2/OR14"] = _blocchi(_OR14)

_OR14 += [
    _sotto_task("A14.3"),
    ("e", ("Problema.", "Il dimostratore esegue a bordo modelli AI di più partner: il modello del contesto, la componente "
           "adattiva e i profili degli occupanti (OR1), e i modelli di percezione della scena (OR12). I modelli "
           "cambiano nel corso del progetto e possono degradare quando i dati in esercizio si discostano da quelli di "
           "addestramento, per esempio per stagione, percorso o tipo di occupanti. Un modello aggiornato può anche "
           "comportarsi in modo diverso da quello verificato rispetto alle policy. Il veicolo ha connettività "
           "intermittente e risorse di calcolo limitate, quindi rilascio e controllo non possono dipendere da un "
           "collegamento continuo al cloud.")),
    ("e", ("Soluzione proposta.", "Un servizio di gestione del ciclo di vita dei modelli in esercizio, integrato con la "
           "piattaforma OTA di OR8:")),
    ("p", "criteri di rilascio: un modello è distribuito solo dopo aver superato le verifiche sugli scenari del digital "
          "twin (OR6) e la verifica di coerenza con le policy;"),
    ("p", "rilascio graduale: il modello entra sul veicolo per gradi, con ritorno automatico alla versione precedente "
          "quando gli indicatori in esercizio superano le soglie;"),
    ("p", "monitoraggio a bordo: drift dei dati e delle prestazioni, con invio di soli indicatori sintetici, non di dati "
          "personali."),
    ("t", "La distribuzione avviene con la piattaforma OTA di OR8; questa attività ne definisce i criteri e i controlli "
          "applicati ai modelli."),
    ("e", ("Novità e incertezza.", "La novità è un ciclo di vita dei modelli in cui rilascio e ritorno alla versione "
           "precedente dipendono dalla coerenza con le policy sui contenuti, oltre che dall'accuratezza. L'incertezza "
           "riguarda due punti:")),
    ("p", "quali indicatori calcolabili a bordo rilevino il drift con anticipo sufficiente, senza falsi allarmi frequenti;"),
    ("p", "se il ritorno alla versione precedente sia rapido e sicuro anche con connettività intermittente."),
    ("e", ("Metodo.", "")),
    ("t", "1. Censimento dei modelli in esercizio e dei relativi indicatori."),
    ("t", "2. Definizione dei criteri di rilascio con i partner che sviluppano i modelli."),
    ("t", "3. Realizzazione del servizio e integrazione con la piattaforma OTA."),
    ("t", "4. Prove di rilascio, di drift simulato e di ritorno alla versione precedente sul veicolo di prova."),
    ("e", ("Risultati misurabili.", "Servizio di gestione del ciclo di vita dei modelli (D14.3). Indicatori:")),
    ("p", "ritorno alla versione precedente verificato sul veicolo in non più di 15 minuti;"),
    ("p", "100% dei modelli in esercizio rilasciati secondo i criteri e monitorati."),
]
CONTENUTI["II.7.2/OR14"] = _blocchi(_OR14)

_OR14 += [
    _sotto_task("A14.4"),
    ("e", ("Problema.", "Componenti verificati separatamente, in laboratorio o in simulazione, possono non funzionare "
           "insieme sul veicolo. Le latenze si sommano lungo la catena che va dalla percezione alla visualizzazione, i "
           "componenti si contendono le risorse di calcolo di bordo, e il servizio perde continuità quando cala la "
           "connettività. I servizi di terra devono poi reggere il carico di una flotta, non di un solo veicolo. Le "
           "prove su strada aperta, infine, richiedono un protocollo che ne garantisca sicurezza e ripetibilità.")),
    ("e", ("Soluzione proposta.", "")),
    ("p", "Integrazione: i componenti si installano per gradi sul veicolo di prova di OR4, insieme al kit di percezione "
          "di OR13, secondo la matrice delle interfacce di A14.1 e con verifiche a ogni passo."),
    ("p", "Misure: un sistema di acquisizione dati sincronizzata, a noleggio, registra su una base temporale comune "
          "segnali del veicolo, sensori, decisioni del content policy engine e contenuti visualizzati. Le registrazioni "
          "alimentano anche la validazione del digital twin (A6.4)."),
    ("p", "Prove di carico: i servizi di terra sono sollecitati, su infrastruttura cloud a consumo, con il traffico "
          "simulato di una flotta di veicoli."),
    ("p", "Protocollo di prova: percorsi, condizioni, criteri di interruzione e cautele per le prove su strada aperta, "
          "come la presenza di un operatore di prova a bordo e la scelta di percorsi e fasce orarie a basso traffico."),
    ("e", ("Novità e incertezza.", "La novità è misurare latenza e continuità sull'intera catena, dall'evento nella "
           "scena alla presentazione del contenuto, con il veicolo in movimento. L'incertezza riguarda due punti:")),
    ("p", "se la latenza complessiva resti entro il valore obiettivo quando tutti i componenti condividono le risorse di "
          "bordo;"),
    ("p", "se la continuità dei contenuti regga nelle zone con copertura di rete scarsa."),
    ("e", ("Metodo.", "")),
    ("t", "1. Piano di integrazione e ordine di installazione dei componenti."),
    ("t", "2. Integrazione progressiva sul veicolo, con verifiche di interfaccia."),
    ("t", "3. Prove di carico dei servizi di terra."),
    ("t", "4. Misura di latenza e continuità sui percorsi di prova."),
    ("t", "5. Redazione del protocollo per le prove su strada."),
    ("e", ("Risultati misurabili.", "Dimostratore integrato e rapporto delle prove di carico (D14.4). Indicatori:")),
    ("p", "latenza end-to-end di consegna, dall'evento nella scena alla presentazione o rimozione del contenuto, non "
          "superiore a 500 ms; l'allineamento dei contenuti AR è gestito localmente dai dispositivi ed è misurato da K3;"),
    ("p", "almeno il 95% dei contenuti disponibili nel momento utile sui percorsi di prova (K2)."),
]
CONTENUTI["II.7.2/OR14"] = _blocchi(_OR14)

_OR14 += [
    _sotto_task("A14.5"),
    ("e", ("Problema.", "I valori obiettivo del progetto sono stati misurati finora in laboratorio, in simulazione o su "
           "dati registrati. Solo le prove su strada mostrano il comportamento del sistema completo nelle condizioni "
           "operative reali: traffico, luce variabile, occupanti che non conoscono il sistema, connettività reale. Le "
           "prove devono essere sicure, ripetibili e confrontabili con i risultati del digital twin.")),
    ("e", ("Soluzione proposta.", "Campagne di prova su strada, con occupanti a bordo, secondo il protocollo di A14.4 e "
           "sui percorsi e nelle condizioni definiti con i partner. Si concentrano sui casi non verificabili in "
           "simulazione, selezionati in A6.5. Per ciascun valore obiettivo il rapporto di sperimentazione riporta:")),
    ("p", "il valore misurato e il confronto con il riferimento di partenza;"),
    ("p", "le condizioni di misura: percorso, luce, meteo, copertura di rete;"),
    ("p", "lo scarto rispetto al valore previsto dal digital twin sugli stessi percorsi."),
    ("e", ("Novità e incertezza.", "La novità è verificare su strada, con lo stesso veicolo e sugli stessi percorsi, "
           "indicatori di sicurezza, di esperienza degli occupanti e di fedeltà del digital twin. L'incertezza riguarda "
           "due punti:")),
    ("p", "se i valori obiettivo raggiunti in laboratorio e in simulazione si confermino nelle condizioni reali;"),
    ("p", "se la variabilità delle condizioni su strada consenta misure ripetibili con il numero di prove previsto."),
    ("e", ("Metodo.", "")),
    ("t", "1. Definizione dei percorsi e del piano delle prove."),
    ("t", "2. Esecuzione delle campagne con acquisizione sincronizzata."),
    ("t", "3. Elaborazione dei dati e confronto con il digital twin."),
    ("t", "4. Rapporto di sperimentazione."),
    ("e", ("Risultati misurabili.", "Rapporto di sperimentazione (D14.5). Indicatori:")),
    ("p", "K1, K3, K4 e K6 misurati sui percorsi di prova;"),
    ("p", "valori obiettivo degli OR verificati su strada, come previsto dal criterio di accettazione di D14.5."),
]
CONTENUTI["II.7.2/OR14"] = _blocchi(_OR14)


# ---------------------------------------------------------------- OR7 e OR8 (Anitia), testi della rev1 (23/11)
# Testi del documento di revisione di Anitia (MooVXR_Anitia_revisione_rev1.docx), estratti con
# importa_testi_partner.py in testi_anitia_moovxr.py, con le correzioni ai riferimenti confermate il 23/11.
_sp = importlib.util.spec_from_file_location("testi_anitia_moovxr", QUI / "testi_anitia_moovxr.py")
_ma = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_ma)
TESTI_ANITIA = _ma.TESTI_ANITIA


def _correggi(testi, vecchio, nuovo):
    """Sostituisce un passaggio che deve comparire una sola volta nei testi di un partner."""
    n = 0
    for o in testi.values():
        for sez in o.values():
            for i, (k, v) in enumerate(sez):
                if isinstance(v, tuple):
                    if vecchio in v[1]:
                        sez[i] = (k, (v[0], v[1].replace(vecchio, nuovo))); n += 1
                elif vecchio in v:
                    sez[i] = (k, v.replace(vecchio, nuovo)); n += 1
    assert n == 1, (vecchio, n)


for _v, _n in [
    ("sono trattati nei servizi di contenuto di OR4 (Aubay)",
     "sono trattati nella raccomandazione personalizzata di Aubay (A1.6)"),
    ("Il dimostratore integrato è disponibile solo dal mese 24. Per questo le prove si svolgono sul veicolo di prova "
     "di OR5 (GSNet)",
     "Il dimostratore integrato è disponibile solo dal mese 25 (A14.4). Per questo le prove si svolgono sul veicolo di "
     "prova messo a disposizione da GSNet (OR4)"),
    ("confluisce nelle prove di A3.7.", "confluisce nelle prove su strada di A14.5."),
    ("Aubay quella di applicazione e contenuti (A3.4).", "Aubay quella di applicazione e contenuti (A14.2)."),
    ("Le centraline di serie sono escluse.",
     "Le centraline di serie sono escluse. Il servizio distribuisce anche i modelli AI dei partner, secondo i criteri "
     "di rilascio e di ritorno alla versione precedente definiti in A14.3."),
    ("Le prove di carico della piattaforma di erogazione dei contenuti restano in A3.5 (Aubay), con cui si concordano "
     "profili di flotta comuni.",
     "Le prove di carico del sistema completo si svolgono nell'integrazione del dimostratore (A14.4, Aubay), con cui si "
     "concordano profili di flotta comuni."),
]:
    _correggi(TESTI_ANITIA, _v, _n)

for _o in ("OR7", "OR8"):
    CONTENUTI["II.7.1/%s" % _o] = _blocchi(TESTI_ANITIA[_o]["7.1"])
    CONTENUTI["II.7.2/%s" % _o] = _blocchi(TESTI_ANITIA[_o]["7.2"])


# ---------------------------------------------------------------- OR12 (nLight), forma Frascati dal testo di revisione (23/11)
# Testi riscritti dalla revisione di nLight (MooVXR_nLight_revisione.docx) con le correzioni delle note di
# integrazione; valori obiettivo proposti da Aubay, da condividere con nLight; limite del laser da confermare.
CONTENUTI["II.7.1/OR12"] = _blocchi([
    _intestazione("Percezione della scena multispettrale e LiDAR, tracking dei punti di interesse", "nLight",
                  "ricerca industriale", "Torino, via G. Schiaparelli 14 (Piemonte)"),
    ("t", "L'obiettivo realizzativo riguarda i metodi per rilevare e seguire, nella scena attorno al veicolo, i punti di "
          "interesse su cui agganciare i contenuti. Sono monumenti, edifici ed elementi del paesaggio, ma anche "
          "soggetti mobili come animali selvatici e volatili, che nelle aree naturali possono comparire per pochi "
          "istanti e sfuggire ai passeggeri. La percezione combina:"),
    ("p", "video nel visibile su quattro lati;"),
    ("p", "infrarosso e termico;"),
    ("p", "LiDAR."),
    ("t", "Il kit di percezione è dedicato all'esperienza degli occupanti, non alla guida, e non si sovrappone ai sistemi "
          "ADAS di serie. Le attività sono ricerca industriale ai sensi dell'art. 1, lett. o), del DD: sviluppano metodi "
          "di percezione multisensore per una finalità nuova, verificati su banco e su percorsi registrati."),
])
CONTENUTI["II.7.2/OR12"] = _blocchi([
    ("s", "A12.1"),
    ("e", ("Problema.", "I sistemi di percezione di serie sono orientati alla guida e coprono soprattutto la scena "
           "frontale. La scena vista dai passeggeri è laterale, con angoli e distanze diversi, e richiede una "
           "combinazione di sensori che non esiste come configurazione di riferimento. Le schede tecniche dei sensori "
           "non bastano a prevederne il comportamento sul veicolo in movimento.")),
    ("e", ("Soluzione proposta.", "Una configurazione sensoriale progettata per la scena laterale. Definisce numero, "
           "posizione, campo visivo e caratteristiche di:")),
    ("p", "telecamere grandangolari sui quattro lati;"),
    ("p", "telecamere infrarosse e termiche;"),
    ("p", "LiDAR e telemetri laser;"),
    ("p", "illuminatori;"),
    ("p", "obiettivi ottici e attuatori meccanici per scansione e tracking."),
    ("t", "La scelta si basa su una valutazione sperimentale di sensori e accessori, non solo sulle specifiche "
          "dichiarate."),
    ("e", ("Novità e incertezza.", "La novità è una configurazione multisensore progettata per l'esperienza degli "
           "occupanti anziché per la guida. L'incertezza riguarda quale combinazione di sensori e posizioni copra la "
           "scena laterale con ingombri, consumi e costi compatibili con un kit installabile.")),
    ("e", ("Metodo.", "")),
    ("t", "1. Requisiti di copertura ricavati dagli scenari dei contenuti."),
    ("t", "2. Selezione dei sensori candidati e prove al banco e in campo."),
    ("t", "3. Simulazione della copertura con diverse disposizioni."),
    ("t", "4. Specifica della configurazione."),
    ("e", ("Risultati misurabili.", "Specifica della configurazione sensoriale (D12.1). Indicatori:")),
    ("p", "copertura del campo visivo laterale dei passeggeri non inferiore al 90%;"),
    ("p", "condizioni operative di luce, distanza e velocità definite per ciascun sensore."),

    ("s", "A12.2"),
    ("e", ("Problema.", "Seguire punti di interesse e soggetti mobili da un veicolo in movimento è diverso dal tracking "
           "da camera fissa. Distanze e angolazioni cambiano di continuo, gli oggetti entrano ed escono dal campo "
           "visivo in pochi secondi, occlusioni e variazioni di luce interrompono le tracce.")),
    ("e", ("Soluzione proposta.", "Algoritmi di rilevamento e tracking addestrati su dataset annotati, che usano il moto "
           "noto del veicolo per prevedere la posizione degli oggetti nei fotogrammi successivi e mantenere la traccia "
           "durante le occlusioni brevi. L'addestramento è affidato a un fornitore esterno, su dati e specifiche "
           "definiti da nLight. Progettazione dei modelli e validazione dei risultati restano a nLight.")),
    ("e", ("Novità e incertezza.", "La novità è il tracking laterale, da veicolo in movimento, di punti di interesse "
           "statici e di soggetti mobili a cui agganciare contenuti. L'incertezza riguarda due punti:")),
    ("p", "la continuità del tracking con occlusioni e variazioni di luce;"),
    ("p", "il rilevamento di soggetti visibili solo per pochi istanti."),
    ("e", ("Metodo.", "")),
    ("t", "1. Costruzione del dataset, con licenze di dataset multispettrali e annotazione dei dati acquisiti."),
    ("t", "2. Addestramento e confronto di architetture di rilevamento e tracking."),
    ("t", "3. Valutazione con metriche standard, per classe di oggetto e per condizione."),
    ("e", ("Risultati misurabili.", "Algoritmi di rilevamento e tracking (D12.2). Indicatori:")),
    ("p", "precisione media di rilevamento (mAP) non inferiore a 0,8 sui punti di interesse statici;"),
    ("p", "almeno il 90% delle tracce mantenute durante occlusioni inferiori a 1 s."),

    ("s", "A12.3"),
    ("e", ("Problema.", "Vibrazioni, sobbalzi e cambi di direzione improvvisi degradano le immagini e la stima di "
           "posizione dei punti di interesse, interrompono il tracking e rendono impreciso l'ancoraggio dei "
           "contenuti.")),
    ("e", ("Soluzione proposta.", "Accelerometri e giroscopi integrati sul modulo sensoriale e algoritmi di "
           "stabilizzazione inerziale che compensano il moto del veicolo su immagini e stime di posizione. L'obiettivo "
           "è mantenere stabili le immagini acquisite e la stima di posizione dei punti di interesse, condizione per un "
           "tracking continuo e per un ancoraggio preciso dei contenuti. L'attività riguarda il modulo sensoriale; la "
           "localizzazione del veicolo è trattata in OR9.")),
    ("e", ("Novità e incertezza.", "La stabilizzazione è consolidata per la singola telecamera, non per un modulo che "
           "combina video, infrarosso, termico e LiDAR con frequenze e latenze diverse. L'incertezza riguarda "
           "l'efficacia di una compensazione coerente fra i sensori sulle sollecitazioni reali del veicolo.")),
    ("e", ("Metodo.", "")),
    ("t", "1. Caratterizzazione delle vibrazioni su percorsi di riferimento."),
    ("t", "2. Selezione dei sensori inerziali."),
    ("t", "3. Confronto degli algoritmi su banco con sollecitazioni riprodotte."),
    ("t", "4. Verifica su percorsi registrati."),
    ("e", ("Risultati misurabili.", "Modulo di stabilizzazione inerziale (D12.3). Indicatori:")),
    ("p", "tremolio delle immagini ridotto di almeno il 50% rispetto al modulo non stabilizzato;"),
    ("p", "errore di posizione dei punti di interesse ridotto di almeno il 30%."),

    ("s", "A12.4"),
    ("e", ("Problema.", "Di notte e con visibilità ridotta la telecamera nel visibile non rileva i punti di interesse, e "
           "le esperienze si interromperebbero. La distanza degli oggetti, necessaria per ancorare i contenuti, non si "
           "ricava con precisione da una sola immagine.")),
    ("e", ("Soluzione proposta.", "Rilevamento e tracking estesi ai sensori termici passivi e all'illuminazione attiva, "
           "con fusione di video, infrarosso, termico e LiDAR per stimare distanza e geometria dei punti di interesse. "
           "Le sorgenti di illuminazione sono valutate sperimentalmente: visibile, vicino infrarosso e ultravioletto, a "
           "emissione continua o impulsata. Su strada l'illuminazione attiva è limitata al vicino infrarosso in classe "
           "1 secondo IEC 60825-1, per la sicurezza oculare e per non abbagliare gli altri utenti della strada.")),
    ("e", ("Novità e incertezza.", "La novità è fondere sensori termici, infrarossi e LiDAR per agganciare contenuti a "
           "oggetti osservati di notte. L'incertezza riguarda due punti:")),
    ("p", "la stima di distanza con sensori di risoluzione e frequenza diverse;"),
    ("p", "il guadagno reale dell'illuminazione attiva entro i limiti di sicurezza."),
    ("e", ("Metodo.", "")),
    ("t", "1. Prove comparative delle sorgenti di illuminazione in laboratorio."),
    ("t", "2. Estensione dei modelli di rilevamento ai canali termico e infrarosso."),
    ("t", "3. Algoritmi di fusione per distanza e geometria."),
    ("t", "4. Valutazione su percorsi notturni registrati."),
    ("e", ("Risultati misurabili.", "Modulo di percezione in bassa visibilità e di fusione multisensore (D12.4). "
           "Indicatori:")),
    ("p", "precisione di rilevamento notturna non inferiore all'80% di quella diurna;"),
    ("p", "errore di distanza dei punti di interesse inferiore al 5% entro 100 m."),

    ("s", "A12.5"),
    ("e", ("Problema.", "Gli algoritmi sviluppati separatamente vanno verificati insieme, con dati non usati in "
           "addestramento e in condizioni rappresentative, prima della prototipazione del kit.")),
    ("e", ("Soluzione proposta.", "Verifiche su banco e su percorsi registrati con i sensori di sviluppo, con indicatori "
           "di precisione, continuità del tracking ed errore di distanza. I percorsi registrati servono anche alla prima "
           "validazione del digital twin (A6.4).")),
    ("e", ("Novità e incertezza.", "L'attività verifica se le prestazioni misurate sui dataset si confermano su percorsi "
           "registrati con la configurazione reale. L'incertezza riguarda la generalizzazione a luoghi, stagioni e "
           "condizioni di luce non presenti nei dati di addestramento.")),
    ("e", ("Metodo.", "")),
    ("t", "1. Protocollo di verifica e separazione dei dati."),
    ("t", "2. Prove su banco con sollecitazioni riprodotte."),
    ("t", "3. Registrazione dei percorsi di riferimento."),
    ("t", "4. Misura degli indicatori per classe e condizione."),
    ("e", ("Risultati misurabili.", "Rapporto delle verifiche della percezione (D12.5). Indicatori:")),
    ("p", "indicatori di A12.2-A12.4 misurati su dati non usati in addestramento;"),
    ("p", "percorsi registrati consegnati per la validazione del digital twin."),
])


# ---------------------------------------------------------------- OR13 (nLight), forma Frascati dagli abstract di revisione (23/11)
# nLight non ha inviato la riscrittura di OR13: testi redatti da Aubay dagli abstract e dalle voci di costo del
# modello; valori obiettivo proposti, da condividere con nLight.
CONTENUTI["II.7.1/OR13"] = _blocchi([
    _intestazione("Prototipo del kit di percezione e dell'unità di calcolo di bordo, validazione su veicolo", "nLight",
                  "sviluppo sperimentale", "Torino, via G. Schiaparelli 14 (Piemonte); prove sul veicolo di prova"),
    ("t", "L'obiettivo realizzativo realizza il prototipo del kit di percezione multisensore e dell'unità di calcolo di "
          "bordo. Il kit è poi installato e calibrato sul veicolo di prova (OR4), e le sue prestazioni sono validate su "
          "strada nelle prove del dimostratore (OR14). Le attività sono sviluppo sperimentale ai sensi dell'art. 1 del "
          "DD: costruzione di prototipi, test e convalida in condizioni operative reali."),
])
CONTENUTI["II.7.2/OR13"] = _blocchi([
    ("s", "A13.1"),
    ("e", ("Problema.", "Un kit di sensori da laboratorio non è installabile su un veicolo. Servono alimentazione dal "
           "veicolo, cablaggi, contenitori, dissipazione del calore, e un'unità di calcolo che esegua gli algoritmi di "
           "OR12 entro i vincoli di bordo indicati nelle specifiche del Politecnico (A9.4).")),
    ("e", ("Soluzione proposta.", "Un progetto integrato del kit e dell'unità di calcolo:")),
    ("p", "disposizione meccanica dei sensori secondo la configurazione di A12.1;"),
    ("p", "alimentazione da veicolo e cablaggi;"),
    ("p", "contenitori protetti da polvere e umidità, con dissipazione del calore;"),
    ("p", "architettura dell'unità di calcolo dimensionata sui carichi misurati in OR12."),
    ("e", ("Novità e incertezza.", "La novità è un kit multisensore per la scena laterale progettato come prototipo "
           "installabile. L'incertezza riguarda la conciliazione fra prestazioni di calcolo, consumi e dissipazione "
           "nello spazio disponibile.")),
    ("e", ("Metodo.", "")),
    ("t", "1. Requisiti dalle specifiche di A9.4 e dalla configurazione di A12.1."),
    ("t", "2. Progetto meccanico, elettrico e termico."),
    ("t", "3. Revisione del progetto con il Politecnico e con l'integrazione di sistema (A14.1)."),
    ("e", ("Risultati misurabili.", "Progetto del kit e dell'unità di calcolo (D13.1). Indicatori:")),
    ("p", "100% delle specifiche di A9.4 soddisfatte o derogate con motivazione;"),
    ("p", "assorbimento elettrico entro il budget concordato con l'integrazione di sistema (A14.1)."),

    ("s", "A13.2"),
    ("e", ("Problema.", "Allineamento e sincronizzazione dei sensori devono restare stabili con le vibrazioni del "
           "veicolo e le variazioni di temperatura.")),
    ("e", ("Soluzione proposta.", "Realizzazione del prototipo su progetto nLight. Lavorazioni meccaniche, ottiche, "
           "cablaggi e contenitori sono affidati a fornitori esterni; i componenti rientrano nei materiali. I sensori "
           "sono sincronizzati via hardware su un riferimento temporale comune, e montati su supporti che mantengono "
           "l'allineamento.")),
    ("e", ("Novità e incertezza.", "L'incertezza riguarda la stabilità nel tempo dell'allineamento fra sensori e la "
           "precisione della sincronizzazione sul veicolo.")),
    ("e", ("Metodo.", "")),
    ("t", "1. Realizzazione delle parti presso i fornitori."),
    ("t", "2. Montaggio e sincronizzazione dei sensori."),
    ("t", "3. Prove su banco con alimentazione da veicolo."),
    ("t", "4. Misura di sincronizzazione e allineamento dopo cicli di vibrazione."),
    ("e", ("Risultati misurabili.", "Kit funzionante su banco con alimentazione da veicolo (D13.2). Indicatori:")),
    ("p", "scarto di sincronizzazione fra i sensori inferiore a 1 ms;"),
    ("p", "deriva dell'allineamento entro 0,1° dopo i cicli di vibrazione."),

    ("s", "A13.3"),
    ("e", ("Problema.", "Gli algoritmi di OR12 devono girare su un'unità di bordo che resista a vibrazioni, temperature "
           "e disturbi elettromagnetici del veicolo.")),
    ("e", ("Soluzione proposta.", "Prototipo dell'unità di calcolo, con la scheda prodotta da un fornitore esterno su "
           "progetto nLight. Le prove di vibrazione, temperatura e compatibilità elettromagnetica si svolgono presso un "
           "laboratorio accreditato.")),
    ("e", ("Novità e incertezza.", "L'incertezza riguarda la possibilità di mantenere le prestazioni degli algoritmi "
           "entro i vincoli termici e di alimentazione di bordo.")),
    ("e", ("Metodo.", "")),
    ("t", "1. Realizzazione della scheda."),
    ("t", "2. Porting degli algoritmi, con le ottimizzazioni per l'esecuzione a bordo del Politecnico (A9.5)."),
    ("t", "3. Prove ambientali e correzioni."),
    ("e", ("Risultati misurabili.", "Prototipo dell'unità di calcolo di bordo (D13.3). Indicatori:")),
    ("p", "prove di vibrazione, temperatura e compatibilità elettromagnetica superate;"),
    ("p", "algoritmi di OR12 eseguiti in tempo reale sull'unità, alla frequenza di acquisizione dei sensori."),

    ("s", "A13.4"),
    ("e", ("Problema.", "Sul veicolo i sensori vanno calibrati fra loro e rispetto al veicolo: un errore di calibrazione "
           "diventa errore di posizione dei contenuti.")),
    ("e", ("Soluzione proposta.", "Installazione del kit e dell'unità di calcolo sul veicolo di prova (OR4), con la "
           "strumentazione di calibrazione. Una procedura di calibrazione intrinseca ed estrinseca ripetibile, con "
           "verifica periodica.")),
    ("e", ("Novità e incertezza.", "L'incertezza riguarda la stabilità della calibrazione sul veicolo nel tempo e sotto "
           "le sollecitazioni di guida.")),
    ("e", ("Metodo.", "")),
    ("t", "1. Installazione."),
    ("t", "2. Calibrazione."),
    ("t", "3. Verifica su bersagli noti."),
    ("t", "4. Ripetizione della verifica dopo i percorsi di prova."),
    ("e", ("Risultati misurabili.", "Kit installato e calibrato sul veicolo di prova (D13.4). Indicatori:")),
    ("p", "errore di calibrazione estrinseca inferiore a 0,1° in orientamento e a 2 cm in posizione;"),
    ("p", "calibrazione mantenuta entro le stesse soglie dopo i percorsi di prova."),

    ("s", "A13.5"),
    ("e", ("Problema.", "Gli indicatori di percezione misurati nella ricerca industriale vanno confermati in condizioni "
           "reali.")),
    ("e", ("Soluzione proposta.", "Validazione su strada nelle prove del dimostratore (A14.5), con gli stessi indicatori "
           "e protocolli di A12.5, e confronto con la percezione simulata nel digital twin (OR6).")),
    ("e", ("Novità e incertezza.", "L'incertezza riguarda lo scarto fra le prestazioni misurate in laboratorio e quelle "
           "su strada, e le condizioni non coperte dai dati di sviluppo.")),
    ("e", ("Metodo.", "")),
    ("t", "1. Piano di prova condiviso con A14.5."),
    ("t", "2. Acquisizione dei dati durante le prove."),
    ("t", "3. Analisi per classe di oggetto e per condizione."),
    ("t", "4. Rapporto di validazione."),
    ("e", ("Risultati misurabili.", "Rapporto di validazione della percezione su strada (D13.5). Indicatori:")),
    ("p", "indicatori di A12.2-A12.4 confermati su strada entro il 10% dei valori di laboratorio;"),
    ("p", "risultati riportati per condizione di luce: giorno, notte, bassa visibilità."),
])


# ---------------------------------------------------------------- OR9 (Politecnico), forma Frascati dal testo del 23/11
# Testi riscritti da MooVXR_MVR-FINAL-01_CORRETTO.docx: struttura a 14 OR, Cognitive Mesh ricondotta a strato di
# esecuzione e coordinamento a bordo (schema comune di affidabilità, orchestrazione, monitor), senza decisioni sui
# contenuti, che restano a OR1 (decisione del 23/11). Valori obiettivo proposti da Aubay, da condividere.
CONTENUTI["II.7.1/OR9"] = _blocchi([
    _intestazione("Localizzazione di precisione, ancoraggio dei contenuti e calcolo a bordo", "Politecnico di Milano",
                  "ricerca industriale", "Dipartimento di Energia, Campus Bovisa, Milano (Lombardia)"),
    ("t", "L'obiettivo realizzativo riguarda i metodi per posizionare con precisione i contenuti sulla scena reale, sia "
          "sugli HUD sia sugli occhiali, riconoscendo quando la precisione non è sufficiente. Comprende anche le "
          "specifiche dell'unità di calcolo di bordo su cui eseguire gli algoritmi."),
    ("t", "Il contributo trasversale è la Cognitive Mesh, uno strato di esecuzione e coordinamento a bordo. Rende "
          "confrontabili le uscite dei moduli dei partner con uno schema comune di affidabilità, e ne orchestra "
          "l'esecuzione sull'unità di calcolo con priorità, budget e monitor. Il content policy engine (OR1) usa queste "
          "informazioni per decidere i contenuti: la Cognitive Mesh non prende decisioni sui contenuti."),
    ("t", "Le attività sono ricerca industriale ai sensi dell'art. 1, lett. o), del DD: producono nuove conoscenze su "
          "localizzazione e registrazione dei contenuti per un componente di un sistema complesso, verificate su dati "
          "registrati e su percorsi di prova."),
])
CONTENUTI["II.7.2/OR9"] = _blocchi([
    ("s", "A9.1"),
    ("e", ("Problema.", "GNSS RTK, navigazione inerziale e localizzazione visiva sono disponibili separatamente, ma la "
           "loro continuità e riferibilità geometrica non sono garantite in galleria, nei canyon urbani, con riflessi o "
           "perdita di visibilità. I sistemi di serie localizzano il veicolo per la navigazione. La registrazione "
           "stabile di contenuti XR sugli oggetti reali richiede invece accuratezza, continuità e latenza adeguate alla "
           "distanza degli oggetti e alla superficie di visualizzazione.")),
    ("e", ("Soluzione proposta.", "Una fusione temporale probabilistica di osservazioni GNSS RTK, inerziali e visive, "
           "con rappresentazione esplicita di covarianza, bias, disallineamento e ritardi. Stima insieme la posa del "
           "veicolo, la sua qualità e la sua disponibilità.")),
    ("e", ("Novità e incertezza.", "La novità è la stima congiunta di posa, qualità e disponibilità per l'ancoraggio "
           "di contenuti XR su un veicolo in movimento. L'incertezza riguarda come contenere il drift e recuperare "
           "l'allineamento dopo un'interruzione prolungata del segnale.")),
    ("e", ("Metodo.", "")),
    ("t", "1. Benchmark con ground truth indipendente su percorsi ripetuti."),
    ("t", "2. Confronto di filtri e metodi di ottimizzazione con baseline standard."),
    ("t", "3. Ablation study su scenari nominali e degradati, come gallerie e canyon urbani."),
    ("e", ("Risultati misurabili.", "Algoritmi, dataset e rapporto riproducibile (D9.1). Indicatori:")),
    ("p", "errore di posizione inferiore a 10 cm al 95° percentile in condizioni nominali;"),
    ("p", "errore di assetto inferiore a 0,1° al 95° percentile;"),
    ("p", "recupero dell'allineamento entro 5 s dopo un'interruzione del segnale GNSS."),
    ("t", "I dati di percezione e tracking sono prodotti da nLight (OR12). OR9 stima il riferimento globale e le "
          "incertezze, che GSNet usa per gli occhiali AR (OR5) senza duplicare la stima del moto relativo della testa. "
          "Le stime sono esposte secondo lo schema comune di affidabilità della Cognitive Mesh (A9.3)."),

    ("s", "A9.2"),
    ("e", ("Problema.", "Su HUD, occhiali e visori cambia il punto di vista, e i ritardi della catena che va dai sensori "
           "alla presentazione causano errori di parallasse e instabilità. Con il veicolo in movimento e più superfici, "
           "i metodi AR disponibili non garantiscono un riferimento geometrico e temporale coerente fra veicolo, scena "
           "e dispositivi.")),
    ("e", ("Soluzione proposta.", "Trasformazioni di coordinate versionate, mappe di ancoraggio temporizzate e "
           "propagazione dell'incertezza fra posa del veicolo, scena e superficie di visualizzazione. Il punto di "
           "partenza è la geometria della scena rilevata dal kit di percezione (OR12), per i punti di vista del "
           "guidatore, del passeggero e di chi indossa gli occhiali.")),
    ("e", ("Novità e incertezza.", "La novità è un ancoraggio temporizzato con incertezza esplicita, comune a più "
           "superfici e punti di vista. L'incertezza riguarda la stabilità con occlusioni, velocità elevate e "
           "disallineamenti temporali fra le sorgenti.")),
    ("e", ("Metodo.", "")),
    ("t", "1. Prove con target noti, filmati sincronizzati e ricostruzioni multi-view, in diverse condizioni di luce e "
          "velocità."),
    ("t", "2. Confronto fra ancoraggio statico, compensato e temporizzato."),
    ("e", ("Risultati misurabili.", "Algoritmi di ancoraggio e specifiche dei riferimenti (D9.2). Indicatori:")),
    ("p", "scarto di registrazione inferiore a 5 mrad al 95° percentile;"),
    ("p", "ancoraggio mantenuto dopo occlusioni fino a 1 s in almeno il 90% dei casi."),
    ("t", "nLight (OR12) consegna geometrie e punti di interesse rilevati, il Politecnico produce ancoraggi e "
          "trasformazioni. GSNet realizza calibrazione e applicazioni per occhiali e visori (OR4, OR5), oltre "
          "all'erogazione e all'applicazione di bordo (OR3). A OR9 non è attribuita alcuna produzione di contenuti."),

    ("s", "A9.3"),
    ("e", ("Problema.", "La qualità della localizzazione non è costante, e un contenuto apparentemente preciso ma mal "
           "posizionato distrae più di un contenuto assente. Soglie statiche e probabilità nominali non reggono le "
           "variazioni ambientali e la correlazione degli errori. Inoltre ogni modulo del progetto (localizzazione, "
           "percezione, dati esterni, stima dell'attenzione) esprime la propria affidabilità in modo diverso, o non la "
           "esprime affatto. Il content policy engine riceve così ingressi non confrontabili.")),
    ("e", ("Soluzione proposta.", "Due risultati:")),
    ("p", "uno stimatore calibrato del rischio di registrazione della localizzazione, con una rappresentazione "
          "multimodale dell'incertezza (posa, scena, ritardo, dati fuori distribuzione) e criteri di riduzione dei "
          "contenuti espressi come livelli di servizio;"),
    ("p", "lo schema comune di affidabilità della Cognitive Mesh: ogni modulo dei partner espone le proprie uscite con "
          "una rappresentazione uniforme di confidenza, validità temporale e latenza, che il modello del contesto del "
          "content policy engine (OR1, A1.1) usa direttamente."),
    ("e", ("Novità e incertezza.", "La novità è trattare l'affidabilità come grandezza esplicita e confrontabile fra "
           "moduli eterogenei, che governa la presentazione dei contenuti. L'incertezza riguarda due punti:")),
    ("p", "come distinguere gli errori rari dalla mancanza di dati senza ridurre i contenuti troppo spesso;"),
    ("p", "se una rappresentazione comune resti fedele a incertezze di natura diversa: geometrica, statistica e "
          "temporale."),
    ("e", ("Metodo.", "")),
    ("t", "1. Validazione dello stimatore su eventi degradati, registrati e perturbati."),
    ("t", "2. Curve di affidabilità e test con input incoerenti; confronto con soglie fisse."),
    ("t", "3. Definizione dello schema comune con i partner che forniscono i moduli (OR7, OR10, OR12) e con Aubay per "
          "il modello del contesto."),
    ("e", ("Risultati misurabili.", "Stimatore di affidabilità, schema comune di affidabilità e raccomandazioni per "
           "livelli di servizio (D9.3). Indicatori:")),
    ("p", "errore di calibrazione dell'affidabilità inferiore a 0,05;"),
    ("p", "falsi ancoraggi accettati inferiori all'1%;"),
    ("p", "schema comune adottato dal 100% dei moduli che alimentano il modello del contesto."),
    ("t", "La decisione vincolante sui contenuti, i livelli di funzionamento e il comportamento prudente restano al "
          "content policy engine (OR1, A1.2-A1.4). Anitia (OR7) produce l'affidabilità dei dati esterni e la espone "
          "secondo lo schema comune."),

    ("s", "A9.4"),
    ("e", ("Problema.", "Sul veicolo devono girare insieme percezione, stima geometrica, modelli AI compatti e "
           "sincronizzazione dei contenuti XR, con vincoli di alimentazione, memoria, acceleratori, calore e "
           "comunicazioni intermittenti. Moduli sviluppati da partner diversi competono per le stesse risorse senza un "
           "coordinamento comune, e un dimensionamento generico fra bordo e cloud non garantisce latenze sicure con "
           "carichi concorrenti.")),
    ("e", ("Soluzione proposta.", "La Cognitive Mesh come strato di esecuzione e coordinamento a bordo, insieme alle "
           "specifiche dell'unità di calcolo che la ospita:")),
    ("p", "orchestrazione deterministica dei moduli dei partner: priorità e classi di criticità, budget di calcolo, "
          "memoria ed energia, timeout e degradazione quando le risorse non bastano;"),
    ("p", "monitor di esecuzione: rilevano ingressi incoerenti, ritardi e moduli fuori servizio e li segnalano al "
          "content policy engine (OR1), che applica i livelli prudenti (A1.4);"),
    ("p", "specifiche dell'unità: ripartizione fra bordo e cloud, isolamento dei processi, riferimento temporale comune."),
    ("t", "Le specifiche sono la base del prototipo realizzato da nLight (OR13)."),
    ("e", ("Novità e incertezza.", "La novità è uno strato di coordinamento che garantisce latenze e degradazione "
           "controllata a moduli eterogenei di più fornitori, che condividono le stesse risorse di bordo. L'incertezza "
           "riguarda la possibilità di soddisfare insieme qualità, consumi e scadenze con carichi concorrenti.")),
    ("e", ("Metodo.", "")),
    ("t", "1. Profili di carico dei moduli dei partner."),
    ("t", "2. Modelli prestazionali e simulazioni di saturazione."),
    ("t", "3. Prototipo dell'orchestrazione e dei monitor su kit di sviluppo embedded, con iniezione di guasti e replay "
          "deterministico."),
    ("t", "4. Specifiche dell'unità di calcolo."),
    ("e", ("Risultati misurabili.", "Specifiche dell'unità di calcolo di bordo, comprensive dello strato di "
           "coordinamento (D9.4). Indicatori:")),
    ("p", "latenza al 99° percentile dei carichi critici compatibile con il budget di consegna end-to-end di A14.4, "
          "nelle simulazioni di saturazione;"),
    ("p", "nessuna scadenza mancata per i processi critici nelle prove di schedulazione;"),
    ("p", "guasti iniettati rilevati dai monitor entro 100 ms nel 99% dei casi."),
    ("t", "Il Politecnico formula specifiche verificabili e prototipa lo strato di coordinamento; nLight progetta e "
          "realizza kit e unità di calcolo (A13.1-A13.3). L'integrazione di sistema resta in OR14 (Aubay), con la "
          "gestione dei modelli in esercizio in A14.3; il device management e l'OTA restano in OR8 (Anitia)."),

    ("s", "A9.5"),
    ("e", ("Problema.", "Gli algoritmi sperimentali richiedono spesso potenza e memoria non compatibili con i "
           "processori automotive, e competono per le risorse con visione, audio e rendering. La semplice portabilità "
           "del software non assicura riproducibilità né controllo del degrado.")),
    ("e", ("Soluzione proposta.", "Distillazione, quantizzazione, pruning e caching selettivo dei modelli, con lo "
           "scheduler della Cognitive Mesh (A9.4), attento alle scadenze e alla qualità delle informazioni. Tempi di "
           "calcolo e consumi sono misurati sull'unità di bordo.")),
    ("e", ("Novità e incertezza.", "La novità è ottimizzare insieme più algoritmi di percezione e ancoraggio sotto "
           "scadenze comuni. L'incertezza riguarda la perdita di accuratezza nelle condizioni rare e gli effetti delle "
           "contese di risorse.")),
    ("e", ("Metodo.", "")),
    ("t", "1. Benchmark realistici."),
    ("t", "2. Misure ripetute di consumo e latenza."),
    ("t", "3. Stress test con dati fuori distribuzione e test di regressione."),
    ("e", ("Risultati misurabili.", "Algoritmi ottimizzati e rapporto sui compromessi (D9.5). Indicatori:")),
    ("p", "tempi di calcolo ridotti di almeno 3 volte rispetto alla versione non ottimizzata;"),
    ("p", "perdita di accuratezza inferiore al 5%;"),
    ("p", "almeno il 99% dei compiti completati entro la scadenza."),
    ("t", "Le verifiche algoritmiche sono del Politecnico. nLight fornisce la piattaforma prototipale e le prove "
          "ambientali (OR13), Aubay cura l'integrazione (OR14) e Anitia gli aggiornamenti (OR8)."),
])


# ================================================================ RISORSE E COSTI PER ATTIVITÀ E PER OR (23/11)
# Questa sezione deve restare l'ultima del file: i testi nuovi degli OR si aggiungono sopra questo marcatore.
# Per ogni attività: tabella del personale e dei servizi attribuiti all'attività; per ogni OR: riepilogo con
# attrezzature, servizi assegnati all'OR e totali per voce. I dati si leggono dal modello economico (MODELLO),
# senza ricalcoli; i totali per OR sono verificati sul foglio Riepilogo. I sottotitoli delle attività di tutti
# gli OR si generano dal modello. I vecchi paragrafi "Risorse umane"
# dei testi degli OR sono sostituiti dalle tabelle.
def _num(v, dec=0):
    s = format(v, ",.%df" % dec)
    return s.replace(",", "§").replace(".", ",").replace("§", ".")


def _eur(v):
    return _num(round(v)) + " €"


def _carica_costi():
    import openpyxl
    wb = openpyxl.load_workbook(MODELLO, data_only=True)
    att = {}
    for r in wb["Attività"].iter_rows(min_row=2, values_only=True):
        if r[1]:
            att[r[1]] = dict(OR=r[0], ini=r[3], fine=r[4], n=(r[6], r[7], r[8]), imp=r[9], ore=(r[20], r[21], r[22]),
                             tar=(r[23], r[24], r[26]), costo=r[25], ruoli=(r[27], r[28], r[29]))
    serv = [dict(ogg=r[1], OR=r[2], imp=r[3], mot=r[4], att=r[8], ruolo=r[9])
            for r in wb["Consulenze e servizi"].iter_rows(min_row=2, values_only=True) if r[1] and r[2]]
    attr = [dict(nome=r[0], OR=r[2], q=r[3], amm=r[6], uso=r[7], imput=r[8], intero=r[9], spesa=r[11], costo=r[12])
            for r in wb["Attrezzature"].iter_rows(min_row=2, values_only=True) if r[0] and r[2]]
    riep, dentro = {}, False
    for r in wb["Riepilogo"].iter_rows(values_only=True):
        if r[0] == "OR":
            dentro = True
            continue
        if dentro and r[0] and str(r[0]).startswith("OR"):
            riep[r[0]] = dict(pers=r[3], attr=r[4], serv=r[5], sg=r[6], tot=r[7])
    assert att and riep, "modello non ricalcolato: %s" % MODELLO
    return att, serv, attr, riep


_ATT, _SERV, _ATTR, _RIEP = _carica_costi()
_W = 9526


def _tab(larghezze, intest, righe, totale=None):
    R = [[{"t": x, "b": True, "al": "center" if i else "left", "sz": 16} for i, x in enumerate(intest)]]
    for r in righe:
        R.append([{"t": x, "sz": 16, "al": al} for x, al in r])
    if totale:
        R.append([{"t": x, "sz": 16, "b": True, "al": al} for x, al in totale])
    assert sum(larghezze) == _W
    return {"larghezze": larghezze, "righe": R, "testa": 1}


def _tab_personale(cod):
    a = _ATT[cod]
    righe, fte, ore, costo = [], 0, 0, 0
    for k, fascia in enumerate(("Alto", "Medio", "Basso")):
        if not a["ore"][k]:
            continue
        f = a["n"][k] * a["imp"]
        c = a["ore"][k] * a["tar"][k]
        righe.append([(fascia, "left"), (a["ruoli"][k] or "", "left"), (_num(f, 2), "right"),
                      (_num(a["ore"][k]), "right"), (_num(a["tar"][k]), "right"), (_eur(c), "right")])
        fte += f; ore += a["ore"][k]; costo += c
    assert round(costo) == round(a["costo"]), (cod, costo, a["costo"])
    return _tab([1450, 4176, 800, 900, 700, 1500], ["Fascia", "Profilo e ruolo", "FTE", "Ore", "€/h", "Costo"], righe,
                [("Totale personale", "left"), ("", "left"), (_num(fte, 2), "right"), (_num(ore), "right"),
                 ("", "right"), (_eur(costo), "right")])


def _tab_servizi(lista, col="Ruolo nell'attività"):
    righe = [[(s["ogg"], "left"), (s["ruolo"] or s["mot"] or "", "left"), (_eur(s["imp"]), "right")] for s in lista]
    tot = [("Totale servizi", "left"), ("", "left"), (_eur(sum(s["imp"] for s in lista)), "right")] if len(lista) > 1 else None
    return _tab([3900, 4126, 1500], ["Servizi e licenze", col, "Importo"], righe, tot)


def _tab_attrezzature(lista):
    def uso(x):
        if x["intero"] == "Sì":
            return "intero costo, vita utile entro la durata"
        s = "%d mesi su %d" % (x["uso"], x["amm"])
        return s + ("" if (x["imput"] or 1) >= 1 else ", imputazione %d%%" % round(x["imput"] * 100))
    righe = [[("%s%s" % (x["nome"], " (%d)" % x["q"] if x["q"] and x["q"] > 1 else ""), "left"),
              (_eur(x["spesa"]), "right"), (uso(x), "left"), (_eur(x["costo"]), "right")] for x in lista]
    tot = [("Totale", "left"), (_eur(sum(x["spesa"] for x in lista)), "right"), ("", "left"),
           (_eur(sum(x["costo"] for x in lista)), "right")] if len(lista) > 1 else None
    return _tab([3826, 1500, 2400, 1800], ["Strumenti e attrezzature", "Spesa prevista", "Ammortamento e utilizzo",
                                           "Costo ammissibile"], righe, tot)


def _blocco_attivita(cod):
    a = _ATT[cod]
    out = [("s", "Risorse e costi di %s, mesi %d-%d" % (cod, a["ini"], a["fine"])), ("x", _tab_personale(cod))]
    s = [x for x in _SERV if x["att"] == cod]
    if s:
        out.append(("x", _tab_servizi(s)))
    return out


def _blocco_or(o):
    out = [("s", "Riepilogo dei costi di %s" % o)]
    attr = [x for x in _ATTR if x["OR"] == o]
    serv = [x for x in _SERV if x["OR"] == o and not x["att"]]
    if attr:
        out.append(("x", _tab_attrezzature(attr)))
    if serv:
        out.append(("x", _tab_servizi(serv, "Ruolo nell'OR")))
    r = _RIEP[o]
    cod = [c for c, a in _ATT.items() if a["OR"] == o]
    assert round(sum(_ATT[c]["costo"] for c in cod)) == round(r["pers"]), (o, "personale")
    assert round(sum(x["costo"] for x in attr), 2) == round(r["attr"], 2), (o, "attrezzature")
    assert round(sum(x["imp"] for x in _SERV if x["OR"] == o)) == round(r["serv"]), (o, "servizi")
    righe = [[("Personale", "left"), (_eur(r["pers"]), "right")],
             [("Strumenti e attrezzature (quota imputata)", "left"), (_eur(r["attr"]), "right")],
             [("Servizi di consulenza e altri servizi", "left"), (_eur(r["serv"]), "right")],
             [("Spese generali e materiali (20%)", "left"), (_eur(r["sg"]), "right")]]
    out.append(("x", _tab([7026, 2500], ["Voce di costo", "Costo"], righe,
                          [("Totale %s" % o, "left"), (_eur(r["tot"]), "right")])))
    return out


def _render(spec):
    f = {"t": testo, "p": punto, "s": sottotitolo, "e": _etichetta}
    return lambda: [v if k == "x" else f[k](v) for k, v in spec]


_RE_TASK = _re.compile(r"^(A\d+\.\d+)\b")
TESTI_SENZA_ATTIVITA, ATTIVITA_SENZA_TESTO = [], []
for _o in [o[0] for o in CFG["or"]]:
    _k = "II.7.2/%s" % _o
    _sp = _spec(_k) if _k in CONTENUTI else []
    _out, _cur, _skip = [], None, False
    _visti = set()
    for _t, _v in _sp + [("s", "§fine")]:
        if _t == "s":
            if _cur:
                _out += _blocco_attivita(_cur)
                _cur = None
            _skip = _v.strip().lower().startswith("risorse umane")
            _m = _RE_TASK.match(_v)
            if _m:
                if _m.group(1) in _ATT and _ATT[_m.group(1)]["OR"] == _o:
                    _cur = _m.group(1); _visti.add(_cur)
                    _v = _sotto_task(_cur)[1]          # sottotitolo (codice, titolo, mesi) dal modello
                else:
                    TESTI_SENZA_ATTIVITA.append("%s: %s" % (_o, _v[:60]))
            if _v == "§fine" or _skip:
                continue
        if not _skip:
            _out.append((_t, _v))
    for _c in [c for c, a in _ATT.items() if a["OR"] == _o and c not in _visti]:
        ATTIVITA_SENZA_TESTO.append(_c)
        _out += [_sotto_task(_c)] + _blocco_attivita(_c)
    _out += _blocco_or(_o)
    CONTENUTI[_k] = _render(_out)
