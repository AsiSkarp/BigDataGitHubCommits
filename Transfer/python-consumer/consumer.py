from kafka import KafkaConsumer

consumer = KafkaConsumer("new_commits", bootstrap_servers="kafka:9092")

for msg in consumer:
    print(msg)
