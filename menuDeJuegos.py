import os
#MENU SELECCIONADOR DE JUEGOS
selecionarJuego = 0
while selecionarJuego != 5:
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("◀ Bienvenido a Play 4 in 1🕹️")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print("1 ▷Adivina el número 🚀")
    print("2 ▷Tablas de multiplicación 🚀")
    print("3 ▷Piedra, paperl o tijera 🚀")
    print("4 ▷PELEA POKEMON 🚀")
    print("5 ▷Salir del programa ❌")
    selecionarJuego = int(input("Ingresa una opción\n..."))
    os.system("cls")

    #ENTRADA PARA EL PRIMER JUEGO
    if selecionarJuego == 1:
        os.system("cls")    
    #ENTRADA PARA EL SEGUNDO JUEGO
    if selecionarJuego == 2:
        os.system("cls")
    #ENTRDADA PARA EL TERCER JUEGO
    if selecionarJuego == 3:
        os.system("cls")
    #ENTRADA PARA EL CUARTO JUEGO
    if selecionarJuego == 4:
        os.system("cls")
    
#FINALIZACIÓN DEL PROGRAMA
os.system("cls" )
print("")
print("###################################")
print("Finalizaste el programa!!")
print("Gracias por jugar en Play 4 in 1 😜")
print("###################################")
