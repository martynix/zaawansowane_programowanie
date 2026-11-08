import time
import os


def zmien_status(task_id, nowy_status):
    with open("tasks.csv", "r") as file:
        linie = file.readlines()

    with open("tasks.csv", "w") as file:
        for linia in linie:
            if linia.startswith(f"{task_id},"):
                file.write(f"{task_id},{nowy_status}\n")
            else:
                file.write(linia)


def pobierz_zadanie():
    if not os.path.exists("tasks.csv"):
        return None

    with open("tasks.csv", "r") as file:
        for linia in file:
            task_id, status = linia.strip().split(",")
            if status == "pending":
                return task_id
    return None


def main():
    print("Consumer uruchomiony. Szukam zadań...")
    while True:
        task_id = pobierz_zadanie()

        if task_id:
            # 1. Zmiana statusu na in_progress
            zmien_status(task_id, "in_progress")
            print(
                f"Consumer: Pobrałem zadanie {task_id}. Zmieniam status na 'in_progress'."
            )

            # 2. Wykonywanie pracy (30s)
            time.sleep(30)

            # 3. Zmiana statusu na done
            zmien_status(task_id, "done")
            print(f"Consumer: Zakończyłem zadanie {task_id}. Status 'done'.")
        else:
            # Sprawdzanie pliku co 5 sekund w przypadku braku zadań
            time.sleep(5)


if __name__ == "__main__":
    main()
