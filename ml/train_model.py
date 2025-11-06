import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump

# Simulated training data (CPU hours vs cost)
df = pd.DataFrame({
    "cpu_hours": [10, 20, 30, 40, 50, 60],
    "cost_usd": [5, 10, 15, 20, 27, 33]
})

model = LinearRegression()
model.fit(df[["cpu_hours"]], df["cost_usd"])

dump(model, "ml/model.joblib")
print("Model trained and saved as model.joblib")
