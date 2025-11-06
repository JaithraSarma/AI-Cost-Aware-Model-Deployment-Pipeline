import os, json
from pathlib import Path

Path("reports").mkdir(exist_ok=True)
report_file = Path("reports/finops_report.json")

required = ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_DEFAULT_REGION"]
if not all(os.getenv(k) for k in required):
    print("⚠️ AWS secrets not set. Running in safe placeholder mode.")
    status = "skipped"
else:
    print("AWS deployment would be executed here (placeholder).")
    status = "deployed"

report_file.write_text(json.dumps({
    "mode": "aws",
    "status": status,
    "note": "Integrate SageMaker/ECS/EKS deployment here."
}, indent=2))
