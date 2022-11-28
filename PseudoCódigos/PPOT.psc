Proceso PPOT
	Definir a Como Caracter;
	Definir jugador,pc,contadorJugador,contadorPc Como Entero;
	Escribir 'BIENVENIDO A EL JUEGO - PIEDRA,PAPEL Y TIJERA';
	Escribir '';
	Escribir '1° Para jugar debe elegir entre piedra,papel o tijera';
	Escribir '2° El primero que llegue a 3 puntos sera el ganador(Si gana una partida se suma 1 punto)';
	Escribir '3° El número 1 es piedra, el 2 es tijera y el número 3 es papel';
	Escribir '';
	Escribir 'Presione cualquier tecla para continuar...';
	Leer a;
	contadorJugador <- 0;
	contadorPc <- 0;
	Mientras contadorJugador<3 Y contadorPc<3 Hacer
		Escribir 'Ingrese un número piedra,tijera o papel';
		Leer jugador;
		si jugador < 1 o jugador>3 Entonces
			Escribir 'Las opciones son del 1 al 3 vuelva a intentar';
			Escribir '';
		FinSi
		pc <- azar(3)+1;
		Escribir pc;
		Si pc==1 Y jugador==2 Entonces
			escribir 'PERDISTE, La PC eligio Piedra y vos Tijera';
			Escribir '';
			contadorPc <- contadorPc+1;
		FinSi
		
		Si pc==3 Y jugador==1 Entonces
			Escribir 'PERDISTE, La PC eligio Papel y vos Tijera';
			Escribir '';
			contadorPc <- contadorPc+1;
		FinSi
		
		Si pc==2 Y jugador==3 Entonces
			Escribir 'PERDISTE, La PC eligio Tijera y vos Papel';
			Escribir '';
			contadorPc <- contadorPc+1;
		FinSi
		
		Si pc==2 Y jugador==1 Entonces
			Escribir 'GANASTE!! La Pc eligio Tijera y vos Piedra';
			Escribir '';
			contadorJugador <- contadorJugador+1;
		FinSi
		
		Si pc==1 Y jugador==3 Entonces
			Escribir 'GANASTE!! La Pc eligio Piedra y vos Papel';
			Escribir '';
			contadorJugador <- contadorJugador+1;
		FinSi
		
		Si pc==3 Y jugador==2 Entonces
			Escribir 'GANASTE!! La Pc eligio papel y vos Tijera';
			Escribir '';
			contadorJugador <- contadorJugador+1;
		FinSi
		
		Si pc==jugador Entonces
				Escribir 'EMPATE!, Se repite la partida';
				Escribir '';
			FinSi
	FinMientras
	Si contadorJugador==3 Entonces
		Escribir 'FELICITACIONES!! Ganaste!';
	FinSi
	
	Si contadorPc==3 Entonces
		Escribir 'PERDISTE!! La Pc ganó la partida';
	FinSi
FinProceso