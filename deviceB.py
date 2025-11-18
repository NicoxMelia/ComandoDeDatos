import paho.mqtt.client as paho
from paho import mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("Device B connected with code %s" % rc)
    client.subscribe("lan/deviceA/status", qos=1)

def on_message(client, userdata, msg):
    print(f"Received on {msg.topic}: {msg.payload.decode()}")

client = paho.Client(client_id="DeviceB", userdata=None, protocol=paho.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("ComandoDeDatos", "ComandoDeDatos2025")
client.connect("4fab220d63614e79a112f02cda5ad71d.s1.eu.hivemq.cloud", 8883)

client.loop_forever()
