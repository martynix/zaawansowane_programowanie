import time
import uuid


def dodaj_zadanie():
    # Generowanie unikalnego ID dla zadania
    task_id = str(uuid.uuid4())[:8]

    with open("tasks.csv", "a") as file:
        file.write(f"{task_id},pending\n")

    print(f"Producer: Dodano zadanie {task_id} (pending)")


if __name__ == "__main__":
    dodaj_zadanie()


# for i in {1..100}; do python producer.py;
