# MooVXR, sintesi di progetto

Uso interno. Aggiornata al 18 novembre 2026.

## 1. In breve

MooVXR è un progetto di ricerca industriale e sviluppo sperimentale per una piattaforma di spatial intelligence dell'abitacolo del veicolo connesso. Il sistema decide quali contenuti mostrare a bordo, a chi e su quale superficie, in base alla situazione di guida e all'attenzione del guidatore.

| Voce | Valore |
|:---|:---|
| Bando | MIMIT, Accordi per l'innovazione nella filiera automotive |
| Budget di progetto | circa 18,8 M€ (ipotesi di lavoro) |
| Durata | 36 mesi |
| Proponenti | Aubay, Politecnico di Milano, GSNet, Anitia, nLight |
| Obiettivi realizzativi | 12 (massimo ammesso 15) |
| Deliverable principale | Allegato 4, Piano di Sviluppo |

## 2. Il bando

- **Atti:** Decreto Direttoriale 17 settembre 2026, DM 31 dicembre 2021, DPCM 10 giugno 2026.
- **Dotazione:** 631 M€, di cui 40% riservato a progetti nel Mezzogiorno.
- **Date:** compilazione guidata dall'11 novembre 2026, sportello dal 25 novembre 2026 alle 10:00. Istruttoria in ordine cronologico fino a esaurimento delle risorse.
- **Progetti ammissibili:** spesa da 5 a 40 M€, durata da 18 a 36 mesi, una sola Area di intervento, beneficiari della filiera automotive.
- **Agevolazioni:** contributo diretto alla spesa e finanziamento agevolato facoltativo (dettaglio nella sezione 7).
- **Valutazione:** caratteristiche dei proponenti, qualità della proposta, impatto. Soglia minima di 70 punti e soglie minime per criterio.

I dati provengono da una lettura preliminare del decreto e da fonti secondarie: vanno verificati sui testi ufficiali.

## 3. Problema e risposta

**Problema.** HUD, schermo centrale, display posteriori e smartphone decidono ognuno per conto proprio, con regole fisse. Il guidatore resta esposto a contenuti non pensati per lui, i passeggeri ricevono servizi scollegati dal viaggio, il costruttore integra fornitori diversi senza una regia.

**Risposta.** Un content policy engine adattivo coordina tutte le superfici di bordo:

- guidatore e passeggeri ricevono contenuti diversi, con separazione anche fisica;
- al guidatore arrivano solo AR-HUD e audio essenziali, gli occhiali AR sono riservati ai passeggeri;
- il sistema si adatta all'attenzione del singolo guidatore, riducendo o semplificando le informazioni quando cala;
- l'adattamento può solo restringere le regole validate, mai allargarle.

## 4. Componenti principali

- **Hardware di bordo:** AR-HUD guidatore, AR-HUD passeggero invisibile dal posto di guida, display passeggero a visibilità controllata, unità di calcolo automotive-grade.
- **Piattaforma software:** content policy engine, streaming edge-cloud con prefetch predittivo, integrazione con infotainment e sistemi di bordo (SDV, OTA, cybersecurity), piattaforma IoT.
- **Esperienza dei passeggeri:** storytelling geo-temporale generativo, Open Heritage Cloud collaborativo, marketplace di esperienze, POI commerciali, percorsi a minor consumo, AR e XR su occhiali e visori.
- **Segnali di serie:** ADAS e DMS non si sviluppano, se ne usano i segnali per sospendere i contenuti durante gli avvisi, stimare l'attenzione, arricchire l'AR-HUD ed evitare messaggi in conflitto.

## 5. Architettura

| Livello | Funzione | Componenti |
|:---|:---|:---|
| Erogazione | Porta i contenuti agli occupanti | AR-HUD, display, infotainment, occhiali e visori, streaming |
| Decisione | Sceglie cosa mostrare, a chi e dove | Content policy engine adattivo |
| Comprensione | Localizza il veicolo e aggancia i contenuti alla scena | Localizzazione di precisione, ancoraggio, tracking occhiali |
| Acquisizione | Raccoglie i dati | Unità di bordo, piattaforma IoT, V2X, segnali ADAS e DMS |

## 6. Partenariato e obiettivi realizzativi

| OR | Proponente | Tipo | Titolo | M€ |
|:---|:---|:---|:---|---:|
| 1 | Aubay | RI | Content policy engine adattivo | 1,2 |
| 2 | Aubay | RI | Storytelling geo-temporale generativo | 1,0 |
| 3 | Aubay | SS | Erogazione dei contenuti e integrazione con il veicolo | 3,0 |
| 4 | Aubay | SS | Servizi di contenuto: piattaforma collaborativa, marketplace, POI | 1,9 |
| 5 | GSNet | RI | Occhiali AR in un veicolo in movimento | 0,7 |
| 6 | GSNet | SS | Esperienze AR e XR per i passeggeri | 0,7 |
| 7 | Anitia | RI | Integrazione di dati da strada e infrastruttura | 0,5 |
| 8 | Anitia | SS | Piattaforma IoT per i dati dei veicoli | 0,9 |
| 9 | Politecnico di Milano | RI | Ancoraggio dei contenuti alla scena e calcolo a bordo | 1,3 |
| 10 | Politecnico di Milano | RI | Contenuti a bordo e attenzione degli occupanti | 1,2 |
| 11 | nLight | RI | AR-HUD per guidatore e passeggero | 1,5 |
| 12 | nLight | SS | Prototipi hardware, integrazione e validazione su veicolo | 4,9 |

| Proponente | RI (M€) | SS (M€) | Totale (M€) | Quota |
|:---|---:|---:|---:|---:|
| Aubay | 2,2 | 4,9 | 7,1 | 38% |
| nLight | 1,5 | 4,9 | 6,4 | 34% |
| Politecnico di Milano | 2,5 | 0,0 | 2,5 | 13% |
| GSNet | 0,7 | 0,7 | 1,4 | 7% |
| Anitia | 0,5 | 0,9 | 1,4 | 7% |
| **Totale** | **7,4** | **11,4** | **18,8** | **100%** |

## 7. Ipotesi di fondo perduto per Aubay

**Regole della misura**, da fonti secondarie da verificare sul DM 31/12/2021 e sul DD 17/09/2026:

- contributo diretto alla spesa del 50% sui costi di ricerca industriale e del 25% sullo sviluppo sperimentale, uguale per tutte le dimensioni di impresa;
- maggiorazione di 5 punti per le grandi imprese (10 per PMI e Organismi di ricerca) in caso di collaborazione effettiva con Organismi di ricerca che sostengano almeno il 10% dei costi ammissibili del progetto;
- finanziamento agevolato facoltativo fino al 20% dei costi, a un tasso pari al 20% del tasso di riferimento, con durata da 1 a 8 anni più preammortamento; richiede un indicatore di capacità di rimborso di almeno 0,8.

**Assunzioni:** Aubay Italia considerata grande impresa; costi di Aubay pari a 7,1 M€ (2,2 RI, 4,9 SS), già comprensivi delle spese generali forfettarie; Politecnico di Milano al 13% dei costi, sopra la soglia del 10%.

**Ipotesi di riferimento: maggiorazione per collaborazione con Organismi di ricerca.** Il Politecnico di Milano sostiene circa il 13% dei costi del progetto, sopra la soglia del 10%.

| Voce | Costi Aubay | Intensità | Fondo perduto |
|:---|---:|---:|---:|
| Ricerca industriale | 2,2 M€ | 55% | 1,21 M€ |
| Sviluppo sperimentale | 4,9 M€ | 30% | 1,47 M€ |
| **Totale** | **7,1 M€** | **38%** | **2,68 M€** |

- **Finanziamento agevolato facoltativo:** fino a circa 1,42 M€ (20% di 7,1 M€). Se l'equivalente sovvenzione lordo del finanziamento porta l'aiuto complessivo oltre i massimali GBER, il contributo viene ridotto.
- **Quota non coperta dal fondo perduto:** circa 4,4 M€, in parte coperta dal personale interno già in organico.
- **Senza maggiorazione:** se la quota del Politecnico scendesse sotto il 10% dei costi, il fondo perduto scenderebbe a 2,33 M€ (50% RI, 25% SS).

**Vincolo:** mantenere il Politecnico stabilmente sopra il 10% dei costi ammissibili del progetto.

**Leve per migliorare il risultato:**

- spostare attività da sviluppo sperimentale a ricerca industriale dove giustificabile, perché la ricerca ha un'intensità quasi doppia;
- verificare la base di calcolo delle spese generali forfettarie, che le fonti riportano in modo diverso (20% degli altri costi, oppure 20% di personale, attrezzature e servizi).

## 8. Ulteriori ambiti per nLight

- **Smart Interior e superfici intelligenti:** rivestimenti, pannelli e superfici che integrano display, sensori, illuminazione e interfacce digitali.
- **Audio immersivo e personalizzato:** esperienze sonore differenziate fra guidatore e passeggeri, con storytelling AI e comfort acustico.
- **Immersive Passenger Experience:** integrazione di contenuti AR, Digital Twin e Spatial Memory con gli elementi fisici dell'abitacolo.

## 9. Decisioni chiave

- La parte culturale (piattaforma collaborativa, Open Heritage Cloud, marketplace) resta nel perimetro come fonte di contenuti per i passeggeri; i costi riguardano lo sviluppo della piattaforma.
- Le funzioni ADAS e DMS di serie non si sviluppano.
- GSNet e Anitia hanno un massimo di 1,4 M€ ciascuno.
- La struttura è ridotta a 12 OR, ciascuno di un solo proponente e solo RI o solo SS.
- Le validazioni sono descritte come svolte in ambienti simulati, senza citare un simulatore specifico.

## 10. Stato e punti aperti

**Deliverable prodotti:**

- documento per i partner (Word, 11 pagine) nell'Area di Lavoro;
- presentazione per il partner automotive, adattata a nLight (14 slide, Claude Slides);
- video di presentazione interno (circa 80 secondi, Motion).

**Punti aperti:**

- verificare per l'entità italiana di nLight il requisito di filiera automotive, i bilanci e la regione; nLight può coinvolgere forniture specializzate (ottiche, display, elettronica di bordo);
- acquisire e verificare il decreto e gli allegati (A, 4bis, 8, 9, 10, 23), compresi intensità e maggiorazioni;
- verificare l'Area di intervento e il requisito di filiera di ogni proponente;
- raccogliere sedi operative, bilanci, personale e stime di costo dei partner;
- costruire il modello economico con i costi standard e preparare il Piano di Sviluppo.

**Prossime scadenze:** 11 novembre apertura della compilazione guidata, 18 novembre bozza del Piano di Sviluppo, 24 novembre revisione e firme, 25 novembre presentazione.

## Fonti

- [Bi-Rex, Bando Accordi per l'innovazione filiera automotive 2026](https://bi-rex.it/bando-accordi-innovazione-filiera-automotive-2026/)
- [Incentivimpresa, Accordi per l'innovazione automotive 2026](https://www.incentivimpresa.it/accordi-innovazione-automotive/)
- [Ransomtax, Accordi per l'innovazione automotive 2026](https://www.ransomtax.it/finanza-agevolata/accordi-per-innovazione-automotive-2026-informazioni-misura/)
- [TiAgevoliamo, Accordi per l'innovazione automotive 2026](https://www.tiagevoliamo.it/finanziamenti/automotive-accordi-innovazione-filiera-2026)
- [Regione Campania, apertura nuovo sportello 2026](https://www.regione.campania.it/regione-informa/notizie/accordi-l-innovazione-filiera-automotive-apertura-nuovo-sportello-2026)
