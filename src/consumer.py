from kafka import KafkaConsumer
import json
from pymongo import MongoClient

# Configuración de Kafka
consumer = KafkaConsumer(
    'user-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Configuración de MongoDB
# Se conecta al contenedor de MongoDB en localhost:27017
mongo_client = MongoClient('mongodb://localhost:27017/')

# Selecciona la base de datos y la colección
db = mongo_client['comments_db']
collection = db['user_comments']

print("Consumiendo mensajes y guardando en MongoDB...")
for msg in consumer:
    try:
        # Extrae los datos del mensaje de Kafka
        data = msg.value

        # Inserta el documento en la colección de MongoDB
        result = collection.insert_one(data)
        print(f"Insertado en MongoDB con _id: {result.inserted_id}")

        # Imprime el mensaje consumido
        print(f"Consumido: {data}\n")
    except Exception as e:
        print(f"Error al procesar el mensaje: {e}")

# Cierra la conexión al salir del bucle
consumer.close()
mongo_client.close()