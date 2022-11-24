Algoritmo adivinarElNumero
	// DELCLARACIÓN DE VARIABLES
	Definir generarMaximo,generarNumero,adivinar,nuevoJuego,intentos Como Entero
	generarMaximo <- 0
	generarNumero <- 0
	adivinar <- 0
	nuevoJuego <- 0
	intentos <- 0
	// REGLAS DEL JUEGO
	Escribir ('BIENVENIDO AL JUEGO ADIVINA EL NÚMERO')
	Escribir ('')
	Escribir ('1° Primero, digite un valor máximo para generar un número para avinar correspondido entre (0 y el maximo)')
	Escribir ('2° Segundo, empiece a adivinar el número ATENCIÓN! Tiene intentos ilimitados')
	Escribir ('3° Tercero, el juego te ira dando pistas para hallar el número')
	Escribir ('Cuando adivines el número el juego finalizara')
	Escribir ('')
	// LEER NÚMERO MÁXIMO
	Escribir 'Introduce un valor máximo(Entero y Positivo)'
	Leer generarMaximo
	Borrar Pantalla
	Mientras (generarMaximo)=(CARACTER) Hacer
		Escribir 'Introduce un valor máximo(Entero y Positivo)'
		Leer generarMaximo
	FinMientras
	// GENERAR NÚMERO ALEATORIO
	generarNumero <- azar(generarMaximo)
	Escribir 'Digite su 1° adivinanza'
	Leer adivinar
	// COMPROBACIÓN DE NO CARACTER
	Mientras (adivinar)=(CARACTER) Hacer
		Escribir 'Debe ser un numero(Entero y Positivo)'
		Leer adivinar
	FinMientras
	intentos <- 1
	Mientras adivinar<>generarNumero Hacer
		intentos <- intentos+1
		Si adivinar>generarNumero Entonces
			Escribir 'El número es menor, intenta de vuelta'
			Leer adivinar
			// COMPROBACIÓN DE NO CARACTER
			Mientras (adivinar)=(CARACTER) Hacer
				Escribir 'Debe ser un numero(Entero y Positivo)'
				Leer adivinar
			FinMientras
		SiNo
			Escribir 'El número es mayor, intenta de vuelta'
			Leer adivinar
			// COMPROBACIÓN DE NO CARACTER
			Mientras (adivinar)=(CARACTER) Hacer
				Escribir 'Debe ser un numero(Entero y Positivo)'
				Leer adivinar
			FinMientras
		FinSi
	FinMientras
	Borrar Pantalla
	Escribir 'Felicitaciones!! Adivinaste el número ',generarNumero,' en ',intentos,' intentos'
FinAlgoritmo
