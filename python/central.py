##Crear un tópico general lan/broadcast/#. Configurar al menos dos clientes para suscribirse a
##lan/broadcast/#. Desde un cliente “central”, publicar mensajes en lan/broadcast/all. Capturar y
##documentar resultados. Con esto simularemos broadcasting en esta pequeña LAN.

import time
import paho.mqtt.client as paho
from paho import mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("Central esta conectado:%s" % rc)

client = paho.Client(client_id="central", userdata=None, protocol=paho.MQTTv311)
client.on_connect = on_connect

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("ComandoDeDatos", "ComandoDeDatos2025")
client.connect("4fab220d63614e79a112f02cda5ad71d.s1.eu.hivemq.cloud", 8883)

client.loop_start()

# Enviamos un mensaje cada 3 segundos
while True:
    message = "Central enviando datos"
    client.publish("lan/broadcast/all", payload=message, qos=1)
    print("Publicado:", message)
    time.sleep(3)
