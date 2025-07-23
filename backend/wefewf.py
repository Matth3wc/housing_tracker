import pandas as pd

# Load the first 20 rows to inspect
df = pd.read_excel("/Users/mattthew/Documents/GitHub/housing_tracker/data_pipeline/undesa_pd_2024_ims_stock_by_sex_and_destination.xlsx", 
                   sheet_name="Table 1", 
                   nrows=20)

print(df.head(20))

