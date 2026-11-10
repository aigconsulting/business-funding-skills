---
name: business-funding-opportunity-finder
description: Cerca opportunità ufficiali di finanza agevolata, investimenti e servizi per imprese per territorio, profilo e obiettivo, riportando identificativi, documenti e stato verificato alla data della ricerca.
---

# Business Funding Opportunity Finder

## Input
Territorio di sede o intervento, tipo di soggetto (anche in costituzione), attività e fabbisogno; chiedere solo il dato indispensabile se mancante.

## Procedura
1. Definire perimetro geografico, settore, fase aziendale e strumento, senza assumere che la sede dell'utente equivalga alla sede ammissibile del progetto.
2. Cercare sui portali istituzionali della giurisdizione e sui siti ufficiali di fondi/incubatori; vedere `../jurisdictions/official-sources.md`.
3. Per ogni risultato aprire pagina ufficiale e documentazione specifica (avviso, allegati, rettifiche), individuare ID, versione, autorità concedente, gestore e canale di candidatura.
4. Verificare data, stato (aperto/chiuso/programmato/non verificato), scadenza, eventuale sportello a esaurimento risorse; non inferire disponibilità effettiva dal calendario.
5. Distinguere pertinenza tematica da ammissibilità: applicare `business-funding-eligibility-checker` solo quando esistono profilo ed evidenze sufficienti.
6. Se una fonte non è accessibile, riportare `NON_VERIFICATO`, senza inventare importi, percentuali, deadline o link.

## Output
Una riga per opportunità: `nome/ID | autorità | territorio | strumento/i | beneficiari | stato e data | scadenza | documento ufficiale | condizioni da controllare`. Separare un elenco di **possibili opportunità** dai bandi ufficiali effettivamente verificati; niente ranking di probabilità di finanziamento.

Non attivare monitoraggi, inviare candidature né contattare enti.
