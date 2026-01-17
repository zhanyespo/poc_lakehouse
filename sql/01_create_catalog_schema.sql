CREATE SCHEMA IF NOT EXISTS lakehouse;

CREATE TABLE IF NOT EXISTS lakehouse.tables (
    table_id SERIAL PRIMARY KEY,
    table_name TEXT NOT NULL,
    layer TEXT NOT NULL CHECK (layer IN ('bronze','silver','gold')),
    s3_path TEXT NOT NULL,
    schema_json JSONB,
    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now(),
    UNIQUE (table_name, layer)
);

CREATE TABLE IF NOT EXISTS lakehouse.pipeline_runs (
    run_id UUID PRIMARY KEY,
    dag_id TEXT,
    status TEXT,
    started_at TIMESTAMP,
    finished_at TIMESTAMP,
    error TEXT
);

CREATE TABLE IF NOT EXISTS lakehouse.lineage (
    source_table TEXT,
    target_table TEXT,
    created_at TIMESTAMP DEFAULT now()
);
