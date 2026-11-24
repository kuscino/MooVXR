# -*- coding: utf-8 -*-
"""Parte III, contributi di Aubay Italia. III.2.1 (24/11, confermato): struttura e contenuti ripresi dal Piano di
Sviluppo SolarSwarm (paragrafo 2.1, parte Aubay: certificazioni e profilo del responsabile tecnico), adattati a
MooVXR con importi del modello v25 e interfacce dei testi di OR1, OR6, OR14."""

III_2_1 = [
    ("e", ("Risorse strumentali esistenti.", "Le attività si svolgono nell'unità locale di Roma, descritta nella "
           "struttura organizzativa del proponente, con postazioni di lavoro, rete aziendale protetta e un centro dati che "
           "consente di separare gli ambienti di sviluppo, registrare le versioni software e riprodurre le configurazioni "
           "sottoposte a prova. Il Centro di Competenza Infrastructure & Cloud mette a disposizione gli ambienti di "
           "sviluppo, integrazione e test usati nei progetti di Aubay. Le partnership con i principali fornitori cloud "
           "consentono di attivare a consumo le risorse di calcolo e storage, senza acquisto di infrastrutture. Per la "
           "simulazione del digital twin si usano strumenti open source (CARLA, SUMO, esmini, ns-3), senza costi di "
           "licenza.")),
    ("e", ("Strumenti di nuovo acquisto.", "Sono previsti:")),
    ("p", "quattro workstation di sviluppo per OR1, con una spesa di 24.000 € e un costo ammissibile di 9.600 € per 24 "
          "mesi di utilizzo su 60 di ammortamento;"),
    ("p", "sei workstation con GPU per il digital twin di OR6, con una spesa di 54.000 € e un costo ammissibile di "
          "24.300 € per 27 mesi su 60;"),
    ("p", "il noleggio del sistema di acquisizione dati sincronizzata per le prove su strada di OR14, per 10 mesi (mesi "
          "26-35), con canoni per 12.000 €."),
    ("e", ("Risorse organizzative e procedure.", "Aubay gestisce i progetti di ricerca e sviluppo all'interno del "
           "sistema di gestione certificato ISO 9001:2015, con le procedure di sicurezza delle informazioni ISO/IEC "
           "27001:2022, di gestione dei servizi IT ISO/IEC 20000-1:2018 e di business continuity ISO 22301:2019. La "
           "maturità tecnologica avanza per livelli TRL in modo incrementale:")),
    ("p", "OR1 e OR6, di ricerca industriale, portano content policy engine e digital twin dalla formulazione alla "
          "validazione in simulazione e su dati registrati;"),
    ("p", "OR14, di sviluppo sperimentale, integra i componenti di tutti i proponenti nel dimostratore su veicolo e lo "
          "verifica su strada."),
    ("t", "L'avanzamento è governato da punti di verifica associati ai deliverable, ciascuno con un criterio di "
          "accettazione, e dalla verifica intermedia al mese 18. Le interfacce con gli altri proponenti sono gestite "
          "come requisiti condivisi e versionati, raccolti nella base di conoscenza tecnica del progetto (A14.1):"),
    ("p", "decisioni del content policy engine di OR1 verso l'applicazione di bordo di OR3 e le esperienze per i "
          "passeggeri di OR4;"),
    ("p", "percorsi registrati da nLight (A12.5) e prove su strada verso la validazione del digital twin di OR6;"),
    ("p", "modelli AI in esercizio verso la piattaforma OTA di OR8, secondo i criteri di rilascio e di ritorno alla "
          "versione precedente (A14.3)."),
    ("e", ("Responsabile tecnico.", "Il responsabile tecnico per Aubay Italia è Marco Appetito, responsabile del Centro "
           "di Competenza Digital. Laureato in Ingegneria Informatica all'Università degli Studi di Roma La Sapienza, ha "
           "oltre vent'anni di esperienza in Aubay nella trasformazione digitale e nell'architettura applicativa:")),
    ("p", "responsabile dell'unità di competenza Digital e Architetture, con responsabilità di conto economico su "
          "definizione dell'offerta, go-to-market e delivery;"),
    ("p", "direttore dei Centri di Competenza Architecture e Digital dal 2014, con il coordinamento di oltre 350 "
          "professionisti e la responsabilità di costi, ricavi, margini e rischi;"),
    ("p", "manager del Centro di Competenza Architecture dal 2010, con delivery management, scouting tecnologico e "
          "progettazione di soluzioni su misura;"),
    ("p", "in precedenza Competence Center Manager, Professional Service Manager e Technical Project Manager, con "
          "esperienza di software architect su soluzioni ad alta affidabilità."),
    ("t", "Ha progettato offerte basate su modelli predittivi di machine learning e deep learning, sull'integrazione di "
          "IoT e intelligenza artificiale per il monitoraggio predittivo e su infrastrutture basate su LLM conformi "
          "all'AI Act e alle norme ISO. Ha partecipato a iniziative di ricerca industriale connesse al PNRR ed è stato "
          "fondatore e CTO della start-up Hendo (2014-2017), incubata presso BIC, su algoritmi di intelligenza "
          "artificiale applicati al marketing."),
    ("e", ("Pertinenza dei costi e congruità con i tempi.", "Il costo di Aubay è di 5.899.434 € e si compone delle voci "
           "seguenti:")),
    ("p", "personale: 4.483.295 €, pari a 118.921 ore;"),
    ("p", "spese generali e materiali a forfait: 983.239 €;"),
    ("p", "strumenti e attrezzature: 45.900 €, in quota di ammortamento e canoni di noleggio;"),
    ("p", "licenze: 110.000 €, cioè la soluzione Wiki-RAG di 42Rows per la base di conoscenza tecnica del progetto "
          "(OR14) per 90.000 € e i dataset di guida registrati (OR1) per 20.000 €;"),
    ("p", "servizi cloud a consumo: 102.000 €, al posto dell'acquisto di infrastrutture, ripartiti fra le risorse GPU "
          "per i modelli di OR1 (36.000 €), gli scenari del digital twin di OR6 (36.000 €) e le prove di carico di OR14 "
          "(30.000 €);"),
    ("p", "servizi di modelli linguistici e strumenti di sviluppo basati su LLM: 80.000 €, ripartiti fra OR1 "
          "(32.000 €), OR6 (22.000 €) e OR14 (26.000 €);"),
    ("p", "servizi specialistici esterni per OR14: 95.000 €, cioè 60.000 € per il penetration test e 35.000 € per "
          "l'assessment di conformità a UNECE R155 e ISO/SAE 21434."),
    ("t", "La ricerca industriale di OR1 (mesi 1-24) e OR6 (mesi 4-30) rilascia progressivamente i risultati verso "
          "l'integrazione. OR14 (mesi 13-36) si avvia quando sono disponibili le prime release dei componenti, e le "
          "prove su strada ricadono negli ultimi mesi del progetto. Il personale è dedicato al progetto fino alle ore "
          "annue dei costi standard e raggiunge un picco di circa 27 FTE al mese 13, sostenibile dal gruppo di 30 "
          "persone indicato per il progetto."),
]

# III.3.1 (24/11, confermato): impianto della parte Aubay del SolarSwarm; numeri da completare con i dati di Aubay
# ("seg" = segnaposto grigio). Nessuna assunzione prevista (decisione di Francesco).
III_3_1 = [
    ("e", ("Settore di destinazione.", "I risultati di Aubay sono destinati al software di bordo e ai servizi per "
           "l'abitacolo dei veicoli connessi. I clienti sono costruttori di veicoli, fornitori di elettronica e software "
           "di bordo (Tier 1) e operatori di flotte, già indicati fra gli acquirenti potenziali nel settore di attività "
           "del proponente. Il content policy engine e il digital twin rispondono a due esigenze dei costruttori che "
           "adottano l'architettura Software Defined Vehicle: aggiungere servizi e superfici di visualizzazione durante "
           "la vita del veicolo, e dimostrare che nessun contenuto distrae il guidatore. Il progetto estende "
           "all'automotive l'offerta di integrazione, dati e intelligenza artificiale che Aubay già fornisce ai clienti "
           "dei trasporti, dell'industria e delle telecomunicazioni.")),
    ("e", ("Mercato estero.", "Il gruppo Aubay opera in Francia, Spagna, Portogallo, Belgio, Lussemburgo e Regno "
           "Unito. Questa rete è il canale per proporre i risultati a costruttori e fornitori europei. La replicabilità "
           "all'estero è favorita dalle norme comuni a cui il progetto fa riferimento: la Raccomandazione 2008/653/CE per "
           "l'HMI, il Regolamento UNECE n. 155 e la ISO/SAE 21434 per la sicurezza, l'aggiornamento OTA nelle "
           "architetture Software Defined Vehicle.")),
    ("e", ("Sistema competitivo.", "I concorrenti di Aubay nei servizi software per la mobilità sono indicati nel "
           "settore di attività del proponente: integratori ICT, fornitori di piattaforme telematiche e società di "
           "ingegneria automotive. L'offerta attuale regola i contenuti con regole fisse per singola superficie, oppure "
           "oscura un solo schermo. Il content policy engine invece decide per più occupanti e più superfici con regole "
           "verificate formalmente, e si integra con applicazioni di bordo di fornitori diversi.")),
    ("e", ("Interesse industriale.", "Per Aubay il progetto consolida in componenti proprie le competenze di system "
           "integration, dati e intelligenza artificiale. Il risultato si valorizza in tre forme:")),
    ("p", "licenza del content policy engine e della componente di personalizzazione per costruttori e Tier 1, con "
          "l'integrazione nelle loro applicazioni di bordo;"),
    ("p", "servizi di validazione virtuale dell'HMI e dell'esperienza a bordo con il digital twin;"),
    ("p", "servizi professionali di integrazione di sistema, di analisi dei rischi e assessment secondo UNECE R155 e "
          "ISO/SAE 21434, e di gestione del ciclo di vita dei modelli AI in esercizio."),
    ("e", ("Impatto economico a regime.", "I ricavi sono prevalentemente aggiuntivi. Una parte delle opportunità verrà "
           "dall'estensione dei rapporti con i clienti dei trasporti e dell'industria già serviti.")),
    ("seg", "[Ricavi aggiuntivi e sostitutivi a regime con l'anno di riferimento, quota export e margine: da completare "
            "con i dati di Aubay]"),
    ("e", ("Investimenti per l'industrializzazione.", "Dopo l'esito positivo della sperimentazione, "
           "l'industrializzazione comprende:")),
    ("p", "l'evoluzione del content policy engine in un prodotto configurabile per più costruttori e piattaforme di "
          "bordo;"),
    ("p", "l'estensione all'esercizio dei sistemi di gestione certificati per la sicurezza delle informazioni e i "
          "servizi IT;"),
    ("p", "la documentazione d'uso e di integrazione, il supporto di esercizio e le procedure di rilascio dei modelli "
          "via OTA."),
    ("t", "L'industrializzazione si realizza prevalentemente con risorse interne, adeguando sviluppo, rilascio, "
          "esercizio e assistenza alla gestione di componenti installati a bordo per tutta la vita del veicolo."),
    ("seg", "[Importo degli investimenti: da completare con i dati di Aubay]"),
    ("e", ("Ricadute occupazionali.", "Dopo la conclusione, il gruppo di lavoro del progetto, che opera nell'unità "
           "locale di Roma, costituisce il nucleo della nuova linea di offerta. Le competenze di machine learning, "
           "digital twin, verifica formale, MLOps e sicurezza restano nell'impresa per l'esercizio e l'evoluzione dei "
           "componenti. Il progetto è anche un'occasione di riqualificazione del personale interno, che acquisisce "
           "competenze sul dominio automotive, sull'HMI e sulla sicurezza dei sistemi di bordo.")),
    ("e", ("Bisogni esistenti e nuovi.", "Il progetto risponde a un bisogno esistente dei costruttori: usare più "
           "superfici di visualizzazione nell'abitacolo senza aumentare la distrazione del guidatore. Genera inoltre un "
           "bisogno nuovo, cioè disporre di decisioni sui contenuti verificabili e adattate al singolo guidatore, da "
           "documentare verso clienti e autorità. Ad Aubay il progetto consente di entrare nel mercato dei componenti "
           "software per l'abitacolo, oggi non presidiato dalla sua offerta.")),
]

# III.3.2 (24/11, confermato): testo proposto il 24/11 con i blocchi del SolarSwarm (competitività, impatto,
# sfruttamento); senza pubblicazione delle interfacce (decisione di Francesco).
III_3_2 = [
    ("e", ("Sviluppo del settore.", "Il progetto cambia il modo in cui sono collegate le parti del sistema di bordo che "
           "presentano contenuti agli occupanti. Oggi ogni applicazione applica le proprie regole sulla propria "
           "superficie. Con il content policy engine la decisione su cosa mostrare, a chi e dove è separata dalle "
           "applicazioni che presentano i contenuti. Le applicazioni di più fornitori eseguono decisioni comuni, "
           "verificate formalmente, e possono essere aggiunte o aggiornate via OTA restando soggette alle stesse regole. "
           "Questo cambiamento di architettura sviluppa il settore in tre direzioni:")),
    ("p", "costruttori e fornitori Tier 1 possono integrare nell'abitacolo servizi di terzi governati da regole comuni "
          "e verificabili, invece di regole fisse per ciascuna applicazione;"),
    ("p", "una parte della validazione dell'HMI si sposta in simulazione, perché il digital twin calibrato sui dati "
          "reali concentra le prove su strada sui casi critici;"),
    ("p", "i modelli AI in esercizio a bordo seguono un ciclo di vita in cui il rilascio e il ritorno alla versione "
          "precedente sono condizionati dalle policy, coerente con le architetture Software Defined Vehicle."),
    ("e", ("Ricadute in altri ambiti.", "Le stesse componenti hanno ricadute negli ambiti in cui più occupanti o più "
           "operatori condividono un veicolo con più superfici:")),
    ("p", "autobus turistici, con contenuti diversi per gruppi di passeggeri e il conducente protetto dalle stesse "
          "regole;"),
    ("p", "veicoli per il trasporto di personalità e veicoli blindati, con una distribuzione controllata delle "
          "informazioni fra conducente e occupanti;"),
    ("p", "servizi di sicurezza e ricognizione del territorio, in cui i dati della percezione della scena vengono "
          "presentati agli operatori a bordo senza distrarre il conducente."),
    ("t", "Fuori dalla mobilità, il ciclo di vita dei modelli condizionato alle policy e la verifica formale delle "
          "regole sono riutilizzabili nei progetti di intelligenza artificiale che Aubay realizza nei settori regolati "
          "in cui opera, come banche, assicurazioni ed energia."),
    ("e", ("Competitività e crescita dell'impresa.", "Il progetto consente ad Aubay di affiancare alla system "
           "integration e ai servizi di intelligenza artificiale un'offerta propria per l'automotive. Si fonda su "
           "componenti di cui Aubay detiene le competenze di sviluppo: il content policy engine, il digital twin "
           "dell'esperienza a bordo e il ciclo di vita dei modelli condizionato alle policy.")),
    ("e", ("Impatto ambientale e sociale.", "Il progetto contribuisce alla sicurezza stradale, riducendo di almeno il "
           "15% gli sguardi fuori strada del guidatore rispetto alle regole fisse (K1). I profili degli occupanti si "
           "costruiscono a bordo, senza trasferimento di dati personali. La validazione nel digital twin riduce le prove "
           "su strada e le concentra sui casi critici.")),
    ("e", ("Sfruttamento e disseminazione.", "Sono previste le azioni seguenti:")),
    ("p", "sfruttamento commerciale del content policy engine, del digital twin e dei servizi di integrazione e "
          "sicurezza, nelle forme descritte per l'interesse industriale;"),
    ("p", "pubblicazioni scientifiche congiunte con il Politecnico di Milano sui risultati delle prove con "
          "partecipanti, e partecipazione a eventi di settore."),
]
