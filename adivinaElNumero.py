#IMPORTAR LIBRERIAS EXTERNAS DE PYTHON
import random,os
# DEFINICION DE VARIABLES
generarMaximo = 0
generarNumero = 0
adivinar = 0
nuevoJuego = 0
#EXPLICACIÖN DEL JUEGO
print("🚀BIENVENIDO AL JUEGO ADIVINA EL NÚMERO🚀")
print("##############################")
print("1° Primero, digite un valor máximo para generar un número para avinar correspondido entre (0 y el maximo)")
print("2° Segundo, empiece a adivinar el número ATENCIÓN! Tiene intentos ilimitados")
print("3° Tercero, el juego te ira dando pistas para hallar el número")
print("Cuando adivines el número el juego finalizara")
print("")
#FUNCION DEL JUEGO ENTERO
def advinarNumeroJuego():
    input("Presiona enter para comenzar el juego...✔️")
    os.system("cls")
    generarMaximo = int(input("Digite un valor máximo distinto de 0\n-->"))
    while generarMaximo == 0:
        generarMaximo = int(input("ERROR!! Debe digitar un número distinto de 0\n-->"))
    generarNumero = random.randint(1,generarMaximo) 
    adivinar = int(input("Digite su primera adivinanza\n-->"))
    intentos = 1
    while adivinar != generarNumero:
        intentos +=1
        if adivinar < generarNumero:
            adivinar = int(input("El número es mayor!! Intenta de nuevo\n-->"))
        else:
            adivinar = int(input("El número es menor!! Intenta de nuevo\n-->"))
    os.system("cls")
    print(f"Felicitaciones🎉 Adivinaste el número {generarNumero} en {intentos} intentos👏")
    #PREGUNTA SI EL USUARIO DESEA SEGUIR JUGANDO O NO
    nuevoJuego = str(input("Quiere continuar jugando😀\n(SI O NO) "))
    while nuevoJuego.lower() != "si" and nuevoJuego.lower() != "no": 
        nuevoJuego = str(input("Quiere continuar jugando😀\n(SI O NO) "))
    if nuevoJuego == "si":
        advinarNumeroJuego()
    else:
        input("Presiona enter para regresar al menú...✔️")
advinarNumeroJuego()
