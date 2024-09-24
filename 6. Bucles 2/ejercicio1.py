'''Programa que adivinar la palabra'''

palabraAdivinar = "HolaProgramadores"

intentos_max = 4

intento = 0

while intentos_max != intento:
    
    print("*********** Juego Adivinar ***************")
    print(f"Tienes {intentos_max} intentos te quedan {intentos_max - intento}")
    
    intentoAdivinar = input(f"Ingresa la palabra: ")
    
    if intentoAdivinar == palabraAdivinar:
        print("Ganaste...")
        break
    elif intentoAdivinar < palabraAdivinar:
        print("Fallaste... Intenta de nuevo")
        intento = intento+1
    else:
        print(f"Perdiste la palabra era: {palabraAdivinar}")