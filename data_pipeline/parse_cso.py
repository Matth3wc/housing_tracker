# data_pipeline/parse_cso.py
import pandas as pd

def load_cso(filepath):
    df = pd.read_csv(filepath)
    df = df[['County', 'Quarter', 'Number of Completions']]
    df.columns = ['county', 'quarter', 'completions']
    df['quarter'] = pd.to_datetime(df['quarter'], errors='coerce')
    return df

if __name__ == "__main__":
    df = load_cso("completions_by_quarter.csv")
    print(df.head())
