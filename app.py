
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from predict import load_model_bundle, predict_bridge_condition

app = FastAPI(title="Bridge Condition Prediction API")

bundle = load_model_bundle("model_bundle.pkl")

class BridgeInput(BaseModel):
    District: float
    Structure_Type: float
    Deck_Area: float
    Deck_Wearing: float
    Deck_Structure_Type: float
    Average_Daily_Traffic_ADT: float
    Number_of_Spans: float
    Length_of_Maximum_Span: float
    Wearing_Surface: float
    Channel_Protection: float
    Scour: float
    Structural_Evaluation: float
    Inventory_Rating: float
    Operating_Rating: float
    Deck_Width: float
    Deck_Geometry: float
    Type_of_Wearing_Surface: float
    Bridge_Median: float
    Skew: float
    Reconstruction: float
    Year: float

@app.get("/")
def home():
    return {"message": "Bridge Condition Prediction API is running."}

@app.post("/predict")
def predict(input_data: BridgeInput):
    try:
        payload = {
            "District": input_data.District,
            "Structure Type": input_data.Structure_Type,
            "Deck Area": input_data.Deck_Area,
            "Deck Wearing": input_data.Deck_Wearing,
            "Deck Structure Type": input_data.Deck_Structure_Type,
            "Average Daily Traffic (ADT)": input_data.Average_Daily_Traffic_ADT,
            "Number of Spans": input_data.Number_of_Spans,
            "Length of Maximum Span": input_data.Length_of_Maximum_Span,
            "Wearing Surface": input_data.Wearing_Surface,
            "Channel Protection": input_data.Channel_Protection,
            "Scour": input_data.Scour,
            "Structural Evaluation": input_data.Structural_Evaluation,
            "Inventory Rating": input_data.Inventory_Rating,
            "Operating Rating": input_data.Operating_Rating,
            "Deck Width": input_data.Deck_Width,
            "Deck Geometry": input_data.Deck_Geometry,
            "Type of Wearing Surface": input_data.Type_of_Wearing_Surface,
            "Bridge Median": input_data.Bridge_Median,
            "Skew": input_data.Skew,
            "Reconstruction": input_data.Reconstruction,
            "Year": input_data.Year
        }

        result = predict_bridge_condition(payload, bundle)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
