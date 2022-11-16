print("Bienvenido a nuestro juego🎉")
print("El juego se trata, de que aprendas las tablas de multiplicar de los numeros que deseas")
num=int(input("Ingrese un numero para saber su tabla\n"))
respuesta=""
for i in range(1,11):
    total=num*i
    print(str(num)+"x"+str(i)+"="+str(total))
respuesta=str(input("(si),para continuar🤯 \n"))
while respuesta=="si":
    if respuesta.lower()=="si":
        num=int(input("Ingrese un numero para saber su tabla\n"))
        for i in range(1,11):
            total=num*i
            print(str(num)+"x"+str(i)+"="+str(total))
    respuesta=str(input("Desea Continuar?\n"))
else:
        print("Finalizo 👌")