import csv
import time
import paho.mqtt.client as paho
import prometheus_client
from paho import mqtt
from prometheus_client import start_http_server, Gauge

HUMIDITY_GAUGE = Gauge('sensor_humedad', 'Humedad del sensor MQTT', ['sala', 'sensor_tipo'])
TEMPERATURE_GAUGE = Gauge('sensor_temperatura', 'Temperatura del sensor MQTT', ['sala', 'sensor_tipo'])

start_http_server(8080)
print("Servidor Prometheus Exporter iniciado en el puerto 8080")

def on_connect(client, userdata, flags, rc, properties=None):
    print("Gateway conectado con código %s" % rc)
    client.subscribe("lan/#", qos=1)

def on_message(client, userdata, msg):
    topic = msg.topic
    #value = msg.payload.decode()
    raw_value = msg.payload.decode()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    print(f"{timestamp} | {topic} -> {raw_value}")

    if "broadcast" in topic:
        print(f"Tópico {topic} es un comando, no un valor de sensor. Ignorado para Prometheus/CSV.")
        return 

    # Guardar en CSV
    with open("datos_sensores.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, topic, raw_value])

    # --- Lógica de Actualización de Prometheus ---
    try:
        # 1. Intentar convertir el valor a float para Prometheus
        value = float(raw_value)
    except ValueError:
        print(f"Valor no numérico en el tópico {topic}. No se actualiza Prometheus.")
        return

    # 2. Parsear el tópico (ej: lan/sala1/sensor/hum)
    parts = topic.split('/')
    
    if len(parts) >= 4 and parts[0] == 'lan':
        sala = parts[1]
        sensor_tipo = parts[3] 
        
        # 3. Asignar el valor al Gauge correcto según el tipo de sensor
        if sensor_tipo == 'hum':
            HUMIDITY_GAUGE.labels(sala=sala, sensor_tipo=sensor_tipo).set(value)
            print(f"📈 Métrica de Humedad actualizada para {sala}")
        
        elif sensor_tipo == 'temp':
            TEMPERATURE_GAUGE.labels(sala=sala, sensor_tipo=sensor_tipo).set(value)
            print(f"🔥 Métrica de Temperatura actualizada para {sala}")

        else:
            print(f"Tipo de sensor ({sensor_tipo}) no reconocido para Prometheus.")
    # -----------------------------------------------

client = paho.Client(client_id="GatewayCentral", userdata=None, protocol=paho.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("ComandoDeDatos", "ComandoDeDatos2025")
client.connect("4fab220d63614e79a112f02cda5ad71d.s1.eu.hivemq.cloud", 8883)

# Crear archivo CSV con encabezado
with open("datos_sensores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "topic", "valor"])

client.loop_forever()
