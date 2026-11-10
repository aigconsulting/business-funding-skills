---
name: business-submission-checker
description: Esegue controlli documentali pre-invio di domande o application, senza inviare, firmare o dichiarare ricevute di presentazione inesistenti.
---

# Business Submission Checker

## Scopo
Skill specializzata nel ciclo di sostegno alle imprese. Si attiva su richiesta dell'utente o quando il processo richiede questa fase; è utilizzabile anche autonomamente.

## Procedura
1. Fissare opportunità, fase, cut-off, canale ufficiale, versione finale dei file e istante della verifica.
2. Confrontare **documenti effettivamente disponibili** con checklist fonte: allegati, limiti di dimensione, formati, firme e dichiarazioni ove richieste.
3. Controllare consistenza anagrafica, importi, date, progetti, documentazione di supporto e validità delle versioni.
4. Evidenziare requisiti esterni non comprovabili localmente: credenziali portale, profilo abilitato, firma digitale, pagamento/bollo, ricezione server, disponibilità fondi. Non dichiararli completati.
5. Verificare situazione temporale con fuso, chiusure anticipate e possibili rettifiche solo se consultabili; lo stato `NON_VERIFICATO` impedisce una dichiarazione di prontezza totale.
6. Per VC/acceleratori trattare l'invio di pitch e application come processo distinto da una procedura amministrativa.

## Output
`controllo | evidenza concreta | fonte/sezione | stato (PASS/FAIL/NON_VERIFICATO/NON_APPLICABILE) | blocco`. Conclusione `PRONTO_DOCUMENTALMENTE` solo se tutti i controlli documentali decisivi risultano PASS; non equivale a invio o accettazione.

## Regole comuni
- Lavorare sul documento **specifico e vigente** della misura, fondo o programma, distinguendo autorità, gestore e intermediario. Annotare URL diretto, identificativo/versione, sezione e data di consultazione; in caso di conflitto documentale sospendere le conclusioni interessate.
- Marcare ogni informazione come **VERIFICATA**, **DICHIARATA_DAL_RICHIEDENTE**, **IPOTESI** oppure **NON_VERIFICATA**. Non inventare requisiti, spese, partner, dati economici, approvazioni o documenti.
- Tenere distinti contributo pubblico (concessione e rendicontazione), prestito (istruttoria e rimborso), equity (negoziazione e partecipazione), incubazione (servizi, eventuali grant/equity) e internazionalizzazione (finalità trasversale); per misure ibride documentare separatamente ciascun ramo.
- Nessuna presentazione, modifica su portali, comunicazione a terzi, firma, negoziazione, pagamento o assunzione di obblighi senza autorizzazione esplicita. Le checklist e le bozze non sono invii effettivi.
- Minimizzare dati personali e riservati. Se un documento non è disponibile, restituire la lacuna, non una dichiarazione di conformità.
