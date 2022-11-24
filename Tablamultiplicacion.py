print("Bienvenido a nuestro juego🎉")
print("El juego se trata, de que aprendas las tablas de multiplicar de los numeros que deseas")
num=int(input("Ingrese un numero para saber su tabla\n"))
cantmultiplos=int(input("Hasta que numero lo desea multiplicar?"))
respuesta=""
cantmultiplos+=1
tabla=[0]*cantmultiplos
for i in range(1,cantmultiplos):
    total=num*i
    tabla[i]=num*i
    print(str(num)+"x"+str(i)+"="+str(total))
print(tabla)
respuesta=str(input("(si),para continuar🤯 \n"))
while respuesta=="si":
    if respuesta.lower()=="si":
        num=int(input("Ingrese un numero para saber su tabla\n"))
        cantmultiplos=int(input("Hasta que numero lo desea multiplicar?"))
        for i in range(1,cantmultiplos+1):
            total=num*i
            print(str(num)+"x"+str(i)+"="+str(total))
    print(tabla)
    respuesta=str(input("Desea Continuar?\n"))
else:
        print("Finalizo 👌")