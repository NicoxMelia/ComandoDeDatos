# Comunicaciones de Datos - Trabajo Practico N°1 

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
El objetivo de este trabajo práctico es repasar los fundamentos básicos de Teoría de las Comunicaciones y Comunicaciones Digitales, vinculando conceptos de la capa física con los modelos de transmisión y recepción de datos. Se abordan temas como ondas electromagnéticas, modulación/demodulación, comportamiento de señales y transmisión. Se analiza la importancia de la correcta representación y transmisión de señales digitales, evaluando técnicas de modulación y parámetros como la tasa de error de bit (BER). Finalmente, se realiza la implementación de una red simple en Packet Tracer, compuesta por un router, una computadora de escritorio y una notebook, con el fin de comprender la configuración, operación y alcance de redes inalámbricas en un entorno de simulación.

**Palabras Clave**: _modulación, demodulación, ondas electromagneticas, Packet Tracer_

## Introducción
Las comunicaciones digitales constituyen la base tecnológica que permite la interconexión global de dispositivos y sistemas. Comprender sus fundamentos es esencial para el diseño, análisis y optimización de redes modernas. Este trabajo práctico busca integrar conocimientos teóricos previamente adquiridos con su aplicación en un entorno de simulación mediante Packet Tracer, reforzando el vínculo entre la capa física y las capas superiores del modelo de comunicaciones. A través del estudio de las ondas electromagnéticas, las técnicas de modulación, la representación de señales digitales y los fenómenos que afectan su propagación, se desarrolla un marco conceptual que sirve de soporte para la configuración y prueba de redes reales o simuladas. La práctica final, enfocada en la implementación de una red inalámbrica, permite afianzar la comprensión de los parámetros de configuración y de las limitaciones físicas que intervienen en su funcionamiento.

## Metodologia
El desarrollo del trabajo práctico se realizó en tres etapas principales:

1. Revisión teórica: Se repasaron los fundamentos de ondas electromagnéticas, señales de tiempo continuo/discreto, y técnicas de modulación y demodulación, con apoyo en bibliografía de comunicaciones digitales.

2. Análisis conceptual: Se aplicaron los conceptos estudiados a situaciones prácticas mediante el análisis de gráficos y esquemas provistos en la consigna. Esto permitió vincular los fundamentos de la capa física con fenómenos como la atenuación, la sincronización y la relación entre ancho de banda y BER.

3. Simulación práctica: Se implementó en Cisco Packet Tracer una red inalámbrica compuesta por un router, una PC y una laptop. Se configuraron parámetros de red (DHCP, direcciones IP, conexión Wi-Fi) y se evaluó la conectividad y el alcance de la señal variando la distancia.

## Resultados

### Consigna N°1: Resumir brevemente los fundamentos basicos y esenciales de los siguientes conceptos:
1. **Ondas Electromagneticas:**
>Son perturbaciones periódicas de campos eléctrico y magnético que se propagan en el espacio transportando energía. No necesitan un medio material para propagarse (pueden viajar en el vacío). Se caracterizan por su frecuencia *f*, longitud de onda *λ*, y velocidad de propagación *c*. La relación entre ellas es:
>
>$$c=\lambda \cdot f$$
>
>En telecomunicaciones, distintas bandas de frecuencia se asignan a diferentes aplicaciones (radio, microondas, luz visible, etc.).

 2. **Modulación/Demodulación**:
  * **Modulación**:
>Proceso de variar una señal portadora (generalmente sinusoidal) en amplitud, frecuencia o fase para transmitir información. *Ejemplos: AM (amplitud), FM (frecuencia), PM (fase).*
 * **Demodulación**:
>Proceso inverso, donde el receptor extrae la información de la señal modulada.
 Se utilizan para adaptar la señal al medio de transmisión, reducir interferencias y permitir la transmisión simultánea de múltiples señales.

3. **Señales de Tiempo Continuo**:
> Son funciones definidas para todo instante de tiempo *t*. Ejemplo: la tensión analógica captada por un micrófono. Se describen matemáticamente como:
$$x(t)$$

4. **Señales de Tiempo Discreto**:
> Son secuencias de valores definidas en instantes separados de tiempo (muestras). Provienen de muestrear una señal continua con un período *T*. Se describen como:
$$x[n]$$
Necesitan cumplir el criterio de Nyquist para evitar aliasing.


### Luego de repasar estos conceptos debemos analizar la siguiente imagen y responder las siguientes preguntas

![image](https://hackmd.io/_uploads/r1b2PZY_xx.png)




 a. ¿Qué frecuencia y longitud de onda tiene esta onda?. Considerar que viaja exactamente a la velocidad de la luz *c* ?
 
> la velocidad de la luz es $300000 \space {\frac{km}s}$ o $300000000 \space \frac{m}{s}$, la longitud de onda vista en la imagen es de $60 \space mm$ y es basicamente tal cual se entiende es la longitud de un punto a otro desde donde empieza hasta donde termina la onda.
Como la relacion es $$\lambda = \frac{c}{f}$$ entonces
$$f=\frac{c}{λ} = \frac{300000000\space\frac{m}s}{0.06 \space m} = 5 \cdot 10^9 \space Hz$$

b. El espectro EM está dividido en regiones y bandas. Investigar y mencionar en qué región del espectro opera esta onda, y más precisamente, en qué banda.
![image](https://hackmd.io/_uploads/ry9DtZFdgl.png)

>Se encuentra en el espectro de las ondas centimetricas y opera en banda 10 segun la definicion de la ITU. 

c. Investigar qué dispositivos para comunicaciones de datos operan en esta banda y brindar al menos un ejemplo.

> Un ejemplo muy comun son algunos routers wifi que operan en una banda de 5 Ghz, Router Wi-Fi estándar 802.11ac doméstico de doble banda (2.4 y 5 GHz).

d. ¿Qué fenómeno se quiere representar con la línea de trazos roja en la figura de la onda?

> **Atenuación**: la disminución de la amplitud de la señal a medida que se propaga debido a la absorción, dispersión o pérdidas en el medio. basicamente la intensidad disminuye

e. El fenómeno descrito en el ítem anterior, ¿Afecta al dispositivo que diste de ejemplo? ¿Podés notar esto en alguna experiencia de la vida cotidiana?

> Sí, la atenuación afecta a routers Wi-Fi en 5 GHz. La señal pierde fuerza al atravesar paredes, techos o muebles.
>
>**Ejemplo cotidiano**: cuando te alejás de un router Wi-Fi 5 GHz a otra habitación, la velocidad de conexión disminuye o la señal se pierde antes que en la banda de 2.4 GHz, debido a la mayor atenuación y menor penetración de 5 GHz.
Basicamente un ejemplo son esos mismos routers a 5 GHz tambien hay de 2.4 GHz, pero la diferencia entre ambas es que el de 5Ghz por ejemplo transmite los datos mucho mas rapido pero la longitud de onda sera mucho menor que el de 2.4 GHz entonces el alcance del de 5 GHz es menor pero trasmite datos a mayor velocidad, en cambio el de 2.4 GHz trasmite a menor velocidad pero con mayor longitud de onda.

f. El fenómeno descrito anteriormente:
  - ¿Afecta a las transmisiones de telefonía celular?
  
  > Sí, especialmente en frecuencias más altas (como 5G mmWave) que tienen menos alcance y penetran peor obstáculos.
  
- ¿Afecta a las transmisiones por cable coaxial?

> Mucho menos afectadas, ya que la señal está guiada dentro del cable y protegida del medio libre; aun así, existe atenuación por la resistencia y pérdidas dieléctricas del cable.

- ¿Afecta a las transmisiones por fibra óptica?

> Muy poco afectadas en términos de distancia (la atenuación típica es de 0.2 dB/km), ya que la luz viaja confinada en el núcleo de la fibra, con pérdidas mínimas.

### Consigna N°2: Analizar el siguiente sistema y responder las siguientes preguntas

![image](https://hackmd.io/_uploads/rkUuhWKdee.png)


a. Según su direccionalidad y características temporales, ¿Qué tipo y modo de transmisión se quieren representar?

> Es la transmision sincronica, la cual segun la imagen es unidireccional en donde ademas de los datos la señal de reloj de esta manera el receptor se sincroniza con el emisor y determina instantes significativos de la señal que recibe, los datos se transmiten de manera consecutiva entre el emisor y el receptor un flujo constante que la determina la señal de sincronismo

b. ¿Es este el mejor paradigma si busco transmitir datos rápidamente y de forma bidireccional?

> No ya que segun el esquema presentado el envio el unidireccional, aunque este tipo de transmision es mas eficiente en la utilizacion del medio de transmisión que la asincronica siendo mas inmune a errores por lo que se suele usar para mayores velocidades que la asincronica

c. En la expresión más simple de señal digital, podemos pensar que un nivel de tensión “1” representa un 1 digital, y un nivel de tensión “0” representa un 0 digital. Con esto en mente, analicemos el siguiente gráfico, que podría representar un tipo de comunicación UART:

![image](https://hackmd.io/_uploads/BJIMa-tdxg.png)

En este caso estamos representando la transmisión del siguiente byte: “00100011”, que en codificación ASCII representa el símbolo “#”. Si quisiéramos transmitir la 4ta letra del nombre de tu grupo, ¿Cómo se vería la señal?

> Nuestro grupo se llama “ComandoDeDatos” por ende la cuarta letra del grupo es “a” que de Ascii a Codificacion binaria representa el numero 01100001 por ende quedaria algo asi la señal representada

![image](https://hackmd.io/_uploads/S1_w6-KOeg.png)

d. Dada la pendiente en los niveles de tensión que podemos ver indicada con flechas en el gráfico de ejemplo. ¿En qué marcas temporales medirían la señal para determinar el valor digital de la misma?

> En las marcas temporales pares como en el ejemplo se pueden ver T0, T2, T4, etc. Osea basicamente, si nosotros trataramos de medir el valor digital en la marcas temporales de la pendiente el valor seria indeterminado por eso se esperaria a que el valor se establezca un poco y donde el valor de tension es claro son en los tiempos Ti-par.
