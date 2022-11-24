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


## ANALISIS Y DISEÑO
___
### 1° JUEGO "ADIVINAR EL NÚMERO
*Datos de entrada*
- generarMaximo: tipo de dato númerico(entero),para determinar un número máximo
- adivinar: tipo de dato númerico(entero), para adivinar el número máximo(Puede repertise varias veces)
- nuevoJuego: tipo de dato caracter, para determinar si el usuario desea seguir jugando

*Datos de entradas*
- generarNumero: tipo de dato númerico(entero), genera un valor aleatorio de 0 al númeor máximo
- intentos: tipo de dato númerico(entero), muestra por pantalla la cantidad de intentos

*Proceso*

El programa pide números enteros, el usuario digita y se corrobora si el mismo es un dato
númerico entero o no, luego realiza la misma función con la variable adivinar para continuar
con el programa, por último cuando se pide un dato de cadena, si la variable nuevoJuego es igual
a un dato de caracter y es igual a "si" o "no" el programa continua, de no ser así se realiza una comprobación y se pregunta de nuevo si el tipo de dato no es caracter o no corresponde al condicional.

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

**Pseudocódigo**

El Pseudocódigo de este juego, esta hecho en el programa Pseint, definiendo todas sus variables,
explicando cada tipo de dato y con comentarios que ayudan a leer el código de una mejor manera, y con el mismo programa pudimos realizar un diagrama de flujo para una revisió gráfica del mismo Juego.
## DOCUMENTACIÓN DE REFERENCIA
___
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