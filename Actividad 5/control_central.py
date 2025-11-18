import paho.mqtt.client as paho
from paho import mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("Control central conectado con código %s" % rc)

client = paho.Client(client_id="ControlCentral", userdata=None, protocol=paho.MQTTv311)
client.on_connect = on_connect

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("ComandoDeDatos", "ComandoDeDatos2025")
client.connect("4fab220d63614e79a112f02cda5ad71d.s1.eu.hivemq.cloud", 8883)

client.loop_start()

print("\n--- Control Central ---")
print("Comandos disponibles: START, STOP, EXIT\n")

while True:
    cmd = input("Enviar comando: ").strip().upper()
    if cmd == "EXIT":
        break
    elif cmd in ["START", "STOP"]:
        client.publish("lan/broadcast/all", payload=cmd, qos=1)
        print(f"📡 Enviado comando: {cmd}")
    else:
        print("⚠️ Comando inválido. Usa START, STOP o EXIT.")
