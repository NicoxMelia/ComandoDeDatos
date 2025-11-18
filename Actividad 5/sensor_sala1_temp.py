import time
import random
import paho.mqtt.client as paho
from paho import mqtt

running = False  # bandera para saber si el sensor está activo

def on_connect(client, userdata, flags, rc, properties=None):
    print("Sensor sala1/temp conectado con código %s" % rc)
    # Escucha mensajes de broadcast
    client.subscribe("lan/broadcast/#", qos=1)

def on_message(client, userdata, msg):
    global running
    command = msg.payload.decode()
    print(f"Comando recibido: {command}") 

    if command.upper() == "START":

        running = True
        print("Sensor ACTIVADO")
    elif command.upper() == "STOP":
        running = False
        print("Sensor DETENIDO")

client = paho.Client(client_id="sensor_sala1_temp", userdata=None, protocol=paho.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("ComandoDeDatos", "ComandoDeDatos2025")
client.connect("4fab220d63614e79a112f02cda5ad71d.s1.eu.hivemq.cloud", 8883)

client.loop_start()

while True:
    if running:
        temp = round(random.uniform(18.0, 30.0), 2)
        client.publish("lan/sala1/sensor/temp", payload=str(temp), qos=1)
        print("🌡️ Publicado temp:", temp)
    time.sleep(2)

