# -*- coding: utf-8 -*-
# Generato da importa_testi_partner.py da MooVXR_Anitia_revisione_rev1.docx. Non modificare a mano.
TESTI_ANITIA = {'OR7': {'7.1': [('t',
                  'Titolo: Integrazione di dati da strada e infrastruttura. Soggetto proponente: Anitia. Tipologia: '
                  'ricerca industriale. Luogo di svolgimento: Sona (VR), Veneto.'),
                 ('t',
                  "L'obiettivo realizzativo studia i metodi per arricchire le informazioni a disposizione del veicolo "
                  'con dati esterni: stato e fasatura dei semafori, cantieri, incidenti, traffico e condizioni meteo '
                  'locali. I dati arrivano dalla comunicazione V2X (messaggi ETSI C-ITS come DENM, SPATEM/MAPEM e '
                  'IVIM) e dalle piattaforme dei gestori di strade e servizi (DATEX II, API dei gestori della '
                  'mobilità). I dati su POI e disponibilità delle colonnine di ricarica sono trattati nei servizi di '
                  'contenuto di OR4 (Aubay) e non rientrano in questo obiettivo.'),
                 ('t',
                  "Lo stato dell'arte copre bene il trasporto di questi dati. Non definisce invece come stabilire, "
                  'istante per istante, quanto un dato esterno sia affidabile e attuale, e quando sia abbastanza '
                  'affidabile da essere mostrato al guidatore. Le fonti hanno latenze che vanno dai millisecondi del '
                  'V2X diretto ai minuti delle piattaforme aggregate. La copertura è disomogenea e i metadati di '
                  'qualità spesso mancano.'),
                 ('t',
                  "L'obiettivo produce tre risultati, usati dal content policy engine (OR1) e dalla piattaforma IoT "
                  '(OR8):'),
                 ('p', 'un modello di qualità del dato esterno;'),
                 ('p', 'i metodi di fusione con i dati di bordo;'),
                 ('p', 'i criteri di promozione ad avviso.'),
                 ('t',
                  "Le attività sono ricerca industriale ai sensi dell'art. 1, lett. o), del DD: il criterio con cui un "
                  'dato esterno diventa abbastanza affidabile e tempestivo da essere mostrato al guidatore non è '
                  "definito dallo stato dell'arte.")],
         '7.2': [('s', 'A7.1 Censimento delle fonti esterne (mesi 1-5)'),
                 ('e', ('Problema.', 'Le fonti di dati esterni disponibili nelle aree pilota sono eterogenee:')),
                 ('p', 'unità di bordo strada V2X;'),
                 ('p', 'piattaforme dei gestori stradali e dei comuni;'),
                 ('p', 'fornitori commerciali di dati di traffico.'),
                 ('t',
                  'Differiscono per protocollo, modello dati, frequenza di aggiornamento, copertura e licenza. Per '
                  "nessuna di esse sono documentati in modo sistematico la latenza reale e l'accuratezza. Senza questa "
                  'base non si possono progettare la fusione (A7.2) e i criteri di avviso (A7.3).'),
                 ('e',
                  ('Soluzione proposta.',
                   'Un catalogo strutturato e aggiornabile delle fonti. Per ciascuna fonte descrive:')),
                 ('p', 'formato e protocollo;'),
                 ('p', 'semantica degli eventi;'),
                 ('p', 'latenza dichiarata e latenza misurata;'),
                 ('p', 'copertura spaziale e temporale;'),
                 ('p', 'metadati di qualità disponibili;'),
                 ('p', "condizioni d'uso e di licenza."),
                 ('t',
                  'Si affianca un modello dati comune degli eventi esterni (tipo di evento, posizione e area di '
                  'validità, istante di osservazione e di pubblicazione, fonte, qualità dichiarata). Il modello è '
                  'allineato alle tassonomie ETSI C-ITS e DATEX II e convertibile nel modello dati del veicolo usato '
                  'da OR8.'),
                 ('e',
                  ('Novità e incertezza.',
                   "Il catalogo in sé è un'attività preparatoria. La parte di ricerca è la definizione di un modello "
                   'di qualità del dato esterno che sia comune a fonti con semantiche diverse. Non è noto a priori '
                   'quali attributi di qualità si possano stimare per ciascuna fonte quando la fonte non li '
                   'dichiara.')),
                 ('e', ('Metodo.', '')),
                 ('t', '1. Rassegna di standard e piattaforme.'),
                 ('t',
                  '2. Acquisizione di campioni reali da ciascuna fonte nelle aree pilota per un periodo minimo di 4 '
                  'settimane.'),
                 ('t',
                  "3. Misura della latenza come differenza fra l'istante dell'evento e l'istante di disponibilità. "
                  'Dove esiste, si usa un riferimento indipendente: osservazione diretta, dati di bordo, seconda '
                  'fonte.'),
                 ('t',
                  '4. Per ogni profilo (DENM, SPATEM/MAPEM, IVIM, DATEX II) si registrano versione, significato dei '
                  "tempi, validità dichiarata e modalità di aggiornamento o cessazione, ove previste. Dove l'istante "
                  "dell'evento non è osservabile si misura il tempo da pubblicazione a ricezione."),
                 ('t', '5. Definizione del modello dati e del modello di qualità.'),
                 ('e',
                  ('Risultati misurabili.',
                   'Catalogo delle fonti esterne (D7.1) con almeno 8 fonti caratterizzate. Per ciascuna: latenza '
                   'misurata (mediana e 95° percentile), copertura e completezza dei metadati. Specifica del modello '
                   'dati comune degli eventi esterni.')),
                 ('s', 'A7.2 Fusione dei dati esterni con i dati di bordo (mesi 4-14)'),
                 ('e',
                  ('Problema.',
                   'Lo stesso evento, per esempio un cantiere o una coda, può essere segnalato da più fonti con '
                   'ritardi, posizioni e descrizioni diverse. Può anche essere osservato o smentito dai dati del '
                   'veicolo (velocità, frenate, segnali ADAS) e dalla percezione di bordo (OR12). Le fonti raramente '
                   'dichiarano accuratezza e validità. Un evento può inoltre essere ancora pubblicato quando non è più '
                   'vero: i messaggi DENM prevedono aggiornamento e cessazione, ma molte piattaforme aggregate non '
                   'segnalano in modo affidabile la fine di un evento.')),
                 ('e', ('Soluzione proposta.', 'Un modulo di fusione che fa tre cose:')),
                 ('p',
                  'associa le segnalazioni che si riferiscono allo stesso evento (associazione spazio-temporale e '
                  'semantica);'),
                 ('p',
                  "mantiene per ogni evento uno stato con due stime: probabilità che l'evento sia vero (affidabilità) "
                  'e probabilità che sia ancora in corso (attualità);'),
                 ('p',
                  "aggiorna lo stato all'arrivo di nuove segnalazioni, di conferme o smentite dai dati di bordo, e con "
                  'il passare del tempo.'),
                 ('t',
                  "Il modulo assegna a ogni dato un'etichetta di confidenza utilizzabile dagli strati successivi, in "
                  'particolare dal modello di contesto del content policy engine (OR1, A1.1), che gestisce '
                  "l'affidabilità di ciascun dato."),
                 ('e',
                  ('Novità e incertezza.',
                   'I metodi di fusione multisensore di bordo sono maturi. È invece aperta la fusione di fonti esterne '
                   'con queste caratteristiche:')),
                 ('p', 'ritardi che variano di più ordini di grandezza;'),
                 ('p', 'qualità non dichiarata;'),
                 ('p', 'dati di bordo che confermano un evento solo quando il veicolo lo raggiunge.'),
                 ('t', "L'incertezza riguarda tre punti:"),
                 ('p',
                  "se l'affidabilità di una fonte si possa stimare in modo stabile dai dati storici e aggiornare in "
                  'esercizio, tenendo conto della dipendenza fra fonti che ripubblicano lo stesso evento;'),
                 ('p', "quale modello di decadimento dell'attualità sia adatto a ciascuna classe di evento;"),
                 ('p',
                  'se la fusione migliori la precisione rispetto alla migliore fonte singola senza introdurre ritardi '
                  'inaccettabili.'),
                 ('e', ('Metodo.', '')),
                 ('p',
                  'Si confrontano modelli probabilistici di complessità crescente: regole pesate, aggiornamento '
                  "bayesiano dell'affidabilità per fonte, modelli di sopravvivenza per la durata degli eventi."),
                 ('p', 'I modelli sono addestrati e verificati su dati storici delle aree pilota raccolti in A7.1.'),
                 ('p',
                  'La verità di riferimento viene dai passaggi dei veicoli di prova e dalle chiusure ufficiali degli '
                  'eventi.'),
                 ('p', 'La valutazione avviene in simulazione, con riproduzione temporale dei flussi registrati.'),
                 ('p',
                  'Dati di sviluppo e dati di prova sono separati per periodo e percorso. Modello e fonte di confronto '
                  'sono scelti sui dati di sviluppo e congelati prima della prova. Nessuna fonte usata dal modello '
                  'funge da riferimento, e i casi privi di riscontro sono riportati a parte.'),
                 ('e',
                  ('Risultati misurabili.',
                   'Modulo di fusione (D7.2) e rapporto di valutazione, con questi indicatori:')),
                 ('p',
                  'precisione e richiamo degli eventi fusi rispetto alla migliore fonte singola (obiettivo: F1 '
                  'migliorato di almeno il 10% in termini relativi). D7.2 riporta anche F1 assoluto, numerosità e '
                  'risultati per classe di evento. Se la fonte migliore ha già F1 superiore a 0,9, il confronto si '
                  'sposta su calibrazione e latenza;'),
                 ('p', "errore di calibrazione dell'affidabilità stimata (obiettivo < 0,1);"),
                 ('p', 'latenza aggiunta dalla fusione (obiettivo < 100 ms per evento).'),
                 ('s', 'A7.3 Criteri di promozione di un dato ad avviso per il guidatore (mesi 9-16)'),
                 ('e',
                  ('Problema.',
                   'Un dato esterno fuso con la sua affidabilità non è ancora un avviso. Mostrarlo al guidatore ha un '
                   'costo in termini di distrazione e di fiducia nel sistema. Un avviso sbagliato o in ritardo riduce '
                   "l'attenzione agli avvisi successivi. Gli standard C-ITS definiscono i messaggi e alcuni casi "
                   "d'uso, ma non danno soglie operative che combinino:")),
                 ('p', 'affidabilità del dato;'),
                 ('p', "anticipo rispetto all'evento;"),
                 ('p', 'pertinenza per il percorso del veicolo;'),
                 ('p', 'stato di attenzione del guidatore.'),
                 ('e',
                  ('Soluzione proposta.',
                   'Un insieme di criteri e soglie, parametrizzati per classe di evento, che decide se un dato diventa '
                   'un avviso. Il dato può avere tre esiti:')),
                 ('p', "resta un'informazione disponibile;"),
                 ('p', 'diventa un avviso;'),
                 ('p', 'viene scartato.'),
                 ('t',
                  'La decisione dipende da affidabilità e attualità (A7.2), anticipo disponibile rispetto alla '
                  'posizione e alla velocità del veicolo, pertinenza per il percorso stimato e livello di criticità. I '
                  'criteri sono espressi in forma eseguibile come regole del content policy engine (OR1), che li '
                  "combina con l'attenzione del guidatore (OR10)."),
                 ('e',
                  ('Novità e incertezza.',
                   'Il contributo nuovo è un criterio quantitativo e verificabile per la promozione ad avviso di dati '
                   "con affidabilità variabile. L'incertezza riguarda l'esistenza di soglie che mantengano bassa la "
                   'frequenza di falsi avvisi senza perdere gli eventi rilevanti. Riguarda anche quanto tali soglie '
                   'siano trasferibili fra aree e classi di evento diverse.')),
                 ('e', ('Metodo.', '')),
                 ('p',
                  "Analisi dei casi d'uso C-ITS e delle linee guida di settore. Un esperto di dominio esterno al "
                  "raggruppamento analizza i casi d'uso C-ITS e le prassi operative dei gestori stradali e riesamina i "
                  'criteri di rilevanza. Modellazione, soglie e validazione tecnica restano in carico ad Anitia.'),
                 ('p',
                  'Definizione dello spazio delle soglie e ottimizzazione su dati storici, con una funzione di costo '
                  'che pesa in modo diverso avvisi mancati e falsi avvisi.'),
                 ('p', 'Analisi di sensibilità per area e classe di evento.'),
                 ('p',
                  'Entro il mese 16, consegna ad Aubay (OR1) della candidatura ad avviso, con confidenza, pertinenza e '
                  'scadenza. La decisione di presentazione resta al content policy engine, che applica le informazioni '
                  "sull'attenzione del guidatore prodotte da OR10."),
                 ('e',
                  ('Risultati misurabili.',
                   'Criteri di promozione ad avviso (D7.3), con regole integrate nel content policy engine. Indicatori '
                   'su dati storici:')),
                 ('p', 'tasso di falsi avvisi < 10%, calcolato sugli avvisi emessi;'),
                 ('p', 'quota di eventi rilevanti segnalati > 85%, calcolata sugli eventi rilevanti annotati;'),
                 ('p', "anticipo mediano dell'avviso > 30 s per le classi di evento non urgenti."),
                 ('s', 'A7.4 Prove su area pilota (mesi 14-18)'),
                 ('e',
                  ('Problema.',
                   'I risultati ottenuti su dati storici e in simulazione vanno verificati con veicoli reali, in '
                   'condizioni di connettività variabile, con unità V2X installate e ricezione in tempo reale.')),
                 ('e',
                  ('Soluzione proposta.',
                   "Una campagna di prove sull'area pilota con il prototipo di fusione e promozione ad avviso, "
                   'collegato alle unità V2X di prova (RSU e OBU) e alle fonti in tempo reale. Il dimostratore '
                   'integrato è disponibile solo dal mese 24. Per questo le prove si svolgono sul veicolo di prova di '
                   'OR5 (GSNet), in uso nello stesso periodo. Prima del mese 14 Anitia predispone un acquisitore dei '
                   'segnali minimi, con orologio sincronizzato e registrazione locale. Veicolo, percorsi, area e '
                   "autorizzazione delle RSU sono da concordare con GSNet e con il gestore dell'area. La verifica sul "
                   'dimostratore completo confluisce nelle prove di A3.7.')),
                 ('e',
                  ('Novità e incertezza.',
                   'La campagna verifica se le prestazioni misurate su dati storici reggono in tempo reale. '
                   "L'incertezza riguarda gli effetti di perdita di pacchetti, copertura radio, ritardo di rete e "
                   'sincronizzazione temporale fra fonti e veicolo.')),
                 ('e', ('Metodo.', 'Protocollo di prova con:')),
                 ('p', 'percorsi ripetuti;'),
                 ('p', "eventi reali e simulati (eventi generati sulle RSU di prova), tenuti distinti nell'analisi;"),
                 ('p', 'registrazione sincronizzata di dati esterni, dati di bordo e decisioni del sistema.'),
                 ('t', 'Ogni misura è confrontata con la verità di riferimento rilevata sul percorso.'),
                 ('e', ('Risultati misurabili.', 'Rapporto delle prove (D7.4), con:')),
                 ('p',
                  'anticipo con cui un evento è noto rispetto alla sola percezione di bordo (obiettivo mediano > 20 '
                  's);'),
                 ('p', 'percentuale di segnalazioni corrette > 90%;'),
                 ('p', "ritardo di propagazione dall'evento al veicolo (V2X diretto < 300 ms; piattaforme < 60 s);"),
                 ('p', 'tasso di falsi avvisi in esercizio.')]},
 'OR8': {'7.1': [('t',
                  'Titolo: Piattaforma IoT: accesso ai dati del veicolo, device management e OTA. Soggetto proponente: '
                  'Anitia. Tipologia: sviluppo sperimentale. Luogo di svolgimento: Sona (VR), Veneto.'),
                 ('t',
                  "L'obiettivo realizzativo sviluppa la piattaforma che costituisce l'unico punto di accesso al "
                  'veicolo per tutti i componenti del sistema. Le sue funzioni sono quattro:'),
                 ('p',
                  'leggere i dati del veicolo, compresi i segnali dei sistemi ADAS e DMS di serie, e renderli '
                  'disponibili con un modello dati standard;'),
                 ('p', 'raccogliere e governare i dati in cloud;'),
                 ('p', 'gestire i dispositivi di bordo;'),
                 ('p',
                  'aggiornare a distanza in modo sicuro il software dei componenti di progetto installati dai '
                  'partner.'),
                 ('t', 'La piattaforma è composta da tre parti:'),
                 ('p',
                  "un middleware di bordo eseguito su un gateway telematico dedicato, distinto dall'unità di calcolo "
                  'di percezione (OR13), basato su componenti open source consolidati per Linux embedded. Il gateway è '
                  'collegato ai bus del veicolo e alla rete di bordo dei partner;'),
                 ('p', 'un backend cloud basato su microservizi e messaggistica (MQTT, streaming di eventi);'),
                 ('p', 'un servizio di gestione dei dispositivi e degli aggiornamenti.'),
                 ('t',
                  'La sicurezza è progettata secondo ISO/SAE 21434 e UNECE R155. Il processo di aggiornamento è '
                  'compatibile con un sistema di gestione degli aggiornamenti software (SUMS) conforme a UNECE R156.'),
                 ('t',
                  "Le attività sono sviluppo sperimentale ai sensi dell'art. 1 del DD: la piattaforma è costruita come "
                  'prototipo e convalidata sui veicoli di prova in condizioni operative reali.')],
         '7.2': [('s', 'A8.1 Accesso ai dati del veicolo tramite modello dati standard (mesi 7-18)'),
                 ('e', ('Problema.', 'I dati del veicolo sono esposti in modo diverso da ogni costruttore e modello:')),
                 ('p', 'bus CAN con database di segnali proprietari;'),
                 ('p', 'porte diagnostiche;'),
                 ('p', 'interfacce dei sistemi infotainment;'),
                 ('p', 'in alcuni casi, API cloud del costruttore.'),
                 ('t',
                  'I componenti del progetto (content policy engine, applicazione di bordo, percezione, HUD) hanno '
                  'bisogno degli stessi segnali con la stessa semantica, unità e marca temporale. I segnali ADAS e DMS '
                  'di serie (per esempio stato degli avvisi, attenzione del guidatore) sono spesso disponibili solo in '
                  'parte e con frequenze diverse.'),
                 ('e',
                  ('Soluzione proposta.',
                   'Un servizio eseguito sul gateway telematico di bordo. Il gateway è un dispositivo separato '
                   "dall'unità di calcolo di percezione, così che l'accesso ai bus del veicolo resti isolato dai "
                   'carichi di calcolo dei partner. Il servizio:')),
                 ('p',
                  'acquisisce i segnali tramite adattatori specifici per interfaccia (CAN, diagnostica, '
                  'infotainment);'),
                 ('p', 'li normalizza sul modello dati standard COVESA Vehicle Signal Specification (VSS);'),
                 ('p',
                  'li espone agli altri componenti (unità di calcolo, applicazione di bordo, HUD) tramite API sulla '
                  "rete Ethernet di bordo, in sottoscrizione e in lettura, con controllo d'accesso per componente e "
                  'per segnale.'),
                 ('t',
                  'Il servizio aggiunge a ogni segnale la marca temporale di acquisizione, sincronizzata con il '
                  'riferimento di bordo, e un indicatore di qualità (valido, stimato, non disponibile). I segnali ADAS '
                  'e DMS di serie non si sviluppano ma si usano.'),
                 ('e',
                  ('Novità e incertezza.',
                   "Lo stato dell'arte offre il modello VSS e alcuni broker di segnali open source. Resta da "
                   'verificare quattro cose:')),
                 ('p',
                  'se il mapping da interfacce proprietarie a VSS possa essere configurato invece che programmato per '
                  'ogni veicolo;'),
                 ('p',
                  'se i requisiti di latenza dei componenti a valle (HUD e AR) siano rispettati con molti '
                  'sottoscrittori;'),
                 ('p', 'come rappresentare segnali ADAS e DMS non coperti da VSS;'),
                 ('p', 'come garantire che un componente acceda solo ai segnali autorizzati.'),
                 ('e', ('Metodo.', '')),
                 ('t',
                  '1. Raccolta dei requisiti di segnali, frequenze e latenze da tutti i partner, e coordinamento con '
                  "le specifiche dell'unità di calcolo (A9.4, Politecnico) per la ripartizione delle funzioni fra "
                  'gateway e unità di calcolo.'),
                 ('t',
                  '2. Progetto degli adattatori con un archetipo comune, per aggiungere nuove interfacce senza '
                  'modificare il nucleo.'),
                 ('t', '3. Estensioni VSS per i segnali mancanti.'),
                 ('t',
                  '4. Prove al banco con registrazioni CAN reali di più modelli di veicolo, poi sul veicolo di prova.'),
                 ('e',
                  ('Risultati misurabili.',
                   'Servizio di accesso ai dati del veicolo (D8.1), con catalogo dei segnali VSS, versione VSS '
                   'adottata ed estensioni, e specifica delle API. Indicatori:')),
                 ('p',
                  "prima delle prove i partner approvano l'elenco dei segnali richiesti, con unità, frequenza minima e "
                  "uso previsto. Sul veicolo di prova almeno il 90% dell'elenco è acquisito con la qualità richiesta. "
                  'I segnali assenti, inaccessibili o solo stimati sono rendicontati a parte;'),
                 ('p',
                  'per un secondo modello di veicolo, verifica al banco del riuso del mapping su registrazioni '
                  'autorizzate, con la copertura ottenuta;'),
                 ('p',
                  "latenza dall'acquisizione sul gateway alla consegna al componente p95 < 20 ms, con frequenza e "
                  'numero di sottoscrittori dichiarati;'),
                 ('p', 'tempo per integrare un nuovo modello di veicolo < 10 giorni-persona.'),
                 ('s', 'A8.2 Raccolta, archiviazione e governance dei dati in cloud (mesi 10-24)'),
                 ('e',
                  ('Problema.',
                   'I dati del veicolo, dei dispositivi di bordo e delle fonti esterne servono in cloud a più '
                   'finalità:')),
                 ('p', 'analisi;'),
                 ('p', 'addestramento dei modelli dei partner;'),
                 ('p', 'monitoraggio della flotta;'),
                 ('p', 'valutazione delle prove.'),
                 ('t',
                  'La connettività è intermittente e i volumi sono variabili. Ogni dato deve essere usato solo dai '
                  'componenti e per le finalità autorizzate, in conformità al GDPR (i dati di posizione e del DMS sono '
                  'dati personali) e al Data Act.'),
                 ('e',
                  ('Soluzione proposta.',
                   'La raccolta usa componenti standard di messaggistica e archiviazione in cloud. Lo sviluppo si '
                   'concentra su ciò che è specifico del veicolo:')),
                 ('p', 'invio differito dei segnali VSS con ordinamento e deduplicazione dopo lunghe assenze di rete;'),
                 ('p',
                  'associazione di ogni dato a veicolo, occupante (quando pertinente), finalità consentite e '
                  'scadenza;'),
                 ('p',
                  'accesso ai dati del veicolo secondo il Data Act, distinto per utente richiedente e per occupanti '
                  "diversi dall'utente."),
                 ('t',
                  'Le regole di conservazione, di accesso e di pseudonimizzazione sono definite per componente e per '
                  'finalità e applicate dalla piattaforma tramite un sistema di identità e permessi comune.'),
                 ('e',
                  ('Novità e incertezza.',
                   "L'incertezza riguarda la possibilità di garantire nello stesso sistema due cose:")),
                 ('p', 'consegna senza perdite con connettività intermittente;'),
                 ('p', 'applicazione automatica delle regole per finalità.'),
                 ('t',
                  'Il tutto con costi e latenze compatibili con una flotta in crescita. Riguarda anche la '
                  "tracciabilità dell'origine del dato (lineage) attraverso fusione e trasformazioni."),
                 ('e', ('Metodo.', '')),
                 ('t', '1. Progetto della pipeline e del modello di metadati.'),
                 ('t', '2. Prove di perdita e duplicazione con interruzioni di rete simulate e reali.'),
                 ('t', '3. Verifica delle regole di accesso con casi di prova per ogni coppia componente-finalità.'),
                 ('t', '4. Misure sui veicoli di prova.'),
                 ('t',
                  'Prima della raccolta, per ogni flusso si documentano finalità, soggetti coinvolti, ruoli privacy, '
                  'base giuridica, destinatari e tempi di conservazione. Si valuta la necessità di una valutazione '
                  "d'impatto (DPIA) prima delle prove con persone. Per il DMS si privilegiano indicatori derivati "
                  'elaborati a bordo. Il trasferimento di dati grezzi e il riuso per addestramento richiedono una '
                  'motivazione specifica. I test comprendono accessi consentiti e negati, scadenza e cancellazione dei '
                  'dati.'),
                 ('e', ('Risultati misurabili.', 'Piattaforma dati in cloud (D8.2). Indicatori:')),
                 ('p',
                  'percentuale di dati raccolti senza perdite > 99,9% anche dopo interruzioni di rete fino a 24 h;'),
                 ('p', 'ritardo fra evento a bordo e disponibilità in cloud p95 < 5 s con rete disponibile;'),
                 ('p', 'copertura delle regole di accesso verificate da test 100%.'),
                 ('s', 'A8.3 Device management e aggiornamento OTA (mesi 13-28)'),
                 ('e',
                  ('Problema.',
                   'Il software di bordo del progetto proviene da cinque partner e gira su più dispositivi:')),
                 ('p', 'unità di calcolo;'),
                 ('p', 'gateway;'),
                 ('p', 'HUD;'),
                 ('p', 'dispositivi per occhiali e visori.'),
                 ('t',
                  'Deve essere aggiornato a distanza senza mai lasciare il dispositivo inutilizzabile, garantendo '
                  'autenticità e integrità di ogni aggiornamento e mantenendo traccia di quale versione è installata '
                  'su quale veicolo. Il canale di aggiornamento è la superficie di attacco più critica del sistema.'),
                 ('e',
                  ('Soluzione proposta.',
                   "Il servizio di device management copre l'intero ciclo di vita del dispositivo:")),
                 ('p', 'registrazione con identità crittografica per dispositivo;'),
                 ('p', 'monitoraggio dello stato;'),
                 ('p', 'configurazione;'),
                 ('p', 'comandi remoti;'),
                 ('p', 'dismissione.'),
                 ('t',
                  'Per il singolo dispositivo Linux si adottano meccanismi di aggiornamento open source consolidati '
                  '(aggiornamento atomico con ripristino, pacchetti firmati), che non sono oggetto di sviluppo. Lo '
                  'sviluppo riguarda il livello del veicolo:'),
                 ('p', 'formato di pacchetto e manifesto di versione comuni per il software applicativo dei partner;'),
                 ('p', 'aggiornamento coordinato di più dispositivi e fornitori, con dipendenze fra versioni;'),
                 ('p',
                  'campagne di aggiornamento per gruppi di veicoli, con precondizioni (veicolo fermo, carica '
                  'sufficiente).'),
                 ('t', 'La sicurezza segue ISO/SAE 21434:'),
                 ('p', 'analisi delle minacce e dei rischi (TARA) del canale OTA e della piattaforma;'),
                 ('p', 'avvio sicuro;'),
                 ('p', 'protezione delle chiavi in elemento sicuro (TPM o HSM);'),
                 ('p', 'registro delle versioni installate per veicolo, a supporto di un SUMS conforme a UNECE R156.'),
                 ('t',
                  'Il servizio OTA gestisce il gateway e i componenti di progetto per i quali il partner responsabile '
                  'dichiara interfaccia di aggiornamento, versioni compatibili, condizioni di installazione e '
                  "procedura di recupero. Le centraline di serie sono escluse. Anitia cura l'analisi dei rischi del "
                  'gateway e della catena OTA, Aubay quella di applicazione e contenuti (A3.4). Le interfacce '
                  'condivise sono verificate insieme. Il penetration test del gateway e del canale OTA è affidato a un '
                  'fornitore esterno.'),
                 ('e',
                  ('Novità e incertezza.',
                   'Per singoli dispositivi Linux esistono strumenti di aggiornamento maturi. Restano aperti quattro '
                   'punti:')),
                 ('p',
                  'coordinare un aggiornamento coerente di più dispositivi e di software di più fornitori sullo stesso '
                  'veicolo, con dipendenze fra versioni;'),
                 ('p', 'garantire il ripristino in caso di fallimento parziale;'),
                 ('p', 'rispettare le precondizioni di sicurezza del veicolo;'),
                 ('p',
                  'applicare una catena di fiducia resistente alla compromissione di un singolo server o chiave, '
                  "secondo l'approccio Uptane."),
                 ('e', ('Metodo.', '')),
                 ('t', '1. Analisi TARA.'),
                 ('t', '2. Progetto del formato di pacchetto e del manifesto di versione per veicolo.'),
                 ('t', '3. Sviluppo incrementale su banco con i dispositivi dei partner.'),
                 ('t',
                  "4. Prove di guasto: interruzione di alimentazione e di rete durante l'aggiornamento, pacchetti "
                  'corrotti o non firmati.'),
                 ('t', '5. Penetration test esterno.'),
                 ('e',
                  ('Risultati misurabili.',
                   'Servizio di device management e OTA (D8.3) e rapporto TARA. D8.3 documenta i ruoli Uptane '
                   'adottati, la verifica dei metadati e delle versioni autorizzate e le evidenze utilizzabili dal '
                   'costruttore nei propri processi CSMS e SUMS. Indicatori:')),
                 ('p',
                  'installazioni riuscite in condizioni nominali e recuperi riusciti nelle prove di guasto, misurati '
                  'separatamente. Una prova è superata solo se il veicolo torna a una combinazione di versioni '
                  'autorizzata e funzionante (obiettivo: 100% di recuperi, nessun dispositivo inutilizzabile);'),
                 ('p', 'pacchetti non firmati o alterati rifiutati 100%;'),
                 ('p', 'vulnerabilità critiche aperte dopo il penetration test 0.'),
                 ('s', 'A8.4 Fonti esterne, affidabilità e scalabilità (mesi 22-33)'),
                 ('e',
                  ('Problema.',
                   'I metodi sviluppati in OR7 vanno portati dentro la piattaforma e resi disponibili in esercizio. La '
                   'piattaforma deve dimostrare di reggere un numero di veicoli molto superiore a quello dei veicoli '
                   'di prova, con guasti dei componenti cloud e connettività degradata.')),
                 ('e', ('Soluzione proposta.', 'Integrazione nella piattaforma di quattro elementi:')),
                 ('p', 'connettori verso le fonti esterne;'),
                 ('p', 'modulo di fusione (D7.2);'),
                 ('p', 'criteri di promozione ad avviso (D7.3);'),
                 ('p', 'distribuzione degli eventi esterni ai veicoli interessati per area geografica.'),
                 ('t',
                  'A questo si aggiungono un banco di prova con flotte simulate (simulatori di veicolo e di '
                  "dispositivo che riproducono traffico reale registrato) e un'architettura cloud con scalabilità "
                  'orizzontale dei broker e dei servizi di ingestione.'),
                 ('e',
                  ('Novità e incertezza.',
                   "L'incertezza riguarda il comportamento del sistema completo sotto carico:")),
                 ('p', 'se distribuzione geografica degli eventi, ingestione e device management scalino linearmente;'),
                 ('p', 'quali componenti diventino il collo di bottiglia;'),
                 ('p', 'se i tempi di ripristino dopo un guasto restino entro i limiti richiesti dai servizi a valle.'),
                 ('e', ('Metodo.', '')),
                 ('t', '1. Prove di carico progressive con flotte simulate di dimensione crescente.'),
                 ('t', '2. Iniezione di guasti: caduta di nodi, broker e rete.'),
                 ('t', '3. Prove di affidabilità di lunga durata sui veicoli di prova.'),
                 ('t', "4. Analisi dei colli di bottiglia e iterazione sull'architettura."),
                 ('t',
                  'Il profilo di carico è ricavato da tracce reali dei veicoli e fissato prima della campagna: '
                  'connessioni simultanee, messaggi al secondo per veicolo, dimensione dei messaggi, durata, '
                  'destinatari per evento, risorse cloud impiegate. A 10.000 veicoli simulati si misurano '
                  'separatamente ingestione, distribuzione geografica e recupero dopo riconnessione, riportando '
                  "duplicati, perdite, latenza p95 e costo della prova. La completezza dopo un'interruzione è "
                  'calcolata sugli identificativi univoci emessi a bordo. Le prove riguardano la piattaforma IoT '
                  '(ingestione, device management, distribuzione degli eventi esterni). Le prove di carico della '
                  'piattaforma di erogazione dei contenuti restano in A3.5 (Aubay), con cui si concordano profili di '
                  'flotta comuni.'),
                 ('e', ('Risultati misurabili.', 'Rapporto delle prove (D8.4). Indicatori:')),
                 ('p',
                  'numero di veicoli gestibili con le latenze di A8.2 rispettate (obiettivo ≥ 10.000 veicoli '
                  'simulati);'),
                 ('p', "ritardo di distribuzione di un evento esterno ai veicoli dell'area p95 < 2 s;"),
                 ('p', 'disponibilità del servizio nelle prove di lunga durata ≥ 99,5%;'),
                 ('p', 'tempo di ripristino dopo guasto di un nodo < 5 min.')]}}
