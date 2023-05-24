from kafka import KafkaConsumer

consumer = KafkaConsumer('segundo_teste')
for msg in consumer:
    print (msg)