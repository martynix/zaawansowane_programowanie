import sqlite3
import time


DB_NAME = "tasks.db"


def pobierz_i_zarezerwuj_zadanie():
    """
    Pobiera jedno zadanie ze statusem 'pending' 
    i natychmiast zmienia jego status na 'in_progress'.
    """
    # timeout=30 sprawia, że jeśli baza jest chwilowo zablokowana przez inny proces,
    # consumer odczeka do 30s zamiast wyrzucić błąd
    with sqlite3.connect(DB_NAME, timeout=30) as conn:
        cursor = conn.cursor()
        
        # 1. Szukamy pierwszego zadania ze statusem 'pending'
        cursor.execute(
            "SELECT id FROM tasks WHERE status = 'pending' LIMIT 1"
        )
        row = cursor.fetchone()
        
        if row:
            task_id = row[0]
            # 2. Rezerwujemy je (zmieniamy na in_progress)
            cursor.execute(
                "UPDATE tasks SET status = 'in_progress' WHERE id = ?", 
                (task_id,)
            )
            conn.commit()
            return task_id
            
    return None


def oznacz_jako_done(task_id):
    """Zmienia status wybranego zadania na 'done'"""
    with sqlite3.connect(DB_NAME, timeout=30) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET status = 'done' WHERE id = ?", 
            (task_id,)
        )
        conn.commit()


def main():
    print("Consumer uruchomiony. Szukam zadań w bazie SQLite...")
    while True:
        task_id = pobierz_i_zarezerwuj_zadanie()
        
        if task_id:
            print(f"Consumer: Pobrałem zadanie {task_id}. Status -> 'in_progress'.")
            
            # 3. Wykonywanie pracy (30s)
            time.sleep(30)
            
            # 4. Zakończenie pracy
            oznacz_jako_done(task_id)
            print(f"Consumer: Zakończyłem zadanie {task_id}. Status -> 'done'.")
        else:
            # Jeśli brakuje zadań, czekamy 5 sekund
            time.sleep(5)

if __name__ == "__main__":
    main()
