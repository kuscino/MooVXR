# -*- coding: utf-8 -*-
# Generato da importa_anitia_24nov.py da Piano_di_Sviluppo_scheletro_v15_Anitia_r2.docx. Non modificare a mano.
III_3_2 = [('e',
  ('Sviluppo del settore.',
   'I risultati di Anitia cambiano il modo in cui i servizi di bordo accedono al veicolo e ai dati esterni. Oggi ogni '
   'servizio deve integrarsi con le interfacce proprietarie dei singoli costruttori e con fonti stradali che non '
   "dichiarano qualità e attualità del dato. Con MooVXR l'accesso ai segnali del veicolo passa per un modello dati "
   "standard (COVESA VSS), la qualità del dato esterno diventa un attributo esplicito e l'aggiornamento del software "
   "di bordo è coordinato a livello di veicolo. Cambia così l'architettura dei servizi: l'applicazione non dipende più "
   'dal singolo veicolo o dalla singola fonte, ma si collega a un livello comune di segnali, qualità e versioni. Ne '
   'beneficiano soprattutto i soggetti che restano fuori dai grandi programmi dei costruttori: gestori di flotte, '
   'allestitori di veicoli speciali, fornitori di secondo livello e integratori ITS.')),
 ('e',
  ('Trasporto turistico.',
   'Sugli autobus turistici la stessa piattaforma permette di gestire a distanza il software e i contenuti di più '
   "dispositivi a bordo e di fornire ai servizi per i passeggeri dati di posizione e di percorso con un'affidabilità "
   'dichiarata.')),
 ('e',
  ('Veicoli per la sicurezza e il soccorso.',
   'I criteri di affidabilità e di promozione ad avviso si applicano alle informazioni ricevute da centrali operative '
   "e infrastruttura, dove un avviso sbagliato o in ritardo ha conseguenze operative. L'aggiornamento firmato e "
   'tracciato del software è un requisito per i mezzi in servizio.')),
 ('e',
  ('Ricognizione del territorio.',
   'I veicoli che raccolgono dati georeferenziati operano spesso con connettività intermittente. La raccolta senza '
   "perdite, la marcatura temporale dei dati e le regole d'uso per finalità sviluppate in OR8 sono riutilizzabili "
   'direttamente. Queste capacità potranno integrarsi con le competenze del gruppo in geografia informatica.')),
 ('e',
  ('Reti di dispositivi distribuiti.',
   'Nei servizi che Anitia gestisce per telecomunicazioni, gioco ed energia, i metodi per riconoscere eventi tardivi, '
   "duplicati o fuori sequenza e l'aggiornamento coordinato di dispositivi eterogenei migliorano la riconciliazione "
   'degli eventi e la gestione del software installato in campo.')),
 ('e',
  ('Cambiamenti nei processi.',
   'Il registro delle versioni installate e le evidenze della catena di aggiornamento producono la documentazione '
   'richiesta dai Regolamenti UNECE n. 155 e n. 156. Questo riduce il costo di conformità per i fornitori più piccoli '
   "e consente di aggiornare le funzioni durante la vita del veicolo senza sostituire l'hardware, prolungando la vita "
   'utile dei sistemi di bordo.'))]

I_1 = [['testo',
  [['Anitia S.r.l. è una società di diritto italiano iscritta alla CCIAA di Verona con numero di iscrizione al '
    'registro delle imprese n. 406179, codice fiscale e partita IVA n. 04265340234, operante nel settore della '
    'consulenza e della system integration, con circa 15 dipendenti. Il capitale sociale è detenuto per il 51% da '
    'Dodifferent S.r.l. e per il 49% da Vahana S.r.l. La società è amministrata da un consiglio di amministrazione '
    'composto da Diego Melchiori, presidente e amministratore delegato, e da Mauro Grandotto.',
    False,
    False]]],
 ['sotto', 'Struttura organizzativa e produttiva'],
 ['testo',
  [['Anitia opera con circa 15 dipendenti. Le attività del progetto si svolgono presso la sede operativa di Sona (VR).',
    False,
    False]]],
 ['testo',
  [['La struttura tecnica comprende profili di delivery management, analisi funzionale, sviluppo software, '
    'architettura di sistema e integrazione di dispositivi IoT.',
    False,
    False]]],
 ['testo',
  [["L'organizzazione si articola in due business unit, Customer Engagement e System Integration & IoT, che servono "
    'clienti diversi ma condividono lo stesso nucleo tecnologico: architetture cloud native e API-first, integrazione '
    'e rilascio continui, esercizio di piattaforme con livelli di servizio contrattuali. La società ha sede operativa '
    'a Sona (VR) e un ufficio a Milano.',
    False,
    False]]],
 ['testo',
  [['Dal marzo 2024 Anitia fa parte del gruppo Different Factory, gruppo italiano indipendente del settore IT che '
    'integra marketing, pubblicità, dati e tecnologia. La controllante Dodifferent S.r.l., con sede a Milano, detiene '
    'partecipazioni di maggioranza in società con competenze complementari: Trilogis S.r.l., specializzata in '
    'geografia informatica e geomarketing, con una forte presenza nella Pubblica Amministrazione; Happy Finish S.r.l., '
    'agenzia di creative technology attiva in CGI, animazione, realtà aumentata e virtuale, con sedi a Milano, Londra '
    'e Portland; società specializzate in master data management, analisi dei dati, applicazioni mobile e web, '
    'commercio elettronico e marketing digitale.',
    False,
    False]]],
 ['testo',
  [['Il gruppo ha sei sedi (Milano, Verona, Trento, Reggio Calabria, Londra e Portland), gestisce oltre 400 progetti '
    "all'anno ed elabora ogni anno oltre 500 milioni di record geografici e da dispositivi IoT. Ogni società opera in "
    'autonomia e con un proprio ambito di specializzazione; nel gruppo Anitia presidia il customer engagement e la '
    'system integration & IoT.',
    False,
    False]]],
 ['img_originale'],
 ['sotto', 'Management aziendale'],
 ['testo',
  [['Il management aziendale è rappresentato essenzialmente da Diego Melchiori che riveste anche la carica di '
    'Presidente del CdA e AD. Nell’ambito del gruppo di lavoro che gestisce sono presenti figure senior che hanno '
    'maturato decennali esperienze nel settore dell’Information Technology. Alberto Gaspari, General Manager, dirige '
    "la divisione tecnica ed è il responsabile tecnico del progetto. Martina Callegaro è responsabile dell'area "
    'amministrativa e contabile, compresa la rendicontazione dei progetti finanziati.',
    False,
    False]]],
 ['sotto', 'Descrizione della struttura dedicata ad attività di ricerca e sviluppo'],
 ['testo',
  [['Anitia dispone di un gruppo dedicato alla ricerca e sviluppo di 14 persone, fra profili senior e tecnici, che '
    "opera presso la sede di Sona (VR). Il gruppo è attualmente impegnato in un progetto di R&S finanziato nell'ambito "
    "degli Accordi per l'innovazione (DM 31/12/2021, prog. F/310276/04/X56), che si conclude nell'ottobre 2027. Le ore "
    'dedicate alla R&S sono state 906 nel 2024, 8.956 nel 2025 e 5.371 nei primi cinque mesi del 2026. In precedenza '
    'la società ha partecipato a un progetto di innovazione nella mobilità finanziato dalla Regione Veneto nel 2020.',
    False,
    False]]],
 ['tab_grezza',
  [['Ubicazione dei principali Centri di Competenza/R&D', 'Area tematica', 'Personale Coinvolto'],
   ['Sona (VR)',
    'Piattaforme IoT e cloudIntegrazione di sistemi e dispositiviMetodologie e ambienti di sviluppo',
    '14']]],
 ['testo',
  [['Le attività di ricerca si svolgono presso la sede di Sona (VR), anche in collaborazione con università.',
    False,
    False]]],
 ['testo',
  [['La sede operativa di Sona (VR) dispone di circa 300 mq di spazi attrezzati, con postazioni di lavoro e rete '
    'aziendale protetta, e di ambienti di sviluppo e test basati su container e su pipeline di integrazione e rilascio '
    'continui, che rendono rapide e riproducibili le iterazioni fra ricerca e sviluppo. I dati sono trattati su '
    "sistemi in data center e su infrastrutture cloud con regione nell'Unione europea.",
    False,
    False]]]]

I_2 = [['sotto', 'Attività e mercati serviti'],
 ['testo',
  [['Anitia sviluppa piattaforme cloud e servizi di integrazione per telecomunicazioni, finanza e commercio.',
    False,
    False]]],
 ['testo',
  [['Anitia è una software house che opera esclusivamente nel mercato business-to-business. Fondata a Sona (VR) nel '
    'luglio 2014 come consorzio di esperti tecnologici, è oggi una società di circa 15 dipendenti con oltre 50 clienti '
    'attivi. Opera come system integrator in telecomunicazioni, banche e servizi finanziari, commercio, trasporti, '
    'gioco, utility ed energia. I problemi posti dai clienti sono in larga parte comuni ai diversi settori: '
    'raccogliere e normalizzare grandi flussi di dati, integrare sistemi eterogenei, mantenere in esercizio '
    'piattaforme critiche con livelli di servizio contrattuali.',
    False,
    False]]],
 ['testo',
  [["L'offerta copre l'intero ciclo di un progetto: analisi del contesto, dei dati disponibili e degli obiettivi del "
    'cliente (Strategy); sviluppo e integrazione di soluzioni con architetture scalabili, cloud native e API-first '
    '(Technology); piattaforme per coinvolgere e fidelizzare gli utenti finali (Engagement).',
    False,
    False]]],
 ['testo',
  [['La business unit Customer Engagement progetta, sviluppa e gestisce piattaforme proprietarie, vendute in licenza e '
    'come servizio:',
    False,
    False]]],
 ['punto',
  'Worldngage, piattaforma di loyalty modulare con moduli di gaming, marketplace, instant win, member get member e '
  'analytics;'],
 ['punto', 'CinePlatform, distribuzione di biglietti cinema integrata con i sistemi di cassa delle sale;'],
 ['punto', 'Benefit Suite, piattaforma web e app per enti e associazioni che erogano benefici agli associati;'],
 ['punto',
  'SmartSoci, servizi digitali per i soci delle Banche di Credito Cooperativo: eventi, assemblee digitali, marketplace '
  'di vantaggi.'],
 ['testo',
  [['Con WindTre, e prima con H3G, la collaborazione prosegue da oltre quindici anni sul programma di fedeltà Winday, '
    'rivolto a milioni di utenti. Per Trenord Anitia ha realizzato una piattaforma di community e loyalty per i '
    'viaggiatori del trasporto regionale lombardo, integrata con i sistemi di biglietteria. Fra i clienti figurano '
    'anche Very Mobile, BCC Milano ed Euronics.',
    False,
    False]]],
 ['testo',
  [['La business unit System Integration & IoT vende competenza ingegneristica su tre filoni:', False, False]]],
 ['punto',
  'integrazione di sistemi e sviluppo di piattaforme: architetture API-first e cloud native, in particolare su AWS, '
  'strati di integrazione verso sistemi eterogenei, pipeline di integrazione e rilascio continui, sicurezza degli '
  'accessi e disaster recovery;'],
 ['punto',
  'application management: presa in carico di piattaforme in produzione, con manutenzione correttiva ed evolutiva, '
  'monitoraggio e livelli di servizio contrattuali;'],
 ['punto',
  "IoT: progettazione e realizzazione di sistemi cloud native per l'ingestione di eventi in tempo reale, con regole di "
  'allarme configurabili, escalation automatica, notifiche multicanale e monitoraggio unificato di asset distribuiti.'],
 ['testo',
  [['I ricavi delle vendite e delle prestazioni di Anitia sono passati da € 1.806.475 nel 2024 a € 2.509.805 nel 2025. '
    'Questi importi si riferiscono al portafoglio aziendale complessivo. La crescita è di circa il 39%. Per il '
    'triennio 2027-2029 la società prevede ricavi complessivi di circa 3,5, 4,2 e 5,0 milioni di euro, senza '
    'considerare i risultati di MooVXR.',
    False,
    False]]],
 ['testo',
  [['Per WindTre ha integrato applicazioni mobili e sistemi di cassa per verificare i voucher in tempo reale. Per la '
    'Banca BCC di Milano ha realizzato una piattaforma per la comunicazione con i soci e la gestione degli accessi '
    'agli eventi. Le attività svolte con SISAL e MOONEY hanno riguardato il collegamento fra punti vendita e sistemi '
    'centrali. Sono esperienze rilevanti per MooVXR perché richiedono di identificare l’origine di un evento, '
    'verificarne la validità e impedirne l’elaborazione duplicata.',
    False,
    False]]],
 ['testo',
  [['Altri riferimenti sono vicini ai temi del progetto. Per Sisal Anitia ha sviluppato la gestione centralizzata dei '
    'terminali di gioco, con migrazione dei sistemi operativi su scala nazionale, aggiornamenti automatizzati, '
    'monitoraggio in tempo reale e cruscotti per il team operativo. Per Minsait (gruppo Indra) ha realizzato un '
    "sistema di raccolta eventi e allarmi per le cabine di distribuzione dell'energia elettrica, che normalizza in "
    'tempo reale gli eventi di migliaia di punti di campo e li presenta in un cruscotto unificato. Per Ifitalia, oggi '
    'Fabrick (gruppo BNP Paribas), gestisce dal 2016 il portale di remote factoring Mediana.',
    False,
    False]]],
 ['sotto', 'Consolidamento delle piattaforme e dei servizi esistenti'],
 ['testo',
  [['I metodi sviluppati in MooVXR per riconoscere messaggi tardivi, duplicati o fuori sequenza potranno essere '
    'riutilizzati nei servizi che Anitia gestisce per operatori di telecomunicazioni e reti distribuite. Un punto '
    'vendita che riprende la connessione dopo un’interruzione presenta un’esigenza analoga a quella di un nodo '
    'stradale che torna disponibile. La riconciliazione degli eventi e la possibilità di ricostruirne l’ordine possono '
    'migliorare sia il servizio al cliente sia la diagnosi dei malfunzionamenti. Le competenze sviluppate su gestione '
    'dei dispositivi e aggiornamento sicuro del software potranno inoltre rafforzare i servizi di integrazione e di '
    'gestione applicativa che Anitia offre ai propri clienti.',
    False,
    False]]],
 ['sotto', 'Nuovi sbocchi nella cooperazione fra veicolo e strada'],
 ['testo',
  [['Anitia potrà rivolgersi ai concessionari stradali, agli integratori ITS, agli operatori telematici e ai fornitori '
    'di servizi per flotte. L’offerta riguarda i connettori fra i nodi di bordo e stradali, la verifica temporale e '
    'geografica dei messaggi e il servizio applicativo che rende disponibile un evento ai sistemi del gestore. Le '
    'alternative per il committente sono le piattaforme telematiche proprietarie e i servizi di integrazione inclusi '
    'nell’acquisto degli apparati stradali. Con la piattaforma sviluppata in OR8 Anitia potrà offrire anche servizi di '
    'accesso ai dati del veicolo, gestione dei dispositivi di bordo e aggiornamento software a distanza a costruttori, '
    'fornitori di primo livello e gestori di flotte.',
    False,
    False]]],
 ['sotto', 'Prospettive nel triennio'],
 ['testo',
  [['Il primo passaggio è dimostrare che la stessa informazione resta riconoscibile nel transito fra apparati diversi. '
    'A seguito della sperimentazione Anitia potrà proporre una prima integrazione a commessa, quindi il collegamento '
    'di ulteriori nodi o tratti stradali. Assistenza operativa e aggiornamento dei connettori potranno essere offerti '
    'come servizi continuativi, secondo il numero di apparati collegati e i livelli di servizio richiesti. Per la '
    'piattaforma di bordo il percorso prevede una prima adozione su flotte sperimentali, seguita da servizi gestiti di '
    'monitoraggio e aggiornamento.',
    False,
    False]]],
 ['testo', [['Principali clienti già serviti dalla società in Italia e in Europa', False, False]]],
 ['img_originale']]

III_1_1 = [['testo',
  [['Anitia impiega analisti software, sviluppatori senior, progettisti di sistemi e personale con esperienza IoT. Le '
    'attività del progetto si svolgono presso la sede di Sona (VR). Il coordinamento aziendale fa capo a Diego '
    'Melchiori, presidente del consiglio di amministrazione e amministratore delegato. Il responsabile tecnico per '
    'MooVXR è Alberto Gaspari.',
    False,
    False]]],
 ['testo', [['Competenze.', True, False], [' Le competenze di Anitia più pertinenti per MooVXR sono:', False, False]]],
 ['punto', 'infrastrutture cloud native e backend a microservizi con approccio API-first, su AWS, Azure e GCP;'],
 ['punto',
  "sistemi IoT per l'ingestione, la validazione e l'elaborazione in tempo reale di eventi da dispositivi distribuiti "
  'sul territorio;'],
 ['punto',
  'gestione centralizzata e aggiornamento automatizzato del software di dispositivi in campo, maturati sui terminali '
  'di gioco gestiti su scala nazionale;'],
 ['punto',
  'esercizio di piattaforme critiche con livelli di servizio contrattuali e cruscotti di controllo unificati per '
  "l'operatore."],
 ['testo',
  [['Maturità tecnologica.', True, False],
   [" Anitia porta le soluzioni dalla prototipazione all'esercizio e gestisce da anni piattaforme in produzione su "
    'scala nazionale. Il passaggio di maturità segue quattro principi: validazione incrementale con rilasci frequenti '
    'e controllati; test automatizzati nelle pipeline di integrazione e rilascio continui; architetture modulari, che '
    'consentono di sostituire un componente senza compromettere il sistema; verifica delle prestazioni in condizioni '
    "via via più vicine all'uso reale, con criteri di passaggio definiti in anticipo.",
    False,
    False]]],
 ['testo',
  [['Coordinamento con soggetti terzi.', True, False],
   [' Per i clienti enterprise Anitia integra piattaforme proprie con sistemi di terze parti, lavora con i team '
    'interni del cliente e con altri fornitori e gestisce servizi critici con livelli di servizio contrattuali. Ha '
    'esperienza nella gestione amministrativa di progetti di ricerca e sviluppo finanziati con fondi pubblici: regole '
    'di spesa, tracciabilità dei costi, rendicontazione e verifiche.',
    False,
    False]]],
 ['sotto', 'Dati del veicolo, cooperazione fra bordo e strada e aggiornamento del software di bordo'],
 ['testo',
  [['In MooVXR Anitia definisce il contenuto degli eventi scambiati fra il nodo stradale e quello di bordo. Per ogni '
    'messaggio occorre associare origine, posizione, tempo di osservazione e durata di validità. La ricerca riguarda '
    'il comportamento del servizio quando due nodi descrivono lo stesso evento oppure quando un messaggio arriva '
    'tardi, fuori sequenza o dopo un’interruzione.',
    False,
    False]]],
 ['testo',
  [["In OR8 Anitia realizza la piattaforma che costituisce l'unico punto di accesso al veicolo per i componenti del "
    'progetto. La piattaforma legge i segnali del veicolo secondo il modello COVESA VSS su un gateway dedicato, '
    'raccoglie e governa i dati in cloud, gestisce i dispositivi di bordo e aggiorna a distanza il software dei '
    'partner, compresi i modelli AI. La sicurezza del gateway e della catena di aggiornamento è progettata secondo '
    'ISO/SAE 21434 e UNECE R155, in modo compatibile con un sistema di gestione degli aggiornamenti conforme a R156.',
    False,
    False]]],
 ['testo',
  [['Nel dimostratore Anitia integra i connettori con le interfacce di Aubay. Registra i tempi di emissione e '
    'ricezione e rende disponibili al Politecnico le tracce necessarie per confrontare i casi con e senza il '
    'contributo del nodo stradale. Il risultato atteso è una procedura documentata per accettare, scartare o '
    'riconciliare osservazioni in funzione della loro qualità e attualità.',
    False,
    False]]]]

OR78 = [('La verità di riferimento viene dai passaggi dei veicoli di prova e dalle chiusure ufficiali degli eventi.',
  'La verità di riferimento viene dai passaggi dei veicoli di prova e dalle chiusure ufficiali degli eventi. Per '
  'posizione e tempo degli eventi si usa il riferimento indipendente di localizzazione di A9.1 (OR9). I criteri per '
  'trattare i dati in ritardo o fuori sequenza seguono lo schema comune di affidabilità definito in A9.3.'),
 ('Entro il mese 16, consegna ad Aubay (OR1) della candidatura ad avviso, con confidenza, pertinenza e scadenza. La '
  "decisione di presentazione resta al content policy engine, che applica le informazioni sull'attenzione del "
  'guidatore prodotte da OR10.',
  'Entro il mese 16, consegna a OR1 della candidatura ad avviso, con confidenza, pertinenza e scadenza. La decisione '
  "di presentazione resta al content policy engine, che applica le informazioni sull'attenzione del guidatore prodotte "
  'da OR10.'),
 ("Soluzione proposta. Una campagna di prove sull'area pilota con il prototipo di fusione e promozione ad avviso, "
  'collegato alle unità V2X di prova (RSU e OBU) e alle fonti in tempo reale. Il dimostratore integrato è disponibile '
  'solo dal mese 25 (A14.4). Per questo le prove si svolgono sul veicolo di prova messo a disposizione da GSNet (OR4), '
  'in uso nello stesso periodo. Prima del mese 14 Anitia predispone un acquisitore dei segnali minimi, con orologio '
  'sincronizzato e registrazione locale. Veicolo, percorsi, area e autorizzazione delle RSU sono da concordare con '
  "GSNet e con il gestore dell'area. La verifica sul dimostratore completo confluisce nelle prove su strada di A14.5.",
  "Soluzione proposta. Una campagna di prove sull'area pilota con il prototipo di fusione e promozione ad avviso, "
  'collegato alle unità V2X di prova (RSU e OBU) e alle fonti in tempo reale. Il dimostratore integrato è disponibile '
  'solo dal mese 25 (A14.4). Per questo le prove si svolgono sul veicolo di prova messo a disposizione da GSNet (OR4), '
  'in uso nello stesso periodo. Prima del mese 14 Anitia predispone un acquisitore dei segnali minimi, con orologio '
  'sincronizzato e registrazione locale. Tratte e autorizzazione delle RSU sono definite con Autostrada del Brennero '
  'S.p.A., sperimentatore esterno del progetto. La verifica sul dimostratore completo confluisce nelle prove su strada '
  'di A14.5.'),
 ('Ogni misura è confrontata con la verità di riferimento rilevata sul percorso.',
  'Ogni misura è confrontata con la verità di riferimento rilevata sul percorso. Messaggi, log temporali e tracce '
  'delle prove sono resi disponibili come dati di ingresso per le verifiche sperimentali di OR9 e OR10, anche per i '
  'casi con e senza il contributo del nodo stradale.'),
 ('Risultati misurabili. Rapporto delle prove (D7.4), con:',
  'Risultati misurabili. Rapporto delle prove (D7.4), che include il confronto con il riferimento di localizzazione di '
  'A9.1, con:'),
 ('1. Raccolta dei requisiti di segnali, frequenze e latenze da tutti i partner, e coordinamento con le specifiche '
  "dell'unità di calcolo (A9.4, Politecnico) per la ripartizione delle funzioni fra gateway e unità di calcolo.",
  '1. Raccolta dei requisiti di segnali, frequenze e latenze dagli OR che usano i dati del veicolo, e allineamento con '
  "le specifiche dell'unità di calcolo di A9.4 per la ripartizione delle funzioni fra gateway e unità di calcolo."),
 ("prima delle prove i partner approvano l'elenco dei segnali richiesti, con unità, frequenza minima e uso previsto. "
  "Sul veicolo di prova almeno il 90% dell'elenco è acquisito con la qualità richiesta. I segnali assenti, "
  'inaccessibili o solo stimati sono rendicontati a parte;',
  "prima delle prove l'elenco dei segnali richiesti, con unità, frequenza minima e uso previsto, è fissato sulla base "
  'dei requisiti degli OR che usano i dati del veicolo (OR1, OR3, OR5, OR10, OR14). Sul veicolo di prova almeno il 90% '
  "dell'elenco è acquisito con la qualità richiesta. I segnali assenti, inaccessibili o solo stimati sono rendicontati "
  'a parte;'),
 ('Problema. Il software di bordo del progetto proviene da cinque partner e gira su più dispositivi:',
  'Problema. Il software di bordo del progetto proviene da più obiettivi realizzativi e gira su più dispositivi:'),
 ('Il servizio OTA gestisce il gateway e i componenti di progetto per i quali il partner responsabile dichiara '
  'interfaccia di aggiornamento, versioni compatibili, condizioni di installazione e procedura di recupero. Le '
  'centraline di serie sono escluse. Il servizio distribuisce anche i modelli AI dei partner, secondo i criteri di '
  "rilascio e di ritorno alla versione precedente definiti in A14.3. Anitia cura l'analisi dei rischi del gateway e "
  'della catena OTA, Aubay quella di applicazione e contenuti (A14.2). Le interfacce condivise sono verificate '
  'insieme. Il penetration test del gateway e del canale OTA è affidato a un fornitore esterno.',
  "Il servizio OTA gestisce il gateway e i componenti di progetto per i quali l'OR di provenienza definisce "
  'interfaccia di aggiornamento, versioni compatibili, condizioni di installazione e procedura di recupero. Le '
  'centraline di serie sono escluse. Il servizio distribuisce anche i modelli AI prodotti negli altri OR, secondo i '
  "criteri di rilascio e di ritorno alla versione precedente definiti in A14.3. L'attività comprende l'analisi dei "
  "rischi del gateway e della catena OTA; l'analisi di applicazione e contenuti e la verifica delle interfacce "
  'condivise sono svolte in A14.2. Il penetration test del gateway e del canale OTA è affidato a un fornitore '
  'esterno.'),
 ('3. Sviluppo incrementale su banco con i dispositivi dei partner.',
  '3. Sviluppo incrementale su banco con i dispositivi degli altri OR.'),
 ('Il profilo di carico è ricavato da tracce reali dei veicoli e fissato prima della campagna: connessioni simultanee, '
  'messaggi al secondo per veicolo, dimensione dei messaggi, durata, destinatari per evento, risorse cloud impiegate. '
  'A 10.000 veicoli simulati si misurano separatamente ingestione, distribuzione geografica e recupero dopo '
  "riconnessione, riportando duplicati, perdite, latenza p95 e costo della prova. La completezza dopo un'interruzione "
  'è calcolata sugli identificativi univoci emessi a bordo. Le prove riguardano la piattaforma IoT (ingestione, device '
  'management, distribuzione degli eventi esterni). Le prove di carico del sistema completo si svolgono '
  "nell'integrazione del dimostratore (A14.4, Aubay), con cui si concordano profili di flotta comuni.",
  'Il profilo di carico è ricavato da tracce reali dei veicoli e fissato prima della campagna: connessioni simultanee, '
  'messaggi al secondo per veicolo, dimensione dei messaggi, durata, destinatari per evento, risorse cloud impiegate. '
  'A 10.000 veicoli simulati si misurano separatamente ingestione, distribuzione geografica e recupero dopo '
  "riconnessione, riportando duplicati, perdite, latenza p95 e costo della prova. La completezza dopo un'interruzione "
  'è calcolata sugli identificativi univoci emessi a bordo. Le prove riguardano la piattaforma IoT (ingestione, device '
  'management, distribuzione degli eventi esterni). Le prove di carico del sistema completo si svolgono '
  "nell'integrazione del dimostratore (A14.4), con profili di flotta allineati a quelli di questa attività.")]

III_2_1 = [('e',
  ('Risorse strumentali possedute.',
   'Anitia dispone di un ambiente di sviluppo e integrazione continua, con repository Git e pipeline automatiche di '
   'compilazione, analisi del codice, test e rilascio, usato per il software di OR7 e OR8. Dispone inoltre di un '
   'sistema di build containerizzato per la generazione riproducibile di immagini Linux embedded (Yocto) per '
   'architetture x86 e ARM, che costituisce la base del software del gateway di bordo (A8.1, A8.3). Anitia non '
   'possiede veicoli: le prove in veicolo usano il veicolo di prova di OR4 e le prove su tratta stradale si svolgono '
   "con Autostrada del Brennero S.p.A., sperimentatore esterno. L'infrastruttura cloud della piattaforma IoT è "
   'dedicata al progetto e acquisita come servizio a consumo (OR8).')),
 ('e', ('Risorse strumentali da acquistare.', 'Sono previsti due beni:')),
 ('p',
  "quattro unità V2X di prova (RSU e OBU) conformi ETSI C-ITS per OR7, a 5.000 € l'una: spesa di 20.000 €, costo "
  "ammissibile di 6.000 € per l'ammortamento di 18 mesi su 60;"),
 ('p',
  "sei gateway telematici di bordo con CAN/CAN-FD, Ethernet, rete mobile ed elemento sicuro per OR8, a 2.500 € l'uno "
  "compresi gli accessori: spesa di 15.000 €, costo ammissibile di 6.750 € per l'ammortamento di 27 mesi su 60."),
 ('t',
  'La congruità è stimata su offerte comparabili. Il database dei costi ITS del Dipartimento dei Trasporti '
  'statunitense riporta circa 3.000 $ per una singola unità stradale; le unità professionali complete sono vendute su '
  'preventivo. Un gateway Linux automotive con quattro porte CAN costa circa 690 $ e una piattaforma di sviluppo per '
  'gateway veicolari NXP GoldBox S32G 3.340 $: il valore di 2.500 € corrisponde a un mix di due piattaforme di '
  'sviluppo e quattro gateway per i veicoli di prova, con antenne, cablaggi e alimentazione. I prezzi saranno '
  'sostituiti dai preventivi dei fornitori.'),
 ('e',
  ('Procedure di gestione della R&S.',
   'Ogni progetto parte con una checklist di avvio che fissa ruoli e responsabilità, contratti e ruoli privacy, '
   'accessi nominativi con privilegi minimi e autenticazione a più fattori. Il lavoro è pianificato per obiettivo '
   'realizzativo, attività e deliverable. Le ore sono registrate mensilmente per persona e per attività, su schede '
   'presenze distinte per progetto; piano e consuntivo sono confrontati per attività e milestone e deliverable sono '
   'verificati rispetto ai criteri di accettazione. Codice e configurazioni sono gestiti in Git, con ambienti separati '
   "di sviluppo, collaudo e produzione, revisione obbligatoria del codice da parte di una persona diversa dall'autore, "
   'scansioni di sicurezza automatiche e una procedura di change management con piano di ritorno alla versione '
   'precedente.')),
 ('t',
  'Anitia adotta un sistema documentato di procedure di sicurezza delle informazioni, revisionato nel 2026 e riferito '
  'alla norma ISO/IEC 27001:2022, con audit interni annuali e riesame della direzione; non dispone di certificazioni '
  'ISO 9001 o ISO/IEC 27001. Ha esperienza di rendicontazione per stati di avanzamento in progetti finanziati dal '
  'MIMIT. Il responsabile tecnico per MooVXR è Alberto Gaspari.')]

III_2_2 = [('t',
  "I risultati attesi di Anitia sono due componenti del sistema, valutati rispetto allo stato dell'arte "
  'internazionale.'),
 ('e',
  ('Qualificazione dei dati da strada e infrastruttura (OR7).',
   'I messaggi ETSI C-ITS (DENM, SPATEM/MAPEM, IVIM) e il formato DATEX II definiscono come trasportare gli eventi '
   'stradali. Non stabiliscono invece, istante per istante, quanto un dato esterno sia affidabile e ancora attuale, né '
   'quando sia abbastanza affidabile da diventare un avviso per il guidatore. Le fonti hanno latenze che vanno dai '
   'millisecondi del V2X diretto ai minuti delle piattaforme aggregate e raramente dichiarano accuratezza e validità. '
   'Le soluzioni C-ITS disponibili forniscono infrastruttura e messaggi, non la valutazione del dato a bordo. '
   "L'originalità sta in tre elementi:")),
 ('p',
  'un modello di qualità comune a fonti con semantiche diverse, che stima gli attributi di qualità anche quando la '
  'fonte non li dichiara;'),
 ('p',
  'una fusione che mantiene per ogni evento due stime distinte, affidabilità e attualità, aggiornate dalle nuove '
  'segnalazioni, dalle conferme o smentite dei dati di bordo e dal passare del tempo;'),
 ('p',
  'un criterio quantitativo e verificabile, parametrizzato per classe di evento, che decide se un dato resta '
  "un'informazione, diventa un avviso o viene scartato."),
 ('t',
  'La rilevanza si misura con un F1 migliorato di almeno il 10% rispetto alla migliore fonte singola, un errore di '
  "calibrazione dell'affidabilità inferiore a 0,1 e una latenza aggiunta inferiore a 100 ms (D7.2); con meno del 10% "
  "di falsi avvisi, oltre l'85% degli eventi rilevanti segnalati e un anticipo mediano superiore a 30 s per gli eventi "
  'non urgenti (D7.3); su strada, con un anticipo mediano di oltre 20 s rispetto alla sola percezione di bordo e oltre '
  'il 90% di segnalazioni corrette (D7.4).'),
 ('e',
  ('Piattaforma di accesso ai dati del veicolo e di aggiornamento coordinato del software di bordo (OR8).',
   "Lo stato dell'arte offre il modello dati COVESA VSS, alcuni broker di segnali open source e strumenti maturi per "
   'aggiornare un singolo dispositivo Linux. Le piattaforme OTA commerciali sono pensate soprattutto per i programmi '
   'dei grandi costruttori o per singoli dispositivi; gli aggregatori di dati danno accesso via cloud ai dati del '
   "costruttore, non ai segnali del veicolo a bordo. L'originalità sta in tre elementi:")),
 ('p',
  'un collegamento configurabile, e non programmato per ogni veicolo, fra le interfacce proprietarie e il modello VSS, '
  "esteso ai segnali ADAS e DMS di serie, con controllo d'accesso per componente e per segnale;"),
 ('p',
  "l'aggiornamento coordinato a livello di veicolo del software di più dispositivi e fornitori, compresi i modelli AI "
  'prodotti negli altri OR, con dipendenze fra versioni, ripristino in caso di fallimento parziale e una catena di '
  "fiducia secondo l'approccio Uptane;"),
 ('p',
  "l'applicazione automatica delle regole d'uso dei dati per finalità e per occupante, coerente con il GDPR e il Data "
  'Act, insieme alla consegna senza perdite con connettività intermittente.'),
 ('t',
  "La rilevanza si misura con l'acquisizione di almeno il 90% dei segnali richiesti, una latenza di consegna a bordo "
  'inferiore a 20 ms al 95° percentile e meno di 10 giorni-persona per integrare un nuovo modello di veicolo (D8.1); '
  'con oltre il 99,9% dei dati raccolti senza perdite dopo interruzioni di rete fino a 24 ore (D8.2); con il 100% di '
  'recuperi nelle prove di guasto, il rifiuto di tutti i pacchetti non firmati o alterati e nessuna vulnerabilità '
  'critica aperta dopo il penetration test (D8.3); con almeno 10.000 veicoli simulati gestiti e la distribuzione di un '
  "evento esterno ai veicoli dell'area entro 2 s al 95° percentile (D8.4)."),
 ('t',
  'Questi risultati non sono miglioramenti incrementali di componenti esistenti: introducono funzioni che le soluzioni '
  "disponibili non svolgono, cioè la valutazione dell'affidabilità del dato stradale prima che arrivi al guidatore e "
  'la gestione coordinata del software di bordo di più fornitori anche su veicoli che non rientrano nei grandi '
  'programmi dei costruttori. Le ricadute tecnologiche sul settore sono tre:'),
 ('p',
  'il modello di qualità e i criteri di promozione ad avviso sono applicabili a qualsiasi servizio C-ITS e ai gestori '
  'stradali che devono decidere quali eventi pubblicare;'),
 ('p',
  "l'accesso standardizzato ai segnali del veicolo riduce il costo di integrazione di nuovi servizi di bordo per "
  'flotte e veicoli speciali;'),
 ('p',
  "l'aggiornamento coordinato e tracciato fornisce ai costruttori evidenze utilizzabili nei processi di gestione della "
  'sicurezza informatica e degli aggiornamenti software richiesti dai Regolamenti UNECE n. 155 e n. 156.')]

III_3_1 = [('e',
  ('Settore di destinazione.',
   'I risultati di Anitia si rivolgono a due mercati. La piattaforma per i dati del veicolo, il device management e '
   "l'aggiornamento software a distanza (OR8) interessa costruttori di veicoli speciali, fornitori di primo livello, "
   'gestori di flotte e operatori telematici, che devono gestire il ciclo di vita del software di bordo in conformità '
   "ai Regolamenti UNECE n. 155 e n. 156. L'integrazione e la qualificazione dei dati da strada e infrastruttura (OR7) "
   'interessa concessionari stradali, integratori ITS e fornitori di servizi per flotte che adottano la comunicazione '
   'C-ITS.')),
 ('e',
  ('Dimensione del mercato.',
   'Le stime che seguono derivano da fonti di analisi di mercato pubbliche e sono indicative:')),
 ('p',
  'il mercato mondiale degli aggiornamenti OTA per autoveicoli è stimato in circa 4,8-4,9 miliardi di dollari nel 2025 '
  "(Mordor Intelligence, Global Market Insights), con l'Europa fra le aree principali;"),
 ('p',
  'in Europa i sistemi di gestione delle flotte attivi erano circa 18,1 milioni a fine 2024 e sono previsti 30,5 '
  "milioni nel 2029 (Berg Insight); l'Italia è il mercato europeo più avanzato nella telematica per noleggio e "
  'leasing;'),
 ('p',
  'il mercato europeo dei sistemi V2X per autoveicoli è stimato in circa 0,8 miliardi di dollari nel 2025 (Global '
  'Market Insights); circolano già circa 2,5 milioni di veicoli dotati di C-ITS e circa 3.000 unità stradali '
  'installate (ERTICO, 2026).'),
 ('t',
  'Il perimetro geografico è in prima battuta nazionale: flotte commerciali e di servizio, costruttori e allestitori '
  'di veicoli speciali, concessionari autostradali e integratori ITS italiani. In una seconda fase Anitia intende '
  "rivolgersi ai mercati dell'Unione europea, dove gli stessi standard (COVESA VSS, ETSI C-ITS, UNECE R155 e R156) "
  'rendono la piattaforma utilizzabile senza adattamenti sostanziali.'),
 ('e',
  ('Sistema competitivo.',
   "Nell'aggiornamento OTA e nella gestione del software di bordo operano Excelfore (eSync), Sibros, Harman e "
   'Northern.tech (Mender), con piattaforme rivolte soprattutto ai programmi dei grandi costruttori o ai singoli '
   'dispositivi. Aggregatori come High Mobility danno accesso via API ai dati dei costruttori ma non ai segnali del '
   'veicolo a bordo. Nei sistemi C-ITS e nelle unità stradali operano Kapsch TrafficCom, Yunex Traffic, Swarco e '
   "Commsignia, che forniscono infrastruttura e messaggi ma non la valutazione dell'affidabilità del dato a bordo.")),
 ('e',
  ('Posizionamento.',
   'Anitia si propone come integratore indipendente in due aree: una piattaforma aperta per i dati del veicolo e gli '
   'aggiornamenti, basata su standard aperti e in grado di coordinare il software di più fornitori sullo stesso '
   'veicolo, pensata per piccole flotte, veicoli speciali e fornitori che non hanno i volumi delle grandi piattaforme '
   'commerciali; e la qualificazione dei dati da strada prima che arrivino al guidatore, nello spazio fra chi fornisce '
   "l'infrastruttura C-ITS e chi decide cosa mostrare a bordo.")),
 ('e',
  ('Impatto economico.',
   'Le cifre che seguono sono stime di Anitia. Il modello di ricavo prevede un canone annuo per veicolo collegato alla '
   'piattaforma (dati, device management e aggiornamenti) e progetti di integrazione a commessa per concessionari e '
   'integratori ITS, con servizi continuativi di assistenza. I ricavi sono interamente aggiuntivi, perché la '
   'piattaforma costituisce una nuova linea di offerta.')),
 ('tab',
  [['Ricavi aggiuntivi attesi (stima)', '2030', '2031', '2032', '2033 (regime)'],
   ['Ricavi Anitia dai risultati di MooVXR', '0,10 M€', '0,30 M€', '0,55 M€', '0,80 M€'],
   ['di cui canoni della piattaforma', '0,05 M€', '0,15 M€', '0,30 M€', '0,48 M€'],
   ['di cui progetti e servizi di integrazione', '0,05 M€', '0,15 M€', '0,25 M€', '0,32 M€'],
   ['Quota export', '0%', '5%', '10%', '20%']]),
 ('t',
  'Il valore a regime corrisponde a circa 8.000 veicoli collegati e a due o tre progetti di integrazione C-ITS '
  "all'anno. A regime si stimano una quota export del 20%, riferita a flotte e fornitori dell'Unione europea, e un "
  'margine operativo lordo di circa il 30%, coerente con un modello basato su canoni software e servizi gestiti.'),
 ('e',
  ("Investimenti per l'industrializzazione.",
   'Nei due anni successivi al progetto (2030-2031) Anitia stima investimenti per circa 250.000 €: ingegnerizzazione '
   'multi-cliente della piattaforma e sua integrazione con gateway commerciali; valutazione di terza parte della '
   'sicurezza del gateway e della catena di aggiornamento secondo ISO/SAE 21434; certificazione ISO/IEC 27001, '
   'richiesta dai clienti del settore; documentazione di prodotto e attività di pre-vendita.')),
 ('e',
  ('Ricadute occupazionali.',
   "Il progetto è svolto con personale già in forza. Per l'esercizio e la commercializzazione dei risultati Anitia "
   'stima a regime tre nuove assunzioni: uno sviluppatore software embedded per Linux automotive, un ingegnere cloud e '
   'DevOps per la gestione della piattaforma in esercizio e un tecnico commerciale per flotte, costruttori di veicoli '
   'speciali e concessionari.'))]

