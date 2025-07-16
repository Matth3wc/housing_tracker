# backend/main.py
pip install fastapi uvicorn

from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Housing Tracker API"}

@app.get("/completions/")
def get_completions():
    df = pd.read_csv("data_pipeline/data_snapshot.csv")  # Load cleaned snapshot
    return df.to_dict(orient="records")
