
import os

def menu():
	os.system("cls")
	print('''
 _______    _______    ______       __        _______       __
|   ____|  /   ____\  |   ___|     /  \      |   _   |     /  \ 
|  |____    \ \       |  |        /    \     |   |   |    /    \ 
|   ____|     \ \     |  |       /  /\  \    |  _____|   /  /\  \ 
|  |____    _____\ \  |  |___   /  /__\  \   |  |       /  /__\  \ 
|_______|  \_______/  |______| /__________\  |__|      /__________\ 
 ________    __
/  ______\  |  |
 \ \        |  |
    \ \     |  |
 ______\ \  |  |
\________/  |__|
 _______    __     __    _______   ______     _______   _______
|   _   |  |  |   |  |  |   ____| |      \   |   ____| /  _____\ 
|   |   |  |  |   |  |  |  |____  |   |   |  |  |____  \ \ 
|  _____|  |  |   |  |  |   ____| |   |   |  |   ____|    \ \  
|  |       |  |___|  |  |  |____  |   |   |  |  |____   _____\ \ 
|__|       |_________|  |_______| |______/   |_______| \_______/
''')
	global opcmenu
	print("\t1. Jugar")
	print("\t2. Salir")
	opcMenu = input("\nBienvenido. Elige una opción: ")

	
	if opcMenu=="1":	
		juego()
	elif opcMenu=="2":
		input("Hasta luego")
		exit()
	else:
		input("Opción no válida")
		menu()


def juego():
	os.system("cls")
	print("\n""Eres el Soldado Johnston y te despertaste en una\n"
      "celda desconocida, tambien te das cuenta que al lado tuyo en una\n"
      "celda contigua esta tu camarada el teniente segundo Rusel,\n"
      "intentas divisar que se encuentra a tu alrededor,\n"
      "vez una celda de barrotes de metal que te rodea y un solo baño\n""\n")
	  
	print("\t1. Mirar por la ventana")
	print("\t2. Tratar de forzar la puerta para ver si se puede abrir\n\n")
	opcion1 = input("Elige una opción: ")

	if opcion1=="1":
		mirarVentana()
	elif opcion1=="2":
		puerta()
	else:
		input("Opción no válida")
		juego()


def mirarVentana():
	os.system("cls")
	print("\nMiras por la ventana y ves a un montón de soldados durmiendo en unas sillas, en un patio bastante grande. Todos tienen algún tipo de arma. No parecen muy amigables.\n")
	print("\t1. Llamarles la atención para preguntarles dónde estás")
	print("\t2. Callarte para que no se despierten\n\n")
	opcion2 = input("Elige una opción: ")

	if opcion2=="1":
		muerte1()
	elif opcion2=="2":
		input("Permaneces callado")
		juego()
	else:
		input("Opción no válida")
		mirarVentana()


def puerta():
	os.system("cls")
	print("\nLogras abrir la puerta forzandola y te encuentras en un pasillo alargado. Hay dos puertas; una al final del pasillo, al norte, y otra al principio, al sur. En medio del pasillo hay un cartel que señala con una flecha hacia el norte.\n")
	print("\t1. Atravesar la puerta norte")
	print("\t2. Atravesar la puerta sur\n\n")
	opcion3 = input("Elige una opción: ")

	if opcion3=="1":
		muerte2()
	elif opcion3=="2":
		ganar()
	else:
		input("Opción no válida")
		puerta()


def muerte1():
	os.system("cls")
	print("\nLos soldados se despiertan sobresaltados, y al verte, empiezan a gritar en una lengua extraña. Uno de ellos coge un rifle y te dispara.\n")
	fin()


def muerte2():
	os.system("cls")
	print("\nAtraviesas la puerta y te encuentras en un patio lleno de guardias dormidos, que se despiertan y empiezan a gritar en una lengua extraña. Uno de ellos agarra un rifle y te dispara.\n")
	fin()


def ganar():
	os.system("cls")
	print("\nAtraviesas la puerta y te encuentras con un túnel en el que decides meterte. Tras andar durante 15 minutos, empiezas a ver luz al final del túnel. Al salir, te das cuenta de que estás fuera de la torre.\n\n")
	print("¡HAS GANADO!\n")
	fin()


def fin():
	print('''
 ____   _____   _    _
|  __| |__ __| | \  | |
| |__    | |   |  \ | |
|  __|   | |   | |\`  |
| |     _| |_  | | \  |
|_|    |_____| |_|  \_|
		''')
	input("Pulsa [ENTER] para volver al menu")
	menu()


menu()