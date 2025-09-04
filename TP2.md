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
