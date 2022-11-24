#IMPORTAR LIBRERIAS EXTERNAS DE PYTHON
import random,os
# DEFINICION DE VARIABLES
generarMaximo = 0
generarNumero = 0
adivinar = 0
nuevoJuego = 0
intentos = 0
#EXPLICACIÖN DEL JUEGO
print("🚀BIENVENIDO AL JUEGO ADIVINA EL NÚMERO🚀")
print("")
print("1° Primero, digite un valor máximo para generar un número para avinar correspondido entre (0 y el maximo)")
print("2° Segundo, empiece a adivinar el número ATENCIÓN! Tiene intentos ilimitados")
print("3° Tercero, el juego te ira dando pistas para hallar el número")
print("Cuando adivines el número el juego finalizara")
print("")
#FUNCION DEL JUEGO ENTERO
def advinarNumeroJuego():
    input("Presiona enter para comenzar el juego...✔️")
    os.system("cls")
    # GENERA EL NÚMERO ALEATORIO
    generarMaximo = input("Digite un valor máximo(ENTERO Y POSITIVO)\n-->")
    # COMPROBACIÓN DE NÚMERO ENTERO
    while not generarMaximo.isdigit(): 
        generarMaximo = input("Debe ser un número entero y positivo\n-->")
    generarMaximo = int(generarMaximo)
    generarNumero = random.randint(0,generarMaximo)
    adivinar = input("Digite su 1° adivinanza\n-->")
    # COMPROBACIÓN DE NÚMERO ENTERO
    while not adivinar.isdigit():
            adivinar = input("Debe ser un número entero y positivo\n-->")
    adivinar=int(adivinar)
    intentos = 1
    while adivinar != generarNumero:
        intentos +=1
        if adivinar < generarNumero:
            adivinar = input("El número es mayor!! Intenta de nuevo\n-->")
            # COMPROBACIÓN DE NÚMERO ENTERO
            while not adivinar.isdigit():
                adivinar = input("Debe ser un número entero y positivo\n-->")
            adivinar=int(adivinar)
        else:
            adivinar = input("El número es menor!! Intenta de nuevo\n-->")
            # COMPROBACIÓN DE NÚMERO ENTERO
            while not adivinar.isdigit():
                adivinar = input("Debe ser un número entero y positivo\n-->")
            adivinar=int(adivinar)
    os.system("cls")
    print(f"Felicitaciones🎉 Adivinaste el número {generarNumero} en {intentos} intentos👏")
    #PREGUNTA SI EL USUARIO DESEA SEGUIR JUGANDO O NO
    nuevoJuego = str(input("Quiere continuar jugando😀\n(SI O NO) "))
    while nuevoJuego.lower() != "si" and nuevoJuego.lower() != "no": 
        nuevoJuego = str(input("Quiere continuar jugando😀\n(SI O NO) "))
    if nuevoJuego.lower() == "si":
        advinarNumeroJuego()
    else:
        input("Presiona enter para regresar al menú...✔️")
advinarNumeroJuego()