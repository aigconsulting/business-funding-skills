---
name: business-funding-financial-comparator
description: Confronta ipotesi economiche di contributi, finanziamenti agevolati, garanzie, equity e servizi in natura tramite flussi di cassa, cofinanziamento e diluizione dichiarati, senza promettere rendimenti o importi ottenibili.
---

# Business Funding Financial Comparator

## Scopo
Confronto **per scenari**, non valutazione creditizia o investimento garantito.

## Procedura
1. Registrare fabbisogno, costo eleggibile documentato, durata e calendario delle spese; distinguere importo richiesto, ammissibile, concesso, erogato.
2. Per grant: tasso e massimale **della specifica misura**; stimare contributo `min(costi_eleggibili × intensità, massimale)` solo se entrambi verificati o esplicitamente ipotetici. Calcolare quota a carico, anticipi, SAL e fabbisogno ponte; non assumere pagamento immediato.
3. Per loan: capitale effettivamente disponibile, tasso fisso/variabile, periodo, ammortamento, spese, garanzie e cash flow del servizio del debito. Rate uniformi: `rata = P*r/(1-(1+r)^(-n))` quando `r>0`, altrimenti `P/n`; `r` deve essere tasso per periodo coerente con `n`.
4. Per equity: per investimento `I` e valutazione pre-money `V`, `quota_post = I/(V+I)`, **solo** nello scenario semplice senza SAFE, convertibili, liquidation preferences, option pool o altri aggiustamenti; segnalare tali condizioni.
5. Per garanzie: distinguere copertura del rischio da cassa erogata; per servizi d'incubazione: valore stimato solo se esplicitato e documentato.
6. Mostrare tabella di scenari: `fonti e ipotesi | cassa iniziale | obbligo di rimborso | possibile diluizione | tempi e vincoli | dati non verificati`. Non sommare strumenti prima di verificare cumulo e compatibilità.

## Controlli
Unità monetarie, IVA se pertinente, periodi, nominale/effettivo, costi accessori e disponibilità effettiva. Nessuna precisione fittizia. Una stima matematica non è una promessa di concessione o una consulenza finanziaria personalizzata.
