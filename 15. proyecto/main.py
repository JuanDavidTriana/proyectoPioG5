directores = [
{
    "nombre": 'Quentin Tarantino',
    "edad": 58,
    "genero": 'Masculino',
},
{
    "nombre": 'James Cameron',
    "edad": 58,
    "genero": 'Masculino',
},
{
    "nombre": 'Steven Spielberg',
    "edad": 58,
    "genero": 'Masculino',
}]

peliculas = [
    {
    "nombre": 'Pulp Fiction',
    "director": 0,
    "duracion": 154,
    "genero": ['Crimen', 'Drama'],
    "clasificación": "B15"
    },
    {
    "nombre": 'Avatar',
    "director": 1,
    "duracion": 162,
    "genero": ['Accion', 'Aventura', 'Fantastico'],
    "clasificación": "PG13"
    },
    {
    "nombre": 'El Padrón',
    "director": 2,
    "duracion": 116,
    "genero": ['Comedia', 'Drama', 'Fantastico'],
    "clasificación": "B15"
    }
]

roles = [
    {
        "username": "admin",    
        "password": "admin123",
        "permisos": True
    },
    {
        "username": "user",
        "password": "user123",    
        "permisos": False,
        "reservas": []
    }
]   

salas = [
    {
        "nombre": "Sala 1",
        "pelicula": 0,
        "capacidad": 100
    },
    {
        "nombre": "Sala 2",
        "pelicula": 1,
        "capacidad": 200,
    }
]

reservas =[]

def mostrar_todas_peliculas(peliculas):
    print("----- Lista de Peliculas -----")
    for pelicula in peliculas:
        print(f"Nombre: {pelicula['nombre']}")
        print(f"Director: {directores[pelicula['director']]['nombre']}")
        print(f"Duración: {pelicula['duracion']} minutos")
        print(f"Género: {', '.join(pelicula['genero'])}")
        print(f"Clasificación: {pelicula['clasificación']}")
        print("------------------------------")


def crear_pelicula():
    print("----- Lista de Directores -----")
    for i, director in enumerate(directores):
        print(f"{i+1}. {director['nombre']}")
    director = int(input("Ingrese el director de la pelicula: ")) - 1
    nombre = input("Ingrese el nombre de la pelicula: ")
    duracion = int(input("Ingrese la duracion de la pelicula: "))
    genero = input("Ingrese el genero de la pelicula(separado por comas): ").split(',')
    clasificacion = input("Ingrese la clasificacion de la pelicula: ")
    peliculas.append({
        "nombre": nombre,
        "director": director,
        "duracion": duracion,
        "genero": genero,
        "clasificación": clasificacion
    })

def mostar_una_pelicula():
    print("----- Lista de Peliculas -----")
    for i, pelicula in enumerate(peliculas):
        print(f"{i+1}. {pelicula['nombre']}")
    indice = int(input("Ingrese el indice de la pelicula: ")) - 1
    print(f"Nombre: {peliculas[indice]['nombre']}")
    print(f"Director: {directores[peliculas[indice]['director']]['nombre']}")
    print(f"Duración: {peliculas[indice]['duracion']} minutos")
    print(f"Género: {', '.join(peliculas[indice]['genero'])}")
    print(f"Clasificación: {peliculas[indice]['clasificación']}")
    print("------------------------------")

def mostar_todos_directores():
    print("----- Lista de Directores -----")
    for director in directores:
        print(f"Nombre: {director['nombre']}")
        print(f"Edad: {director['edad']}")
        print(f"Genero: {director['genero']}")
        print("------------------------------")

def crear_director(): 
    nombre = input("Ingrese el nombre del director: ")
    edad = int(input("Ingrese la edad del director: "))
    genero = input("Ingrese el genero del director: ")
    directores.append({
        "nombre": nombre,
        "edad": edad,
        "genero": genero
    })

def mostar_un_director():
    print("----- Lista de Directores -----")
    for i, director in enumerate(directores):
        print(f"{i+1}. {director['nombre']}")
    indice = int(input("Ingrese el indice del director: ")) - 1
    print(f"Nombre: {directores[indice]['nombre']}")
    print(f"Edad: {directores[indice]['edad']}")
    print(f"Genero: {directores[indice]['genero']}")
    print("------------------------------")
    
def login(username, password):
    for role in roles:
        if role['username'] == username and role['password'] == password:
            return role

def comprar_ticket(persona, sala, pelicula):
    print("----- Compra de tickets -----")
    print(f"Sala: {salas[sala]['nombre']}")
    print(f"Pelicula: {peliculas[pelicula]['nombre']}")
    print("------------------------------")
    if salas[sala]['capacidad'] > 0:
        salas[sala]['capacidad'] -= 1
        reservas.append({
            "sala": sala,
            "pelicula": pelicula
        })
        persona['reservas'].append({
            "sala": sala,
            "pelicula": pelicula
        })
        print("Ticket comprado con éxito")
    else:
        print("No hay capacidad en la sala")


def menu():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    role = login(username, password)
    if role:
        print("¡Inicio de sesión exitoso!")
        
        if role['permisos']:
            while True:
                print("\n----- Menú Administrador -----")
                print("1. Mostrar todas las películas")
                print("2. Crear una nueva película")
                print("3. Mostrar todos los directores")
                print("4. Crear un nuevo director")
                print("5. Mostrar un director")
                print("6. Salir")
                
                opcion = input("Seleccione una opción: ")

                if opcion == '1':
                    mostrar_todas_peliculas(peliculas)
                elif opcion == '2':
                    crear_pelicula()
                elif opcion == '3':
                    mostar_todos_directores()
                elif opcion == '4':
                    crear_director()
                elif opcion == '5':
                    mostar_un_director()
                elif opcion == '6':
                    print("Saliendo del menú administrador...")
                    break
                else:
                    print("Opción inválida. Por favor, intente de nuevo.")
        elif not role['permisos']:
            while True:
                print("\n----- Menú -----")
                print("1. Mostrar todas las películas")
                print("2. Mostrar todos los directores")
                print("3. Salir")
                
                opcion = input("Seleccione una opción: ")

                if opcion == '1':
                    mostrar_todas_peliculas(peliculas)
                elif opcion == '2':
                    mostar_todos_directores()
                elif opcion == '3':
                    print("Saliendo del menú...")
                    break
                else:
                    print("Opción inválida. Por favor, intente de nuevo.")
            
        
        print(f"Permisos de administrador: {role['permisos']}")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

menu()