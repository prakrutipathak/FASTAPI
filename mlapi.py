from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd
app = FastAPI()


class ScoringItem(BaseModel):
    # iris data
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.post("/")
async def scoring(item: ScoringItem):
    # convert to pandas dataframe
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    yhat = model.predict(df)
    return {"prediction": yhat[0]}
# uvicorn mlapi:app --reload