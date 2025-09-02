import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = joblib.load("model.joblib")
features = joblib.load("features.joblib")

class Item(BaseModel):
    data: dict

@app.post("/predict")
def predict(item: Item):
    X = pd.DataFrame([item.data])
    X = X.reindex(columns=features, fill_value=0)
    pred = round(model.predict(X)[0], 2)
    return {"prediction": pred} 
