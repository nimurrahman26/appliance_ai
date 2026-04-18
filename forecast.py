import numpy as np

# ----------------------------
# SIMPLE AI FORECAST ENGINE
# ----------------------------

def forecast_prices(current_price):
    """
    Generates 30-day forecast using trend simulation (AI-ready structure)
    Later we can replace with LSTM/Prophet model
    """

    days = list(range(1, 31))

    # upward market pressure simulation
    growth_rate = 0.0015

    forecast = []

    for d in days:
        future_price = current_price * (1 + growth_rate * d)
        forecast.append(future_price)

    return days, forecast


# ----------------------------
# TREND DIRECTION ENGINE
# ----------------------------

def trend_signal(forecast):
    if forecast[-1] > forecast[0]:
        return "📈 UPWARD TREND (Price Increasing)"
    else:
        return "📉 DOWNWARD TREND"