import os

S3_BUCK =  os.getenv("S3_BUCKET_NAME", "lakehouse")

def s3_path(*paths: str) -> str:
    """This is used to build S3 paths for various lakehouse components."""
    cleaned_paths = [path.strip("/") for path in paths]
    return f"s3://{S3_BUCK}/" + "/".join(cleaned_paths)

