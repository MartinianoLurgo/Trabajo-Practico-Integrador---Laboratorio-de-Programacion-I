Proceso QUIZ
	definir pregunta1,pregunta2,pregunta3,pregunta4,pregunta5,pregunta6,pregunta7,pregunta8,pregunta9,pregunta10 Como Caracter;
	definir puntaje Como Entero;
	puntaje <- 0;
	escribir "Cuanto es (120-34+24)*0?";
	leer pregunta1;
	si pregunta1 = "0" Entonces
		escribir "Correcto";
		puntaje <- puntaje + 1;
	FinSi
	Si pregunta1 <> "0" Entonces
		escribir "Incorrecto";
		puntaje <- puntaje-1;
	FinSi
	escribir "¿¿Cuál es el valor de la potencia de exponente cero??";
	leer pregunta2;
	si pregunta2 = "1" entonces;
		escribir "Correcto";
		puntaje <- puntaje + 1;		
	FinSi
	si pregunta2 <> "1" entonces;
		Escribir "Incorrecto";
		puntaje <- puntaje -1;
	FinSi
	escribir "¿Cuánto da el producto de dos razones inversas?";
	leer pregunta3;
	si pregunta3 = "1" Entonces;
		escribir "Correcto";
		puntaje <- puntaje + 1;
	FinSi
	si pregunta3 <> "1" entonces;
		escribir "Incorrecto";
		puntaje <- puntaje -1;
	FinSi
	escribir "En una divicion si el dividento tiende a 0 y el divisor tiende a infinito,¿como es el cociente?";
	leer pregunta4;
	si pregunta4 = "0" entonces;
		escribir "Correcto";
		puntaje <- puntaje + 1;
	FinSi
	si pregunta4 <> "0" entonces;
		escribir "Incorrecto";
		puntaje <- puntaje -1;
	FinSi
	escribir "¿Cual es el unico numero primo par?";
	leer pregunta5;
	si pregunta5 = "2" entonces;
		escribir "Correcto";
		puntaje <- puntaje + 1;
	FinSi
	si pregunta5 <> "2" entonces;
		escribir "Incorrecto";
		puntaje <- puntaje -1;
	FinSi
	escribir "¿Cual es el resultado de la siguiente expresion 8-2*2+6*3-3?";
	leer pregunta6;
	si pregunta6 = "19" entonces;
		escribir "Correcto";
		puntaje <- puntaje + 1;
	FinSi
	si pregunta6 <> "19" entonces;
		escribir "Incorrecto";
		puntaje <- puntaje -1;
	FinSi
	escribir "¿Cuanto es 2 elevado a la -1?";
	leer pregunta7;
	si pregunta7 = "1/2" entonces;
		escribir "Correcto";
		puntaje <- puntaje + 1;
	FinSi
	si pregunta7 <> "1/2" entonces;
		escribir "Incorrecto";
		puntaje <- puntaje -1;
	FinSi
	escribir "¿Cuanto da la tangente de 45?";
	leer pregunta8;
	si pregunta8 = "1" entonces;
		escribir "Correcto";
		puntaje <- puntaje + 1;
	FinSi
	si pregunta8 <> "1" entonces;
		escribir "Incorrecto";
		puntaje <- puntaje -1;
	FinSi
	escribir "¿Cuantpo vale el numero PI?";
	leer pregunta9;
	si pregunta9 = "3,14" entonces;
		escribir "Correcto";
		puntaje <- puntaje + 1;
	FinSi
	si pregunta9 <> "3,14" entonces;
		escribir "Incorrecto";
		puntaje <- puntaje -1;
	FinSi
	escribir "¿La derivada de X es igual a 1?";
	leer pregunta10;
	si pregunta10 = "si" entonces;
		escribir "Correcto";
		puntaje <- puntaje + 1;
	FinSi
	si pregunta10 <> "si" entonces;
		escribir "Incorrecto";
		puntaje <- puntaje -1;
	FinSi
	
	escribir "Su puntaje es de ",puntaje;
FinProceso
