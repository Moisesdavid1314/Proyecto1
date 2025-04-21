print("Nuevo ejercicio.")

nombre = input("Coloca tu nombre: \n")
nombre2 = input("Coloca tu segundo nombre: \n")
apellido = input("Coloca tu apellido: \n")
apellido2 = input("Coloca tu segundo apellido: \n")

primer_nombre = nombre.strip().capitalize()
primer_apellido = apellido.strip().capitalize()
segundo_nombre = nombre2.strip().capitalize()
segundo_apellido = apellido2.strip().capitalize()

print(f"Tu primer nombre es: {primer_nombre}")
print(f"Tu segundo nombre es: {segundo_nombre}")
print(f"Tu primer apellido es: {primer_apellido}")
print(f"Tu segundo apellido es: {segundo_apellido}")
print(F"Tunombre completo es: {primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido}")
