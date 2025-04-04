Grados = """BIENVENIDOS A LA CALCULADORA DE GRADOS. 
-Celsius.
-Fahrenheit.
-Kelvin.\n """
print(Grados)
while True:
    eleccion = int(input("""Elige la combersion.
    1- Celsius.
    2- Fahrenheit.
    3- Kelvin
    4- Salir.
    -->"""))

    opciones = """1- Celsius.\n 2- Fahrenheit.\n 3- Kelvin:\n """

    if eleccion == 1:
        celsius = float(input("Indique la cantidad de grados celsius:\n"))
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15

        print(f"Los grados celsius ingresados son: {celsius}")
        print(f"La combersion de grados celsius a fahrenheit: {fahrenheit}")
        print(f"La combersion de grados celsius a Kelvin: {kelvin}")

    elif eleccion == 2:
        fahrenheit2 = float(input("Ingresa la cantisdad de grados fahrenheit: \n"))
        celsius2 = (fahrenheit2 - 32) // 1.8
        f_c = (fahrenheit2 - 32) // 1.8
        kelvin2 = f_c + 273
    
        print(f"los grados fahrenheit ingresados: {fahrenheit2}")
        print(f"De fahrenheit a celsius: {celsius2}")
        print(f"De fahrenheit a kelvin: {kelvin2}")

    elif eleccion == 3:
        kelvin3 = float(input("Indique la cnatidad de grados kelvin: \n"))

        celsius3 = kelvin3 - 273
        f_k= kelvin3 - 273
        fahrenheit3 = (f_k * 9/5) + 32
        print(f"Los grados Kelvin igresados: {kelvin3}")
        print(f"De kelvin a celsius: {celsius3}")
        print(f"De kelvin a fahrenheit: {fahrenheit3}")

    elif eleccion == 4:
        print("Gracias por usar la calculadora de grados.")
        break
    else:
        print(f"Por favor ingrese una de estas opciones: \n {opciones}")
        break