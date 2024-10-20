# Reddit Stock Sentiment Analysis #

Il seguente progetto mira ad analizzare le emotions e i sentiment dei posts di un determinato subreddit presente all'interno del social network Reddit.

### Obiettivo ###

Il primo step ha come obiettivo l'estrazione dei post ed i titoli da un subreddit specifico per analizzare i sentimenti e le emozioni espressi. 
Dopo aver ripulito i dati, indago se esiste una correlazione tra questi sentimenti ed emozioni (come hype, rabbia, tristezza, felicità) e il movimento dei titoli nel mercato azionario.

### Struttura del progetto ###

Il progetto sarà composto da 4 parti:

### Scraping ###

La prima fase del progetto prevede la selezione di fonti di dati appropriate e l'implementazione di script per l'estrazione dei dati. I dati sono composti da due parti principali:

* Dati Testuali di Reddit: Post e commenti dal subreddit selezionato (ad esempio, r/wallstreetbets) relativi a discussioni su azioni.
* Dati Storici delle Azioni: Dati storici delle azioni menzionate nei post del subreddit, inclusi prezzi, volume e altri indicatori finanziari.
  
### Data Cleaning ed Analisi ###

Questa fase include l'implementazione di vari modelli analitici:

* Analisi del Sentimento: Classifica il sentimento (positivo, negativo, neutro) dei post e dei commenti.
* Analisi delle Emozioni: Suddivide ulteriormente il sentimento in emozioni specifiche (ad esempio, rabbia, gioia, paura) per ottenere approfondimenti più dettagliati.
* Topic Modeling: Utilizzo di tecniche come la Latent Dirichlet Allocation (LDA) per identificare i principali argomenti discussi in relazione alle azioni selezionate.

### Ottimizzazione delle Analisi ###

Questa fase si concentra sul miglioramento dell'accuratezza e dell'efficacia delle analisi:

* Ottimizzazione LDA.
* Ottimizzazione dell'Accuratezza del Sentiment.

### Model ###

Nella fase finale, viene sviluppato un modello predittivo:

* Fasi di addestramento e validazione con parametri ottimizzati.
* Previsioni finali sulla performance dei titoli.
* Rappresentazione grafica dei risultati

### Who do I talk to? ###

* Domenico Elio Bressanello - 11/82/00309
* d.bressanello@studenti.unica.it