def operaciones(a,b):
    def suma():
        return(a + b)

    def resta():
        return(a - b)
    
    
    #lista_operaciones = [resultado_suma, resultado_resta]
    #Clave/valor
    dic_opciones = { 
        "suma": suma(),
        "resta": resta(),
    }
    
    return dic_opciones
    
password = "pio12345"

passwordopcion = input("Ingrese contraseña: ")
if passwordopcion == password:
    operaciones_dic = operaciones(10,5)
    print(f"Suma: {operaciones_dic["suma"]} y resta: {operaciones_dic["resta"]}")