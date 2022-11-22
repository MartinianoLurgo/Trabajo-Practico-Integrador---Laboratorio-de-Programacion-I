import random
print("bienvenido a este juego llamado piedra papel o tijera\n")
print("elije 1 para piedra, elije 2 para tijera y elije 3 para papel")

i=0
j=0
while j<3 or i<3:
    jugador=int(input("elija piedra papel o tijera\n")) 
    pc=random.randint(1,3)
    if pc == 1 and jugador==2:
        print("perdiste , pc eligio piedra")
        i=i+1
    elif pc == 3 and jugador==1 : 
        print("perdiste , pc eligio papel")
        i=i+1
    elif pc ==2 and jugador== 3:
        print("perdiste , pc eligio tijera")
        i=i+1
    elif pc == 2 and jugador==1:
        print("ganaste , pc eligio piedra")
        j=j+1
    elif pc == 1 and jugador==3 : 
        print("ganste , pc eligio papel")
        j=j+1
    elif pc ==3 and jugador== 2:
        print("ganaste , pc eligio tijera")
        j=j+1
    elif pc == jugador:
        print("empate")
    else:
        print("del 1 al 3 elija ")
if i ==3:
    print("ganaste 3 veces ")
elif j== 3 :
    print("ganaste 3 veces seguidas")
