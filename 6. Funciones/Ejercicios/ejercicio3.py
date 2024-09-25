def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

def estado_del_estudiante(promedio):
    if promedio >= 60:
        return "Aprobado"
    else:
        return "Reprobado"


calificaciones = []
cantidad = int(input("¿Cuántas calificaciones deseas ingresar? "))

for _ in range(cantidad):
    calificacion = float(input("Ingresa la calificación: "))
    calificaciones.append(calificacion)

promedio = calcular_promedio(calificaciones)
estado = estado_del_estudiante(promedio)
print(f"Promedio: {promedio}, Estado: {estado}")
