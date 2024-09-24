'''Sistema de Gestión de Estudiantes
Crea un sistema que permita agregar, ver y eliminar estudiantes de una lista. Usa funciones para las operaciones de agregar, mostrar y eliminar estudiantes.
'''
def agregar_estudiante(estudiantes):
    print("------------- Agregar Estudiante -------------")
    documento = input("Ingrese Documento: ")
    tipo_documento = input("Ingrese tipo documento(cc/ti): ").lower()
    nombre = input("Ingrese nombre: ").capitalize()
    apellido = input("Ingrese apellido: ").capitalize()
    
    if documento.isdigit():
        
        if buscar_estudiante(estudiantes,documento): 
            print("Error: Estudiante ya existe")
            return
    
        if tipo_documento in ['cc', 'ti']:
            estudiantes.append({
                "documento": documento,
                "tipo_documento": tipo_documento, 
                "nombre": nombre, 
                "apellido": apellido,
            })

            print("Estudiante agregado con exito")
        else:
            print("Error: tipo de documento no valido")
    else: 
        print("Error: Documento no valido")

def mostar_estudiante(estudiantes):
    print("------------- Lista de Estudiantes -------------")
    if not estudiantes:
        print("No hay estudiantes registrados")
    else: 
        for estudiante in estudiantes:
            print(f"Documento: {estudiante["tipo_documento"]} {estudiante["documento"]} - {estudiante["apellido"]} {estudiante["nombre"]} ")

def eliminar_estudiante(estudiantes):
    print("------------- Eliminar Estudiante -------------")
    documento_al_eliminar = input("Ingrese el documento del estudiante a eliminar: ")
    estudiante_a_eliminar = buscar_estudiante(estudiantes,documento_al_eliminar)
    if estudiante_a_eliminar:
            estudiantes.remove(estudiante_a_eliminar)
            print("Estudiante Eliminado con exito")
    else:
        print("Error: Estudiante no econtrado")

def buscar_estudiante(estudiantes,documento_estudiante_a_buscar):
    for estudiante in estudiantes:
        if documento_estudiante_a_buscar == estudiante["documento"]:
            return estudiante

def mostar_menu():
    print("1. Agregar estudiante")
    print("2. Mostar estudiante")
    print("3. Eliminar estudiante")
    print("4. Salir")

def main():
    estudiantes = []

    #Programa principal
    while True:
        mostar_menu()
        opcion = int(input("Elije una opcion: "))
        
        if opcion == 1:
            agregar_estudiante(estudiantes)
        elif opcion == 2:
            mostar_estudiante(estudiantes)
        elif opcion == 3:
            eliminar_estudiante(estudiantes)
        elif opcion == 4:
            break
        else:
            print("Error: Opcion no valida")
            
if __name__ == "__main__":
    main()