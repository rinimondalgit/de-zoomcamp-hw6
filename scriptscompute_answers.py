import os
from dotenv import load_dotenv
import duckdb

load_dotenv()

DUCKDB_PATH = os.getenv("DUCKDB_PATH", "workshop1.duckdb")
# adjust schema/table if your dataset name differs
# common pattern: dataset_name.table_name
DATASET = os.getenv("DATASET_NAME", "nyc_taxi_dlt")
TABLE = f"{DATASET}.trips"

def main():
    con = duckdb.connect(DUCKDB_PATH)

    # Q1 date range (adjust pickup column name if needed)
    q1 = con.execute(f"""
        SELECT
          MIN(DATE(pickup_datetime)) AS start_date,
          MAX(DATE(pickup_datetime)) AS end_date
        FROM {TABLE}
    """).fetchone()

    # Q2 proportion credit card: payment_type=1
    q2 = con.execute(f"""
        SELECT
          ROUND(100.0 * SUM(CASE WHEN payment_type = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS pct_cc
        FROM {TABLE}
    """).fetchone()[0]

    # Q3 total tips
    q3 = con.execute(f"""
        SELECT ROUND(SUM(tip_amount), 2) AS total_tips
        FROM {TABLE}
    """).fetchone()[0]

    print("Q1 start_date:", q1[0], "end_date:", q1[1])
    print("Q2 % credit card:", f"{q2}%")
    print("Q3 total tips:", f"${q3}")

if __name__ == "__main__":
    main()