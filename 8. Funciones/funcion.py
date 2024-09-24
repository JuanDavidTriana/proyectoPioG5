def saludar(nombre): #Con retorno 
    mensaje = f"Hola, {nombre}"
    return mensaje

saludo = saludar("Juan")

def despedir(nombre): #Sin retorno
    print(f"Adios, {nombre}")
    
despedida = despedir("Juan")

despedida