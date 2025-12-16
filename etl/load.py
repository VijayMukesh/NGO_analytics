from sqlalchemy import create_engine
from config.db_config import DB_CONFIG

def load(data):
    engine = create_engine(
        f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )

    data["programs"].to_sql(
        "dim_programs", engine, if_exists="append", index=False
    )

    data["beneficiaries"].to_sql(
        "dim_beneficiaries", engine, if_exists="append", index=False
    )

    data["donations"].to_sql(
        "fact_donations", engine, if_exists="append", index=False
    )

    data["expenses"].to_sql(
        "fact_expenses", engine, if_exists="append", index=False
    )

    data["participation"].to_sql(
        "fact_program_participation", engine, if_exists="append", index=False
    )

    print("Data loaded successfully")


if __name__ == "__main__":
    from etl.extract import extract
    from etl.transform import transform

    raw_data = extract()
    clean_data = transform(raw_data)
    load(clean_data)
