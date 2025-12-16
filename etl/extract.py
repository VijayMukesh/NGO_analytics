import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw")

def extract():
    data = {
        "programs": pd.read_csv(RAW_DATA_PATH / "programs.csv"),
        "beneficiaries": pd.read_csv(RAW_DATA_PATH / "beneficiaries.csv"),
        "donations": pd.read_csv(RAW_DATA_PATH / "donations.csv"),
        "expenses": pd.read_csv(RAW_DATA_PATH / "expenses.csv"),
        "participation": pd.read_csv(RAW_DATA_PATH / "program_participation.csv"),
    }
    return data

if __name__ == "__main__":
    datasets = extract()
    for name, df in datasets.items():
        print(f"{name}: {df.shape}")
