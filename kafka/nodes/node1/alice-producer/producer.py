import os
import json
from kafka import KafkaProducer

# "../../../../../test_data/2015-01-01-15.json"
uz_path = "/app/test_data/2015-01-01-15.json"

# print(os.listdir(uz_path))

with open(uz_path, encoding="utf-8") as f:
    producer = KafkaProducer(bootstrap_servers="bddst-g04-Node1.uvm.sdu.dk:9092")
    for line in f:
        producer.send("alice-test", json.loads(line).encode("utf-8"))
