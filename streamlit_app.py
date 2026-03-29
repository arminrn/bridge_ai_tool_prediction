
import streamlit as st
import requests


# ---- PASSWORD PROTECTION ----
PASSWORD = "arminRN1994"  # change this

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    password_input = st.text_input("Enter Password", type="password")

    if password_input == PASSWORD:
        st.session_state.authenticated = True
        st.rerun()
    elif password_input:
        st.error("Incorrect password")

    st.stop()

st.set_page_config(page_title="Bridge Condition Prediction", page_icon="🌉", layout="wide")

st.title("🌉 Bridge Condition Prediction Tool")
st.write("Enter the bridge features below and predict deck, substructure, and superstructure condition.")

API_URL = "https://bridge-ai-backend.onrender.com/predict"
st.caption(f"Connected to backend: {API_URL}")

inputs = {}

col1, col2, col3 = st.columns(3)

with col1:
    inputs["District"] = st.number_input("District", value=0.0)
    inputs["Structure Type"] = st.number_input("Structure Type", value=0.0)
    inputs["Deck Area"] = st.number_input("Deck Area", value=0.0)
    inputs["Deck Wearing"] = st.number_input("Deck Wearing", value=0.0)
    inputs["Deck Structure Type"] = st.number_input("Deck Structure Type", value=0.0)
    inputs["Average Daily Traffic (ADT)"] = st.number_input("Average Daily Traffic (ADT)", value=0.0)
    inputs["Number of Spans"] = st.number_input("Number of Spans", value=0.0)

with col2:
    inputs["Length of Maximum Span"] = st.number_input("Length of Maximum Span", value=0.0)
    inputs["Wearing Surface"] = st.number_input("Wearing Surface", value=0.0)
    inputs["Channel Protection"] = st.number_input("Channel Protection", value=0.0)
    inputs["Scour"] = st.number_input("Scour", value=0.0)
    inputs["Structural Evaluation"] = st.number_input("Structural Evaluation", value=0.0)
    inputs["Inventory Rating"] = st.number_input("Inventory Rating", value=0.0)
    inputs["Operating Rating"] = st.number_input("Operating Rating", value=0.0)

with col3:
    inputs["Deck Width"] = st.number_input("Deck Width", value=0.0)
    inputs["Deck Geometry"] = st.number_input("Deck Geometry", value=0.0)
    inputs["Type of Wearing Surface"] = st.number_input("Type of Wearing Surface", value=0.0)
    inputs["Bridge Median"] = st.number_input("Bridge Median", value=0.0)
    inputs["Skew"] = st.number_input("Skew", value=0.0)
    inputs["Reconstruction"] = st.number_input("Reconstruction", value=0.0)
    inputs["Year"] = st.number_input("Year", value=2000.0)

if st.button("Predict"):
    try:
        payload = {
            "District": inputs["District"],
            "Structure_Type": inputs["Structure Type"],
            "Deck_Area": inputs["Deck Area"],
            "Deck_Wearing": inputs["Deck Wearing"],
            "Deck_Structure_Type": inputs["Deck Structure Type"],
            "Average_Daily_Traffic_ADT": inputs["Average Daily Traffic (ADT)"],
            "Number_of_Spans": inputs["Number of Spans"],
            "Length_of_Maximum_Span": inputs["Length of Maximum Span"],
            "Wearing_Surface": inputs["Wearing Surface"],
            "Channel_Protection": inputs["Channel Protection"],
            "Scour": inputs["Scour"],
            "Structural_Evaluation": inputs["Structural Evaluation"],
            "Inventory_Rating": inputs["Inventory Rating"],
            "Operating_Rating": inputs["Operating Rating"],
            "Deck_Width": inputs["Deck Width"],
            "Deck_Geometry": inputs["Deck Geometry"],
            "Type_of_Wearing_Surface": inputs["Type of Wearing Surface"],
            "Bridge_Median": inputs["Bridge Median"],
            "Skew": inputs["Skew"],
            "Reconstruction": inputs["Reconstruction"],
            "Year": inputs["Year"]
        }

        response = requests.post(API_URL, json=payload, timeout=60)

        if response.status_code == 200:
            result = response.json()

            st.success("Prediction completed successfully")

            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("Deck", result["deck"])
            with c2:
                st.metric("Substructure", result["substructure"])
            with c3:
                st.metric("Superstructure", result["superstructure"])
        else:
            st.error(f"Error {response.status_code}: {response.text}")

    except Exception as e:
        st.error(f"Request failed: {e}")
