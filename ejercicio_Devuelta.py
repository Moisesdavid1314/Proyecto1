hola = "PROGRAMA DE DEVUELTA."

while True:
    
    try:

        dinero = float (input("Ingresa tu dinero:\n"))
        producto = float(input("Costo del producto:\n"))
        

        resta = dinero -producto 
        resta2 = f"Tu devuelta es de: {resta}" if resta >= 0 else "Te fata dinero"
        print(resta2)


        otros = "Tienes mucho dinero." if dinero >= 1000 else "ok esta bien"
        print(otros)
        
        salir = str (input("Deseas salir? si / no \n"))

        g = "Gracias por usar el sistema de devueltas."

        te = f"ok saliste. \n {g}" if salir == "si" else "ok sigamos"

        print(te)
        break
    except:

        print("Uvo un error intentalo de nuevo...")
    