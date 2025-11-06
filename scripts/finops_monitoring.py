import json, random
from datetime import datetime
from pathlib import Path

Path("reports").mkdir(exist_ok=True)
report_file = Path("reports/finops_report.json")

data = []
for i in range(5):
    timestamp = datetime.utcnow().isoformat()
    cost = round(random.uniform(10, 25), 2)
    load = round(random.uniform(0.1, 1.0), 2)
    action = "scale_down" if load < 0.3 else "keep_running"
    data.append({"timestamp": timestamp, "cost_usd": cost, "load": load, "action": action})

report_file.write_text(json.dumps(data, indent=2))
print("FinOps automation simulated. Report written to reports/finops_report.json")
