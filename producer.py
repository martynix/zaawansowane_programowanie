import pika
import uuid


def dodaj_zadanie():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="task_queue", durable=True)

    task_id = str(uuid.uuid4())[:8]

    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=task_id,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE  # Trwała wiadomość
        ),
    )

    print(f"Producer: Dodano zadanie {task_id} (pending)")
    connection.close()


if __name__ == "__main__":
    dodaj_zadanie()
