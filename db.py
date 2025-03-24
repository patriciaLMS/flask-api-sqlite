import sqlite3

DB_NAME = "data.db"

def connect_db():
    
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row 
    return conn

def create_table():
   
    with connect_db() as conn:
        conn.execute(
            """CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                value TEXT NOT NULL
            )"""
        )

def insert_data(value):
   
    with connect_db() as conn:
        conn.execute("INSERT INTO data (value) VALUES (?)", (value,))
        conn.commit()

def fetch_data():
    
    try:
        with connect_db() as conn:
            cursor = conn.execute("SELECT * FROM data LIMIT 100")
            return [{"id": row["id"], "data": row["value"]} for row in cursor.fetchall()]
    except Exception as e:
        return {"error": str(e)}
