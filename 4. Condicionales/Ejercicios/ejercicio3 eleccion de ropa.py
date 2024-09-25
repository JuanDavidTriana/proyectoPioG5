temperatura = float(input("Ingrese la temperatura actual: "))
llueve = input("¿Esta llovienod ? (Si/No)").lower()

if temperatura < 15:
    if llueve == 'SI':
        print("Usa un abrigo y paraguas")
    else:
        print("Usa un abrigo")
elif 15 <= temperatura <= 25:
    if llueve == 'SI':
        print("lleva un paraguas")
    else:
        print("usa ropa ligera")
else:
    print("usa ropa fresca")