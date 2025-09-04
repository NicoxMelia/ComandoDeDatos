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
