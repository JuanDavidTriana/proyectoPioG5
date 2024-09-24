# Guía de Funciones en Python

Este repositorio contiene ejemplos y explicaciones sobre cómo crear y usar funciones en Python. Las funciones son fundamentales para organizar, reutilizar y mantener el código limpio y eficiente. A continuación, se presenta una guía básica sobre las funciones en Python.

## ¿Qué es una Función en Python?

Una función es un bloque de código reutilizable que realiza una tarea específica. Las funciones permiten dividir problemas complejos en partes más pequeñas y manejables, promoviendo la modularidad y la reutilización de código.

### Estructura de una Función

Una función en Python sigue esta estructura general:

```python
def nombre_de_funcion(parametros):
    """
    Descripción de la función (opcional).
    """
    # Cuerpo de la función: código que se ejecuta.
    return resultado  # Opcional: devuelve un valor.
```

- `def`: Palabra clave para definir una función.
- `nombre_de_funcion`: El nombre que le asignas a la función.
- `parametros`: (Opcional) Valores que se pasan a la función para ser procesados.
- `return`: (Opcional) Especifica el valor que devuelve la función.

### Ejemplo: Una Función Simple

Veamos un ejemplo básico de una función:

```python
def saludar(nombre):
    return f"¡Hola, {nombre}!"
```

En este ejemplo:
- `saludar` es el nombre de la función.
- `nombre` es el parámetro que recibe la función.
- La función devuelve un mensaje que saluda al usuario.

#### Llamada a la Función:

```python
print(saludar("Carlos"))  # Salida: ¡Hola, Carlos!
```

### Tipos de Funciones

1. **Función sin parámetros**: No recibe datos de entrada.

```python
def decir_hola():
    return "¡Hola!"
    
print(decir_hola())  # Salida: ¡Hola!
```

2. **Función con parámetros**: Recibe datos de entrada.

```python
def suma(a, b):
    return a + b
    
print(suma(3, 5))  # Salida: 8
```

3. **Función sin valor de retorno**: No devuelve ningún valor.

```python
def imprimir_suma(a, b):
    print(a + b)
    
imprimir_suma(4, 7)  # Salida: 11
```

### Beneficios de Usar Funciones

- **Modularidad**: El código se organiza en partes más pequeñas, facilitando su comprensión.
- **Reutilización**: Puedes reutilizar una función varias veces sin duplicar el código.
- **Mantenimiento**: Si necesitas cambiar la funcionalidad, solo tienes que modificar la función, lo que afecta a todas las llamadas a la misma.

