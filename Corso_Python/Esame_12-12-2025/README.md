L’obiettivo di questo progetto è capire il comportamento dei clienti di una compagnia di telecomunicazioni e prevedere quali clienti potrebbero abbandonare il servizio, utilizzando tecniche di machine learning sia supervisionato che non supervisionato

Ho utilizzato il dataset Telco Customer Churn, che contiene informazioni sui clienti, come dati personali, tipo di contratto e costi del servizio

PULIZIA DEI DATI
Correzione dei tipi di dato (ad esempio la colonna TotalCharges)
Gestione dei valori mancanti
Rimozione della colonna identificativa customerID
Conversione delle variabili categoriche in formato numerico

ANALISI
Analisi delle principali variabili numeriche
Studio della variabile target Churn
Visualizzazione dei dati tramite grafici come istogrammi e boxplot

ML NON SUP
Applicazione dell’algoritmo K-Means
Individuazione di gruppi di clienti con caratteristiche simili
Analisi del tasso di abbandono all’interno di ciascun gruppo

ML SUP
Utilizzo della regressione logistica per prevedere il churn
Gestione dello sbilanciamento tra le classi
Valutazione delle prestazioni del modello tramite precision, recall e F1-score

MIGLIORAMENTO DEL DS
Creazione di una nuova variabile avg_monthly_charge
Miglioramento della capacità del modello di individuare i clienti che abbandonano il servizio

RISULTATI
Il modello supervisionato riesce a identificare bene i clienti che rischiano di abbandonare il servizio.
In particolare, mostra come il miglioramento dei dati e la creazione di nuove variabili possano davvero fare la differenza nelle prestazioni del modello.

In seguito, è stato sviluppato un modello di regressione logistica per prevedere il churn. Aggiungendo una nuova variabile che rappresenta la spesa media mensile del cliente, il modello ha ottenuto dei miglioramenti significativi, aumentando la capacità di identificare correttamente i clienti a rischio churn (recall dell’82%), seppur con una leggera diminuzione dell'accuratezza complessiva.

I risultati confermano che, spesso, migliorare la qualità dei dati è più utile che usare modelli più complessi. Questo progetto dimostra l'importanza di un processo completo che includa analisi dei dati, creazione del modello e interpretazione dei risultati.
