import psycopg2
import os
import json
from typing import Dict, Any

def register_table(
    table_name: str,
    layer: str,
    s3_path: str,
    schema: Dict[str, Any] | None = None,
):
    conn = psycopg2.connect(
        host=os.getenv("CATALOG_DB_HOST"),
        dbname=os.getenv("CATALOG_DB_NAME"),
        user=os.getenv("CATALOG_DB_USER"),
        password=os.getenv("CATALOG_DB_PASSWORD"),
        port=os.getenv("CATALOG_DB_PORT"),
    )
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO lakehouse.tables (table_name, layer, s3_path, schema_json)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (table_name, layer)
        DO UPDATE SET
            s3_path = EXCLUDED.s3_path,
            schema_json = EXCLUDED.schema_json,
            updated_at = now()
        """,
        (
            table_name,
            layer,
            s3_path,
            json.dumps(schema) if schema else None,
        ),
    )

    conn.commit()
    cur.close()
    conn.close()
