# Bozze di testi in forma Frascati non ancora consolidate

Redatte il 20 novembre 2026 e presentate in chat. Non sono nel Piano di Sviluppo. Valori obiettivo
proposti, da confermare con i team tecnici.

## OR2, Storytelling geo-temporale generativo (ora di GSNet), con le modifiche di leggibilità

Sospesa il 20/11 per sovrapposizioni con GSNet; dal 20/11 l'OR è proposto a GSNet, che può partire
da questa bozza.

**7.1** L'obiettivo realizzativo studia i metodi con cui le informazioni storiche e culturali sui
luoghi diventano racconti generati da modelli di AI generativa, adatti al viaggio e ancorati a fonti
verificate. Lo stato dell'arte offre due strumenti, ciascuno con un limite: i modelli linguistici
producono testi scorrevoli ma possono inventare fatti, soprattutto sui luoghi minori; le audioguide
geolocalizzate usano testi fissi attivati dalla posizione e non si adattano né al tempo che separa il
veicolo dal luogo né agli occupanti. Manca un metodo che garantisca insieme l'attribuzione di ogni
affermazione a una fonte e la sincronizzazione del racconto con il viaggio. L'obiettivo produce tre
risultati: un knowledge graph culturale, cioè una base di conoscenza che collega luoghi, epoche,
eventi, persone e fonti; un motore di generazione ancorato alle fonti; i metodi per valutare
l'attendibilità dei contributi e la qualità dei racconti. Ricerca industriale ai sensi dell'art. 1,
lett. o), del DD.

**A2.1 Knowledge graph culturale dei luoghi (mesi 1-10)**
- Problema. Informazioni distribuite fra archivi diversi (Europeana, Wikidata, cataloghi regionali),
  con modelli dati, licenze e precisione di posizione ed epoca diversi; molti luoghi senza coordinate
  precise, molti eventi con datazione incerta.
- Soluzione proposta. Modello concettuale basato su CIDOC-CRM, lo standard internazionale per la
  documentazione del patrimonio culturale, esteso a georeferenziazione con la sua precisione, licenza
  e attendibilità della fonte. Procedure automatiche di acquisizione riconoscono quando fonti diverse
  descrivono lo stesso luogo o evento e le collegano.
- Novità e incertezza. Modellazione congiunta di incertezza spaziale, temporale e attendibilità,
  interrogabile in viaggio. Non noti a priori la qualità dell'allineamento automatico e la copertura
  ottenibile sui territori pilota.
- Metodo. 1. Territori pilota e fonti. 2. Modello concettuale. 3. Acquisizione e collegamento delle
  entità. 4. Controllo di qualità su campione validato da esperti.
- Risultati misurabili (D2.1). Almeno 2.000 entità georeferenziate per territorio pilota; precisione
  dell'allineamento di almeno il 90% sul campione; fonte e licenza tracciate per il 100% delle entità.

**A2.2 Generazione dei racconti ancorata alle fonti (mesi 6-18)**
- Problema. I modelli linguistici possono inventare fatti, soprattutto per luoghi poco documentati;
  un errore fattuale compromette l'affidabilità del servizio.
- Soluzione proposta. Retrieval-augmented generation: il modello scrive il racconto a partire dai
  fatti recuperati dal knowledge graph, non dalla propria memoria; verifica a posteriori che ogni
  affermazione sia sostenuta da un fatto con citazione; parti interpretative marcate; affermazioni
  non sostenute riformulate o eliminate.
- Novità e incertezza. Verifica automatica affermazione-fonte in un dominio culturale multilingue.
  Non noti a priori il tasso residuo di errori raggiungibile senza perdere scorrevolezza e
  l'affidabilità del verificatore.
- Metodo. 1. Insieme di valutazione annotato da esperti. 2. Confronto di strategie di recupero e
  vincolo. 3. Verificatore. 4. Misura degli errori con annotazione cieca.
- Risultati misurabili (D2.2). Almeno 95% delle affermazioni fattuali sostenute da fonte; errori
  fattuali non oltre il 2%; 100% delle citazioni tracciabili.

**A2.3 Adattamento al contesto di viaggio e agli occupanti (mesi 12-22)**
- Problema. Il racconto è utile solo se inizia e finisce mentre il luogo è visibile o vicino; tempi
  di arrivo variabili; occupanti diversi per lingua, età, interessi; al guidatore solo brevi
  contenuti audio ammessi dal content policy engine.
- Soluzione proposta. Racconto in blocchi di durata stimata, pianificati sulla stima del tempo di
  arrivo e ripianificati in viaggio; profili per occupante; versione audio per il guidatore a
  durata vincolata.
- Novità e incertezza. Pianificazione narrativa con tempi incerti; non noto se la ripianificazione
  conservi la coerenza del racconto.
- Metodo. 1. Modello della durata. 2. Pianificazione e ripianificazione. 3. Simulazione su tracce di
  percorso. 4. Prove con utenti.
- Risultati misurabili (D2.3). Almeno 90% dei racconti conclusi nella finestra di visibilità o
  prossimità; scarto medio inferiore a 10 s fra inizio del racconto e ingresso nella finestra;
  coerenza giudicata almeno 4 su 5.

**A2.4 Attendibilità e provenienza dei contributi (mesi 10-20)**
- Problema. Contributi della piattaforma collaborativa di qualità variabile; integrarli senza ridurre
  l'affidabilità del knowledge graph.
- Soluzione proposta. Punteggio di attendibilità da provenienza (livello aperto o professionale),
  coerenza con i fatti presenti, conferma da altre fonti, storico del contributore; soglie per
  integrazione automatica, revisione, esclusione; provenienza tracciata secondo W3C PROV, lo standard
  per descrivere la provenienza dei dati.
- Novità e incertezza. Attendibilità di contenuti nuovi senza riscontro diretto; non noti a priori la
  calibrazione con pochi dati etichettati e la resistenza a contributi manipolati.
- Metodo. 1. Campione etichettato da esperti. 2. Confronto fra modelli. 3. Calibrazione. 4. Prove di
  robustezza.
- Risultati misurabili (D2.4). AUC di almeno 0,85, su una scala da 0,5 (scelta casuale) a 1
  (distinzione perfetta); punteggio coerente con la frequenza reale degli errori, scarto inferiore a
  0,1; provenienza tracciata per il 100% dei contributi integrati.

**A2.5 Valutazione della qualità sui territori pilota (mesi 18-24)**
- Problema. La qualità dei racconti non si misura con le sole metriche automatiche.
- Soluzione proposta. Protocollo su correttezza fattuale (esperti, consulenza culturale), coerenza
  con la posizione (tracce), gradimento (campioni di utenti).
- Novità e incertezza. Non nota a priori la correlazione fra metriche automatiche e giudizio esperto.
- Metodo. 1. Scelta dei racconti in proporzione a territori, tipi di luogo e lingue. 2. Annotazione
  cieca di almeno due esperti con misura dell'accordo. 3. Prove con utenti. 4. Analisi di
  correlazione.
- Risultati misurabili (D2.5). Accordo fra esperti, indice kappa di Cohen, di almeno 0,7; gradimento
  medio di almeno 4 su 5; correlazione misurata e riportata. Protocollo e dataset riusabili.

## OR3 (struttura a 13 OR), presentata in chat il 20/11

Con la distribuzione del 20/11 i task si dividono: A3.1-A3.3 vanno a GSNet (OR3, piattaforma di
erogazione e applicazione di bordo); A3.4-A3.7 diventano A14.2, A14.4, A14.5, A14.6 di Aubay (OR14).

- **A3.1 Architettura edge-cloud (mesi 7-15).** Problema: contenuti legati al luogo con scadenza,
  connettività variabile, molti veicoli. Soluzione: cloud, nodi edge vicini alla rete mobile, cache
  di bordo, requisiti di latenza allocati fra i livelli. Novità e incertezza: ripartizione ottimale
  e disponibilità reale di risorse edge. Metodo: requisiti, alternative, simulazione di ritardi e
  costi su tracce di connettività, scelta motivata. Risultati (D3.1): 100% dei requisiti allocati;
  latenza stimata inferiore a 500 ms nel 95% dei casi per i contenuti non precaricati; costo per
  veicolo stimato.
- **A3.2 Streaming adattivo e prefetch predittivo (mesi 10-27).** Problema: lo streaming adattivo
  non anticipa le zone senza copertura. Soluzione: prefetch su stima di percorso, tempo di arrivo e
  mappa di copertura costruita dai veicoli; cache con priorità e scadenza; funzionamento offline.
  Novità e incertezza: accuratezza su percorsi non pianificati, dimensione della cache. Metodo:
  tracce, algoritmi confrontati con strategie di base, simulazione, prove su strada. Risultati
  (D3.2): almeno 95% dei contenuti disponibili nel momento utile; meno di un'interruzione percepita
  per ora; traffico scaricato e non usato inferiore al 30%.
- **A3.3 Applicazione di bordo e HMI multi-display (mesi 13-33).** Problema: superfici con
  interfacce diverse e chiuse; HUD di serie limitato a navigazione e assistenza. Soluzione: strato di
  astrazione con adattatori per schermo centrale, HUD di serie (tramite la piattaforma IoT), HUD
  passeggero, dispositivi XR; esecuzione delle decisioni del content policy engine; interfaccia
  vocale. Novità e incertezza: livello di accesso all'HUD di serie e tempi di aggiornamento. Metodo:
  censimento delle interfacce su due sistemi infotainment, astrazione, sviluppo, banco, veicolo.
  Risultati (D3.3): aggiornamento della superficie inferiore a 100 ms nel 95% dei casi; 100% delle
  decisioni applicate su banco; integrazione su almeno due sistemi infotainment.
- **A3.4 Sicurezza dei contenuti e dell'applicazione (mesi 13-30), ora A14.2.** Cifratura, firma e
  verifica, gestione dei diritti, isolamento; analisi delle minacce secondo ISO/SAE 21434; UNECE
  R155; penetration test e assessment esterni. Risultati: nessuna vulnerabilità critica aperta;
  100% dei contenuti firmati e verificati; aumento di latenza inferiore al 10%.
- **A3.5 Prove di carico e continuità (mesi 22-30), ora A14.4.** Flotte simulate con profili comuni
  con Anitia, iniezione di guasti. Risultati: almeno 10.000 veicoli simulati; disponibilità almeno
  99,5%; ripristino in meno di 5 minuti.
- **A3.6 Integrazione del dimostratore e protocollo (mesi 24-32), ora A14.5.** Integrazione su banco
  hardware-in-the-loop e poi sul veicolo di prova, matrice delle interfacce, prove in area chiusa.
  Risultati: 100% delle interfacce verificate; dalla rilevazione di un punto di interesse alla
  visualizzazione meno di 200 ms nel 95% dei casi; protocollo approvato da tutti i partner.
- **A3.7 Prove su strada (mesi 30-36), ora A14.6.** Percorsi ripetuti per condizione, confronto con
  riferimenti indipendenti. Risultati: almeno 2.000 km in almeno tre aree pilota, di giorno e di
  notte (ipotesi da decidere); valori obiettivo di ciascun OR verificati con limiti e condizioni.

## A12.3 di nLight in forma Frascati (proposta)

- Problema. Vibrazioni, sobbalzi e cambi di direzione degradano immagini e stima di posizione dei
  punti di interesse, interrompono il tracking e rendono impreciso l'ancoraggio dei contenuti.
- Soluzione proposta. Accelerometri e giroscopi sul modulo e algoritmi di stabilizzazione inerziale
  che compensano il moto del veicolo su immagini e stime di posizione.
- Novità e incertezza. Stabilizzazione consolidata per la singola telecamera, non per un modulo che
  combina video, infrarosso, termico e LiDAR con frequenze e latenze diverse; non noto a priori se una
  compensazione coerente resti efficace sulle sollecitazioni reali.
- Metodo. 1. Caratterizzazione delle vibrazioni su percorsi di riferimento. 2. Selezione dei sensori
  inerziali. 3. Algoritmi confrontati su banco con sollecitazioni riprodotte. 4. Verifica su percorsi
  registrati.
- Risultati misurabili (D12.3). Riduzione del tremolio delle immagini e dell'errore di posizione
  rispetto al modulo non stabilizzato, con valori obiettivo da fissare con nLight.
