---
name: business-closure-obligations
description: Supporta chiusura amministrativa e finanziaria, verifica di saldo e obblighi successivi previsti, inclusi vincoli di mantenimento, rimborso, exit e rapporti con incubatori.
---

# Business Closure & Obligations

## Scopo
Skill specializzata nel ciclo di sostegno alle imprese. Si attiva su richiesta dell'utente o quando il processo richiede questa fase; è utilizzabile anche autonomamente.

## Procedura
1. Identificare eventi che determinano chiusura per quello strumento: saldo grant, estinzione prestito, exit/riorganizzazione equity, termine programma di incubazione.
2. Verificare documenti effettivi di liquidazione, saldo, quietanza, accordo/atto di cessazione e approvazione finale; non equiparare domanda di saldo a saldo erogato.
3. Estrarre da fonti vincoli di mantenimento, destinazione dei beni, obblighi occupazionali, audit, conservazione documentale, garanzie, scadenze, diritti informativi e clausole di exit, quando applicabili.
4. Segnalare eventuali controlli successivi, cause di revoca e recupero o debiti residui senza presumere che esistano per tutte le misure.
5. Separare `CHIUSURA_DOCUMENTATA`, `CHIUSURA_PARZIALE`, `OBBLIGHI_RESIDUI`, `DATI_INSUFFICIENTI` con evidenze e condizioni.
6. Non cancellare dati, liberare garanzie, contattare enti o terminare rapporti automaticamente.

## Output
`strumento | evento di chiusura | documento | obbligo residuo | scadenza | stato | fonte`.

## Regole comuni
- Lavorare sul documento **specifico e vigente** della misura, fondo o programma, distinguendo autorità, gestore e intermediario. Annotare URL diretto, identificativo/versione, sezione e data di consultazione; in caso di conflitto documentale sospendere le conclusioni interessate.
- Marcare ogni informazione come **VERIFICATA**, **DICHIARATA_DAL_RICHIEDENTE**, **IPOTESI** oppure **NON_VERIFICATA**. Non inventare requisiti, spese, partner, dati economici, approvazioni o documenti.
- Tenere distinti contributo pubblico (concessione e rendicontazione), prestito (istruttoria e rimborso), equity (negoziazione e partecipazione), incubazione (servizi, eventuali grant/equity) e internazionalizzazione (finalità trasversale); per misure ibride documentare separatamente ciascun ramo.
- Nessuna presentazione, modifica su portali, comunicazione a terzi, firma, negoziazione, pagamento o assunzione di obblighi senza autorizzazione esplicita. Le checklist e le bozze non sono invii effettivi.
- Minimizzare dati personali e riservati. Se un documento non è disponibile, restituire la lacuna, non una dichiarazione di conformità.
