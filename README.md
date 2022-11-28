# Trabajo-Integrador Laboratorio de Computación I
![Captura de pantalla 2022-10-18 090801](https://user-images.githubusercontent.com/105757516/196425218-51ef11dc-1d91-4c14-8cdb-e89bf8207200.png)

## Resumen Del Trabajo Practico:

La empresa Play.In en respuesta a las necesidades de la escuela local decide realizar un
programa que le permita a los estudiantes de primaria aprender mientras se divierten. Al
mismo tiempo dicha empresa quiere premiar a sus empleados por su arduo desempeño.
Por tal motivo Play.In solicita a sus programadores que presenten sus opciones, las mismas
deben cumplir con lo siguiente:
● El programa debe contar con 4 juegos didácticos diferentes.
● El jugador debe poder optar a qué juego quiere jugar y no hay límite de veces para
jugarlo.
● La empresa controlará que el código del programa esté comentado correctamente
para poder darle continuidad con algún otro programador.



## Integrantes:

● Lurgo Johnston Martiniano
https://github.com/MartinianoLurgo
  
● Mollina Mansilla Ignacio
https://github.com/NachoMansilla2103
  
● Piñan Federico 
https://github.com/federicopinan

● Porello Nicolas
https://github.com/NicolasPorello

##  Presentación de enunciados
___
### 1° Juego "ADIVINAR EL NÚMERO"
En este juego, el usuario deberá introducir un valor máximo para el comienzo del mismo. Por ejemplo:
el usuario introduce el número 10 el número que se debe adivinar esta correspondio entre 0 y 10. luego, el usuario deberá ingresar por teclado u número para intentar adivinar el número, el mismo posee infinitos intentos para hallar el número. Si el usuario digita un número, y si es el incorrecto el programa ayuda al usuario y la cantidad de intentos irá incrementado de a 1, avisando que el número a encontrar es mayor o menor dependiendo lo digitado. Cuando el jugador halla adivinado el número, el programa muestra un cartel felicitando al usuario, además muestra el número de intentos para el hallazgo. Por último, el programa pregunta si desea seguir jugando o no, si la respuestas es sí, el programa se ejecuta nuevamente por el otro lado si la respuesta es no, el usuario se dirigirá al menu de opciones.

### 2° Juego "Tabla de Multiplicación"
En el siguiente programa el usuario debera ingresar un numero que desea saber su tabla de multiplicar
y luego se le pedira ingresar otro numero, que es hasta que numero desea multipiplicar el numero anteriormente ingresado,
luego de esto se mostrara por pantalla la tabla de multiplicar y ademas un vector generado con esos resultados,
tambien prodra volver a realizar el juego cuantas veces quiera con diferentes numeros

### 3°Juego "Piedra,Papel o Tijera"
El usuario debera introducir un numero del 1 al 3 
1 es piedra, que le ganara a tijera pero perdera contra papel
2 es tijera, que le ganara a papel pero perdera con piedra
3 es papel, que le ganara a piedra  pero perdera con tijera
si la pc y el jugador eligen lo mismo empataran 
cada vez que uno de los dos gane una ronda se le sumara un punto esto asi hasta que uno de los dos gane 3 veces 
si empatan no se tomara la jugada y si eligen otro numero que no sea del 1 al 3 le saldra un cartel diciendo que debe elegir un numero del 1 al 3

### 4º Juego "ESCAPA SI PUEDES"
El usuario debera conforme avanza en el juego ir eligiendo diferentes opciones de historia para asi poder lograr escapar de la prision en la que se encuentra, si este perdio el juego, el mismo puede volver a intentarlo.
!!!SUERTE!!!
___

### ANALISIS Y DISEÑO

### 1° JUEGO "ADIVINAR EL NÚMERO
*Datos de entrada*
- generarMaximo: tipo de dato númerico(entero),para determinar un número máximo
- adivinar: tipo de dato númerico(entero), para adivinar el número máximo(Puede repertise varias veces)
- nuevoJuego: tipo de dato caracter, para determinar si el usuario desea seguir jugando

*Datos de salida*
- generarNumero: tipo de dato númerico(entero), genera un valor aleatorio de 0 al númeor máximo
- intentos: tipo de dato númerico(entero), muestra por pantalla la cantidad de intentos

*Proceso*

1° El programa le pide al usuario que digite un número entero y positivo.
2° Luego de comprobar que es entero y positivo, el programa genera un número aleatorio entre 0 y el número digitado.
3° Comienza el juego, el usuario debera ingresar número para intentar adivinar el número generado.
4° Si el jugador falla, se le sumara un acumulador de intentos y el programa dará una ayuda para intentar adivinarlo.
5° Si el jugador adivina el número, se mostrara un cartel felicitando al jugador y la cantidad de intentos realizados.
6° Por último, el programa pregunta si quiere seguir jugando o no.

### 2° Juego "TABLAS DE MULTIPLICACIÓN"

*Datos de Entrada*
-num: tipo de dato númerico(entero), para saber que numero desea multiplicar
-cantmultiplos: tipo de dato númerico(entero), para saber hasta que numero desea multiplicar
-respuesta: tipo de dato caracter(string), para confirmar si quiere seguir jugando

*Datos de Salida*
-total: tipo de dato númerico(entero), muestra las multiplicaciones sucesivas
-tabla: tipo de dato vector, vector generado por las multiplicaciones

*Proceso*

El programa pide un numero que desea saber su tabla y luego pide otro para saber hasta que numero lo desea multiplicar, luego de eso el programa entra en un ciclo donde multiplica el numero por I que es el contador, hasta el 2do numero ingresado. luego el programa pregunta si desea seguir jugando mediante una confirmacion

### 3° Juego "Piedra, Papel o Tijera"
*Datos de entrada*
jugador= tipo de dato númerico(entero), elige un numero
letra= tipo de dato cadena(caracter),para comenzar el juego

*Datos de salida*
contadorJugador= tipo de dato númerico(entero),cuenta cuantas veces gano el jugador
contadorPc= tipo de dato númerico(entero),cuenta cuantas veces gano la pc

*Datos*
pc= tipo de dato númerico(entero),elige un numero

**Pseudocódigo**

El Pseudocódigo de este juego, esta hecho en el programa Pseint, definiendo todas sus variables,
explicando cada tipo de dato y con comentarios que ayudan a leer el código de una mejor manera, y con el mismo programa pudimos realizar un diagrama de flujo para una revisió gráfica del mismo Juego.

### 4º Juego "ESCAPA SI PUEDES"

*Datos de entrada*

Interracion del usuario

*Proceso*

En este juego utilie una serie de funciones las cuales conforme se desarrolla la historia se van aplicando, primero cree el menu del juego y desde alli comienza el codigo.

*Datos de salida*

Desarollo de la trama

*Pseudocodigo*

este mismo esta echo en un procesador de texto de codigo llamado "sublime text"
y en este desarrolle el pseudo codigo a mano sin la necesidad de utilizar pseint.
___

## DOCUMENTACIÓN DE REFERENCIA

### 1° JUEGO "ADIVINAR EL NÚMERO"
- Unidad 1°: Pensamiento Computacional, Pseudocodigo
- Unidad 2°: Estructuras selectivas
- Unidad 3°: Estructuras Repetitivas
- Uso de funciones
- Python
- Importación de librería **OS**
- Importación de librería **RANDOM**

### 2° JUEGO "TABLA DE MULTIPLICACIÓN"
- Unidad 1°: Pensamiento Computacional, Pseudocodigo
- Unidad 2°: Estructuras selectivas
- Unidad 3°: Estructuras Repetitivas
- Python

### 3° JUEGO "PIEDRA,PAPEL o TIJERA"
- Unidad 1°: Pensamiento Computacional, Pseudocodigo
- Unidad 2°: Estructuras selectivas
- Unidad 3°: Estructuras Repetitivas
- Python
- Uso de funciones
- Importación de librería **OS**

### 4º JUEGO "ESCAPA SI PUEDES"

- Unidad 1°: Pensamiento Computacional, Pseudocodigo
- Unidad 2°: Estructuras selectivas
- Python
- Uso de funciones
- Importación de librería **OS**
