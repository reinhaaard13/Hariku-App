from sqlalchemy import create_engine

DB_NAME = "my-hariku.db"
engine = create_engine(f"sqlite:///hariku/{DB_NAME}")