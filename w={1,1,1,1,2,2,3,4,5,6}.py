titulo = print("Bienvenido a la calculadora ¡Mejorada!")

eleccion = input("""
1- Suma
2- Resta
3- Multiplicasion
4- Divicion
5- Elevado
""")
numero_1 = float(input("Ingresa un numero:\n"))
numero_2 = float(input("Ingresa otro numero:\n"))

if eleccion == "1":
    print("Aselegido Suma.")
    print(" ")
    print(f"Resultado: {numero_1+numero_2}")
elif eleccion == "2":
    print("Aselegido Resta.")
    print(" ")
    print(f"Resultado de la rersta: {numero_1-numero_2}")
elif eleccion == "3":
    print("Aselegido Tultiplicacion.")
    print(" ")
    print(f"Resultado de la multiplicacion:{numero_1*numero_2}")
elif eleccion =="4":
    print("Aselegido Divicion.")
    print(" ")
    print(f"Resultado de la divicion:{numero_1/numero_2}")
elif eleccion =="5":
    print("Aselegido Operacion de Desimales.")
    print(" ")
    print(f"Resultado de la operacion con esimales:{numero_1 ** numero_2}")
else:
    print("Noes valido. Por favor ingresa dos numeros nuevamente:")
