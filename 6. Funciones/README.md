# ¿Qué es una Función en Python?

Una **función** es un bloque de código reutilizable que realiza una tarea específica. Las funciones permiten dividir problemas complejos en partes más pequeñas y manejables, promoviendo la modularidad y la reutilización de código.

## Estructura de una Función

Una función en Python sigue esta estructura general:

```python
def nombre_de_funcion(parametros):
    """
    Descripción de la función (opcional).
    """
    # Cuerpo de la función: código que se ejecuta.
    return resultado  # Opcional: devuelve un valor.
```

### Elementos de la Estructura

- `def`: Palabra clave para definir una función.
- `nombre_de_funcion`: El nombre que le asignas a la función.
- `parametros`: (Opcional) Valores que se pasan a la función para ser procesados.
- `return`: (Opcional) Especifica el valor que devuelve la función.

## Ejemplo: Una Función Simple

Veamos un ejemplo básico de una función:

```python
def saludar(nombre):
    return f"¡Hola, {nombre}!"
```

### Llamada a la Función:

```python
print(saludar("Carlos"))  # Salida: ¡Hola, Carlos!
```

## Tipos de Funciones

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

## Funciones Anidadas

Las **funciones anidadas** son funciones definidas dentro de otras funciones. Esto permite encapsular la lógica que solo tiene sentido dentro del contexto de la función externa.

### Ejemplo de Función Anidada

```python
def calcular_area(base, altura):
    def area():
        return base * altura / 2  # Cálculo del área de un triángulo
    
    return area()  # Llamar a la función anidada

# Uso de la función anidada
print(calcular_area(5, 10))  # Salida: 25.0
```

En este ejemplo:
- `calcular_area` es la función externa que recibe `base` y `altura`.
- `area` es la función anidada que calcula y devuelve el área del triángulo.
- La función externa llama a la función anidada y devuelve su resultado.

## Beneficios de Usar Funciones

- **Modularidad**: El código se organiza en partes más pequeñas, facilitando su comprensión.
- **Reutilización**: Puedes reutilizar una función varias veces sin duplicar el código.
- **Mantenimiento**: Si necesitas cambiar la funcionalidad, solo tienes que modificar la función, lo que afecta a todas las llamadas a la misma.
- **Encapsulamiento**: Las funciones anidadas permiten mantener ciertas lógicas encapsuladas y accesibles solo dentro de su contexto, evitando el desorden en el espacio de nombres global.

## Resumen

Las funciones son una parte fundamental de la programación en Python. Facilitan la organización del código, promueven la reutilización y ayudan en el mantenimiento a largo plazo de los programas. Con el uso de funciones anidadas, puedes crear soluciones más sofisticadas y modularizadas.
