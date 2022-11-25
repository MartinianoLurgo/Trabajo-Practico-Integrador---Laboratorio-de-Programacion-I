import os
os.system("cls")
puntaje = 0
print("¿Cuanto es (120-34+24)*0?\n->")
pregunta1 = input()
if pregunta1=="0":
	print("Correcto")
	puntaje = puntaje+1
if pregunta1!="0":
	print("Incorrecto")
	puntaje = puntaje-1
print("¿Cual es el valor de la potencia de exponente cero?\n->")
pregunta2 = input()
if pregunta2=="1":
	print("Correcto")
	puntaje = puntaje+1
if pregunta2!="1":
	print("Incorrecto")
	puntaje = puntaje-1
print("Cuanto da el producto de dos razones inversas?\n->")
pregunta3 = input()
if pregunta3=="1":
	print("Correcto")
	puntaje = puntaje+1
if pregunta3!="1":
	print("Incorrecto")
	puntaje = puntaje-1
print("En una divicion si el dividento tiende a 0 y el divisor tiende a infinito,¿como es el cociente?\n->")
pregunta4 = input()
if pregunta4=="0":
	print("Correcto")
	puntaje = puntaje+1
if pregunta4!="0":
	print("Incorrecto")
	puntaje = puntaje-1
print("¿Cual es el unico numero primo par?\n->")
pregunta5 = input()
if pregunta5=="2":
	print("Correcto")
	puntaje = puntaje+1
if pregunta5!="2":
	print("Incorrecto")
	puntaje = puntaje-1
print("¿Cual es el resultado de la siguiente expresion 8-2*2+6*3-3?\n->")
pregunta6 = input()
if pregunta6=="19":
	print("Correcto")
	puntaje = puntaje+1
if pregunta6!="19":
	print("Incorrecto")
	puntaje = puntaje-1
print("¿Cuanto es 2 elevado a la -1?\n->")
pregunta7 = input()
if pregunta7=="1/2":
	print("Correcto")
	puntaje = puntaje+1
if pregunta7!="1/2":
	print("Incorrecto")
	puntaje = puntaje-1
print("¿Cuanto da la tangente de 45?\n->")
pregunta8 = input()
if pregunta8=="1":
	print("Correcto")
	puntaje = puntaje+1
if pregunta8!="1":
	print("Incorrecto")
	puntaje = puntaje-1
print("¿Cuantpo vale el numero PI?\n->")
pregunta9 = input()
if pregunta9=="3,14":
	print("Correcto")
	puntaje = puntaje+1
if pregunta9!="3,14":
	print("Incorrecto")
	puntaje = puntaje-1
print("¿La derivada de X es igual a 1?\n->")
pregunta10 = input()
if pregunta10=="si":
	print("Correcto")
	puntaje = puntaje+1
if pregunta10!="si":
	print("Incorrecto")
	puntaje = puntaje-1
print("Su puntaje es de ",puntaje)

