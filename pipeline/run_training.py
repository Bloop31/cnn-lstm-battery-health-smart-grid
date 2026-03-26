import yaml
import os
from src.data_ingestion import CSVBatteryLoader
from src.preprocessing import BatteryPreprocessor
from src.feature_builder import SequenceBuilder
from src.model_factory import ModelFactory
from src.trainer import Trainer
from src.evaluator import Evaluator
from src.visualization import BatteryVisualizer
from src.health_index import HealthCalculator
import numpy as np

config_path = os.path.join("config", "config.yaml")

with open(config_path, "r") as f:
    config = yaml.safe_load(f)

print("CONFIG LOADED:", config)

loader = CSVBatteryLoader(
    config["DATA_PATH"],
    config["MAX_FILES"]
)

df = loader.load()

prep = BatteryPreprocessor()
X, y, scaler = prep.transform(df)

builder = SequenceBuilder(config["WINDOW_SIZE"])
X_seq, y_seq = builder.build(X, y)

factory = ModelFactory()
model = factory.create((X_seq.shape[1], X_seq.shape[2]))

trainer = Trainer()
model, X_test, y_test = trainer.run(
    model,
    X_seq,
    y_seq,
    config["EPOCHS"],
    config["BATCH_SIZE"]
)

eval = Evaluator()
eval.check(model, X_test, y_test)

# prediction
pred = model.predict(X_test).flatten()

# visualization
viz = BatteryVisualizer()
viz.plot_degradation(df["capacity"].values)
viz.plot_soh(df["capacity"].values)
viz.plot_prediction(y_test, pred)

# RUL
health = HealthCalculator()
rul = health.compute_rul(df["capacity"].values)

print("Estimated Remaining Useful Life (cycle):", rul)

# save model
os.makedirs("models", exist_ok=True)
model.save("models/battery_cnn_lstm.keras")

print("Model saved successfully")

from src.decision_engine import BatteryDecisionEngine

soh_series = df["capacity"].values / df["capacity"].values[0]
current_soh = soh_series[-1]

engine = BatteryDecisionEngine()
decision = engine.evaluate(current_soh, rul)

print("\n=== BATTERY HEALTH DECISION ===")
for k, v in decision.items():
    print(k, ":", v)