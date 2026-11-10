#!/usr/bin/env python3
"""Bridge esplicito Business -> EU dossier@v1. Senza rete, senza dipendenze."""
from __future__ import annotations
import json
import sys
from datetime import date
from pathlib import Path

TAG = "business-funding-skills/dossier@v1"
EU_TAG = "eu-funding-skills/dossier@v1"
STATES = {"VERIFICATO", "DA_CONFERMARE", "IPOTESI", "PROPOSTA", "DECISIONE_APPROVATA", "MANCANTE", "NON_APPLICABILE"}
TYPES = {"GRANT", "LOAN", "GUARANTEE", "EQUITY", "INCUBATION", "INTERNATIONALIZATION"}

def valid_date(s):
    if not isinstance(s, str):
        return False
    try:
        return date.fromisoformat(s).isoformat() == s
    except ValueError:
        return False

def convert(d):
    if not isinstance(d, dict) or d.get("schema") != TAG:
        raise ValueError("Schema Business non riconosciuto")
    if not isinstance(d.get("dossier_id"), str) or not d["dossier_id"]:
        raise ValueError("dossier_id mancante")
    if not all(valid_date(d.get(k)) for k in ("created", "updated")):
        raise ValueError("created/updated non ISO")
    if not isinstance(d.get("instrument_types"), list) or not d["instrument_types"] or any(t not in TYPES for t in d["instrument_types"]):
        raise ValueError("instrument_types non validi")
    if set(d["instrument_types"]) - {"GRANT", "INTERNATIONALIZATION"}:
        raise ValueError("Esportazione UE limitata a GRANT; prestiti, equity, servizi e strumenti ibridi richiedono valutazione distinta")
    o = d.get("opportunity")
    if not isinstance(o, dict) or not o.get("id") or not o.get("title") or not valid_date(o.get("last_checked")):
        raise ValueError("Opportunità incompleta: id, title e last_checked obbligatori")
    if not o.get("eu_programme") or not o.get("eu_management_mode") in ("diretta", "concorrente", "indiretta", "NON_VERIFICATO"):
        raise ValueError("Non è dimostrato il perimetro di un programma UE")
    if o.get("qfp_cycle") is None:
        raise ValueError("qfp_cycle richiesto, anche come stringa vuota se ignoto")
    sources = d.get("sources")
    if not isinstance(sources, list) or not sources:
        raise ValueError("Fonti obbligatorie: nessuna fonte verificata/identificata")
    evidenze, ids = [], set()
    for s in sources:
        if not isinstance(s, dict) or not isinstance(s.get("id"), str) or not s["id"].startswith("SRC-") or s["id"] in ids:
            raise ValueError("ID fonte assente, duplicato o non SRC-*")
        if not s.get("title") or not s.get("url") or not valid_date(s.get("checked_at")):
            raise ValueError("Fonte priva di titolo/url/data")
        if s.get("state") not in STATES:
            raise ValueError("Stato fonte non riconosciuto")
        ids.add(s["id"])
        evidenze.append({"id":s["id"],"titolo":s["title"],"url":s["url"],"versione":s.get("version"),"data_consultazione":s["checked_at"],"sezione":s.get("section"),"stato":s["state"]})
    requisiti=[]
    for q in d.get("requirements", []):
        if not isinstance(q,dict) or not isinstance(q.get("id"),str) or not q["id"].startswith("REQ-") or not q.get("text") or q.get("state") not in STATES or q.get("source_id") not in ids:
            raise ValueError("Requisito con id, fonte o stato non valido")
        if q["state"] == "VERIFICATO" and not valid_date(q.get("verified_at")):
            raise ValueError("Requisito VERIFICATO senza data")
        requisiti.append({"id":q["id"],"testo":q["text"],"fonte":q["source_id"],"sezione":q.get("section"),"stato":q["state"],"note":q.get("note")})
    # Allineamento esplicito dei campi progettuali comuni allo schema EU.
    project_fields = {
        "context": "contesto", "problems": "problemi", "general_goals": "obiettivi_generali",
        "specific_goals": "obiettivi_specifici", "activities": "attivita",
        "outputs": "output", "outcomes": "outcome", "impacts": "impatti",
        "indicators": "indicatori", "risks": "rischi",
    }
    indicator_fields = {
        "unit": "unita_misura", "baseline": "baseline", "target": "target",
        "period": "periodo", "measurement_method": "metodo_rilevazione",
    }
    project = d.get("project")
    mapped_project = None
    if project is not None:
        if not isinstance(project, dict) or set(project) - set(project_fields):
            raise ValueError("project contiene campi non mappabili")
        mapped_project = {}
        for key, items in project.items():
            if not isinstance(items, list):
                raise ValueError("project." + key + " non è una lista")
            mapped_items = []
            for item in items:
                if not isinstance(item, dict) or not item.get("text") or item.get("state") not in STATES:
                    raise ValueError("Voce progetto priva di testo o stato valido")
                allowed = {"text", "state", "source_id", "verified_at", "approved_at", "approved_by"}
                if key == "indicators":
                    allowed |= set(indicator_fields)
                if set(item) - allowed:
                    raise ValueError("Voce progetto contiene campi non mappabili")
                src = item.get("source_id")
                if src is not None and src not in ids:
                    raise ValueError("Voce progetto con fonte inesistente")
                if item["state"] == "VERIFICATO" and (not src or not valid_date(item.get("verified_at"))):
                    raise ValueError("Voce VERIFICATO senza fonte/data")
                if item["state"] == "DECISIONE_APPROVATA" and not valid_date(item.get("approved_at")):
                    raise ValueError("Decisione approvata senza data")
                mapped = {"testo":item["text"],"stato":item["state"],"fonte":src}
                if item.get("verified_at") is not None:
                    if not valid_date(item["verified_at"]):
                        raise ValueError("Data di verifica non ISO")
                    mapped["verificato_il"] = item["verified_at"]
                if item.get("approved_at") is not None:
                    if not valid_date(item["approved_at"]):
                        raise ValueError("Data di approvazione non ISO")
                    mapped["approvato_il"] = item["approved_at"]
                if item.get("approved_by") is not None:
                    mapped["approvato_da"] = item["approved_by"]
                if key == "indicators":
                    for english, italian in indicator_fields.items():
                        if english in item:
                            mapped[italian] = item[english]
                mapped_items.append(mapped)
            mapped_project[project_fields[key]] = mapped_items
    finance_fields = {
        "currency": "valuta", "project_costs": "costi_progetto",
        "grant_requested": "contributo_richiesto", "rate": "tasso",
        "cofinancing": "cofinanziamento", "rule_source_id": "fonte_regole",
        "state": "stato",
    }
    finance = d.get("financials")
    mapped_finance = None
    if finance is not None:
        if not isinstance(finance, dict) or set(finance) - set(finance_fields):
            raise ValueError("financials contiene campi non mappabili")
        if finance and (not finance.get("currency") or finance.get("state") not in STATES):
            raise ValueError("financials richiede currency e state validi")
        if finance.get("rule_source_id") is not None and finance["rule_source_id"] not in ids:
            raise ValueError("financials con fonte di regole inesistente")
        for field in ("project_costs", "grant_requested"):
            value = finance.get(field)
            if value is not None and (isinstance(value, bool) or not isinstance(value,(int,float)) or value < 0):
                raise ValueError("Importo non valido: " + field)
        mapped_finance = {finance_fields[k]:v for k,v in finance.items()}
    result={
        "schema":EU_TAG,"dossier_id":d["dossier_id"],"created":d["created"],"updated":d["updated"],
        "opportunita":{"programma":o["eu_programme"],"ciclo_QFP":o["qfp_cycle"],"titolo":o["title"],"autorita":o.get("authority",""),"modalita_gestione":o["eu_management_mode"],"avviso_id":o["id"],"call_id":None,"topic_id":None,"ultima_verifica":o["last_checked"]},
        "evidenze":evidenze,"requisiti":requisiti,
        "revisioni":[{"data":d["updated"],"descrizione":"Esportazione manuale da Business Funding: nessuna verifica automatica di veridicità", "motivo":"altro"}],
    }
    if mapped_project is not None:
        result["progetto"] = mapped_project
    if mapped_finance is not None:
        result["finanza"] = mapped_finance
    return result

def main():
    if len(sys.argv)!=3:
        print("Uso: python3 core/export_eu_dossier.py input-business.json output-eu.json",file=sys.stderr)
        return 2
    try:
        src=Path(sys.argv[1]).resolve()
        dst=Path(sys.argv[2]).resolve()
        if src == dst:
            raise ValueError("Input e output devono essere file distinti")
        value=convert(json.loads(src.read_text(encoding="utf-8")))
        dst.write_text(json.dumps(value,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}",file=sys.stderr)
        return 1
    print("PASS: dossier UE esportato; verificare con eu-funding-skills/dossier/check_dossier.py")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
