# Dossier interoperabile v1

Formato canonico Business: [dossier.schema.json](dossier.schema.json), tag `business-funding-skills/dossier@v1`. È un file JSON locale; nessuna persistenza o scambio automatico su rete. Non utilizzare dati reali senza autorizzazione.

Il comando `python3 core/export_eu_dossier.py business.json eu.json` produce un dossier con tag `eu-funding-skills/dossier@v1`, **solo** quando:
- lo strumento è un GRANT (eventualmente destinato all'internazionalizzazione), non include loan/equity/servizi o composizioni ibride;
- il programma UE e la modalità di gestione sono dichiarati; `opportunity.id` è un ID ufficiale e non un titolo generico;
- esistono una o più fonti con ID SRC-* e data; requisiti con ID REQ- e fonte valida;
- i dati di `project` e `financials`, se presenti, utilizzano esclusivamente i campi esplicitamente mappati nel convertitore; campi sconosciuti causano un errore, senza perdita silenziosa.

**Non certifica** provenienza europea o contenuto delle fonti: le dichiarazioni vengono trasferite senza elevarle a VERIFICATO. Verificare l'output anche con `python3 dossier/check_dossier.py eu.json` nel repo EU. In assenza di programmazione UE accertata o con dati non mappabili, il convertitore rifiuta l'export senza generare un dossier sostitutivo.

Mappatura: `sources → evidenze`, `requirements → requisiti`, `opportunity → opportunita`, identità e date mantenute. Le specializzazioni `instrument_types` non vengono conservate nell'output UE. I campi progettuali comuni (`context`, `problems`, `general_goals`, `specific_goals`, `activities`, `outputs`, `outcomes`, `impacts`, `indicators`, `risks`) e finanziari (`currency`, `project_costs`, `grant_requested`, `rate`, `cofinancing`, `rule_source_id`, `state`) vengono trasferiti con i relativi stati, se rappresentabili. Campi non previsti bloccano l'export: utilizzare sempre anche il file Business originale. Le revisioni preesistenti non sono trasferite: l'export crea una nuova riga esplicita; non usarlo come archivio storico completo.

Gli altri strumenti (venture capital, prestiti, accelerazione) restano nel formato Business. Non convertirli artificiosamente in una call europea.

## Verifica locale
```bash
python3 core/test_export_eu_dossier.py
python3 core/export_eu_dossier.py path/to/business.json path/to/eu.json
# Nel repo eu-funding-skills:
python3 dossier/check_dossier.py path/to/eu.json
```
