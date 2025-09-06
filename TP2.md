# Comunicaciones de Datos - Trabajo Practico N°2 

**Integrantes**
_Pablo Castilla; Javier A. Fatu; Enzo L. Laura Surco; Nicolás O. Melia; Saqib D. Mohammad Cabrejos;_


**ComandoDeDatos**

**Facultad de Ciencias Exactas, Físicas y Naturales**

**Asignatura: Comunicaciones de datos**

**Profesores: Facundo Oliva Cuneo y Santiago Martin Henn**

### Informacion de los autores

 **Información de contactos**:   
_saqib.mohammad@mi.unc.edu.ar;_     
_javier.fatu@mi.unc.edu.ar;_  
_nicolas.melia@mi.unc.edu.ar;_  
_pablo.castilla@mi.unc.edu.ar;_  
_enzo.laura.surco@mi.unc.edu.ar;_  

## Resumen
> Este informe esta centrado en los conceptos fundamentales de las capas física y de enlace de datos del modelo OSI. Se analizan fenómenos físicos como la atenuación y la distorsión por retardo, su impacto en las transmisiones según el tipo de banda, y se introduce el uso de Wireshark para el análisis de tráfico de red. Además, se investigan aspectos prácticos como la estructura de tramas Ethernet, tipos de cables UTP, y la trazabilidad de direcciones MAC. Finalmente, se reflexiona sobre la privacidad en red y el rol de tecnologías como las VPNs en la ocultación de información del dispositivo.
> 
**Palabras Clave**: _Ruido Electromagnetico, SNR, Ethernet, Wireshark, MAC_

## Introducción
> En el presente trabajo práctico se abordan distintos conceptos fundamentales relacionados con las comunicaciones digitales y las redes de datos. A partir del análisis de fenómenos físicos como el efecto Doppler y la interferencia electromagnética, se estudian sus implicancias sobre distintos tipos de transmisión. También se exploran tecnologías clave como Ethernet, el uso de cables UTP, la estructura de tramas de red, y herramientas de análisis como Wireshark. Además, se analizan aspectos relacionados con la privacidad y trazabilidad de los dispositivos en la red, incluyendo conceptos como la dirección MAC, el IMEI y el funcionamiento de las VPN. El objetivo general es comprender cómo interactúan estos elementos en un entorno de red real y cómo impactan en la calidad, seguridad y eficiencia de las comunicaciones.

## Metodologia
> El trabajo se desarrolló en base a consignas teórico-prácticas, combinando investigación bibliográfica, análisis de figuras, y experimentación con herramientas de red como el Wireshark. En primer lugar, se estudiaron fenómenos físicos que afectan la propagación de ondas electromagnéticas, como el efecto Doppler y el ruido. Luego, se revisaron aspectos técnicos de las tecnologías Ethernet y el cableado estructurado. En una segunda etapa, se realizaron pruebas prácticas utilizando comandos de red (como ipconfig y ping) y el software Wireshark para capturar y analizar tramas de red. A partir de los datos obtenidos, se identificaron direcciones IP, MAC, y se consultaron bases de datos de fabricantes. Finalmente, se investigaron temas relacionados con la privacidad en la red y se compararon identificadores como la dirección MAC y el IMEI.


## Resultados

### Consigna N°1: Analizar la siguiente figura y responder

![image](https://hackmd.io/_uploads/BkMf5s7cgg.png)

1. ¿Qué fenómeno físico se está representando en la Figura? ¿Cuáles son las características principales del mismo?

> El fenomeno que se puede apreciar en el grafico se llama efecto Doppler aplicado a ondas electromagnéticas; las caracteristica son que ocurre cuando hay un movimiento relativo entre el emisor y el receptor, si el emisor se acerca se percibe una frecuencia mayor, y si se aleja se percibe una menor.
> 
> La velocidad de propagacion no cambia, lo que cambia es la frecuencia, y por lo tanto la longitud de onda observada. Es algo muy relevante en comunicaciones satelitales, GNSS, radar y enlaces moviles.
> $$\Delta f=f_c\bullet \frac{v}{c}$$
> - $\Delta f$ es el cambio de frecuencia observado
> - $f_c$ es la frecuencia de la portadora
> - $v$ es la velocidad relativa entre el emisor y el receptor
> - $c$ es la velocidad de la luz

2. Recordando las bandas de transmisión vistas en el TP01, investigar: ¿A qué tipos de transmisión afecta más este fenómeno? ¿Cuáles son más resilientes al mismo?
>  Las mas afectadas son las frecuencias altas como `UHF`, `SHF`, `EHF`, `microondas`, tipicas de satelites, celular wifi; donde si la $f_c$ es alta eso significa que $\Delta f$ tambien sera alto.
>
>La mas resilientes son las frecuencias bajas como las `LF`, `MF`, `HF` y servicios de gran ancho de banda o con tecnicas de seguimiento y correccion. Tambien hay resiliencia cuando existe baja velocidad relativa.

3. Investigar: ¿Cuáles son las razones por las cuales no se debe encender el celular arriba de un avión? ¿Tiene algo que ver el fenómeno descrito en los puntos anteriores?

> No se debe encender el telefono sobre un avion porque sus ondas electromagneticas pueden causar interferencias en las comunicaciones de radio y los sistemas de neavegacion del avion, lo cual es especialmente critico durante el despegue y el aterrizaje.
> 
> Los telefonos buscan constantemente señal de las antenas terrestres y sus ondas pueden interferir con las comunicaciones de radio entre el avion y la torre de control.
>  
> Como el `Efecto Doppler` a velocidades de avion complica la sincronización y el enlace celular ademas para mantener la conexión el equipo puede aumentar potencia elevando el riesgo de interferencias.
>
### Consigna N°2: Analizar la siguiente figura y responder:
![image](https://hackmd.io/_uploads/rkNx5iQ5ge.png)

a. ¿Qué fenómeno físico se está representando en la Figura? ¿Cuáles son las características principales del mismo?
> El fenómeno físico representado es la interferencia o ruido en la señal. Se trata de perturbaciones que se superponen a la señal original y alteran su comportamiento. Estas perturbaciones pueden tener distintos orígenes: naturales (como rayos, descargas eléctricas o radiación cósmica), artificiales (provenientes de equipos electrónicos, motores o herramientas eléctricas) e incluso ambientales (ruidos y vibraciones presentes en el entorno).
>
>La presencia de este fenómeno afecta directamente la calidad de la comunicación, haciendo que la señal transmitida llegue al receptor menos clara, distorsionada o, en algunos casos, completamente ilegible. En la figura se observa cómo una señal limpia experimenta estas alteraciones debido a una fuente de ruido externa representada por el trabajador con una herramienta eléctrica.

b. Recordando las bandas de transmisión vistas en el TP01, investigar: ¿A qué tipos de transmisión afecta más este fenómeno? ¿Cuáles son más resilientes al mismo?

>![image](https://hackmd.io/_uploads/BJd1pim5ge.png)
> Observando la tabla de bandas de frecuencias, podemos notar que los tipos de transmisión más afectados son aquellos que utilizan bandas de frecuencias bajas, como la radio AM o las comunicaciones submarinas. Esto se debe a que sus longitudes de onda coinciden con las generadas por fenómenos naturales como rayos, tormentas eléctricas y descargas atmosféricas, que producen impulsos eléctricos intensos. Como resultado, el ruido atmosférico se acopla fácilmente a las ondas de baja frecuencia. En cambio, las bandas de frecuencia altas son más resilientes al ruido ambiente, como comunicaciones satelitales o Redes 5G, por lo que resultan más confiables en entornos donde la interferencia natural es significativa, aunque presentan sus propias limitaciones relacionadas con la atenuación y la necesidad de mantener línea de vista.

c. ¿Qué es la SNR? ¿Tiene algo que ver con el concepto de BER que vimos en el TP01?
> La relación señal-ruido (SNR) y la tasa de bits errados (BER) están íntimamente ligadas: un SNR más alto generalmente se traduce en un BER más bajo. En el caso de la modulación BPSK en un canal con desvanecimiento de Rayleigh, la función Q se utiliza para calcular el BER a partir del SNR. Esto significa que a medida que la calidad de la señal mejora (mayor SNR), la cantidad de errores en la transmisión de datos disminuye, logrando una comunicación más confiable.
> 
> La distancia es un factor crucial que afecta directamente el SNR. A medida que la distancia entre el transmisor y el receptor aumenta, la intensidad de la señal recibida disminuye debido a la pérdida de trayectoria. En el espacio libre, esta pérdida es típicamente proporcional al cuadrado de la distancia, lo que significa que un aumento en la distancia resulta en una reducción significativa del SNR.
> 
> La relación entre BER, SNR y distancia es clara: a mayor distancia, el SNR disminuye debido a la pérdida de trayectoria, lo que a su vez causa un aumento en el BER. En otras palabras, si la potencia de transmisión es fija, una mayor distancia resultará en un BER más alto debido al menor SNR recibido.
> 
> Sin embargo, hay otros factores que influyen en esta relación. El esquema de modulación es uno de ellos, ya que distintos esquemas tienen sensibilidades variadas a los cambios en el SNR. Por ejemplo, QAM es generalmente más sensible que BPSK, lo que significa que su BER aumentará más rápidamente con la disminución del SNR. Las características del canal, como la severidad del desvanecimiento, la propagación multitrayectoria y la interferencia, también pueden impactar esta relación. Un canal ruidoso o con un alto desvanecimiento puede amplificar el aumento del BER, incluso si la distancia y el SNR se mantienen constantes en comparación con un canal más limpio.

### Consigna N°3: 

>a. Ethernet es una familia de tecnologías de red de capa de enlace (IEEE 802.3) para LAN. Define las características de cableado y señalización; de nivel físico y los formatos de tramas de datos del nivel de enlace de datos del modelo OSI.

> Es una de las tecnologías de red más utlizadas para las redes locales, y sus características son las siguientes:

>1. Velocidad y escalabilidad
Ethernet admite múltiples opciones de velocidad, que van desde 10 Mbps hasta 800 Gbps. Permite satisfacer las crecientes demandas de ancho de banda.
>2. Conectividad por cable para la estabilidad
Proporciona una conexión estable y de baja latencia, ideal para aplicaciones de juegos, videoconferencias y aplicaciones intensivas en datos.
>3. Comunicación completa Duplex y Half Duplex
Ethernet permite a los dispositivos enviar y recibir datos simultáneamente o permite la transferencia de datos en una sola dirección.
>4. Manipulación de colisión
Para gestionar el tráfico de la red, Ethernet utiliza el acceso múltiple sentido del portaaviones con la detección de colisiones (CSMA/CD), y detecta y evita la colisión de paquetes, que mejora la eficiencia de la red.
>5. Comunicación Basada en bolsillo
Para transmitir los datos, Ethernet lo divide en marcos, lo que garantiza una entrega de datos eficiente y fiable.

> Ethernet tambien cuenta con:
> + Direcciones MAC de 48 bits (hex).
>+ Tramas con campos fijos (ver abajo).
>+ MTU típica 1500 bytes (tamaño total de trama ≈ 1518 sin contar preámbulo/FCS en captura).
>+ Funciona en medios cobre (UTP), fibra, radio (sobre 802.11 es Wi-Fi).


>La estructura interna de una trama Ethernet se especifica en la norma IEEE 802.3.

>![image](https://hackmd.io/_uploads/Sy-2Asm9el.png)

>**Estructura de una trama Ethernet II:**

> ![image](https://hackmd.io/_uploads/rJOTS2X5gx.png)


**Diferencias: Ethernet / Fast Ethernet / Gigabit**

>**Ethernet (10BASE-T):** 10 Mb/s, UTP Cat3/5.


>**Fast Ethernet (100BASE-TX):** 100 Mb/s, UTP Cat5 (mejor Cat5e).


>**Gigabit Ethernet (1000BASE-T):** 1 Gb/s, UTP Cat5e/Cat6 (recomendado). (La trama a nivel 2 es la misma; cambia velocidad/codificación/medio.)

**b. Cable UTP derecho vs cruzado** 
>**UTP (Unshielded Twisted Pair)**:Consiste en cuatro pares de hilos de cobre aislados y trenzados entre sí, par trenzado sin blindaje; los trenzados reducen interferencia y diafonía. Categorías (Cat5e, Cat6…) determinan hasta qué velocidad/frecuencia soporta (relación con a)).

>**Derecho (straight-through) vs cruzado (crossover):**

>**Derecho**: mismo orden de colores en ambos extremos (p. ej., T568B–T568B). Tradicional para PC ↔ switch.


>**Cruzado**: extremos diferentes (T568A–T568B). Tradicional para PC ↔ PC o switch ↔ switch sin uplink.


>Hoy casi todas las NIC/switches tienen auto MDI-X, así que cualquiera suele funcionar, pero derecho es el estándar.





**c) Conectado a internet, averiguar la puerta de enlace predeterminada de tu conexión (podés utilizar
ipconfig en la línea de comandos en Windows, ifconfig en Linux, o acceder a las opciones de
conexión de tu dispositivo). Luego, en wireshark, filtrar los paquetes de esa dirección IP (Ayuda:
podés utilizar el filtro ip.addr == <dirección>). Ejecutar una función ping en la línea de
comandos hacia la puerta de enlace, monitorear Wireshark y extraer alguno de los paquetes
recibidos. Extraer y documentar en el informe los datos de este paquete, en formato hexadecimal.**

> Desde la terminal se hace ipconfig para averiguar la puerta de enlace predeterminada la cual como podemos apreciar es: 192.168.100.1 

> ![image](https://hackmd.io/_uploads/rJbclnQqgl.png)


> Se copia esa direccion al wireshark para apreciar la captura

> ![image](https://hackmd.io/_uploads/HJing3X5eg.png)

> Filtramos en la seccion superior con el IP del gateway

> ![image](https://hackmd.io/_uploads/SkApe2X9xl.png)

> Desde la terminal escribo el comando "ping" para el envio de paquetes hacia esa direccion IP del gateway. recibiendo exitosamente los paquetes sin ninguna perdida en el medio.

> ![image](https://hackmd.io/_uploads/S1DgWnQqgl.png)

> Con el filtro aplicado y los paquetes enviados y recibidos podemos visualizar en el wireshark esos paquetes y su respectiva respuesta
 
> ![image](https://hackmd.io/_uploads/ryY-ZnXqge.png)

> Se decide seleccionar el ultimo paquete "echo reply" para su analisis

> ![image](https://hackmd.io/_uploads/ByaXZhQ9gg.png)

> Los datos del paquete de ese paquete en formato hexadecimal es el siguiente: 98541b494cc460d7553bf82308004500003c7deb00004001b312c0a86401c0a864710000554b000100106162636465666768696a6b6c6d6e6f7071727374757677616263646566676869

**d) Extraer de la información del punto anterior la dirección MAC del dispositivo. Documentar la
misma e investigar datos del fabricante en internet (utilizar servicios online como este).
Documentar el nombre y dirección de la empresa.**

>  Visualizando nuestra direccion MAC source and destination:

>![image](https://hackmd.io/_uploads/BJl8b2X5ll.png)

> Utilizando los primeros 3 hexadecimales del Mac del source y visualizandolo en la pagina podemos observar los datos del fabricante: 

> ![image](https://hackmd.io/_uploads/ByqvZhQcee.png)

> La misma es Huawei


**e) Repetir los ejercicios c) y d), pero comunicándote con la computadora de un compañero/a.**

> Para esta consigna se usaron dos notebooks conectadas al mismo router. En una de las notebook desde la terminal se hace ipconfig para averiguar la direccion IP la cual como podemos apreciar es: 192.168.0.141 
>
>![Imagen de WhatsApp 2025-09-01 a las 21.56.20_65ab0d81](https://hackmd.io/_uploads/BJbb-p7cge.jpg)
> Se copia esa direccion al wireshark para apreciar la captura
> ![image](https://hackmd.io/_uploads/H1uzVTXcee.png)
> Filtramos en la seccion superior con el IP de la notebook receptora.
> ![image](https://hackmd.io/_uploads/SJTLmaQcxl.png)
> Desde la terminal escribo el comando "ping" para el envio de paquetes hacia esa direccion IP de la notebook receptora. Recibiendo exitosamente los paquetes sin ninguna perdida en el medio.
>
>![Imagen de WhatsApp 2025-09-01 a las 21.56.20_e6b93b8d](https://hackmd.io/_uploads/BydeWaQcex.jpg)
>
> Con el filtro aplicado y los paquetes enviados y recibidos podemos visualizar en el wireshark esos paquetes y su respectiva respuesta
>
>![image](https://hackmd.io/_uploads/H1CHVTQ5lx.png)
>
> Se decide seleccionar el ultimo paquete "echo reply" para su analisis
>![image](https://hackmd.io/_uploads/SkZF4T79gx.png)
>
> Los datos del paquete de ese paquete en formato hexadecimal es el siguiente:
> b8 03 05 78 bb 67 3c 6a d2 dd 69 6a 08 00 45 00
  00 3c 57 65 00 00 80 01 60 90 c0 a8 00 ee c0 a8
  00 8d 00 00 55 33 00 01 00 28 61 62 63 64 65 66
  67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76
  77 61 62 63 64 65 66 67 68 69
>
>  Visualizando nuestra direccion MAC source and destination:
>![image](https://hackmd.io/_uploads/S1xhmSTQcgl.png)
> Utilizando los primeros 3 hexadecimales del Mac del source y visualizandolo en la pagina podemos observar los datos del fabricante: 
>![image](https://hackmd.io/_uploads/SyPCSpQcll.png)
> La misma es TP-LINK Sytems Inc la fabricante de la notebook emisora.
> 

### Consigna N°4: 

**a) Según los resultados obtenidos en este trabajo práctico y la información que obtengan de internet, elaborar conclusiones acerca de la privacidad de un dispositivo en la red y la trazabilidad de una dirección MAC.**

> Durante las capturas realizadas en Wireshark se observo que cada trama lleva informacion sensible como la direccion IP y la direccion MAC, esto significa que un observador dentro de la misma red local puede identificar otros dispositivos conectados, que IP utilizan y a que destino se comunica. La privacidad de una red depende en gran medida de la seguridad aplicada (uso de cifrado, VPN, etc). La misma direccion MAC es unica para cada tarjeta de red y esta grabada de fabrica, los 3 primeros 3 pares hexadecimales identifican al fabricante del dispositivo; lo cual permite rastrear de donde proviene un dispositivo y en combinacion con registros de red y te permite identificar a que usuario corresponde sin embargo la MAC solo es visible dentro de una red local.

**b) Investigar que es el IMEI y qué similitud tiene con la dirección MAC**

> El IMEI (International Mobile Equipment Identity) es un identificador único que poseen los teléfonos móviles y que los operadores utilizan para registrar y bloquear dispositivos. La similitud con la dirección MAC es que ambos son identificadores únicos de hardware que permiten reconocer un dispositivo en una red. La principal diferenica es que la MAC se usa en redes locales (LAN/WiFi), mientras que el IMEI se usa en redes celulares (GSM/4G/5G).


**c) Investigar e incluir una respuesta al siguiente interrogante: ¿Una VPN oculta la dirección MAC del dispositivo?**

> No. Una VPN oculta la dirección IP pública, cifrando y tunelizando el tráfico a través de un servidor intermedio. La dirección MAC no viaja más allá de la red local; solo es visible hasta el router o switch de la red. Por lo tanto, la VPN no oculta la MAC, porque esta nunca se transmite a través de internet, pero tampoco impide que sea vista por otros equipos dentro de la misma red local.


## Conclusion

> Este trabajo permitió comprender cómo distintos factores físicos y técnicos afectan directamente la calidad de una red. Fenómenos como el efecto Doppler o el ruido no son solo teoría: influyen en cómo se transmiten los datos. También se vio cómo tecnologías como Ethernet y Wi-Fi requieren configuraciones específicas para funcionar bien y de forma segura.

> Además, herramientas como Wireshark mostraron que en una red local circula mucha información sensible, como direcciones IP y MAC, lo que abre la puerta a posibles riesgos si no se toman medidas. En resumen, el trabajo ayudó a conectar la teoría con la práctica, y a valorar la importancia de entender cómo funcionan las redes para poder usarlas y protegerlas mejor.


## Bibliografia y referencias
>
> * [Stallings, W. (2004). Comunicaciones y redes de computadores (7ª ed.). Pearson Prentice Hall.](https://drive.google.com/file/d/14wtpr0_eigALENVraeLnF5faYEM4aQB9/view?usp=drive_link)
> * [Radar Doppler](https://es.wikipedia.org/wiki/Radar_Doppler)
> * [El desvanecimiento de Rayleigh](https://en.wikipedia.org/wiki/Rayleigh_fading)
> * [What is the relation between Bit Error Rate (BER), distance d and SNR(dB)? - MATLAB Community](https://au.mathworks.com/matlabcentral/answers/2068346-what-is-the-relation-between-bit-error-rate-ber-distance-d-and-snr-db)
> * [What is my IP address](https://whatismyipaddress.com/)
