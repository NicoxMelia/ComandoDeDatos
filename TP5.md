# Comunicaciones de Datos - Trabajo Practico N°5

**Integrantes**
_Pablo Castilla; Javier A. Fatu; Enzo L. Laura Surco; Nicolás O. Melia; Saqib D. Mohammad Cabrejos;_


**ComandoDeDatos**

**Facultad de Ciencias Exactas, Físicas y Naturales**

**Asignatura: Comunicaciones de datos**

**Profesores: Facundo Oliva Cuneo y Santiago Martin Henn**

### Informacion de los autores

 **Información de contactos**:
_pablo.castilla@mi.unc.edu.ar;_
_javier.fatu@mi.unc.edu.ar;_
_enzo.laura.surco@mi.unc.edu.ar;_
_nicolas.melia@mi.unc.edu.ar;_
_saqib.mohammad@mi.unc.edu.ar;_


## Resumen

Este informe detalla el diseño, implementación y análisis de un sistema de comunicaciones para el Internet de las Cosas (IoT) basado en el protocolo MQTT. El objetivo fue construir y evaluar una arquitectura completa, desde la simulación de dispositivos (sensores y actuadores) hasta la recolección, almacenamiento y visualización de datos en la nube.

Se utilizó un broker MQTTS gestionado (HiveMQ Cloud) como intermediario central. Se desarrollaron clientes en Python con la biblioteca paho-mqtt para simular patrones de comunicación Publish/Subscribe, incluyendo direccionamiento 1-a-1 y broadcast. La arquitectura se completó con un gateway que persiste los datos en archivos CSV y los expone a Prometheus, para su posterior visualización en un dashboard de Grafana.

El análisis de la arquitectura incluyó una inspección de paquetes con Wireshark, que confirmó la confidencialidad de los datos gracias al cifrado de TLS (MQTTS). El estudio concluye validando la flexibilidad y eficiencia del modelo Pub/Sub para IoT, al tiempo que identifica la dependencia de un broker central como un punto único de falla (SPOF) crítico en el diseño del sistema.

## Introducción

En el contexto actual del Internet de las Cosas (IoT), la comunicación eficiente entre un número masivo de dispositivos con recursos limitados es un desafío fundamental. Los protocolos de comunicación tradicionales, como HTTP, no son siempre adecuados debido a su alto consumo de recursos y su modelo de solicitud-respuesta.

El protocolo MQTT (Message Queuing Telemetry Transport) se ha establecido como el estándar de facto para la mensajería en IoT. Su ligereza, bajo overhead y, fundamentalmente, su arquitectura Publish/Subscribe (Pub/Sub), lo hacen ideal para redes con ancho de banda limitado o conexiones inestables.

El objetivo de este trabajo práctico es ir más allá de la teoría y construir una solución de IoT funcional de extremo a extremo (end-to-end). Se implementará un ecosistema completo que simula la recolección de datos de sensores, su envío seguro a un broker en la nube, el procesamiento a través de un gateway, y su visualización final en un dashboard de tiempo real.

A lo largo de este informe, se documentará la configuración del broker, el desarrollo de los clientes Python, la implementación de diferentes lógicas de comunicación (1-a-1 y broadcast), la captura de datos y, finalmente, un análisis crítico de la arquitectura, sus protocolos de transporte (TCP/TLS) y sus implicaciones en términos de seguridad y disponibilidad.


## Metodología

El trabajo se implementó en fases incrementales, combinando la configuración de servicios en la nube con el desarrollo de clientes y el análisis de red.

Las herramientas clave fueron:
* **Broker:** **HiveMQ Cloud** (para MQTTS seguro en el puerto 8883).
* **Clientes:** **Python** (con la biblioteca `paho-mqtt`).
* **Análisis de Red:** **Wireshark**.
* **Visualización:** **Grafana** (conectado a **Prometheus** y archivos **CSV**).

El proceso siguió estos pasos:
1.  **Configuración:** Despliegue del *broker* en HiveMQ Cloud y generación de credenciales.
2.  **Simulación:** Desarrollo de scripts en Python para probar la conexión (Ejercicio 3) y simular patrones de comunicación 1-a-1 y 1-a-N (*broadcast*) (Ejercicio 4).
3.  **Implementación del Pipeline:** Creación de un *gateway* para recolectar datos de sensores, persistirlos en CSV y exponerlos a Grafana/Prometheus (Ejercicio 5).
4.  **Análisis:** Captura de tráfico con Wireshark para verificar el cifrado MQTTS (Ejercicio 5e) y análisis teórico de la arquitectura (Ejercicio 6).

## Resultados

### 1) Resumir brevemente las características del protocolo MQTT. Incluir ventajas, desventajas y principales usos. Responder: ¿Qué es el patrón de diseño PubSub?.

* **Primero que responderemos ¿Qué es MQTT?**

MQTT (Message Queuing Telemetry Transport) es un protocolo ligero de mensajería diseñado para conectar dispositivos IoT (Internet of Things) con recursos limitados (como sensores o microcontroladores) a través de redes inestables o con poco ancho de banda.

Funciona sobre TCP/IP y se basa en el modelo Publicar/Suscribirse (Publish/Subscribe).

* **Características principales:**

1) Bajo consumo de ancho de banda: ideal para redes lentas o con interrupciones.

2) Orientado a eventos: los mensajes solo se envían cuando hay algo nuevo que publicar.

3) Arquitectura centralizada: todo pasa por un broker(un intermediario), que recibe los mensajes y los distribuye a los clientes suscritos.

4) Niveles de calidad de servicio (QoS): garantiza distintos niveles de entrega de mensajes (0, 1 o 2).

5) Soporte de tópicos jerárquicos: los mensajes se organizan en tópicos (por ejemplo casa/sala/temp), y se pueden usar comodines (+, #) para agruparlos.

 
**Ventajas:**

- Ligero y eficiente.
- Ideal para IoT y redes con recursos limitados.
- Fácil de implementar.
- Permite comunicación asincrónica (los dispositivos no necesitan estar conectados al mismo tiempo).
- Escalable para muchos dispositivos.

**Desventajas:**

- Depende de un broker central (si se cae, se interrumpe la comunicación).
- No tiene cifrado propio (se usa TLS/SSL aparte).
- No es adecuado para enviar archivos grandes o datos continuos.
- Requiere conexión TCP (no funciona bien en redes extremadamente inestables).

**Usos principales:**

- Sensores y actuadores IoT.
- Domótica (casas inteligentes).
- Vehículos conectados.
- Automatización industrial.
- Comunicación entre microcontroladores y servicios en la nube.

**¿Qué es el patrón Pub/Sub?**

El patrón Publish/Subscribe es un modelo de comunicación desacoplado, donde:

1) Un publicador (publisher) envía mensajes a un tópico.

2) Un suscriptor (subscriber) recibe los mensajes del tópico al que está suscrito.

3) Un broker intermedia entre ambos.

4) Esto evita que los dispositivos tengan que conocerse entre sí: solo deben saber el nombre del tópico.

* Ejemplo:
````
sensor/temp publica → broker reenvía → display/temp recibe.

````

### 2) Instalar/desplegar y ejecutar un broker MQTT. Por ejemplo, en HiveMQ, tendremos un dashboard con parámetros de red para conectarnos (no te preocupes que es gratis):

* Primero generamos el cluster o mejor dicho el broker que conecta el publisher con el suscripter.

![image](https://hackmd.io/_uploads/H1yhvhfgbg.png)

* Generamos la credencial

![image](https://hackmd.io/_uploads/BJlSu3MlZx.png)

* Con esta credencial ya creada, ya tenemos las claves para enlazar el publicador con el suscriptor. 

![image](https://hackmd.io/_uploads/ry7R_2fxWg.png)

### 3) Verificar que el broker funciona, suscribiendote con un cliente (pueden encontrar tutoriales para utilizar Java, python u otros lenguajes para este propósito)

* Usando el codigo y tutorial que existe en la pagina HiveMQ Cloud, nos permite simular en la pagina un cliente suscrito a un topico, por ende el codigo ya ejecutado en VSCode enviara el mensaje "hot" al topico y observaremos el mensaje y la conexion correctamente establecido.

![image](https://hackmd.io/_uploads/HJvbhpGgbe.png)
![image](https://hackmd.io/_uploads/ryEm2azgWx.png)

````python
import time
import paho.mqtt.client as paho
from paho import mqtt

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="clientSaqib", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("ComandoDeDatos", "ComandoDeDatos2025")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("4fab220d63614e79a112f02cda5ad71d.s1.eu.hivemq.cloud", 8883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("encyclopedia/#", qos=1)

# a single publish, this can also be done in loops, etc.
client.publish("encyclopedia/temperature", payload="hot", qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_forever()
````
* Este codigo fue ejecutado en la terminal [nombre_del_archivo].py

### 4) Una vez que tenemos nuestra arquitectura funcionando: 
### a) Simular una comunicación directa entre dos nodos de una red local. Para ello crear dos clientes: Dispositivo A, que publica en lan/deviceA/status, Dispositivo B se suscribe a ese tópico y muestra los mensajes recibidos. Capturar y documentar resultados.

* Repetimos un poco el procedimiento anterior en donde primero ejecutamos el codigo del publicador:

> Codigo DeviceA.py
````python
import time
import paho.mqtt.client as paho
from paho import mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("Dispositivo A esta conectado con el codigo %s" % rc)

client = paho.Client(client_id="DeviceA", userdata=None, protocol=paho.MQTTv311)
client.on_connect = on_connect

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("ComandoDeDatos", "ComandoDeDatos2025")
client.connect("4fab220d63614e79a112f02cda5ad71d.s1.eu.hivemq.cloud", 8883)

client.loop_start()

# Enviamos un mensaje cada 3 segundos
while True:
    message = "Dispositivo A está en línea"
    client.publish("lan/deviceA/status", payload=message, qos=1)
    print("Publicado:", message)
    time.sleep(3)
````

* Y despues el codigo del Cliente que esta suscrito a ese topico especifico: 
> Codigo DeviceB.py
````python
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
````

* Resultados: 

![image](https://hackmd.io/_uploads/HJsShNSgbx.png)

![image](https://hackmd.io/_uploads/ByPjn4Sxbg.png)



### b) Crear un tópico general lan/broadcast/#. Configurar al menos dos clientes para suscribirse a lan/broadcast/#. Desde un cliente “central”, publicar mensajes en lan/broadcast/all. Capturar y documentar resultados. Con esto simularemos broadcasting en esta pequeña LAN.

* Repetimos un poco el procedimiento anterior en donde primero ejecutamos el codigo del publicador, en este caso sera un codigo broadcast hacia todos los dispositivos suscritos a ese topico:

> Codigo Central.py
````python
import time
import paho.mqtt.client as paho
from paho import mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("Central esta conectado, empezando a enviar datos:%s" % rc)

def on_publish(client, userdata, mid, properties=None):
    print("N° de Mensaje: " + str(mid))

client = paho.Client(client_id="central", userdata=None, protocol=paho.MQTTv311)
client.on_connect = on_connect
client.on_publish = on_publish

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("ComandoDeDatos", "ComandoDeDatos2025")
client.connect("4fab220d63614e79a112f02cda5ad71d.s1.eu.hivemq.cloud", 8883)

client.loop_start()

# Enviamos un mensaje cada 3 segundos
message = "Mensaje Broadcast desde el cliente central"
while True:
    client.publish("lan/broadcast/all", payload=message, qos=1)
    print("Publicado:", message)
    time.sleep(3)
````
* Ahora ejecutamos los codigos de los Dispositivos, que son los clientes:

> Codigo Device1.py
````python
import paho.mqtt.client as paho
from paho import mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("Dispositivo 1 Conectado. %s" % rc)
    client.subscribe("lan/broadcast/#", qos=1)

def on_message(client, userdata, msg):
    print(f"Recibido en {msg.topic}: {msg.payload.decode()}")

client = paho.Client(client_id="device1", userdata=None, protocol=paho.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("ComandoDeDatos", "ComandoDeDatos2025")
client.connect("4fab220d63614e79a112f02cda5ad71d.s1.eu.hivemq.cloud", 8883)

client.loop_forever()

````

> Codigo Device2.py
````python
import paho.mqtt.client as paho
from paho import mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("Dispositivo 2 Conectado. %s" % rc)
    client.subscribe("lan/broadcast/#", qos=1)

def on_message(client, userdata, msg):
    print(f"Recibido en {msg.topic}: {msg.payload.decode()}")

client = paho.Client(client_id="device12", userdata=None, protocol=paho.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message


client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("ComandoDeDatos", "ComandoDeDatos2025")
client.connect("4fab220d63614e79a112f02cda5ad71d.s1.eu.hivemq.cloud", 8883)

client.loop_forever()
````

* Resultados:

![image](https://hackmd.io/_uploads/HyIBaErgbe.png)


![image](https://hackmd.io/_uploads/SyCUaNreZx.png)


![image](https://hackmd.io/_uploads/BJow6EHxbl.png)

---
## Ejercicio 5

### a) Simulacion y recoleccion de datos de los clientes subscriptos al gateway
![image](https://hackmd.io/_uploads/HJzLT5ug-l.png)



### b) Recopilacion de datos de los sensores en formato CSV
![image](https://hackmd.io/_uploads/rJ1OpcugWe.png)


### c) Ploteo de datos de los sensores usando Infinity como Data Source con datos en fortato CSV
![image](https://hackmd.io/_uploads/Bk02nY_gbl.png)
### Los siguientes datos de los sensores fueron capturados usando Prometheus como Data Source
![image](https://hackmd.io/_uploads/Hylla3OgWl.png)


### d) Mediante broadcasting enviamos dos mensajes de comandos a los sensores: START y STOP
![image](https://hackmd.io/_uploads/SkmFacdg-e.png)
![image](https://hackmd.io/_uploads/Sy_tTqOxWx.png)


### e) Captura de un paquete de MQTTs mediante wireshark
El servicio de HiveMQ Cloud obliga a usar MQTTS por seguridad, por eso nos conectamos al puerto 8883.
![image](https://hackmd.io/_uploads/S1jTViOgWl.png)
Como se observa, el sniffer (Wireshark) no puede leer el contenido de la comunicación. Solo puede ver que se están enviando "datos de aplicación" cifrados. Esto comprueba que la conexión es segura y protege la confidencialidad de los datos de los sensores contra atacantes que intenten espiar la red.

---

## Ejercicio 6
### a) ¿Sobre qué protocolos de capa de transporte están trabajando en esta actividad?

En esta actividad, MQTT se apoya directamente en TCP como protocolo de transporte.
TCP proporciona características esenciales para un sistema IoT confiable:

* Entrega garantizada, gracias a retransmisiones y ACKs.
* Orden en los paquetes, evitando inconsistencias en datos de sensores.
* Control de flujo, muy útil para dispositivos con distintos recursos.

Cuando se usa un broker en la nube como HiveMQ Cloud, TCP se combina con TLS sobre el puerto 8883, agregando:

* Cifrado punto a punto
* Autenticación del servidor
* Integridad reforzada

Esta combinación segura se conoce comúnmente como MQTTS.

### b) ¿Qué pueden decir sobre la garantía de Integridad, Confidencialidad y Disponibilidad en esta arquitectura?

**1) Integridad**

La integridad es asegurada principalmente por:

* TCP, que valida que los datos lleguen tal como fueron enviados.
* TLS, que agrega una capa criptográfica donde cualquier alteración del mensaje invalida el paquete.

Esto es crítico en IoT, donde la data que viaja suele ser sensible (temperaturas, estados, comandos, etc.).

**2) Confidencialidad**

En esta práctica, toda la comunicación con HiveMQ Cloud va por TLS cifrado.
Esto implica:

* El payload MQTT no puede ser leído por un atacante (ni siquiera por Wireshark).
* Evita ataques de escucha (sniffing) y manipulación.
En la práctica, te da un canal seguro por defecto.

**3) Disponibilidad**

Es el punto más delicado:

* Si el broker central cae, toda la infraestructura MQTT deja de funcionar.
* Depende 100% de la conexión a Internet si usás un broker cloud.
* La disponibilidad del sistema es tan fuerte como la disponibilidad del broker.

MQTT asegura integridad y confidencialidad, pero no puede garantizar disponibilidad por sí solo.

### C) ¿Qué rol juegan los niveles de QoS en la fiabilidad de los mensajes?

MQTT te permite negociar cuánta confiabilidad querés:

**QoS 0 — "At most once"**

- No hay confirmación.
- Es el más rápido y liviano.
- Si se pierde, se perdió.
Ideal para sensores que envían datos constantemente y donde perder algún valor no importa.

**QoS 1 — "At least once"**

- El receptor confirma recepción.
- Puede duplicarse, pero no perderse.
Es el más usado en IoT, un balance entre confiabilidad y rendimiento.

**QoS 2 — "Exactly once"**

- Garantiza entrega única, sin duplicados.
- Es más costoso en latencia.
Se usa en transacciones críticas (pagos, control industrial).

QoS define cuánta garantía de entrega necesita el sistema, según la naturaleza de los datos.

### d) ¿Qué ventajas ofrece el modelo pub/sub frente al modelo cliente-servidor?

El modelo Publish/Subscribe (Pub/Sub) de MQTT ofrece ventajas arquitectónicas significativas sobre el modelo tradicional Cliente-Servidor (ej. HTTP REST), principalmente al desacoplar a los participantes.

### Ventajas Principales:

* **Desacoplamiento de Espacio:** El publicador (sensor) y el suscriptor (gateway) no necesitan conocerse. No intercambian direcciones IP ni puertos; solo necesitan conocer la dirección del broker y el topic (tema) de interés.

* **Desacoplamiento de Tiempo:** Los participantes no necesitan estar conectados simultáneamente. Un sensor puede publicar datos mientras el gateway está desconectado. El broker puede almacenar los mensajes (según la configuración de persistencia) y entregarlos cuando el suscriptor se reconecte.

* **Desacoplamiento de Sincronización:** El acto de publicar un mensaje es asíncrono y no bloqueante. El sensor publica y puede continuar con sus tareas sin esperar a que los suscriptores procesen el mensaje.

* **Escalabilidad y Flexibilidad:** Es trivial añadir nuevos suscriptores (ej. una app móvil, otra base de datos) sin modificar al publicador original. Del mismo modo, se pueden añadir más sensores (publicadores) sin afectar a los suscriptores.

* **Comunicación 1-a-N (Multicast):** Un solo mensaje publicado en un topic puede ser distribuido eficientemente por el broker a miles de suscriptores interesados.


### e) ¿Qué limitaciones tiene MQTT respecto a una red LAN real?

MQTT es ideal para IoT, pero tiene sus límites:

* **Latencia mayor**
En una LAN real la comunicación es inmediata; con MQTT hay intermediación por el broker.

* **No es apto para alta tasa de datos**
Está pensado para mensajes pequeños.
No sirve para: streaming de video, audio, archivos grandes.

* **Dependencia del broker**
Si el broker está en la nube, dependés de Internet.

* **TCP introduce overhead**
Cada paquete requiere más gestión y control.

* **No reemplaza protocolos industriales**
Equipos industriales reales usan CAN, Profibus, Modbus RTU, etc., por robustez física.

**En resumen:**
MQTT es ideal para datos pequeños y eventos, no para tráfico intenso ni control de tiempo real estricto.


### f) ¿Qué implicaciones tiene depender de un broker central para la comunicación?

Esta arquitectura es simple, pero tiene un trade-off fuerte:

**1) Single Point of Failure**

Si el broker falla:

* Nadie publica
* Nadie recibe
* Nadie se entera

Es literalmente el “corazón” del sistema.

**2) Cuello de botella**

Todo el tráfico pasa por el broker.
Si hay cientos o miles de sensores:

* Puede saturarse
* Puede crecer la latencia
* Puede provocar pérdidas (si no se dimensiona)

**3) Riesgos operativos**

* Necesita monitoreo, logs, backups, escalabilidad.
* En la nube: dependés de terceros.

**4) Pero también trae beneficios**

* Seguridad centralizada
* Autenticación unificada
* Gestión de tópicos ordenada
* Administración más sencilla

**En resumen:**
El broker central facilita todo, pero introduce dependencia absoluta. En ingeniería eso implica planificar redundancia o brokers distribuidos si la escala crece.

---

## Conclusiones

Al finalizar este trabajo práctico, comprobamos que MQTT es un protocolo ideal para aplicaciones de IoT por varias razones:

Primero, el modelo Pub/Sub es mucho más flexible que el clásico cliente-servidor. Como vimos en el ejercicio 4, pudimos pasar de una comunicación 1-a-1 a un "broadcast" (1-a-N) simplemente cambiando los *topics*. Esto demuestra que es muy fácil agregar nuevos sensores o aplicaciones sin tener que modificar los dispositivos que ya están funcionando.

Segundo, logramos armar una arquitectura de IoT completa (ejercicio 5). Conseguimos que los datos de los "sensores" llegaran al broker, fueran procesados por un *gateway* y se visualizaran en Grafana.

Por otro lado, vimos la seguridad MQTTS. Al usar Wireshark 5e, vimos que los paquetes de datos estaban realmente cifrados. Un atacante en la red no podría leer la información de nuestros sensores.

Finalmente, el trabajo también nos dejó clara la principal debilidad de esta arquitectura: la dependencia total del broker. El broker es un **Punto Único de Falla**. Si se cae, toda la comunicación se detiene. En una implementación real, esto es un riesgo muy importante que debería solucionarse con sistemas de respaldo (redundancia).

En resumen, MQTT es liviano, eficiente y perfecto para enviar datos pequeños, pero no sirve para cosas pesadas como video. Su gran ventaja es la flexibilidad, pero su gran desventaja es depender de un solo punto central.

## Bibliografía y Referencías

[Fundamentos de seguridad de TLS/SSL y MQTT](https://www.hivemq.com/blog/mqtt-security-fundamentals-tls-ssl/)

[Paho MQTT Client Example](https://github.com/hivemq-cloud/paho-mqtt-client-example)

[CSV en Grafana con fuente de datos Infinity](https://youtu.be/ZVsaCUsZLa8?si=vWhgTOEQJKmv1Cfc)

[Comienza a usar Grafana y Prometheus](https://grafana.com/docs/grafana/latest/getting-started/get-started-grafana-prometheus/)
