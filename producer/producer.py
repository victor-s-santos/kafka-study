from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")
producer.send('python-kafka1', b'using python to send messages')
producer.flush()