num=int(input("Ingrese un numero para saber su tabla\n"))
for i in range(1,11):
    total=num*i
    print(str(num)+"x"+str(i)+"="+str(total))
while True:
    respuesta=str(input("Desea Continuar?\n"))
    if respuesta.lower()=="si":
        num=int(input("Ingrese un numero para saber su tabla\n"))
        for i in range(1,11):
            total=num
            print(str(num)+"x"+str(i)+"="+str(total))
    else:
        print("Finalizo")
        break