from prettytable import PrettyTable

peliculas = [
    {
        "nombre": "Joker: Folie à Deux",
        "descripcion": "Secuela de Joker (2019), de nuevo con Phoenix como Arthur Fleck, y que muestra su relación con el personaje de Harley Quinn, interpretado por Lady Gaga.",
        "estreno": "03-Oct-2024",
        "genero": ["Drama", "Secuela", "Thriller"],
        "clasificación": "Exclusiva para Mayores de 15 años",
        "duracion": 138,
        "director": ["Todd Phillips"],
        "actores": ["Joaquin Phoenix", "Lady Gaga", "Brendan Gleeson"]
    },
    {
        "nombre": "Dune",
        "descripcion": "Adaptación de la novela de ciencia ficción de Frank Herbert, que narra la lucha por el control del planeta desértico Arrakis.",
        "estreno": "22-Oct-2021",
        "genero": ["Ciencia Ficción", "Aventura"],
        "clasificación": "PG-13",
        "duracion": 155,
        "director": ["Denis Villeneuve"],
        "actores": ["Timothée Chalamet", "Rebecca Ferguson", "Oscar Isaac"]
    },
    {
        "nombre": "Spider-Man: No Way Home",
        "descripcion": "Peter Parker busca ayuda para restaurar su identidad secreta, lo que desata un caos multiversal.",
        "estreno": "17-Dic-2021",
        "genero": ["Acción", "Aventura", "Fantástico"],
        "clasificación": "PG-13",
        "duracion": 148,
        "director": ["Jon Watts"],
        "actores": ["Tom Holland", "Zendaya", "Benedict Cumberbatch"]
    },
    {
        "nombre": "La Ballena",
        "descripcion": "Un hombre en crisis intenta reconectar con su hija mientras lidia con su obesidad extrema.",
        "estreno": "09-Dic-2022",
        "genero": ["Drama"],
        "clasificación": "R",
        "duracion": 117,
        "director": ["Darren Aronofsky"],
        "actores": ["Brendan Fraser", "Sadie Sink", "Hong Chau"]
    },
    {
        "nombre": "Top Gun: Maverick",
        "descripcion": "Después de más de 30 años de servicio como uno de los mejores pilotos de la Armada, Pete 'Maverick' Mitchell se enfrenta a nuevas pruebas.",
        "estreno": "27-May-2022",
        "genero": ["Acción", "Drama"],
        "clasificación": "PG-13",
        "duracion": 131,
        "director": ["Joseph Kosinski"],
        "actores": ["Tom Cruise", "Miles Teller", "Jennifer Connelly"]
    },
    {
        "nombre": "Black Panther: Wakanda Forever",
        "descripcion": "Los habitantes de Wakanda luchan por proteger su nación tras la muerte del Rey T'Challa.",
        "estreno": "11-Nov-2022",
        "genero": ["Acción", "Aventura", "Superhéroes"],
        "clasificación": "PG-13",
        "duracion": 161,
        "director": ["Ryan Coogler"],
        "actores": ["Letitia Wright", "Angela Bassett", "Lupita Nyong'o"]
    }
]


def mostrar_todas_peliculas(peliculas):
    for pelicula in peliculas:
        tabla = PrettyTable()
        tabla.field_names = ["Atributo", "Valor"]
        
        tabla.add_row(["Nombre", pelicula['nombre']])
        #tabla.add_row(["Descripción", pelicula['descripcion']])
        tabla.add_row(["Estreno", pelicula['estreno']])
        tabla.add_row(["Género", ', '.join(pelicula['genero'])])
        tabla.add_row(["Clasificación", pelicula['clasificación']])
        tabla.add_row(["Duración (min)", pelicula['duracion']])
        tabla.add_row(["Director", ', '.join(pelicula['director'])])
        tabla.add_row(["Actores", ', '.join(pelicula['actores'])])
        
        print(tabla)
        print("\n" + "-"*40 + "\n")  # Separador entre tablas

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
    """
    Permite crear una nueva película en la lista de películas.
    
    Solicita al usuario los datos de la película a crear, y los agrega a la lista.
    
    Si hay un error en la entrada de datos, muestra un mensaje de error.
    """
    print("Crear pelicula")
    
    # Solicitar los datos de la película
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
    
def buscar_por_id(id_buscar, peliculas):
    try:
        pelicula = peliculas[id_buscar]
        tabla = PrettyTable()
        tabla.field_names = ["Atributo", "Valor"]

        tabla.add_row(["Nombre", pelicula['nombre']])
        #tabla.add_row(["Descripción", pelicula['descripcion']])
        tabla.add_row(["Estreno", pelicula['estreno']])
        tabla.add_row(["Género", ', '.join(pelicula['genero'])])
        tabla.add_row(["Clasificación", pelicula['clasificación']])
        tabla.add_row(["Duración (min)", pelicula['duracion']])
        tabla.add_row(["Director", ', '.join(pelicula['director'])])
        tabla.add_row(["Actores", ', '.join(pelicula['actores'])])

        print(tabla)
    except IndexError:
        print("No se encontró la película con el índice proporcionado.")
    except Exception as e:
        print(f"Error al buscar la película: {e}")



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