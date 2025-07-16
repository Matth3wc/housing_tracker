from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load preprocessed data into memory
@app.get("/migration")
def get_migration_data():
    df = pd.read_csv("data_pipeline/migration_flows.csv")
    return df.to_dict(orient="records")
