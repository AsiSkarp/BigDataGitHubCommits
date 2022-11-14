import json
from kafka import KafkaProducer

with open("../../../../../test_data/2015-01-01-15.json.txt") as f:
    producer = KafkaProducer(bootstrap_servers="bddst-g04-Node1.uvm.sdu.dk:9092")
    for line in f:
        producer.send("alice-test", json.loads(line).encode("utf-8"))


# with client.read("../../../../../test_data/2015-01-01-15.json.txt") as reader:
#    text = reader.read().splitlines()
#    producer = KafkaProducer(bootstrap_servers="bddst-g04-Node1.uvm.sdu.dk:9092")
#    for line in text:
#        producer.send("alice-test", line.encode("utf-8"))
