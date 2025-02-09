import pandas as pd
import json
import psycopg2
from sqlalchemy import create_engine


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data)


def ingest_data(data_dir):
    customers_df = load_json(f"{data_dir}/customers.json")
    policies_df = load_json(f"{data_dir}/policies.json")
    claims_df = load_json(f"{data_dir}/claims.json")
    risk_indicators_df = load_json(f"{data_dir}/risk_indicators.json")
    return customers_df, policies_df, claims_df, risk_indicators_df


def clean_df(df, categorical_cols=None, numerical_cols=None, date_cols=None):
    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    if categorical_cols:
        for col in categorical_cols:
            df[col] = df[col].fillna("unknown")
            # remove leading and trailing spaces and convert to lowercase
            df[col] = df[col].str.strip().str.lower()
    if numerical_cols:
        df[numerical_cols] = (
            df[numerical_cols]
            .apply(pd.to_numeric, errors="coerce")
            .fillna(df[numerical_cols].mean().round(2))
        )
    if date_cols:
        for col in date_cols:
            df[col] = pd.to_datetime(df[col], errors="coerce")
            df[col] = df[col].fillna(pd.Timestamp("2020-01-01"))

    return df


def clean_data(customers_df, policies_df, claims_df, risk_indicators_df):

    customers_df = clean_df(
        customers_df,
        categorical_cols=[
            "customer_name",
            "job",
            "customer_id",
            "phone_number",
            "email",
            "street_address",
            "state",
            "post_code",
            "iban",
            "job",
        ],
        date_cols=["date_of_birth"],
    )
    policies_df = clean_df(
        policies_df,
        categorical_cols=["policy_id", "customer_id", "policy_type"],
        date_cols=["created_at"],
    )
    claims_df = clean_df(
        claims_df,
        categorical_cols=["claim_id", "customer_id", "policy_id"],
        date_cols=["claim_date"],
    )
    risk_indicators_df = clean_df(
        risk_indicators_df,
        categorical_cols=["customer_id"],
        numerical_cols=[
            "driving_violations",
            "property_risk_score",
            "health_risk_score",
        ],
    )
    return customers_df, policies_df, claims_df, risk_indicators_df


def save_to_postgres(df, table_name, engine):
    print(f"Saving {table_name} to PostgreSQL...")
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)


def create_database(db_name, user_name, password, host, port):

    try: 
        conn = psycopg2.connect(
            dbname="postgres", user=user_name, password=password, host=host, port=port
        )
        conn.autocommit = True
        cursor = conn.cursor()

        sql_query = f'''CREATE database {db_name}''';
        db_exists_query = f'''SELECT datname FROM pg_catalog.pg_database where datname = \'{db_name}\'''';
        cursor.execute(db_exists_query)
        db_exists = cursor.fetchall()

        if db_exists:
            print(f"Database '{db_name}' already exists.")
        else:
            cursor.execute(sql_query)
            print(f"Database '{db_name}' created successfully!")

        conn.close()
    except Exception as e:
        print(f"Failed to create database: {e}")


def main():
    data_dir = "data"

    # Load data
    print("Loading data...")
    customers_df, policies_df, claims_df, risk_indicators_df = ingest_data(data_dir)

    categories = ["customers", "policies", "claims", "risk_indicators"]
    df_names = [customers_df, policies_df, claims_df, risk_indicators_df]
    # Display initial datasets information
    for name, df in zip(categories, df_names):
        print(f"{name} data overview before cleaning: ")
        print(f"{df.info()}\n")

    # Clean data step
    print("Cleaning data...")
    customers_df, policies_df, claims_df, risk_indicators_df = clean_data(
        customers_df, policies_df, claims_df, risk_indicators_df
    )

    # Display cleaned dataset info
    for name, df in zip(categories, [customers_df, policies_df, claims_df, risk_indicators_df]):
        print(f"{name} data overview after cleaning: ")
        print(f"{df.info()}\n")

    print("Data cleaning completed!")

    # Load postgresql credentials from config.json
    with open("config.json", "r") as f:
        config = json.load(f)

    db_name = config["DB_NAME"]
    db_user = config["DB_USER"]
    db_password = config["DB_PASSWORD"]
    db_host = config["DB_HOST"]
    db_port = int(config["DB_PORT"])

    # create database in postgres if it doesn't exist
    create_database(db_name, db_user, db_password, db_host, db_port)

    DB_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    engine = create_engine(DB_URL)
    # Save cleaned data to PostgreSQL

    for name, df in zip(categories, [customers_df, policies_df, claims_df, risk_indicators_df]):
        save_to_postgres(df, name, engine)
    print("Data successfully loaded into PostgreSQL!")


if __name__ == "__main__":
    main()
