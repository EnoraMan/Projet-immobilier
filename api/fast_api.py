import os
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

BASE_DIR = os.path.dirname(__file__)

model_path = os.path.join(BASE_DIR, "model.joblib")
features_path = os.path.join(BASE_DIR, "features.joblib")

model = joblib.load(model_path)
features = joblib.load(features_path)

class Item(BaseModel):
    data: dict

@app.post("/predict")
def predict(item: Item):
    X = pd.DataFrame([item.data])
    X = X.reindex(columns=features, fill_value=0)
    pred = round(model.predict(X)[0], 2)
    return {"prediction": pred}
