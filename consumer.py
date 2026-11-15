import pika
import time


def callback(ch, method, properties, body):
    task_id = body.decode()
    print(f"Consumer: Pobrałem zadanie {task_id}. Zmieniam status na 'in_progress'.")

    time.sleep(30)

    print(f"Consumer: Zakończyłem zadanie {task_id}. Status 'done'.")

    # potwierdzenie wykonania zadania - usunięcie z kolejki RabbitMQ
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="task_queue", durable=True)

    # pobieraj tylko 1 zadanie na raz
    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue="task_queue", on_message_callback=callback)

    print("Consumer uruchomiony. Szukam zadań... (Naciśnij CTRL+C aby zatrzymać)")

    channel.start_consuming()


if __name__ == "__main__":
    main()
