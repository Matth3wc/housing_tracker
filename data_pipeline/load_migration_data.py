import pandas as pd

def load_migration_from_excel(file_path):
    df = pd.read_excel(file_path, skiprows=14)
    df = df.drop(columns=['Sort order', 'Notes'], errors='ignore')
    df = df.set_index('Country or area')

    df_long = df.reset_index().melt(id_vars='Country or area',
                                    var_name='origin',
                                    value_name='count')
    df_long = df_long.rename(columns={'Country or area': 'destination'})
    df_long = df_long.dropna()
    df_long = df_long[df_long['count'] > 0]

    return df_long

if __name__ == "__main__":
    file_path = "/Users/mattthew/Documents/GitHub/housing_tracker/data_pipeline/undesa_pd_2024_ims_stock_by_sex_and_destination.xlsx"
    df = load_migration_from_excel(file_path)
    df.to_csv("data_pipeline/migration_flows.csv", index=False)
    print("✅ Migration data saved to CSV.")
