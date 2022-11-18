import random
import os


nombre_del_usuario = None
VIDA_DE_PIKACHU = 80
VIDA_DE_SQUIRTEL = 100

TAMAÑO_BARRA_VIDA = 20

vida_de_Pikachu = VIDA_DE_PIKACHU
vida_de_squirtel = VIDA_DE_SQUIRTEL
nombre_del_usuario = input("ingrese su nombre de Usuario por favor: ")

print("COMENZAMOS LA PARTIDA\n"
    "!!!Suerte",nombre_del_usuario," Pikachu es un oponente duro!!!")


while vida_de_squirtel > 0 and vida_de_Pikachu > 0:

    #empesamos la pelea
    #Turno del la computadora (osea de pikachu)
    print("Turno de Pikachu")
    ataque_pikachu = random.randint(1, 2)

    if ataque_pikachu == 1:
        #bola voltio
        print("Ataque de bola voltio {} de daño".format(10))
        vida_de_squirtel -= 10

    if ataque_pikachu == 2:
        #onda trueno 
        print("Ataque de onda trueno {} de daño".format(11))
        vida_de_squirtel -=11
    


    input("Enter para continuar ")
    os.system("cls")

    barra_de_vida_pikachu = int(vida_de_Pikachu * TAMAÑO_BARRA_VIDA / VIDA_DE_PIKACHU)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * barra_de_vida_pikachu," " * (TAMAÑO_BARRA_VIDA - barra_de_vida_pikachu),
                                             vida_de_Pikachu, VIDA_DE_PIKACHU))

    barra_de_vida_de_squirtel = int(vida_de_squirtel * TAMAÑO_BARRA_VIDA / VIDA_DE_SQUIRTEL)
    print("Squirtel:   [{}{}] ({}/{})".format("*" * barra_de_vida_de_squirtel," "*(TAMAÑO_BARRA_VIDA - barra_de_vida_de_squirtel),
                                              vida_de_squirtel,VIDA_DE_SQUIRTEL))
    if vida_de_squirtel < 0:
        vida_de_squirtel = 0
    if vida_de_Pikachu < 0:
        vida_de_Pikachu = 0

    ataque_squirte = None

    while ataque_squirte != "P" and ataque_squirte != "C" and ataque_squirte != "B" and ataque_squirte != "N" and ataque_squirte != "E":
        print("Turno de squirte del entrenador:",nombre_del_usuario)
        ataque_squirte = input("¿Que ataque decea realizar?\n[P]PLACAJE (10 de daño)\n[C]CHORRO DE AGUA (11 de daño)\n[B]BURBUJA (9 de daño)\n[E]ESCUDO (+5 de vida)\n[N]NO ATACAR""\n")

    if ataque_squirte == "P":
        print("Ataque de placaje {} de daño".format(10))
        vida_de_Pikachu -= 10

    elif ataque_squirte == "C":
        print("Ataque de Chorro de agua {} de daño".format(11))
        vida_de_Pikachu -= 11

    elif ataque_squirte == "B":
        print("Burbuja {} de daño".format(9))
        vida_de_Pikachu -= 9
    elif ataque_squirte == "N":
        print("No Atacara")

    elif ataque_squirte == "E":
        print("Escudo renerador")
        vida_de_squirtel += 5
    

    barra_de_vida_pikachu = int(vida_de_Pikachu * TAMAÑO_BARRA_VIDA / VIDA_DE_PIKACHU)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * barra_de_vida_pikachu, " " * (TAMAÑO_BARRA_VIDA - barra_de_vida_pikachu),
                                              vida_de_Pikachu, VIDA_DE_PIKACHU))

    barra_de_vida_de_squirtel = int(vida_de_squirtel * TAMAÑO_BARRA_VIDA / VIDA_DE_SQUIRTEL)
    print("Squirtel:   [{}{}] ({}/{})".format("*" * barra_de_vida_de_squirtel, " " * (TAMAÑO_BARRA_VIDA - barra_de_vida_de_squirtel),
                                                  vida_de_squirtel, VIDA_DE_SQUIRTEL))
    if vida_de_squirtel < 0:
        vida_de_squirtel = 0
    if vida_de_Pikachu < 0:
        vida_de_Pikachu = 0

if vida_de_Pikachu > vida_de_squirtel:
    print("Gana Pikachu")
if vida_de_squirtel > vida_de_Pikachu:
    print("Gana el Scruirtlel de",nombre_del_usuario)
