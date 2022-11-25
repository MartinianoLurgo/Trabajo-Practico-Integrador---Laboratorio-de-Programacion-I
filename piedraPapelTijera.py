import random,os
os.system("cls")
print("BIENVENIDO A EL JUEGO - PIEDRA,PAPEL Y TIJERA\n")
print("")
print("1° Para jugar debe elegir entre piedra,papel o tijera")
print("2° El primero que llegue a 3 puntos sera el ganador(Si gana una partida se suma 1 punto)")
print("3° El número 1 es piedra, el 2 es tijera y el número 3 es papel")
print("")
input("Presione cualquier tecla para continuar...")
def piedraPapelTijera():
    contadorJugador=0
    contadorPc=0
    while contadorJugador < 3 and contadorPc < 3:
        jugador=int(input("Ingrese un número(piedra,tijera o papel)\n-->")) 
        pc=random.randint(1,3)
        if pc == 1 and jugador==2:
            os.system("cls")
            print("PERDISTE, La PC eligio Piedra y vos Tijera")
            print("")
            contadorPc=contadorPc+1
        elif pc == 3 and jugador==1 : 
            os.system("cls")
            print("PERDISTE, La PC eligio Papel y vos Tijera")
            print("")
            contadorPc=contadorPc+1
        elif pc ==2 and jugador== 3:
            os.system("cls")
            print("PERDISTE, La PC eligio Tijera y vos Papel")
            print("")
            contadorPc=contadorPc+1
        elif pc == 2 and jugador==1:
            os.system("cls")
            print("GANASTE!! La Pc eligio Tijera y vos Piedra")
            print("")
            contadorJugador=contadorJugador + 1
        elif pc == 1 and jugador==3 : 
            os.system("cls")
            print("GANASTE!! La Pc eligio Piedra y vos Papel")
            print("")
            contadorJugador=contadorJugador + 1
        elif pc ==3 and jugador== 2:
            os.system("cls")
            print("GANASTE!! La Pc eligio papel y vos Tijera")
            print("")
            contadorJugador=contadorJugador+1
        elif pc == jugador:
            os.system("cls")
            print("EMPATE!, Se repite la partida")
            print("")
        else:
            print("Las opciones son del 1 al 3 vuelva a intentar")
            print("")
    if contadorJugador==3:
        print("FELICITACIONES!! Ganaste!")
    elif contadorPc== 3 :
        print("PERDISTE!! La Pc ganó la partida")
piedraPapelTijera()
nuevoJuego = input("Quiere continuar jugando?\n")
if nuevoJuego.lower()=="si":
    piedraPapelTijera()
else:
    print("saliste del juego, Hasta la proxima!!")
    input("Presione cualquier tecla para volver al menu...")