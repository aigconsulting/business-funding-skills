---
name: business-funding-classifier
description: Classifica strumenti di sostegno alle imprese come fondo perduto, prestito, garanzia, capitale di rischio, incubazione o internazionalizzazione, riconoscendo strumenti ibridi e distinguendo la finalità economica dalla forma finanziaria.
---

# Business Funding Classifier

## Scopo
Individuare **cosa sia** uno strumento prima di interpretare un bando o confrontare offerte. Non dedurre una forma di finanziamento dal nome commerciale.

## Procedura
1. Acquisire descrizione, link ufficiale o documento della misura. Se manca, fornire classificazione soltanto ipotetica.
2. Determinare chi eroga e chi beneficia; distinguere finanziatore, gestore, intermediario e prestatore di servizi.
3. Identificare ciascun componente: `GRANT` (contributo non ordinariamente rimborsabile, salvo recuperi), `LOAN` (debito da restituire), `GUARANTEE` (copertura del rischio altrui), `EQUITY` (capitale con partecipazione), `INCUBATION` (servizi di accompagnamento), `INTERNATIONALIZATION` (finalità di espansione estera, **non** forma finanziaria).
4. Registrare strumenti ibridi come elenco, non forzare una sola etichetta. Distinguere voucher, credito d'imposta, quasi-equity, premio e servizi in natura.
5. Precisare il canale: gestione UE diretta, nazionale, regionale, intermediata o privata, soltanto se attestato da fonti.
6. Restituire tabella `componente | forma | obbligo economico | destinatario | fonte | certezza`.

## Avvertenze
Un contributo non è necessariamente liquidità anticipata; un fondo equity non concede un prestito. Internazionalizzazione e startup sono ambiti di utilizzo e possono combinarsi con tutte le forme. Non assumere che un programma di incubazione investa sempre nel capitale.
