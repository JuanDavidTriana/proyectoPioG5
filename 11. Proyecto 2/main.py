peliculas = [
    {
    "nombre": "Joker: Folie à Deux",
    "descripcion": "Secuela de Joker (2019), de nuevo con Phoenix como Arthur Fleck, y que muestra su relación con el personaje de Harley Quinn, interpretado por Lady Gaga.",
    "estreno" : "03-Oct-2024",
    "genero": ["Drama", "Secuela", "Thriller"],
    "clasificación":"Exclusiva para Mayores de 15 años",
    "duracion": 138,
    "director": ["Todd Phillips"],
    "actores" : ["Joaquin Phoenix", "Lady Gaga", "Brendan Gleeson"]
    },#Llave 0
]

def mostrar_todas_peliculas(peliculas):
    print("----- Lista de Peliculas -----")
    for pelicula in peliculas:
        print(f"Nombre: {pelicula['nombre']}")
        print(f"Descripción: {pelicula['descripcion']}")
        print(f"Estreno: {pelicula['estreno']}")
        print(f"Género: {', '.join(pelicula['genero'])}")
        print(f"Clasificación: {pelicula['clasificación']}")
        print(f"Duración: {pelicula['duracion']} minutos")
        print(f"Director: {', '.join(pelicula['director'])}")
        print(f"Actores: {', '.join(pelicula['actores'])}")
        print("------------------------------")

def actualizar_una_pelicula(id_actulizar,peliculas):
    for indice, pelicula in enumerate(peliculas):
            if id_actulizar == indice:
                print("Película encontrada")
                try:
                    nombre = input(f"Ingrese nuevo Nombre de la película ({pelicula['nombre']}): ")
                    descripcion = input(f"Ingrese nueva Descripción: ")
                    estreno = input(f"Ingrese nueva Fecha de Estreno: ")
                    genero = input(f"Ingrese nuevo Género (separado por comas): ").split(',')
                    clasificacion = input(f"Ingrese nueva Clasificación: ")
                    duracion = int(input(f"Ingrese nueva Duración (en minutos): "))
                    director = input(f"Ingrese nuevo Director (separado por comas): ").split(',')
                    actores = input(f"Ingrese nuevos Actores (separado por comas): ").split(',')
                    
                    # Actualizar la película
                    pelicula['nombre'] = nombre
                    pelicula['descripcion'] = descripcion
                    pelicula['estreno'] = estreno
                    pelicula['genero'] = [g.strip() for g in genero]
                    pelicula['clasificación'] = clasificacion
                    pelicula['duracion'] = duracion
                    pelicula['director'] = [d.strip() for d in director]
                    pelicula['actores'] = [a.strip() for a in actores]
                    
                    print("Película actualizada exitosamente.")
                    return
                
                except IndexError:
                    print("No se encontró la película con el índice proporcionado.")
                except ValueError:
                    print("Error: La duración debe ser un número entero.")

def crear_una_pelicula(peliculas):
    print("Crear pelicula")
    try:
        nombre = input(f"Ingrese Nombre de la película: ")
        descripcion = input(f"Ingrese nueva Descripción: ")
        estreno = input(f"Ingrese nueva Fecha de Estreno: ")
        genero = input(f"Ingrese nuevo Género (separado por comas): ").split(',')
        clasificacion = input(f"Ingrese nueva Clasificación: ")
        duracion = int(input(f"Ingrese nueva Duración (en minutos): "))
        director = input(f"Ingrese nuevo Director (separado por comas): ").split(',')
        actores = input(f"Ingrese nuevos Actores (separado por comas): ").split(',')
                    
        # Crear la nueva película
        nueva_pelicula = {
            'nombre': nombre,
            'descripcion': descripcion,
            'estreno': estreno,
            'genero': [g.strip() for g in genero],
            'clasificación': clasificacion,
            'duracion': duracion,
            'director': [d.strip() for d in director],
            'actores': [a.strip() for a in actores]
        }
        
        # Agregar la nueva película a la lista
        peliculas.append(nueva_pelicula)
        print("Película agregada exitosamente.")
    except ValueError:
        print("Error: La duración debe ser un número entero.")

def eliminar_pelicula(id_eliminar,peliculas):
    try:
        peliculas.pop(id_eliminar)
        print("Película eliminada exitosamente.")
    except IndexError:
        print("No se encontró la película con el índice proporcionado.")
    
def buscar_por_id(id_buscar,peliculas):
    try: 
        for indice, pelicula in enumerate(peliculas):
            if id_buscar == indice:
                print("Usuario encontrado")
                print(f"Nombre: {pelicula['nombre']}")
                print(f"Descripción: {pelicula['descripcion']}")
                print(f"Estreno: {pelicula['estreno']}")
                print(f"Género: {', '.join(pelicula['genero'])}")
                print(f"Clasificación: {pelicula['clasificación']}")
                print(f"Duración: {pelicula['duracion']} minutos")
                print(f"Director: {', '.join(pelicula['director'])}")
                print(f"Actores: {', '.join(pelicula['actores'])}")
                print("------------------------------")
                return
    except IndexError:
        print("No se encontró la película con el índice proporcionado.")

# Menú principal
while True:
    print("\n----- Menú -----")
    print("1. Mostrar todas las películas")
    print("2. Crear una nueva película")
    print("3. Actualizar una película")
    print("4. Eliminar una película")
    print("5. Buscar una película por ID")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        mostrar_todas_peliculas(peliculas)
    elif opcion == '2':
        crear_una_pelicula(peliculas)
    elif opcion == '3':
        try:
            id_actualizar = int(input("Ingrese el índice de la película a actualizar: "))
            actualizar_una_pelicula(id_actualizar, peliculas)
        except ValueError:
            print("Dato no válido. Ingrese un número entero.")
    elif opcion == '4':
        try:
            id_eliminar = int(input("Ingrese el índice de la película a eliminar: "))
            eliminar_pelicula(id_eliminar, peliculas)
        except ValueError:
            print("Dato no válido. Ingrese un número entero.")
    elif opcion == '5':
        try:
            id_buscar = int(input("Ingrese el índice de la película a buscar: "))
            buscar_por_id(id_buscar, peliculas)
        except ValueError:
            print("Dato no válido. Ingrese un número entero.")
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")