# Business Funding Skills

Skill indipendenti per individuare e valutare **agevolazioni e strumenti di sostegno alle imprese** in Italia e in Europa. Progetto complementare a [EU Funding Skills](https://github.com/aigconsulting/eu-funding-skills): non replica la gerarchia UE, la progettazione Horizon o le verifiche delle call.

## Catalogo

| Skill | Scopo |
| --- | --- |
| [business-funding-classifier](business-funding-classifier/SKILL.md) | Distingue contributi, debito, equity, incubazione e internazionalizzazione; identifica forme ibride |
| [business-funding-opportunity-finder](business-funding-opportunity-finder/SKILL.md) | Ricerca opportunità concrete, ente competente, fonti ufficiali e stato |
| [business-funding-eligibility-checker](business-funding-eligibility-checker/SKILL.md) | Verifica preliminare per beneficiario, progetto, spese e modalità |
| [business-funding-financial-comparator](business-funding-financial-comparator/SKILL.md) | Confronta flussi, cofinanziamento, debito e diluizione su ipotesi dichiarate |
| [business-grants](business-grants/SKILL.md) | Specializzazione per contributi a fondo perduto |
| [business-soft-loans](business-soft-loans/SKILL.md) | Specializzazione per prestiti agevolati e garanzie |
| [business-venture-capital](business-venture-capital/SKILL.md) | Specializzazione per investimenti equity |
| [business-startup-incubation](business-startup-incubation/SKILL.md) | Specializzazione per incubazione e accelerazione |
| [business-internationalization](business-internationalization/SKILL.md) | Specializzazione per export ed espansione estera |

| [business-project-designer](business-project-designer/SKILL.md) | Progetta interventi, risultati, KPI, attività e budget |
| [business-application-planner](business-application-planner/SKILL.md) | Pianifica candidature, documenti, requisiti e tempi |
| [business-application-drafter](business-application-drafter/SKILL.md) | Redige bozze coerenti con formulari e documenti ufficiali |
| [business-application-reviewer](business-application-reviewer/SKILL.md) | Revisiona requisiti, qualità ed evidenze |
| [business-submission-checker](business-submission-checker/SKILL.md) | Esegue controlli documentali pre-invio |
| [business-post-submission-tracker](business-post-submission-tracker/SKILL.md) | Ricostruisce eventi post-candidatura e richieste |
| [business-award-contract-manager](business-award-contract-manager/SKILL.md) | Analizza atti di concessione, prestiti e accordi |
| [business-execution-reporting](business-execution-reporting/SKILL.md) | Monitora attività, milestone, spese e rendicontazione |
| [business-closure-obligations](business-closure-obligations/SKILL.md) | Verifica chiusura e obblighi successivi |
| [business-investment-readiness](business-investment-readiness/SKILL.md) | Prepara pitch, metriche, cap table e data room |
| [business-investment-due-diligence](business-investment-due-diligence/SKILL.md) | Struttura due diligence documentale preliminare |

Ogni skill contiene un file `SKILL.md` autonomamente caricabile da client compatibili Agent Skills. Le skill specialistiche usano quelle comuni senza richiederne l'installazione per fornire un'analisi circoscritta.

## Principi vincolanti

1. **Fonte primaria** per importi, requisiti, finestre, procedure, regime di aiuto e stato; riportare URL diretto, documento/versione e data di consultazione. Le fonti terze servono solo per individuare opportunità.
2. **Nessun importo o ammissibilità inventati.** Distinguere verificato, dichiarato dal richiedente, ipotesi e dato mancante; non presentare una graduatoria come un finanziamento concesso.
3. **Giurisdizione e data.** Regole UE, nazionali e regionali non sono intercambiabili. Verificare sede e fase del progetto; la categoria startup non rende automaticamente ammissibile una società da costituire.
4. **No azioni esterne implicite.** Nessuna domanda, contatto, invio documenti, apertura di account, candidatura o impegno finanziario senza richiesta esplicita.
5. **Strumenti ibridi.** Contributi, finanziamenti, servizi e investimenti possono coesistere nella stessa misura. Il cumulo va verificato sul testo applicabile, non presunto.

## Esecuzione indicativa

**Classificazione → Ricerca → Ammissibilità → Progettazione → Pianificazione → Redazione → Review → Pre-invio → Tracciamento post-invio → Concessione/accordo → Esecuzione e rendicontazione → Chiusura**. Per il venture capital si aggiungono investment readiness e due diligence, con percorso contrattuale distinto. Si possono usare skill singole.

## Installazione

Copiare ciascuna directory `business-*/` in `~/.claude/skills/`, `~/.config/opencode/skills/` oppure `.agents/skills/` (o directory di progetto equivalente). Le directory non contengono credenziali né chiamano automaticamente servizi esterni.

## Controlli

```bash
python3 scripts/check_skills.py
python3 core/test_export_eu_dossier.py
```

Questo controllo verifica soltanto struttura e metadati delle skill. **Non** attesta conformità giuridica, correttezza delle fonti correnti né qualità delle valutazioni prodotte dal modello.

## Interoperabilità

Per una call UE a gestione diretta o per la redazione di una proposta europea, utilizzare le skill di [eu-funding-skills](https://github.com/aigconsulting/eu-funding-skills). Il dossier Business dispone di uno [schema JSON v1](core/dossier.schema.json), di un [convertitore unidirezionale verso il dossier EU](core/export_eu_dossier.py), di [test unitari](core/test_export_eu_dossier.py) e di [limiti e istruzioni](core/INTEROPERABILITY.md). L'esportazione è **solo per GRANT UE documentati**, blocca altri strumenti e trasferisce i campi comuni di progetto e finanza quando rappresentabili, ma non sincronizza i file o gli stati fra repository.

## Fonti di partenza

Consulta [jurisdictions/official-sources.md](jurisdictions/official-sources.md). I link sono punti di accesso, non attestazioni dell'esistenza di opportunità aperte.

## Perimetro del ciclo

- **Grant:** analisi dell'avviso, candidatura, istruttoria, concessione, attività, rendicontazione, saldo e obblighi residui.
- **Debito agevolato:** istruttoria e concessione, utilizzo, rate, covenant, estinzione; non equiparare la delibera all'erogazione.
- **Equity:** scouting, readiness, pitch, negoziazione, due diligence, accordi, milestone, exit; le valutazioni sono preliminari e non equivalgono a consulenza legale o deliberazione di investimento.
- **Incubazione:** selezione, accordo, servizi, milestone, uscita; eventuali grant/equity seguono anche il relativo ciclo.
- **Internazionalizzazione:** è una finalità trasversale; si applica il ciclo dello strumento finanziario effettivamente adottato.

Il catalogo copre le **fasi documentali e analitiche** dell'intero ciclo, non ne automatizza l'esecuzione su portali o la gestione reale. Le skill non attestano conformità giuridica e devono essere valutate con scenari reali prima dell'utilizzo operativo.
