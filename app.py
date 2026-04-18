import streamlit as st
import joblib
import pandas as pd
from utils import (
    get_usd_bdt,
    get_oil_price,
    get_global_materials,
    calculate_business_price
)

# -------------------------
# LOAD MODEL
# -------------------------
model = joblib.load("model.pkl")

# -------------------------
# UI CONFIG
# -------------------------
st.set_page_config(page_title="Appliance AI Business System", layout="wide")

st.title("🏢 Appliance Market Intelligence System (Business Version)")
st.markdown("Real Data + AI Prediction + Profit Engine")

# -------------------------
# INPUT SECTION
# -------------------------
product = st.selectbox("Select Product", ["Washing Machine", "Cookware", "Gas Stove"])

# REAL DATA (AUTO FETCH)
materials = get_global_materials()
usd_bdt = get_usd_bdt()
oil = get_oil_price()

steel = st.number_input("Steel Price", value=materials["steel"])
aluminum = st.number_input("Aluminum Price", value=materials["aluminum"])
copper = st.number_input("Copper Price", value=materials["copper"])
usd = st.number_input("USD/BDT", value=usd_bdt)
oil_price = st.number_input("Oil Price", value=oil)

# -------------------------
# PREDICTION
# -------------------------
if st.button("🔮 Generate Business Price"):

    input_df = pd.DataFrame([[steel, aluminum, copper, usd, oil_price]],
                            columns=["steel","aluminum","copper","usd_bdt","oil"])

    base_price = model.predict(input_df)[0]

    final_price = calculate_business_price(base_price, product)

    profit = final_price - base_price

    # -------------------------
    # OUTPUT DASHBOARD
    # -------------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🏭 Base Import Cost", f"৳{int(base_price)}")

    with col2:
        st.metric("🏷️ Market Price", f"৳{int(final_price)}")

    with col3:
        st.metric("📈 Expected Profit", f"৳{int(profit)}")

    # -------------------------
    # BUSINESS SIGNAL
    # -------------------------
    st.markdown("---")

    if profit > 8000:
        st.success("🟢 STRONG BUY SIGNAL - High Profit Opportunity")
    elif profit > 4000:
        st.warning("⚠️ MEDIUM OPPORTUNITY - Consider carefully")
    else:
        st.error("🔴 LOW PROFIT - Avoid this product")

    # -------------------------
    # TREND INSIGHT
    # -------------------------
    st.subheader("📊 Market Insight")

    trend_data = pd.DataFrame({
        "Cost Trend": [30000, 32000, 35000, base_price, final_price]
    })

    st.line_chart(trend_data)