import pandas as pd

def explore_data(df):
    print("Shape:", df.shape)
    print("\n Columns:", df.columns.tolist())
    print("\n Data Types:\n", df.dtypes)
    print("\n Missing Values:\n", df.isnull().sum())
    print("\n Duplicates:", df.duplicated().sum())
    print("\n Sample Rows:\n", df.head())
    df.info()
    df.describe()

def clean_data(df):
    # Normalize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Rename misformatted column
    df.rename(columns={"activite_(_bq)": "activite_bq"}, inplace=True)

    # Convert volume to numeric
    df["volume_equivalent_conditionne"] = pd.to_numeric(df["volume_equivalent_conditionne"], errors="coerce")

    # Drop rows with missing location info
    df = df.dropna(subset=["ville", "departement", "code_insee"])

    # Keep rows with valid volume
    df = df[df["volume_equivalent_conditionne"].notnull()]
    df = df[df["volume_equivalent_conditionne"] > 0]

    # Drop duplicates
    df = df.drop_duplicates()

    return df



