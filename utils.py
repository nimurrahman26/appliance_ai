import requests


# -------------------------
# REAL DATA PLACEHOLDER (API READY)
# -------------------------

def get_usd_bdt():
    # Later replace with real forex API
    return 120


def get_oil_price():
    # Later replace with World Bank / API
    return 85


def get_global_materials():
    # Later replace with LME API
    return {
        "steel": 950,
        "aluminum": 2700,
        "copper": 8800
    }


# -------------------------
# BUSINESS LOGIC ENGINE
# -------------------------

def calculate_business_price(base_price, product):
    import_factor = 1.25  # duty + logistics
    margin_factor = 1.20  # business profit margin

    product_factor = {
        "Washing Machine": 1.0,
        "Cookware": 0.25,
        "Gas Stove": 0.35
    }

    final_price = base_price * product_factor[product]
    final_price = final_price * import_factor * margin_factor

    return final_price