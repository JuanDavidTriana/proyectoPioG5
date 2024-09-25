# Introducción a Variables y Entrada de Datos en Python

## Variables en Python

Las **variables** son contenedores para almacenar datos. En Python, no es necesario declarar el tipo de variable antes de usarla; el tipo se determina automáticamente en función del valor que se le asigna. Las variables pueden almacenar diferentes tipos de datos, tales como:

- **Números Enteros (`int`)**: Representan números sin decimales.
  ```python
  edad = 25
  ```

- **Números de Punto Flotante (`float`)**: Representan números con decimales.
  ```python
  temperatura = 36.6
  ```

- **Cadenas de Texto (`str`)**: Representan secuencias de caracteres.
  ```python
  nombre = "Juan"
  ```

- **Booleanos (`bool`)**: Representan valores de verdadero o falso.
  ```python
  es_estudiante = True
  ```

### Nombres de Variables

Las variables deben seguir ciertas reglas al nombrarlas:

- Deben comenzar con una letra o un guion bajo (`_`).
- Pueden contener letras, números y guiones bajos.
- No pueden contener espacios ni caracteres especiales.
- No pueden ser palabras reservadas de Python (como `if`, `while`, `for`, etc.).

Ejemplo de nombres válidos:
```python
nombre_completo = "Juan Pérez"
edad_usuario = 30
```

## Entrada de Datos en Python

Para obtener información del usuario, se utiliza la función `input()`. Esta función permite leer datos de la entrada estándar (teclado). Todo lo que se ingresa a través de `input()` se considera una cadena de texto (`str`). 

### Ejemplo de Uso de `input()`
```python
nombre = input("Por favor, introduce tu nombre: ")
edad = input("Por favor, introduce tu edad: ")
print(f"Hola, {nombre}. Tienes {edad} años.")
```

### Conversión de Tipos

Si necesitas realizar operaciones matemáticas con los datos ingresados, es importante convertir las cadenas a un tipo numérico apropiado. Esto se puede hacer utilizando funciones como `int()` o `float()`.

#### Ejemplo de Conversión
```python
edad = input("Por favor, introduce tu edad: ")
edad = int(edad)  # Convertir a entero
print(f"En 5 años tendrás {edad + 5} años.")
```

### Resumen

- Las **variables** almacenan datos y su tipo se determina automáticamente.
- Utiliza `input()` para recibir datos del usuario, y recuerda convertirlos al tipo adecuado si es necesario.
