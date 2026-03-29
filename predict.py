
import pickle
import numpy as np

FEATURES = [
    "District",
    "Structure Type",
    "Deck Area",
    "Deck Wearing",
    "Deck Structure Type",
    "Average Daily Traffic (ADT)",
    "Number of Spans",
    "Length of Maximum Span",
    "Wearing Surface",
    "Channel Protection",
    "Scour",
    "Structural Evaluation",
    "Inventory Rating",
    "Operating Rating",
    "Deck Width",
    "Deck Geometry",
    "Type of Wearing Surface",
    "Bridge Median",
    "Skew",
    "Reconstruction",
    "Year"
]

def load_model_bundle(path="model_bundle.pkl"):
    with open(path, "rb") as f:
        bundle = pickle.load(f)
    return bundle

def predict_bridge_condition(data: dict, bundle: dict):
    missing_features = [feature for feature in FEATURES if feature not in data]
    if missing_features:
        raise ValueError(f"Missing input features: {missing_features}")

    x = np.array([[float(data[feature]) for feature in FEATURES]])
    x_scaled = bundle["scaler"].transform(x)

    deck_pred = int(bundle["model_deck"].predict(x_scaled)[0])
    substructure_pred = int(bundle["model_substructure"].predict(x_scaled)[0])
    superstructure_pred = int(bundle["model_superstructure"].predict(x_scaled)[0])

    label_map = bundle["label_map"]

    result = {
        "deck": label_map[deck_pred],
        "substructure": label_map[substructure_pred],
        "superstructure": label_map[superstructure_pred]
    }

    return result
