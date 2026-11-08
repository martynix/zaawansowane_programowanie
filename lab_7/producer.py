import sqlite3
import uuid


DB_NAME = "tasks.db"


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                status TEXT NOT NULL
            )
        """)
        conn.commit()


def dodaj_zadanie():
    init_db()
    task_id = str(uuid.uuid4())[:8]
    
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (id, status) VALUES (?, ?)", 
            (task_id, "pending")
        )
        conn.commit()
        
    print(f"Producer: Dodano zadanie {task_id} (pending)")

if __name__ == "__main__":
    dodaj_zadanie()
