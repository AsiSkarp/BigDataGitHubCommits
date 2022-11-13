from hdfs import InsecureClient
from kafka import KafkaProducer

client = InsecureClient('http://namenode:9870', user='root')

with client.read('/alice-in-wonderland.txt') as reader:
    text = reader.read().splitlines()
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    for line in text:
        producer.send('alice-test', line.encode('utf-8'))

