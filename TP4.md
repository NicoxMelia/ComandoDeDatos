# Comunicaciones de Datos - Trabajo Practico N°4

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

Este trabajo práctico se centra en la configuración y comprensión de las Capas de Acceso en Redes Locales (LAN), abordando la clasificación de redes (LAN, MAN, WAN), el protocolo IEEE 802.1Q, las VLAN y el concepto de tagging o etiquetado. La parte práctica, realizada en Packet Tracer, se divide en dos fases: primero, la configuración de una topología simple con dos switches (SW-1 y SW-2) para tareas básicas de nombramiento, aseguramiento con contraseñas y creación de VLANs (VLAN 10 Laboratorio, VLAN 20 Bar, VLAN 99 Management).

La segunda fase consiste en la simulación avanzada de una red LAN a bordo de una aeronave, utilizando VLAN, NAT y ACLs para segmentar y controlar el acceso a los usuarios de las clases Turista (acceso solo a servidor local), Business (servidor e Internet) y Administración (acceso total). Se configuran subinterfaces con 802.1Q en el router y se implementan ACLs para aplicar las políticas de seguridad requeridas, como el bloqueo de Internet a la VLAN Turista. El objetivo final es consolidar las habilidades de diseño, configuración y aseguramiento de redes segmentadas.

## Introducción

El presente Trabajo Práctico N°4 busca introducir los fundamentos de la capa de acceso en redes de datos, con un enfoque particular en la segmentación lógica mediante Redes de Área Local Virtual (VLAN). La necesidad de segmentar el tráfico, ya sea por motivos de seguridad o de rendimiento, hace imperativo el dominio del protocolo IEEE 802.1Q y sus mecanismos de etiquetado de tramas (tagging), lo cual permite la interconexión eficiente de múltiples redes virtuales a través de enlaces troncales.

A nivel práctico, el trabajo se desarrolla en Packet Tracer y culmina con un escenario de aplicación real: el diseño y la implementación de una red LAN con políticas de acceso diferenciadas a bordo de una aeronave. Este ejercicio no solo requiere la configuración de VLANs, sino también la aplicación de herramientas de control de tráfico como las Access Control Lists (ACLs) y el enrutamiento con NAT (Network Address Translation), logrando así que los diferentes grupos de usuarios (Turista, Business, Admin) accedan a los recursos de la red y a Internet según las restricciones específicas de cada clase.

## Metodologia

El desarrollo del trabajo práctico se llevó a cabo de manera secuencial, combinando instancias teóricas y prácticas dentro del entorno de simulación Cisco Packet Tracer. En primer lugar, se realizó una investigación teórica sobre la clasificación de redes según su alcance, el funcionamiento del protocolo IEEE 802.1Q, y los conceptos de VLAN y tagging, con el objetivo de comprender los fundamentos necesarios para la configuración de redes segmentadas.

Posteriormente, se procedió a la configuración de una topología básica compuesta por dos switches interconectados (SW-1 y SW-2) y dos PCs, donde se implementaron tareas esenciales como la asignación de nombres, contraseñas, creación de VLANs (Laboratorio, Bar y Management), y la configuración de enlaces troncales entre los dispositivos. Cada etapa fue validada mediante comandos de verificación como show vlan brief, show ip interface brief y pruebas de conectividad por medio de pings entre los nodos.

En la segunda parte, se diseñó y configuró una red LAN simulada a bordo de una aeronave, aplicando los conocimientos previos sobre VLAN, NAT y ACLs. Se crearon tres segmentos lógicos (Turista, Business y Administración), cada uno con políticas de acceso diferenciadas. En el router se configuraron subinterfaces con etiquetado 802.1Q, traducción de direcciones (NAT) y listas de control de acceso (ACLs) para restringir el tráfico según el tipo de usuario.

Finalmente, se realizaron pruebas de conectividad y acceso a recursos locales e Internet, comprobando el cumplimiento de las políticas establecidas: la VLAN Turista con acceso limitado al servidor interno, Business con conexión a Internet y al servidor, y Administración con acceso total. Los resultados de las simulaciones permitieron verificar el correcto funcionamiento de la segmentación y el control de tráfico definidos en el diseño.






## Resultados

## Actividad 1
**a)  Investigar cómo se clasifican las redes según su alcance. Mencionar brevemente las características principales de cada una y colocar en cada cuadro de la Figura el acrónimo de red que corresponda.**



En función del tamaño y del alcance de la red de ordenadores, se puede establecer una diferenciación entre diversas dimensiones de red. Entre los tipos de redes más importantes se encuentran:
 * Personal Area Networks (PAN) o red de área personal
 * Local Area Networks (LAN) o red de área local
 * Metropolitan Area Networks (MAN) o red de área metropolitana
 * Wide Area Networks (WAN) o red de área amplia
 * Global Area Networks (GAN) o red de área global

#### Personal Area Network (PAN)

Para llevar a cabo un intercambio de datos, los terminales modernos permiten asociarse ad hoc a una red. Esto puede realizarse por cable y adoptar la forma de una Personal Area Network (PAN) o red de área personal
El ámbito de acción de las redes PAN y WPAN se limita normalmente a unos pocos metros y, por lo tanto, no son aptas para establecer la conexión con dispositivos que se encuentran en habitaciones o edificios diferentes.

#### Local Area Network (LAN)

Si una red está formada por más de un ordenador, esta recibe el nombre de Local Area Network (LAN). La transmisión de datos tiene lugar o bien de manera electrónica a través de cables de cobre o mediante fibra óptica de vidrio. 
El tipo de red conocido como LAN o red de área local fue desarrollado para posibilitar la rápida transmisión de cantidades de datos más grandes. En función de la estructura de la red y del medio de transmisión utilizado se puede hablar de un rendimiento de 10 a 1.000 Mbit/s.
El alcance de una Local Area Network depende tanto del estándar usado como del medio de transmisión y aumenta a través de un amplificador de señal que recibe el nombre de repetidor (repeater).

#### Metropolitan Area Network (MAN)

La Metropolitan Area Network (MAN) o red de área metropolitana es una red de telecomunicaciones de banda ancha que comunica varias redes LAN en una zona geográficamente cercana.
Los operadores que desempeñan actividades internacionales son los encargados de poner a disposición la infraestructura de las redes MAN. De esta manera, las ciudades conectadas mediante Metropolitan Area Networks pueden contar a nivel suprarregional con Wide Area Networks (WAN) y a nivel internacional con Global Area Networks (GAN).
Para una red MAN, la red Metro Ethernet supone una técnica especial de transmisión con la que se pueden construir redes MEN (Metro Ethernet Network) sobre la base de Carrier Ethernet (CE 1.0) o Carrier Ethernet 2.0 (CE 2.0). 

#### Wide Area Network (WAN)

Las Wide Area Networks (WAN) o redes de área amplia se extienden por zonas geográficas como países o continentes. El número de redes locales o terminales individuales que forman parte de una WAN es, en principio, ilimitado.

#### Global Area Network (GAN)
Una red global como Internet recibe el nombre de Global Area Network (GAN), sin embargo no es la única red de ordenadores de esta índole. Las empresas que también son activas a nivel internacional mantienen redes aisladas que comprenden varias redes WAN y que logran, así, la comunicación entre los ordenadores de las empresas a nivel mundial. Las redes GAN utilizan la infraestructura de fibra de vidrio de las redes de área amplia (Wide Area Networks) y las agrupan mediante cables submarinos internacionales o transmisión por satélite.
https://www.ionos.com/es-us/digitalguide/servidores/know-how/los-tipos-de-redes-mas-conocidos/

**b) ¿Qué es una VLAN? ¿Cómo se clasifican?**

Una VLAN (Virtual LAN) es una tecnología de redes que permite crear redes lógicas separadas dentro de una misma red física en un mismo switch o conjunto de switches conectados.
La VLAN tiene una serie de características:

* Mejora el rendimiento al dividir una red grande en subredes
* Aisla información sensible, ya que dispositivos en una VLAN no se pueden comunicar directamente con dispositivos de otra VLAN
*Permite agrupar dispositivos por función en lugar de por su ubicación física

A su vez las VLAN se clasifican por dos criterios: por su función y por el metodo de asignacion de puertos

#### Segun la asignación de puertos:

|Tipo|Descripción|
|:---------|:---------|
|VLAN estática (basada en puertos)|Es la más común. El administrador asigna manualmente cada puerto del switch a una VLAN específica.|
|VLAN dinámica (basada en MAC)|El switch asigna automáticamente los dispositivos a una VLAN en función de su dirección MAC.|
|VLAN basada en protocolo o capa 3|La asignación se hace según el protocolo o dirección IP del tráfico (por ejemplo, todas las IP del rango 192.168.1.0/24 en una VLAN).|

#### Segun su funcion:

|Tipo|Función principal|
|:----------|:---------|
|VLAN de datos|Transporta el tráfico normal de usuarios (por ejemplo, PCs, impresoras).|
|VLAN de voz|Prioriza el tráfico de voz (VoIP) para mejorar la calidad de las llamadas.|
|VLAN nativa|En un enlace troncal, es la VLAN sin etiqueta (por defecto VLAN 1).|
|VLAN de administración|Se utiliza para la gestión remota de switches y otros dispositivos.|
|VLAN de invitados|Permite acceso limitado a usuarios externos o visitantes.|
|VLAN de seguridad / aislamiento|Se usa para separar tráfico sensible o confinado, evitando accesos no autorizados.|


**c) Investigar y resumir el protocolo IEEE 802.1Q. ¿Cómo se relaciona con las VLAN?** 

IEEE 802.1Q es el estándar que define cómo se implementa el trunking de VLAN en una red Ethernet. En resumen, permite que un enlace Ethernet lleve tráfico de múltiples VLAN al agregar una “etiqueta” en los frames Ethernet que identifica a qué VLAN pertenece un frame en particular. Este proceso de etiquetado se conoce como “tagging”.


El VLAN Trunking es una técnica que se utiliza para permitir que múltiples VLAN se transmitan a través de un único enlace de “trunk” o “troncal” entre switches. Esto permite que los dispositivos en diferentes VLAN se comuniquen entre sí, a pesar de estar en redes separadas.

https://abcxperts.com/vlan-trunking-el-protocolo-ieee-802-1q-explicado/?srsltid=AfmBOoqZgeKvIen4ZulLNkkFXTVDsJw-vZ-Mj4qgho6x8_4ZGlMjKbkA

**d) En el contexto de los dos ítems anteriores ¿Qué es el Tagging?** 

Cuando un switch recibe un frame desde un puerto de acceso (asignado a una VLAN específica), añade una etiqueta 802.1Q al frame antes de enviarlo por el enlace troncal. Esta etiqueta contiene un identificador de VLAN (VID) que especifica a qué VLAN pertenece el frame.

Cuando el frame llega a otro switch a través del enlace troncal, este lee la etiqueta 802.1Q para determinar a qué VLAN pertenece el frame. Luego, elimina la etiqueta y envía el frame a través del puerto de acceso correspondiente a la VLAN especificada.


## 2) Implementaremos la siguiente topología en Packet-Tracer:
![image](https://hackmd.io/_uploads/Sy4CoY6y-l.png)

### Usaremos la siguiente tabla
![image](https://hackmd.io/_uploads/rJ1l2YaJWg.png)


### La siguiente imagen es la topologia planteada en Cisco Packet Tracer:
![image](https://hackmd.io/_uploads/SkEHzsAJbe.png)

### Comprobación de la Tabla de Ruteo activa:
![image](https://hackmd.io/_uploads/Hyjnfs01Zx.png)
![image](https://hackmd.io/_uploads/H1vSVsAJWe.png)
![image](https://hackmd.io/_uploads/rJSwViAJZx.png)

### Configuracion SWITCH 1 (del inciso a hasta el f)
```bash=$
Switch> enable
Switch# configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
```

#### a) Nombrar el switch
```bash=$
Switch(config)# hostname SW-1
```
#### b) Asignar contraseñas
```bash=$
SW-1(config)# enable secret SwitchOne1
SW-1(config)# line console 0
SW-1(config-line)# password cisco-console-0
SW-1(config-line)# login
SW-1(config-line)# exit
SW-1(config)# line vty 0 15
SW-1(config-line)# password cisco-vty
SW-1(config-line)# login
SW-1(config-line)# exit
```
#### c) Encriptar las contraseñas
```bash=$
SW-1(config)# service password-encryption
```
#### d) Configurar IP de VLAN 1
```bash=$
SW-1(config)# interface vlan 1
SW-1(config-if)# ip address 192.168.1.11 255.255.255.0
SW-1(config-if)# no shutdown
SW-1(config-if)# exit
```
#### e) Desconectar interfaces no usadas (Fa0/6 y Fa0/1 están en uso)
```bash=$
SW-1(config)# interface range f0/2-5, f0/7-24, g0/1-2
SW-1(config-if-range)# shutdown
SW-1(config-if-range)# exit
SW-1(config)# end
```
#### f) Guardar la configuración
```bash=#
SW-1# write memory
Building configuration...
[OK]
```

### Configuracion SWITCH 2 (del inciso a hasta el f)
```bash=$
Switch> enable
Switch# configure terminal
```
#### a) Nombrar el switch
```bash=$
Switch(config)# hostname SW-2
```
#### b) Asignar contraseñas (parecidas a las de SW-1)
```bash=$
SW-2(config)# enable secret SwitchTwo2
SW-2(config)# line console 0
SW-2(config-line)# password cisco-console-0
SW-2(config-line)# login
SW-2(config-line)# exit
SW-2(config)# line vty 0 15
SW-2(config-line)# password cisco-vty
SW-2(config-line)# login
SW-2(config-line)# exit
```
#### c) Encriptar las contraseñas
```bash=$
SW-2(config)# service password-encryption
```
#### d) Configurar IP de VLAN 1
```bash=$
SW-2(config)# interface vlan 1
SW-2(config-if)# ip address 192.168.1.12 255.255.255.0
SW-2(config-if)# no shutdown
SW-2(config-if)# exit
```
#### e) Desconectar interfaces no usadas (Fa0/1 y Fa0/18 están en uso)
```bash=$
SW-2(config)# interface range f0/2-17, f0/19-24, g0/1-2
SW-2(config-if-range)# shutdown
SW-2(config-if-range)# exit
SW-2(config)# end
```
#### f) Guardar la configuración
```bash=$
SW-2# write memory
Building configuration...
[OK]
```
#### g) Testear comunicación usando pings entre las computadoras

> Hacemos ping desde PC-A a PC-B:
> ![image](https://hackmd.io/_uploads/rkP1OiRkbl.png)
> ![image](https://hackmd.io/_uploads/r1BGdsCybx.png)

#### h) crear VLANs en ambos switches (misma configuración en SW-1):
```bash=$
SW-2(config)# vlan 10
SW-2(config-vlan)# name Laboratorio
SW-2(config-vlan)# exit
SW-2(config)# vlan 20
SW-2(config-vlan)# name Bar
SW-2(config-vlan)# exit
SW-2(config)# vlan 99
SW-2(config-vlan)# name Management
SW-2(config-vlan)# exit
```
#### i)  Utilizar show vlan brief para visualizar la lista de VLANs en alguno de los switch. ¿Cuál es la VLAN utilizada por defecto?

> ***La VLAN por defecto es la VLAN utilizada por defecto en los switches es la VLAN1.***
>
> - VLANs utilizadas en SW-1
> ![image](https://hackmd.io/_uploads/BJMbYsAyZe.png)
> - VLANs utilizadas en SW-2
> ![image](https://hackmd.io/_uploads/B1WSFsA1Wx.png)

#### j) Asignar PC-A a la VLAN Laboratorio
SW-1(config)# interface f0/6
SW-1(config-if)# switchport mode access
SW-1(config-if)# switchport access vlan 10
SW-1(config-if)# exit

#### k) Mover la IP de Management a la VLAN 99

**Configuración para SW-1 (visualizados en el inciso i)**
```bash=$
SW-1(config)# interface vlan 1
SW-1(config-if)# no ip address
SW-1(config-if)# exit
SW-1(config)# interface vlan 99
SW-1(config-if)# ip address 192.168.1.11 255.255.255.0
SW-1(config-if)# no shutdown
SW-1(config-if)# exit
```

**Configuración para SW-2 (visualizados en el inciso i)**
```bash=$
SW-2(config)# interface vlan 1
SW-2(config-if)# no ip address
SW-2(config-if)# exit
SW-2(config)# interface vlan 99
SW-2(config-if)# ip address 192.168.1.12 255.255.255.0
SW-2(config-if)# no shutdown
SW-2(config-if)# exit
```
#### l y m) Verificar el estado de la VLAN utilizando show vlan brief y el estado de las interfaces, utilizando show ip interface brief. Colocar los output en el informe e interpretar.

###### m) Asignar PC-B a la VLAN Laboratorio (interfaz f0/18)
```bash=$
SW-2(config)# interface f0/18
SW-2(config-if)# switchport mode access
SW-2(config-if)# switchport access vlan 10
SW-2(config-if)# exit
```
Previo a estos comandos se configuró el enlace que conecta a ambos Switches (Fa0/1) en modo trunk para su correcta comunicación entre VLANs, y también se le asignó la PC-B a la VLAN del Laboratorio en SW-2.

**Configuración del modo trunk en SW-1 desde la consola de PC-A**
```bash=$
SW-1# configure terminal
SW-1(config)# interface f0/1
SW-1(config-if)# switchport mode trunk
SW-1(config-if)# end
SW-1# write memory
```
**Configuración del modo trunk en SW-2 desde la consola de PC-B**
```bash=$
SW-2# configure terminal
SW-2(config)# interface f0/1
SW-2(config-if)# switchport mode trunk
SW-2(config-if)# end
SW-2# write memory
```
![image](https://hackmd.io/_uploads/SyMLjjC1Zg.png)
![image](https://hackmd.io/_uploads/B1f5sjRJbe.png)
![image](https://hackmd.io/_uploads/SkInsjCyZg.png)
![image](https://hackmd.io/_uploads/SJM0oiR1bg.png)
Al observarlos outputs de ambos comandos confirman que la configuración de las VLANs, la asignación de puertos de acceso (PC-A a VLAN 10, PC-B a VLAN 10) y la configuración de las interfaces de Management (IPs en VLAN 99) se han realizado con éxito. Los puertos de enlace (Fa0/1) operan como troncales (confirmado por show vlan brief) y los puertos no utilizados están deshabilitados como pedía la parte e).

#### n) Verificar la conectividad entre PC-A y PC-B utilizando pings. Verificar la conectividad entre SW-1 y SW-2 utilizando pings. Interpretar los resultados.
![image](https://hackmd.io/_uploads/ryJ76iCkbl.png)
![image](https://hackmd.io/_uploads/HJi4asRkZx.png)
![image](https://hackmd.io/_uploads/HkXL6sAJbe.png)
![image](https://hackmd.io/_uploads/H1jD6sA1Wx.png)
Podemos observar que todas las pruebas de ping entre PC-A y PC-B, y también entre los switches SW-1 y SW-2 se realizan exitosamente, mostrándonos una perfecta comunicación y configuración de la red. El enlace troncal que nos permite la comunicación simultánea de ambas VLANs (Laboratorio y Management) sobre un mismo cable está funcionando perfectamente.


## 3) Utilizando lo que aprendimos sobre VLAN, e investigando la configuración de NAT y ACLs, simularemos el despliegue de una red LAN a bordo de una aeronave. La idea es la siguiente, tendremos tres segmentos: 
#### i) Clase Turista: acceso solo a un sistema de entretenimiento (server local)
#### ii) Clase Business: acceso a sistema de entretenimiento e internet.
#### iii) Administración: acceso total. 




### Objetivo:
Simular una red LAN en un avión con tres segmentos:

![image](https://hackmd.io/_uploads/SkSbQtpk-x.png)


## Router del avión

#### Objetivos principales:

1) Crear subinterfaces para cada VLAN.
2) Configurar NAT para Business.
3) Bloquear acceso a Internet a Turista usando ACL.
4) Permitir comunicación con servidor local a todas las VLANs.

```bash=$
enable
configure terminal
```

Entramos al modo de configuración global.

a) Subinterfaces para cada VLAN

```bash=$
interface FastEthernet0/0
 no shutdown

interface FastEthernet0/0.10
 encapsulation dot1Q 10
 ip address 10.10.10.1 255.255.255.0
 ip nat inside
 ip access-group 100 out

interface FastEthernet0/0.20
 encapsulation dot1Q 20
 ip address 10.10.20.1 255.255.255.0
 ip nat inside

interface FastEthernet0/0.99
 encapsulation dot1Q 99
 ip address 10.10.99.1 255.255.255.0
 ip nat inside

interface FastEthernet0/1
 ip address 200.0.0.1 255.255.255.252
 ip nat outside
 no shutdown
````

### Explicación:

* encapsulation dot1Q X: asigna la VLAN a la subinterfaz.

* ip address: asigna la IP de gateway para la VLAN.

* ip nat inside/outside: indica qué interfaces participan en NAT.

* ip access-group 100 out: aplica ACL para limitar tráfico de Turista.

b) DHCP para cada VLAN
```bash=$
ip dhcp excluded-address 10.10.10.1 10.10.10.10
ip dhcp excluded-address 10.10.20.1 10.10.20.10
ip dhcp excluded-address 10.10.99.1 10.10.99.10

ip dhcp pool Turista
 network 10.10.10.0 255.255.255.0
 default-router 10.10.10.1
 dns-server 10.10.100.10

ip dhcp pool Business
 network 10.10.20.0 255.255.255.0
 default-router 10.10.20.1
 dns-server 8.8.8.8

ip dhcp pool Admin
 network 10.10.99.0 255.255.255.0
 default-router 10.10.99.1
 dns-server 8.8.8.8
```

* Explicación: Asigna automáticamente IPs, gateway y DNS a cada VLAN.

c) Configuración de NAT
````
access-list 20 permit 10.10.20.0 0.0.0.255
ip nat inside source list 20 interface FastEthernet0/1 overload
````

* Permite que VLAN Business acceda a Internet usando NAT sobre la interfaz del ISP.

d) ACL para bloquear Internet a Turista
````
access-list 100 deny ip 10.10.10.0 0.0.0.255 any
access-list 100 permit ip any any
````

* Bloquea todo el tráfico de Turista hacia Internet, pero permite que acceda al servidor local.

e) Ruta por defecto
````
ip route 0.0.0.0 0.0.0.0 200.0.0.2
````

* Todo el tráfico desconocido se envía hacia el ISP.

## Switch del avión

### Objetivos principales:

1) Crear VLANs.
2) Asignar puertos a cada VLAN.
3) Configurar trunk hacia el router.

* Comandos y explicación

````
enable
configure terminal

vlan 10
 name Turista
vlan 20
 name Business
vlan 99
 name Admin
````
a) Configuración de puertos
````
interface FastEthernet0/1
 switchport mode trunk   # Puerto hacia router

interface range FastEthernet0/2 - 3
 switchport mode access
 switchport access vlan 10  # Turista

interface range FastEthernet0/4 - 5
 switchport mode access
 switchport access vlan 20  # Business

interface FastEthernet0/6
 switchport mode access
 switchport access vlan 99  # Administración

interface FastEthernet0/7
 switchport mode access
 switchport access vlan 99  # Servidor
````

##### Explicación:

* Los puertos de acceso pertenecen a una VLAN específica.

* El puerto trunk transporta todas las VLANs al router.

## Pruebas Realizadas:

![image](https://hackmd.io/_uploads/Bk_3XtTkWe.png)

#### Esquematico:

* Nota: Se uso un server para simular internet del lado del ISP
![image](https://hackmd.io/_uploads/SJ5H_Y6ybl.png)

### Pc-Turista:

> Se ejecuta un ping hacia el servidor local 10.10.99.10 y hacia internet ping 8.8.8.8 
![image](https://hackmd.io/_uploads/B1GXEta1-l.png)

>Se explora la conexion con la pagina del servidor
![image](https://hackmd.io/_uploads/r1R8VFpJ-l.png)

### Pc-Business:
> Se ejecuta ping hacia internet para verificar internet
![image](https://hackmd.io/_uploads/r1ACNtayZe.png)

>Se explora la conexion con la pagina del servidor
![image](https://hackmd.io/_uploads/BJTGHYpyWl.png)

### Pc-Admin:
>Se ejecuta ping hacia el servidor local, pc-turista, pc-business e internet.
![image](https://hackmd.io/_uploads/SkfiHtpkZe.png)
![image](https://hackmd.io/_uploads/SJ_hBKpybg.png)

## Conclusion

El trabajo práctico ha consolidado las habilidades en la configuración de dispositivos de red (switches y routers) y ha profundizado en el concepto de virtualización de redes mediante VLANs. La capacidad de utilizar el estándar IEEE 802.1Q para manejar múltiples dominios de difusión a través de una sola infraestructura física se ha demostrado como una técnica esencial para el diseño de redes escalables y seguras.

La fase más avanzada, al simular la red a bordo del avión, permitió aplicar de manera integrada conceptos de segmentación (VLAN), seguridad (ACLs) y conectividad externa (NAT). Se logró implementar con éxito políticas de acceso estrictas, como el bloqueo de la conectividad a Internet para la clase Turista, validando que el diseño de red cumple con los requisitos operativos y de seguridad. En síntesis, el trabajo práctico confirma el dominio de las herramientas necesarias para la gestión eficiente y segura de la capa de acceso en entornos de red complejos.