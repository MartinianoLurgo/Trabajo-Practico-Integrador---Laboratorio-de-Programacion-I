import os
#MENU SELECCIONADOR DE JUEGOS
os.system("cls")
selecionarJuego = 0
while selecionarJuego != 5:
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("◀ BIENVENIDO A PLAY 4 IN 1🕹️")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print("1 ▷Adivina el número 🚀")
    print("2 ▷Tablas de multiplicación 🚀")
    print("3 ▷Piedra, paperl o tijera 🚀")
    print("4 ▷ESCAPA SI PUEDES 🚀")
    print("5 ▷Salir del programa ❌")
    selecionarJuego = int(input("Ingresa una opción\n..."))
    os.system("cls")
    #ENTRADA PARA EL PRIMER JUEGO
    if selecionarJuego == 1:
        os.system("python advinarElNumero.py")
        os.system("cls")    
    #ENTRADA PARA EL SEGUNDO JUEGO
    if selecionarJuego == 2:
        os.system("python Tablamultiplicacion.py")
        os.system("cls")
    #ENTRDADA PARA EL TERCER JUEGO
    if selecionarJuego == 3:
        os.system("python piedraPapelTijera.py")
        os.system("cls") 
    #ENTRADA PARA EL CUARTO JUEGO
    if selecionarJuego == 4:
        os.system("python ESCAPA_SI_PUEDES.py")
        os.system("cls")
    
#FINALIZACIÓN DEL PROGRAMA
os.system("cls" )
print("")
print("🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀")    
print("->Finalizaste el programa!! Hasta la proxima👋")
print("->Gracias por jugar en Play 4 in 1 😜")
print("🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀")    
