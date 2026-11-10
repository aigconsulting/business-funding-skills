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

Ogni skill contiene un file `SKILL.md` autonomamente caricabile da client compatibili Agent Skills. Le skill specialistiche usano quelle comuni senza richiederne l'installazione per fornire un'analisi circoscritta.

## Principi vincolanti

1. **Fonte primaria** per importi, requisiti, finestre, procedure, regime di aiuto e stato; riportare URL diretto, documento/versione e data di consultazione. Le fonti terze servono solo per individuare opportunità.
2. **Nessun importo o ammissibilità inventati.** Distinguere verificato, dichiarato dal richiedente, ipotesi e dato mancante; non presentare una graduatoria come un finanziamento concesso.
3. **Giurisdizione e data.** Regole UE, nazionali e regionali non sono intercambiabili. Verificare sede e fase del progetto; la categoria startup non rende automaticamente ammissibile una società da costituire.
4. **No azioni esterne implicite.** Nessuna domanda, contatto, invio documenti, apertura di account, candidatura o impegno finanziario senza richiesta esplicita.
5. **Strumenti ibridi.** Contributi, finanziamenti, servizi e investimenti possono coesistere nella stessa misura. Il cumulo va verificato sul testo applicabile, non presunto.

## Esecuzione indicativa

**Classificazione → Ricerca → Ammissibilità preliminare → Comparazione finanziaria → Specializzazione**. Si possono usare skill singole.

## Installazione

Copiare ciascuna directory `business-*/` in `~/.claude/skills/`, `~/.config/opencode/skills/` oppure `.agents/skills/` (o directory di progetto equivalente). Le directory non contengono credenziali né chiamano automaticamente servizi esterni.

## Controlli

```bash
python3 scripts/check_skills.py
```

Questo controllo verifica soltanto struttura e metadati delle skill. **Non** attesta conformità giuridica, correttezza delle fonti correnti né qualità delle valutazioni prodotte dal modello.

## Interoperabilità

Per una call UE a gestione diretta o per la redazione di una proposta europea, utilizzare le skill di [eu-funding-skills](https://github.com/aigconsulting/eu-funding-skills). Il dossier è interoperabile sul piano concettuale tramite [mappatura dei dati](core/dossier.md); non è implementata una sincronizzazione automatica.

## Fonti di partenza

Consulta [jurisdictions/official-sources.md](jurisdictions/official-sources.md). I link sono punti di accesso, non attestazioni dell'esistenza di opportunità aperte.
