import os
#MENU SELECCIONADOR DE JUEGOS
selecionarJuego = 0
while selecionarJuego != 5:
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("◀ BIENVENIDO A PLAY 4 IN 1🕹️")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print("1--> ADIVINA EL NÚMERO  🚀")
    print("2--> TABLAS DE MULTIPLICACIÓN 🚀")
    print("3--> PIEDRA, PAPEL O TIJERA 🚀")
    print("4--> PELEA POKEMON 🚀")
    print("5--> SALIR DEL PROGRAMA ❌")
    selecionarJuego = int(input("Ingresa una opción\n-->"))
    os.system("cls")

    #ENTRADA PARA EL PRIMER JUEGO
    if selecionarJuego == 1:
        os.system("python adivinaElNumero.py")
        os.system("cls")    
    #ENTRADA PARA EL SEGUNDO JUEGO
    if selecionarJuego == 2:
        os.system("python Tablamultiplicacion.py")
        os.system("cls")
    #ENTRDADA PARA EL TERCER JUEGO
    if selecionarJuego == 3:
        os.system("python piedra,papel o tijera.py")
        os.system("cls")
    #ENTRADA PARA EL CUARTO JUEGO
    if selecionarJuego == 4:
        os.system("python ")
        os.system("cls")
    
#FINALIZACIÓN DEL PROGRAMA
os.system("cls" )
print("")
print("🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀")    
print("->Finalizaste el programa!! Hasta la proxima👋")
print("->Gracias por jugar en Play 4 in 1 😜")
print("🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀")    
