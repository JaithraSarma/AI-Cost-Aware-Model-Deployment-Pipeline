import os, json
from pathlib import Path

Path("reports").mkdir(exist_ok=True)
report_file = Path("reports/finops_report.json")

required = ["AZURE_TENANT_ID", "AZURE_SUBSCRIPTION_ID", "AZURE_CLIENT_ID", "AZURE_CLIENT_SECRET"]
if not all(os.getenv(k) for k in required):
    print("⚠️ Azure secrets not set. Running in safe placeholder mode.")
    status = "skipped"
else:
    print("Azure deployment would be executed here (placeholder).")
    status = "deployed"

report_file.write_text(json.dumps({
    "mode": "azure",
    "status": status,
    "note": "Integrate Azure ML/AKS logic here."
}, indent=2))
