import json, random
from datetime import datetime

REPORT_FILE = "reports/finops_report.json"

data = []
for i in range(5):
    timestamp = datetime.utcnow().isoformat()
    cost = round(random.uniform(10, 25), 2)
    load = round(random.uniform(0.1, 1.0), 2)
    action = "scale_down" if load < 0.3 else "keep_running"
    data.append({"timestamp": timestamp, "cost_usd": cost, "load": load, "action": action})

with open(REPORT_FILE, "w") as f:
    json.dump(data, f, indent=2)

print("💰 FinOps automation simulated. Report written to reports/finops_report.json")
