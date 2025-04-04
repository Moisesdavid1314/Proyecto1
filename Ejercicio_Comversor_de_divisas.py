print("Bienvenido al conversor de divisas.\n")

while True: 
    try:
        moneda_local = float(input("Ingresa la cantidad en moneda local:\n"))

        usd = moneda_local * 0.050
        eur = moneda_local * 0.047
        gbp = moneda_local * 0.039
        jpy = moneda_local * 7.71

        print(f"""
            Cantidad en dólares: {usd}
            Cantidad en euros: {eur}
            Cantidad en libras esterlinas: {gbp}
            Cantidad en yenes: {jpy}""")
    except:
        print("Entrada inválida. Por favor, ingresa un número.")