from confluent_kafka import Producer
import json
import socket

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': socket.gethostname()
}

producer = Producer(conf)

# Delivery callback
def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# JSON message
message = {
    "id": 101,
    "name": "Ravi Verma",
    "role": "Data Engineer"
}

# Send message
producer.produce(
    topic='test-topic',
    value=json.dumps(message),
    callback=delivery_report
)

producer.flush()