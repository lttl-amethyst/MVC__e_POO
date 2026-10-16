from kafka import KafkaConsumer, TopicPartition
import json


consumer = KafkaConsumer(
    bootstrap_servers="localhost:9092",
    key_deserializer=lambda chave:
        chave.decode("utf-8"),
    value_deserializer=lambda valor:
        json.loads(valor.decode("utf-8"))
)
consumer.assign([
    TopicPartition("temperaturas", 0)
])

for mensagem in consumer:
    cidade = mensagem.key
    dados = mensagem.value
    print(
        f"Chave: {cidade} | "
        f"Temperatura: {dados['temperatura']}°C | "
        f"Offset: {mensagem.offset}"
    )
