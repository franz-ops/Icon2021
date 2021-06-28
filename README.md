# SMART FARM

## Indice

1. [Introduzione](#1-introduzione)
2. [Struttura Progetto](#2.-struttura-progetto)
3. [Requisiti](#3-requisiti)
4. [Evoluzione del progetto](#4-evoluzione-del-progetto)

## 1. Introduzione

Il progetto in questione è stato realizzato dal Team SmartFarm

- Antonio Valletta
- Alessandro Paparella
- Francesco Lobascio
- Felice Tempesta

Il progetto è stato creato per l'esame di Ingegneria della Conoscenza

A.A 2020-2021

Università degli studi di Bari "Aldo Moro"

## 2. Struttura Progetto

```
|–– datasets
|    |–– Crop_recommendation.csv
|    |–– train_test_crop.py
|–– img
|    |–– bg.png
|    |–– colture.png
|    |–– disease.png
|    |–– logo.png
|    |–– terrain.png
|    |–– terreno.png
|–– kb
|    |–– bc_simple_rules_questions.krb
|    |–– driver_simple.py
|    |–– questions.kqb
|-- Documentazione Smart Farm.pdf
|-- Inserimento_terreni.py
|-- README.md
|-- kb_main.py
|–– main.py
|–– marketplace.py
|–– requirements.txt
|–– terrain_classifier.py
```
Documentazione: https://github.com/franz-ops/Icon2021/blob/main/Documentazione%20Smart%20Farm.pdf

## 3. Requisiti 

Per eseguire il progetto è necessario installare la seguente versione di Python:

- `Python 3.7+`
- Se eseguito su ambiente Linux potrebbe essere necessario installare tkinter: `sudo apt-get install python3-tk`


DETTAGLI PER UNA CORRETTA ESECUZIONE:
- Installare i pacchetti necessari: `pip install -r requirements.txt`
- Eseguito il progetto verrà visualizzata un'interfaccia;
- Saranno mostrate 2 opzioni: "Inserimento terreni" e "Scopri Malattia";
    ### 1° Opzione
          - inserire i dati e visualizzare la ricerca effettuata dal sistema intelligente;
          - inviati i dati e ricevuta conferma, selezionare "Visualizza dati inseriti";
          - Cliccando sulla "X" d'uscita, ci si sposterà sulla console dell'IDE, nella quale si potranno visualizzare: Varietà, Incassi previsti, Costi e Area Coltivata in               mq;
          - Inserire il budget previsto;
          - Il sistema fornirà gli incassi previsti, i costi di mantenimento previsti per ogni varietà.

    ### 2° Opzione
          - Selezionata "Scopri Malattia", ci si sposterà sulla console, nella quale si interrogherà la KB;
          - Selezionare la coltura di interesse;
          - Indicare i sintomi riscontati.


## 4. Evoluzione del progetto

In futuro, il progetto realizzato potrà essere utilizzato, ampliato e migliorato da aziende che operano nel settore, non solo regionale, ma anche nazionale e chissà…mondiale.
Il nostro obiettivo è sempre stato sempre quello di realizzare un sistema non solo efficiente, ma anche utile per le quotidiane mansioni lavorative di una singola azienda.
Funzionalità, quelle del sistema esperto, che consentono di automatizzare, migliorare e rendere più produttivo il lavoro imprenditoriale.
Per fare questo sarà necessario l’utilizzo del dataset. Ovviamente, anche la Knowledge Base usata è solo una minima parte, ma se ampliata permetterebbe di riconoscere e supportare l’utente nell’identificazione di più malattie.
Classificazione dei migliori terreni, ottimizzazione delle colture per un maggior profitto…è l’agricoltura del domani, è l’evoluzione non solo nell’ambito meccanico, ma anche agricolo.
Il Team ha solo rappresentato un modello di sistema intelligente, ma siamo sicuri che l’intelligenza artificiale e l’automazione saranno sempre più popolari nel mondo agricolo.
