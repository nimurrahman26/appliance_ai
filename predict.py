import joblib
import pandas as pd

# 1. Load trained model
model = joblib.load("model.pkl")

# 2. Input data (you can change values anytime)
data = {
    "steel": 1000,   # increase steel
    "aluminum": 2800,
    "copper": 9000,
    "usd_bdt": 125,
    "oil": 90
}

# 3. Convert to DataFrame
df = pd.DataFrame([data])

# 4. Predict price
prediction = model.predict(df)

# 5. Show result
print("Predicted Appliance Price (BDT):", int(prediction[0]))