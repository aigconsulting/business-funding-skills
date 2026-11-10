---
name: business-funding-eligibility-checker
description: Esegue una verifica preliminare documentata di ammissibilità di impresa e progetto a contributi, prestiti, investimenti e programmi di accompagnamento, distinguendo requisiti comprovati da dati mancanti.
---

# Business Funding Eligibility Checker

## Input
ID/URL preciso della misura e profilo, anche parziale, del richiedente e del progetto. Se manca la misura, cercarla con la skill di opportunity finding.

## Procedura
1. Recuperare versione applicabile dell'avviso, normativa richiamata, allegati, eventuali rettifiche e condizioni del gestore, con data di accesso.
2. Classificare requisiti obbligatori separatamente: **beneficiario** (forma, sede, dimensione, anzianità, settore, stato di costituzione), **progetto** (finalità, luogo, tempi), **spese/finanziabilità**, **forma e scadenza**, **capacità ed esclusioni**. Distinguere criteri di merito, condizioni negoziali e requisiti.
3. Per startup da costituire, verificare **chi può presentare domanda** e **quando deve essere costituita**; non inferire ammissibilità dal titolo della misura.
4. Per finanziamenti e equity distinguere accesso al processo di selezione da delibera creditizia o decisione di investimento; non presentare interesse dell'investitore come impegno.
5. Controllare regime di aiuto, cumulo, vincoli territoriali e dimensione PMI **solo dove applicabili e con fonte**. Non attribuire un massimale de minimis universale senza verifica del regime e del periodo pertinenti.
6. Restituire matrice `requisito | prova dell'utente | documento/sezione | termine | stato | azione informativa residua`.

## Stati
Per requisito: `SODDISFATTO`, `NON_SODDISFATTO`, `NON_VERIFICATO`, `NON_APPLICABILE`. Esito per ciascuna dimensione: `COERENTE_PRELIMINARE` solo quando tutte le condizioni decisive sono verificate; `CONDIZIONATO` solo se la rimediabilità entro il termine è documentata; `INCOMPATIBILE_DOCUMENTATO` se un requisito obbligatorio è incompatibile senza rimedio noto; altrimenti `DATI_INSUFFICIENTI`. Riportare sempre blocchi accertati anche in presenza di altri dati mancanti.

Nessuna approvazione ufficiale, certificazione o candidatura automatica.
