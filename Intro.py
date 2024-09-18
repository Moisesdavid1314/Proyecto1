#hay N? si no ingresa el numero calculadora
#Ingrese operacion
#Ingrese otro n
#mostrar resultado y guardar como primer numero
# y con el primero numero hacer la siguiente operacion
#Salir

print("Bienvenidos a la calculadora")
print("Para salir escribe salir")

resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa operacion")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente numero ")
    if n2 == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "mult":
        resultado *= n2
    elif op.lower() == "division":
        resultado /= n2
    else:
        print("Operacion no valida")
        break
    print(f"El resultado es {resultado}")


    
        