# Comunicaciones de Datos - Trabajo Practico N°3

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
> En este trabajo práctico se investigaron y compararon estándares de comunicación de datos en redes locales e inalámbricas, destacando las diferencias entre IEEE 802.3 y 802.11 y las características de las distintas versiones de Wi-Fi. Se analizaron los mecanismos de compatibilidad entre dispositivos y protocolos, así como la relación entre las versiones y los sistemas de seguridad utilizados. También se estudiaron distintos tipos de transmisión en fibra óptica y su relación con las conexiones inalámbricas, considerando conceptos como la Ley de Snell y los modos de propagación. Además, se elaboraron cuadros comparativos de protocolos inalámbricos (Wi-Fi, Bluetooth, ZigBee, NFC, LTE, GSM, 5G, LoRa, NB-IoT, SigFox, Z-Wave) en términos de alcance, data rate y estandarización. Por último, se investigaron las tecnologías que permiten conectividad a internet en aeronaves, analizando su estado del arte, limitaciones y la división del tráfico entre servicios locales de entretenimiento y acceso externo.
> 
**Palabras Clave**: 
>IEEE 802.3; IEEE 802.11; Wi-Fi; Protocolos inalámbricos; Fibra óptica; IoT; Seguridad de red; Internet en aeronaves; Estado del arte.

## Introducción
> El presente trabajo práctico tiene como objetivo profundizar en el estudio de las capas de acceso en redes locales, los protocolos asociados y sus fundamentos técnicos. A través del análisis de estándares clave como IEEE 802.3 (Ethernet) y IEEE 802.11 (Wi-Fi), se busca comprender su evolución histórica, campo de aplicación y las implicancias que tienen sus distintas versiones en términos de velocidad, compatibilidad y seguridad. Asimismo, se abordarán tecnologías de transmisión óptica y diversos protocolos inalámbricos utilizados en la actualidad, con especial énfasis en su alcance, tasa de transferencia y nivel de estandarización. Finalmente, se investigarán las tecnologías que permiten el acceso a internet en aeronaves en vuelo, reflexionando sobre sus características, limitaciones y la forma en que se gestiona el tráfico entre los servicios a bordo y el acceso a la red global.

## Metodologia
> Para la realización de este trabajo se adopto un enfoque de investigacion teórica y práctica. Se analizaron estandares de redes cableadas e inalámbricas, como IEEE 802.3 y 802.11, sus versiones y sistemas de seguridad asociados. Se recopilaron datos sobre distintos protocolos inalámbricos y medios de transmisión mediante fuentes bibliográficas y domentación oficial. Se realizaron pruebas de conectividad en redes de la facultad para identificar protocolos y metodos de autentificación. Además, se estudiaron tecnologías de transmisión  por fibra óptica y conectividad a internet en aeronaves, evaluando características, ventajas y limitaciones. Finalmente, se organizaron los resultados en cuadros compartivos y gráficos para facilitar su análisis. 


## Resultados

## Actividad 1
**a) Investigar los estándares IEEE 802.3 y 802.11, resumir brevemente su historia y campo de aplicación.**
>
>### IEEE 802.3 (Ethernet)
>
>El estándar IEEE 802.3, comúnmente conocido como Ethernet, fue desarrollado en los años 70 por Robert Metcalfe y sus colegas en Xerox PARC. La tecnología original permitía una velocidad de 2.94 Mbps.
>
>En 1980, un consorcio formado por Digital Equipment Corporation (DEC), Intel y Xerox (DIX) publicó la especificación "Ethernet Blue Book" para un sistema de 10 Mbps, que se convirtió en el estándar de facto.
>
>Para evitar una fragmentación de tecnologías propietarias, el Instituto de Ingenieros Eléctricos y Electrónicos (IEEE) tomó este trabajo y lo estandarizó formalmente en 1983 como el IEEE 802.3. Esta estandarización definió las características de la capa física y de enlace de datos (MAC) para redes cableadas. Desde entonces, el estándar ha evolucionado enormemente, aumentando las velocidades desde 10 Mbps hasta los 400 Gbps (y más) de la actualidad.
>
>### Campo de Aplicación:
>IEEE 802.3 es el estándar fundamental para redes de área local (LAN) cableadas. Es la tecnología de red dominante y ubicua en casi todos los entornos:
>* Redes Corporativas y Oficinas
>* Centros de Datos: Interconexión de servidores, switches y almacenamiento.
>* Redes de Acceso: Tecnologías como Ethernet sobre fibra óptica (por ejemplo, FTTH - Fibra al Hogar) se basan en principios 802.3.
>* Conectividad Residencial: La mayoría de los routers modernos incluyen puertos Ethernet para conectar dispositivos de forma fiable y de alto rendimiento.
>
>Su principal ventaja es ofrecer una conexión extremadamente fiable, segura y de alto ancho de banda con interferencias mínimas.
>
>### IEEE 802.11 (Wi-Fi)
>
> El estándar IEEE 802.11, comercialmente conocido como Wi-Fi, nació de la necesidad de eliminar cables y permitir una conectividad de red flexible.
> 
> El trabajo dentro del IEEE comenzó en 1990, y el primer estándar se ratificó en 1997. Esta versión inicial (802.11-1997) permitía velocidades de 1 y 2 Mbps en la banda de 2.4 GHz, pero era costosa y no muy adoptada.
>
> El punto de inflexión llegó en 1999 con la ratificación de dos enmiendas cruciales:
>* 802.11b: Ofrecía 11 Mbps, haciendo la tecnología más práctica y asequible.
>* 802.11a: Operaba en la banda de 5 GHz y ofrecía 54 Mbps, aunque con un alcance menor.
>
>La Wireless Ethernet Compatibility Alliance (WECA), ahora conocida como la Wi-Fi Alliance, se formó para garantizar la interoperabilidad entre dispositivos de diferentes fabricantes bajo la marca Wi-Fi. Esto fue clave para su éxito comercial.
>
>Desde entonces, el estándar ha evolucionado con nuevas enmiendas como 802.11g, 802.11n (Wi-Fi 4), 802.11ac (Wi-Fi 5), y el moderno 802.11ax (Wi-Fi 6 y Wi-Fi 6E), multiplicando exponencialmente la velocidad, eficiencia y capacidad para manejar múltiples dispositivos.
>
>### Campo de Aplicación:
>IEEE 802.11 es el estándar para Redes de Área Local Inalámbricas (WLAN). Su aplicación es masiva y se encuentra en prácticamente todos los ámbitos:
>* Hogares: Proporciona acceso a Internet a smartphones, laptops, televisores inteligentes y dispositivos IoT.
>* Empresas y Oficinas: Permite la movilidad de los empleados dentro de las instalaciones.
>* Espacios Públicos: Hoteles, aeropuertos, cafeterías, centros comerciales y estadios ofrecen acceso Wi-Fi a sus visitantes.
Educación: Universidades y escuelas utilizan redes Wi-Fi para el aprendizaje y la gestión.
>* Internet de las Cosas (IoT): Conecta una miríada de dispositivos sensores y gadgets de forma inalámbrica.
>
> Su principal ventaja es la movilidad y la facilidad de instalación, eliminando la necesidad de cableado físico.
>
**b) En la Facultad, conectarse a alguna de las siguientes redes abiertas: FCEFyN, UNC-LIBRE, EduRoam. Determinar qué versión del protocolo 802.11 utiliza y mostrar el procedimiento que utilizó para averiguarlo.**

> La red a la cual nos conectamos fue a EduRoam, utilizamos el comando en cmd "netsh wlan show interfaces" para averiguar observar en el apartado "tipo de radio" la version de protocolo utilizado el cual es 802.11n. 
>![image](https://hackmd.io/_uploads/rJcHExYilg.png)

**c) ¿Qué sucede si una red Wi-Fi opera con determinado protocolo y un dispositivo (por ejemplo, una notebook vieja) utiliza una NIC que no soporta dicho protocolo?**
>
>Si una red Wi-Fi opera con un protocolo específico y un dispositivo antiguo tiene una NIC que no lo soporta, se producirá una incompatibilidad en la capa física que impedirá que el dispositivo se conecte a la red en sus modos más modernos y eficientes. Sin embargo, para mantener el backward compatibility, los routers modernos suelen implementar mecanismos que permiten la conexión, pero con importantes consecuencias.
>
>#### Incompatibilidad Total (Caso Menos Común)
> Si el punto de acceso está configurado exclusivamente en un modo que el dispositivo antiguo no entiende, la conexión será imposible.
Ejemplo: Un router configurado solo en modo 5 GHz. Un dispositivo que solo tenga una NIC de 2.4 GHz no podrá ver la red. El nombre de la red (SSID) no aparecerá en la lista de redes disponibles.
>
>#### Compatibilidad hacia Atrás (Caso Más Común)
>En este caso, el dispositivo antiguo podrá conectarse, pero con severas limitaciones:
>
>#### Reducción de Velocidad:
> El router debe "bajar" su modo de operación para comunicarse con el dispositivo antiguo. Para gestionar todos los dispositivos, a menudo el rendimiento de toda la red Wi-Fi se ve degradado.
>
>Ejemplo: Un router Wi-Fi 6 que permite la conexión de un dispositivo 802.11g. Mientras ese dispositivo esté transmitiendo o recibiendo datos, el router debe usar técnicas de protección y modulación más lentas, lo que ralentiza la comunicación para todos los dispositivos conectados, incluso los modernos.
>
>#### Pérdida de Características Avanzadas: 
>El dispositivo antiguo no podrá aprovechar las mejoras del protocolo nuevo, como:
>1. No podrá ser uno de los múltiples dispositivos a los que el router envíe datos simultáneamente.
>
>2. No podrá compartir eficientemente los canales de transmisión.
>
>3. Si el dispositivo solo soporta WPA o WEP, podría obligar a toda la red a usar ese nivel de cifrado débil, o será expulsado si la red exige WPA2 o WPA3.
>
>#### Problemas de Estabilidad:
> La comunicación entre protocolos diferentes no siempre es perfecta y puede generar más colisiones de paquetes y retransmisiones, leading a una conexión menos estable para el dispositivo antiguo.
>
**d) ¿Qué relación existe entre la versión del protocolo utilizado y la seguridad de la red? Nuevamente conectado a alguna de las redes del punto b) determinar qué sistema de seguridad utiliza y qué diferencias tiene con el sistema de seguridad de la versión del protocolo que lo precede.**
>
>Versión del protocolo utilizada:
 La red eduroam está usando el protocolo 802.11n, que permite velocidades de hasta 600 Mbps y funciona en las bandas de 2.4 GHz y 5 GHz.
>
>Sistema de seguridad utilizado:
Usa WPA2-Enterprise con cifrado CCMP (basado en AES), que es un sistema de seguridad fuerte y apropiado para entornos como universidades. WPA2-Enterprise requiere autenticación mediante credenciales (usuario y contraseña), en lugar de solo una clave compartida.
>
>Relación entre protocolo y seguridad:
Aunque el protocolo 802.11n no obliga a usar un sistema de seguridad específico, sí es compatible con WPA2, que era el estándar de seguridad más fuerte en el momento en que se lanzó 802.11n (2009).
Por lo tanto, se puede decir que esta red está usando una combinación coherente: protocolo 802.11n con el sistema de seguridad fuerte recomendado para su época, WPA2.
>
>Comparación con la versión anterior:
La versión anterior al protocolo 802.11n sería 802.11g, que también era compatible con WPA, pero:
>
>* WPA (Wi-Fi Protected Access) usaba el cifrado TKIP, que hoy se considera inseguro.
>
>* WPA2, en cambio, usa CCMP/AES, mucho más robusto.
>
>* Además, WPA2-Enterprise añade una capa extra de seguridad usando un servidor de autenticación (como RADIUS), lo cual es más seguro que WPA2-Personal (clave compartida).



## Actividad 2
![image](https://hackmd.io/_uploads/Hk0XOeYsxx.png)
**a) ¿Qué tipos de transmisión se están ilustrando? ¿Cuáles son sus características principales y en qué se diferencian una de otra? ¿Cuál es más costosa de implementar?** 
>
> Se puede observar dos tipos de transmision en fibre optica.
>
>* Fibra Monomodo (izquierda):
>Se transmite un solo modo de luz (un unico rayo recto), se alcanzan grandes distancias con minima atenuacion y dispercio. Es mas costoso de implementar ya que requiere fuentes laser precisas y alineacion exacta. Tiene alta capacidad de transmision de datos.
>
>* Fibra Multimodo (derecha):
>
>Se tranmiten varios modos de luz que rebotan dentro del nucleo, es mas economica y facil de instalar, tiene una mayor dispersion modal osea los diferentes rayos llegan en diferentes tiempos siendo ideal para distancias cortas.
>
>**b) ¿Qué es la Ley de Snell? ¿Cómo se relaciona con las transmisiones en Fibra Óptica y sus distintos modos?**
>
>Ley de Snell o tambien llamada la Ley de la Refracción; describe cómo cambia la dirección de un rayo de luz al pasar de un medio a otro con diferente índice de refracción: 
>            n1 * sen(θ1) = n2 * sen(θ2)
>
>Siendo:
>
>n1, n2 : índices de refracción. 
>θ1, θ2 : ángulos de incidencia y refracción.
>
>Relación con la fibra óptica:
>
>* En la fibra óptica, el núcleo tiene un índice de refracción mayor que el revestimiento.
>
>* Esto genera reflexión interna total si el ángulo de incidencia supera un valor crítico (basado en la Ley de Snell). 
>
>* En el modo multimodo, la luz entra con distintos ángulos, causando múltiples reflexiones. 
>
>* En el modo monomodo, la luz entra en un ángulo preciso, viajando casi sin rebotar
>
**c) ¿Qué relación podés encontrar entre las conexiones inalámbricas y las transmisiones en Fibra Óptica?**

>Similitudes: 
>
>* Ambas tecnologías transmiten datos mediante ondas 
electromagnéticas (luz en la fibra, radiofrecuencia en inalámbrico). 
>
>* En ambos casos, se busca alta velocidad y eficiencia de transmisión. 
>
>* Ambas requieren infraestructura de red adecuada. 
>
>Diferencias: 
>
>* Fibra óptica -> transmisión guiada dentro del cable. 
>
>* Inalámbrica -> transmisión no guiada a través del aire.


## Actividad 3
> a) Completar el siguiente cuadro, que lista algunos de los protocolos inalámbricos más comunes:

| Protocolo | ¿Está estandarizado? (Sí/No) | Estándar / Última versión |
|-----------|-------------------------------|---------------------------|
| **Wi-Fi** | Sí | IEEE 802.11 (última: **802.11ax**, también llamado Wi-Fi 6/6E) |
| **Bluetooth** | Sí | IEEE 802.15.1 (última versión: **Bluetooth 5.4**) |
| **ZigBee** | Sí | IEEE 802.15.4 (**ZigBee PRO 2023** es una versión reciente) |
| **NFC** | Sí | ISO/IEC 18092, 14443, 15693 |
| **LTE** | Sí | 3GPP Release 8 a Release 14 (última versión: **LTE-Advanced Pro**) |
| **GSM** | Sí | 3GPP Release (originalmente ETSI), basado en 3GPP TS 45.x |
| **5G (3GPP)** | Sí | 3GPP Release 15 en adelante (última estable: **Release 18**) |
| **LoRa** | Parcialmente | No es abierto del todo, pero **LoRaWAN** está gestionado por la LoRa Alliance (última: **v1.0.4**) |
| **NB-IoT** | Sí | 3GPP Release 13 en adelante |
| **SigFox** | No (propietario) | Tecnología propietaria, no estandarizada |
| **Z-Wave** | Parcialmente | Antes propietario, ahora abierto desde 2020 y gestionado por Z-Wave Alliance (última: **Z-Wave Plus v2 / 700 series**) |

>b) Sobre los protocolos mencionados, investigar y colocarlos en el siguiente gráfico (de manera aproximada) de acuerdo a sus características de alcance (distancia) y data rate.

### Tabla comparativa de protocolos inalámbricos

| Protocolo | Distancia mínima | Distancia máxima | Data rate mínimo | Data rate máximo | Fuente |
|-----------|------------------|------------------|------------------|------------------|--------|
| **Wi-Fi**     | 0.3 m      | 100 m    | 600 Mb/s      | 9.6 Gb/s       | [Wifi 6 vs Wifi 5](https://www.xataka.com/basics/que-wi-fi-6-que-ventajas-tiene-respecto-a-version-anterior); [Regla de los 30 cm](https://www.xataka.com/basics/regla-30-centimetros-router-que-como-te-ayuda-a-mejorar-senal-wifi-tu-casa)|
| **Bluetooth** | 0.1 m      | 240 m    | 125 kb/s     | 2 Mb/s       | [Bluetooth 5.3 – Features and applications](https://www.rfpage.com/bluetooth-5-3-features-and-applications/); [Bluetooth 5 - Taking Bluetooth further](https://www.nordicsemi.com/Products/Wireless/Bluetooth-Low-Energy/Bluetooth-5) |
| **ZigBee**    | 0.1 m     | 100 m    | 20 kb/s     | 250 kb/s     | [Introduction of ZigBee](https://www.geeksforgeeks.org/computer-networks/introduction-of-zigbee/) |
| **NFC**       | 0.01 m     | 0.1 m    | 106 kb/s     | 424 kb/s     | [Near-field communication](https://en.wikipedia.org/wiki/Near-field_communication) |
| **LTE**  | 1 m     | 100 km    | 1 Mb/s      | 150 Mb/s     | [Performance Evaluation of a Deployed 4G LTE Network](https://thesai.org/Downloads/Volume9No3/Paper_25-Performance_Evaluation_of_a_Deployed_4G_LTE_Network.pdf); [LTE UE Category & Class Definitions](https://www.cablefree.net/wirelesstechnology/4glte/lte-ue-category-class-definitions/); [Long Range Cell Coverage for LTE](https://es.slideshare.net/slideshow/long-range-cell-coverage-for-lte/34708877) |
| **GSM**  | 30 m     | 35 km    | 9.6 kb/s     | 21.4 kb/s    | [Avance de tiempo](https://en.wikipedia.org/wiki/Timing_advance); [Telecom ABC](https://en.telecomabc.nl/g/gprs.html) |
| **5G**     | 35 m    | 5 km     | 150 Mb/s     | 10 Gb/s      | [Commsbrief – 5G speeds](https://commsbrief.com/mobile-data-speed-with-2g-3g-4g-and-5g-cellular-networks/); [ETSI TS 138 104 V15.5.0 (2019-05)](https://www.etsi.org/deliver/etsi_ts/138100_138199/138104/15.05.00_60/ts_138104v150500p.pdf) |
| **LoRa**      | 1 m     | 15 km    | 250 b/s      | 21.9 kb/s      | [LoRaWAN®](https://www.thethingsnetwork.org/docs/lorawan/regional-parameters/us915/); [LoRaWAN - Regional Parameters](https://lora-alliance.org/wp-content/uploads/2020/11/lorawan_regional_parameters_v1.0.3reva_0.pdf) |
| **NB-IoT**    | 10 m     | 100 km    | 264 b/s       | 62 kb/s     | [NB-IoT: From PHY and MAC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6603562/); [Performance Analysis of LoRaWAN and Cellular NB-IoT Networks](https://www.mdpi.com/2079-9292/10/18/2224); [A Primer on 3GPP Narrowband Internet of Things (NB-IoT)](https://arxiv.org/pdf/1606.04171) |
| **SigFox**    | 1 m    | 40 km    | 600 b/s      | 600 b/s      | [Get to know Sigfox](https://build.sigfox.com/study) |
| **Z-Wave**    | 0.1 m     | 100 m    | 9.6 kb/s     | 100 kb/s     | [Z-Wave (not so) Long Range?!](https://blog.zwave-js.io/2025/08/01/zwave-not-so-long-range/); [Z-Wave Technology: Tutorial on Features, Frequency, and Network](https://www.rfwireless-world.com/tutorials/z-wave-technology-tutorial) |
>![image](https://hackmd.io/_uploads/r1ppRFijll.png)
---

💡 **Nota aclaratoria**  

> Los valores de **distancia** y **data rate** (mínimos y máximos) presentados en esta tabla fueron recopilados a partir de distintas tecnologías y configuraciones específicas de cada protocolo.
>  
> **Referencias consideradas:**
> - 📶 **Wi-Fi 6 (2019)**
> - 🔵 **Bluetooth 5.3 (2021)**
> - 🐝 **ZigBee (IEEE 802.15.4)**
> - 📲 **NFC (Near Field Communication)**
> - 📡 **4G LTE (UE categoría 4, con MIMO 2×2)**
> - ☎️ **GSM clásico (2G)**
> - 🛰️ **5G NR con macrocelda**
> - 🌐 **LoRa** 
>   - SF12 / 125 kHz → 250 bit/s
>   - SF7 / 500 kHz → 21.9 kbit/s
> - 📡 **NB-IoT**
>   - *In-band mode*: hasta 100 km
>   - *NPUSCH (uplink físico)*
> - 📨 **SigFox (región RCZ4)**
> - 🏠 **Z-Wave**
>   - 9.6 kbit/s con codificación *Manchester*
>   - 40 kbit/s con codificación *NRZ*

---

c) De acuerdo a lo investigado y visto en las clases teóricas, completar el siguiente cuadro con las características indicadas para los distintos medios de transmisión:
### Tabla comparativa de medios de transmisión

| Característica | UTP | Fibra Óptica | Wi-Fi 802.11be | Bluetooth 5.4 | 5G |
|----------------|-----|--------------|----------------|----------------|----|
| **Ancho de banda** | Hasta 10 Gbps (según categoría, p.ej. Cat6a) | ≥ 100 Gbps | Hasta 46 Gbps | Hasta 2 Mbps | Hasta 20 Gbps |
| **Distancias** | Hasta 100 m | Hasta 80 km (monomodo) | ~30 m en interiores / >100 m en exteriores | Hasta 100 m (típico <10 m) | Varios km |
| **Inmunidad a EMI / RFI** | Baja | Muy alta | Media | Baja | Media (robustez por codificación, pero sensible a interferencias) |
| **Costos de medios/conectores/dispositivos** | Bajo | Alto | Medio | Muy bajo | Alto |
| **¿Disponible en Packet Tracer?** | Sí | Sí (limitado) | Sí (limitado) | No | No |




## Actividad 4

a) Investigar qué tecnologías permiten esto y sus principales características y limitaciones desde una perspectiva de Comunicaciones de Datos.

>1. ***Conectividad vía satélite (Satellite-based Internet).***
>- **Cómo funciona:** El avión se comunica con satélites geoestacionarios (GEO) o de órbita baja (LEO), que a su vez se conectan a estaciones terrestres y luego a internet.
>- **Proveedores conocidos:** Viasat, Inmarsat, Starlink (SpaceX).
>- **Ventajas:**
>    - Cobertura global (incluye océanos).
>    - Conexión más estable durante vuelos largos.
>- **Limitaciones:**
>    - Latencia más alta (especialmente con satélites GEO).
>    - Costos de infraestructura y servicio elevados.
>
>2. ***Conectividad vía estaciones terrestres (Air-to-Ground, ATG)***
>- **Cómo funciona:** El avión se comunica con torres de telecomunicaciones en tierra, de forma similar a una red móvil.
>- **Proveedores conocidos:** Gogo (en EE. UU.).
>- **Ventajas:**
>   - Latencia más baja.
>   - Menor costo que satelital.
>- **Limitaciones:**
>    - Solo disponible sobre tierra firme (no funciona sobre el mar).
>    - Cobertura limitada a zonas con infraestructura terrestre.
>
>Características desde la perspectiva de Comunicaciones de Datos:
>- **Protocolos:** TCP/IP adaptado con mecanismos de corrección de errores y compresión.
>- **Ancho de banda limitado:** Se comparte entre todos los usuarios del avión.
>- **QoS (Quality of Service):** Prioridad para ciertos tipos de tráfico (mensajes, navegación básica).
>- **Seguridad:** Uso de VPNs, cifrado TLS/SSL, firewalls, autenticación de usuarios.
>
>b) Buscar y encontrar al menos una publicación científico/tecnológica con una antigüedad no mayor a un año que aborde algún aspecto de este tema.
>
>***Título:*** Enabling Continuous 5G Connectivity in Aircraft through Low Earth Orbit Satellites
 ***Autores:*** Raúl Parada, Víctor Monzón Baeza, Carlos Horcajo Fernández de Gamboa, Rocío Serrano Camacho, Carlos Monzó
 ***Publicado en:*** arXiv, abril de 2025 arXiv
***Resumen del estudio***
>- Propone mejorar la conectividad a bordo mediante 5G continuo, usando satélites en órbita baja (LEO).
>- Modela trayectorias, movimiento de aeronaves y mecanismos de handover mediante Matlab y Simulink.
>- Integra análisis de propagación en cabina usando ray-tracing.
>- Concluye que la configuración propuesta:
>    - Mejora la cobertura,
>    - Reduce la latencia,
>    - Minimiza interrupciones mediante handovers secuenciales eficientes.
>
>c) La mayoría de los aviones que utilizan redes Wi-Fi permiten sistemas de “entretenimiento a bordo” para, por ejemplo, acceder a películas o contenido de entretenimiento. Pensar y responder:
***¿Cómo se divide el tráfico entre el contenido a bordo y el internet?*** Por ejemplo, ver una película vs. enviar/recibir un correo electrónico. Piensen lo siguiente: el tráfico hacia internet es, naturalmente, pago. Mientras que los contenidos a bordo son gratuitos y están “hosteados” en un sistema local. ¡No hace falta que lo hagan ahora! pero pueden ir pensando cómo simular este sistema en Packet Tracer.
>
>Los aviones comerciales tienen dos opciones:
>
> - **Red aire-tierra (ATG):** Con este tipo de red, la parte inferior del avión está equipada con antenas que se conectan con la torre más cercana en tierra. La señal va al servidor de cabina y luego al enrutador de a bordo, lo que convierte al avión en un hotspot para los pasajeros. Los inconvenientes de este método, sin embargo, son obvios: el avión tiene que estar sobre tierra (o cerca de ella) para que funcione bien. Claro, podrás hacer cosas básicas como consultar un email o enviar un mensaje instantáneo, pero no mucho más, sobre todo en vuelos internacionales. 
>
>- **Red satelital:** Al igual que las ATG, este método también utiliza antenas, pero están montadas en la parte superior del avión y se conectan a una red de satélites (el que esté más cerca) mientras el avión viaja. La señal llega hasta el servidor de a bordo, pasa por un enrutador wifi y llega hasta ti. El servicio por satélite utiliza redes tanto de banda estrecha como de banda ancha para ofrecerte un acceso completo a Internet. Lo que le falta a la banda estrecha en cuanto a la capacidad de ver películas, jugar a videojuegos y cosas por el estilo, la banda ancha lo compensa en cierto modo. 

## Bibliografia y referencias

>* [Fuentes de cada protocolo inalambrico del inciso 3](#tabla-comparativa-de-protocolos-inalámbricos)
>* [Archivo utilizado para hacer el grafico de Data Rate vs Distance](https://colab.research.google.com/drive/1h3gybwqTdVRkLG7jF2H0ILKiRf2Pg8ry?usp=sharing)
>* [¿Los aviones tienen wifi? Todo lo que debes saber](https://es.t-mobile.com/dialed-in/wireless/how-does-airplane-wifi-work)
