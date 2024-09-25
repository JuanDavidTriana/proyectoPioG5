# Bucles en Python

Los **bucles** en Python son estructuras de control que permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición o para cada elemento de una colección. Existen principalmente dos tipos de bucles: `for` y `while`.

## 1. Bucle `for`

El bucle `for` se utiliza para iterar sobre una secuencia (como listas, tuplas, cadenas o rangos) y ejecutar un bloque de código para cada elemento de la secuencia.

### Ejemplo de Bucle `for`
```python
# Iterar sobre una lista de números
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(f"Número: {numero}")
```

### Bucle `for` con `range()`

La función `range()` genera una secuencia de números, que se puede usar en un bucle `for`.

#### Ejemplo de `range()`
```python
# Imprimir números del 0 al 4
for i in range(5):
    print(i)
```

## 2. Bucle `while`

El bucle `while` ejecuta un bloque de código mientras la condición especificada sea verdadera. Es útil cuando no se sabe cuántas veces se debe repetir el bucle.

### Ejemplo de Bucle `while`
```python
# Contador
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementar el contador
```

## 3. Uso de `break` y `continue`

### 3.1 `break`

La declaración `break` se utiliza para salir del bucle antes de que termine todas las iteraciones.

#### Ejemplo de `break`
```python
# Encontrar el primer número par en una lista
numeros = [1, 3, 5, 4, 7, 9]

for numero in numeros:
    if numero % 2 == 0:
        print(f"El primer número par es: {numero}")
        break  # Salir del bucle
```

### 3.2 `continue`

La declaración `continue` se utiliza para saltar a la siguiente iteración del bucle, omitiendo el código que sigue.

#### Ejemplo de `continue`
```python
# Imprimir números del 0 al 9, omitiendo los pares
for i in range(10):
    if i % 2 == 0:
        continue  # Saltar a la siguiente iteración
    print(f"Número impar: {i}")
```

## 4. Anidación de Bucles

Puedes anidar bucles dentro de otros bucles. Esto es útil cuando necesitas realizar operaciones en matrices o estructuras de datos multidimensionales.

### Ejemplo de Bucles Anidados
```python
# Imprimir una tabla de multiplicar
for i in range(1, 4):  # Fila
    for j in range(1, 4):  # Columna
        print(f"{i} * {j} = {i * j}")
```

## 5. Resumen

- Los bucles permiten ejecutar un bloque de código repetidamente.
- El bucle `for` se utiliza para iterar sobre elementos en una secuencia.
- El bucle `while` ejecuta un bloque de código mientras una condición sea verdadera.
- Las declaraciones `break` y `continue` ofrecen control adicional sobre el flujo de los bucles.
- Se pueden anidar bucles para trabajar con estructuras de datos más complejas.

Los bucles son fundamentales en la programación, ya que permiten automatizar tareas repetitivas y manejar grandes conjuntos de datos de manera eficiente.
