from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib

app = FastAPI()

model = joblib.load('iris_model.joblib')

@app.get("/test")
def read_root():
    return {"message": "Hello, FastAPI!"}

class FlowerData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.post("/predict/")
def predict_flower_species(data: FlowerData):
    # Convert input data to a format suitable for prediction
    input_features = [data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]

    # Make prediction using the model
    predicted_class = model.predict([input_features])[0]

    return {"predicted_species": predicted_class}
