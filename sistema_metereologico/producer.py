from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    key_serializer=lambda chave:
        chave.encode("utf-8"),
    value_serializer=lambda valor:
        json.dumps(valor).encode("utf-8")
)

cidades = {
    "Brasília": 0,
    "Londres": 1,
    "Tokyo": 2
}

while(True):
    for cidade, partition in cidades.items():
        temperatura = round(
            random.uniform(15,35), 1)
        dados = {
            "cidade": cidade,
            "temperatura": temperatura
        }
        producer.send(
            "temperaturas",
            key=cidade,
            value=dados,
            partition=partition
        )
        print("enviado evento de: ", cidade)
    producer.flush()
    time.sleep(3)

