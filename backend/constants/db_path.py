import os

# Use environment variable DATABASE_PATH if set, otherwise default to local path
DB_PATH = os.environ.get("DATABASE_PATH", "backend/database/uil_archives.db")
# DB_PATH = "testing/test.db"