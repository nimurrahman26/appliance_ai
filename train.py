import pandas as pd
from xgboost import XGBRegressor
import joblib

df = pd.read_csv("data.csv")

X = df[["steel","aluminum","copper","usd_bdt","oil"]]
y = df["price"]

model = XGBRegressor(n_estimators=200, learning_rate=0.05)
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("✅ Business model trained successfully")