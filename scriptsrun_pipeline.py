import os
from dotenv import load_dotenv

import dlt

load_dotenv()

def main():
    # Example skeleton — plug in the workshop’s source/resource here
    # e.g., source = your_source()
    # pipeline.run(source, table_name="trips")

    pipeline = dlt.pipeline(
        pipeline_name="workshop1_dlt",
        destination=os.getenv("DLT_DESTINATION", "duckdb"),
        dataset_name=os.getenv("DATASET_NAME", "nyc_taxi_dlt"),
    )

    print("Pipeline created:", pipeline.pipeline_name)
    print("Now add your source and pipeline.run(...)")

if __name__ == "__main__":
    main()