from flask import Flask, request, jsonify
from joblib import load
import numpy as np

app = Flask(__name__)
model = load("ml/model.joblib")

@app.route("/")
def home():
    return {"message": "AI Cost-Aware Model API is live."}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    cpu_hours = np.array(data["cpu_hours"]).reshape(-1, 1)
    prediction = model.predict(cpu_hours)
    return jsonify({"predicted_cost_usd": prediction.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
