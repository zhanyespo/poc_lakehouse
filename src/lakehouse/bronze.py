import duckdb as ddb
from deltalake import write_deltalake

from lakehouse.settings  import s3_path

def load_orders_bronze(csv_path: str) -> None:
    """
    Load orders data from a CSV file into a Delta Lake table in the bronze layer.

    Args:
        csv_path (str): The path to the CSV file containing orders data.
    """
    # Read CSV data into a DuckDB table
    con = ddb.connect()
    con.execute(f"""
        CREATE TABLE orders AS 
        SELECT * FROM read_csv_auto('{csv_path}')
    """)
    
    # Fetch the data into a Pandas DataFrame
    df = con.execute("SELECT * FROM orders").df()
    
    # Define the Delta Lake table path in the bronze layer
    delta_table_path = f"{s3_path}/bronze/orders"
    
    # Write the DataFrame to Delta Lake
    write_deltalake(delta_table_path, df, mode="overwrite")
    
    # Close the DuckDB connection
    con.close()