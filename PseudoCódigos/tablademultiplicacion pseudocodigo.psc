Proceso tablademultiplicar
	Definir numeroo,Cantmultiplos,tabla,i Como Entero;
	Definir confirmacion Como Caracter;
	Dimension tabla[11];
	Escribir 'Ingrese el numero que desea saber la tabla de multiplicación';
	Leer numeroo;
	Escribir 'Ingrese hasta que numero desea multiplicar';
	Leer Cantmultiplos;
	Para i<-0 Hasta 10 Hacer
		tabla[i] <- numeroo*i;
	FinPara
	Escribir tabla[0],' ',tabla[1],tabla[2],' ',tabla[3],' ',tabla[4],' ',tabla[5],' ',tabla[6],' ',tabla[7],' ',tabla[8],' ',tabla[9],' ',tabla[10];
	Escribir 'Desea continuar?(si) para continuar';
	Leer confirmacion;
	Mientras confirmacion='si' Hacer
		confirmacion <- Minusculas(confirmacion);
		Si confirmacion='si' Entonces
			Escribir 'Ingrese el numero que desea saber la tabla de multiplicación';
			Leer numeroo;
			Escribir 'Ingrese hasta que numero desea multiplicar';
			Leer Cantmultiplos;
			Para i<-0 Hasta 10 Hacer
				tabla[i] <- numeroo*i;
			FinPara
			Escribir tabla[0],' ',tabla[1],tabla[2],' ',tabla[3],' ',tabla[4],' ',tabla[5],' ',tabla[6],' ',tabla[7],' ',tabla[8],' ',tabla[9],' ',tabla[10];
			Escribir 'Desea continuar?(si) para continuar';
			Leer confirmacion;
		FinSi
		Si confirmacion<>'si' Entonces
			Escribir 'Finalizo';
		FinSi
	FinMientras
FinProceso
