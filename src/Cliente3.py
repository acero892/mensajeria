from kafka import KafkaProducer
import json
import time
import random # Importamos el módulo random

# Configura el productor de Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Archivo de mensajes
json_file_path = 'mensajes_cliente3.json' # Asegúrate de que este archivo exista

print(f"Enviando mensajes desde  '{json_file_path}' al tópico 'user-topic'...")

messages_from_json = [] 

try:
    with open(json_file_path, 'r', encoding='utf-8') as f:
        messages_from_json = json.load(f)

except FileNotFoundError:
    print(f"Error fatal: El archivo '{json_file_path}' no fue encontrado. Verifica la ruta y reinicia el productor.")
    exit() 
except json.JSONDecodeError:
    print(f"Error fatal: No se pudo decodificar el archivo JSON '{json_file_path}'. Asegúrate de que esté bien formado.")
    exit() 
except Exception as e:
    print(f"Ocurrió un error inesperado al cargar el archivo: {e}")
    exit() 

if not messages_from_json:
    print("El archivo no contiene mensajes")
    exit()


while True:
    try:
        # Elige un mensaje aleatorio de json
        msg_data = random.choice(messages_from_json)

        if isinstance(msg_data, dict):
            producer.send('user-topic', value=msg_data)
            print(f"Producido mensaje aleatorio: {msg_data}")
        else:
            print(f"Error al leer el mensaje: {msg_data}")
 # Valida que el mensaje llegue al broker de kafka
        producer.flush() 

        # Genera el tiempo random del envio del mensaje
        random_sleep_time = random.uniform(3, 5) # Genera un float entre 3.0 y 5.0
      
        time.sleep(random_sleep_time)

    except Exception as e:
        print(f"Ocurrió un error al enviar el mensaje: {e}. Reintentando en 5 segundos...")
        time.sleep(5) 

# Estas líneas solo se ejecutarán si el bucle infinito se rompe (lo cual no debería pasar con este diseño)
producer.close()
print("El productor se ha cerrado.")

"""
from kafka import KafkaProducer
import json
import time
import ast

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    try: 
        data = ast.literal_eval(input("Enter data to send (or 'exit' to quit): "))
        if data == 'exit':
            break
        elif isinstance(data, dict):
            producer.send('user-topic', value=data)
            print(f"Produced: {data}")
        else:
            print("Invalid input. Please enter a dictionary.")
    except Exception as e:
        print("Invalid input. Please enter a dictionary.")


producer.flush()
producer.close()"""