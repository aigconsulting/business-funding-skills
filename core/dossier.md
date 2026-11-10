# Dossier Business Funding Skills

Il dossier è un **file JSON locale opzionale**, non una base dati condivisa o un servizio. Il formato v1 è definito in [dossier.schema.json](dossier.schema.json) e distingue strumenti di finanziamento, requisiti, opportunità e fonti.

| Campo | Utilizzo |
| --- | --- |
| `schema` | `business-funding-skills/dossier@v1` |
| `dossier_id`, `created`, `updated` | Identità e date del dossier |
| `instrument_types` | GRANT, LOAN, GUARANTEE, EQUITY, INCUBATION, INTERNATIONALIZATION; combinazioni possibili |
| `opportunity` | ID, titolo, ultimo controllo, autorità, territorio e, dove applicabile, programma UE |
| `sources` | Fonti con ID `SRC-*`, URL, data, versione e stato |
| `requirements` | Requisiti con ID `REQ-*`, stato e riferimento a una fonte |
| `project`, `financials` | Dati opzionali: conservati nel dossier originale; **non ancora esportabili** al formato EU |

Gli stati ammessi sono `VERIFICATO`, `DA_CONFERMARE`, `IPOTESI`, `PROPOSTA`, `DECISIONE_APPROVATA`, `MANCANTE`, `NON_APPLICABILE`. Non convertire informazioni non confermate in fatti, né rinominare approvazioni fittizie.

Per il raccordo con EU Funding Skills utilizzare [INTEROPERABILITY.md](INTEROPERABILITY.md). Il convertitore effettua un export **limitato e fail-closed**: accetta solo grant attribuiti a un programma UE, con fonti e requisiti tracciati e senza perdita silenziosa di progetto/finanza. Lo schema non verifica l'effettiva applicabilità delle regole né sostituisce una validazione documentale.

L'assenza di un dossier non impedisce l'uso autonomo delle skill. Nessuna persistenza remota, nessun invio o sincronizzazione implicita.
