# Variables Básicas y Entrada de Datos en Python

## Variables en Python
Una variable en Python es un espacio de almacenamiento para datos que pueden cambiar durante la ejecución de un programa. Las variables no necesitan ser declaradas con un tipo específico, ya que Python es un lenguaje de tipado dinámico. Los tipos de datos más comunes que se utilizan para las variables incluyen:

- **int**: Números enteros
- **float**: Números con decimales
- **str**: Cadenas de texto
- **bool**: Booleanos (True o False)

### Declaración de Variables
No es necesario especificar el tipo de variable, Python lo detecta automáticamente basándose en el valor que se le asigna.

    # Ejemplo de variables
    edad = 25           # Variable tipo entero (int)
    altura = 1.75       # Variable tipo flotante (float)
    nombre = "Carlos"   # Variable tipo cadena de texto (str)
    es_estudiante = True  # Variable tipo booleano (bool)

### Reasignación de Variables
Las variables pueden ser reasignadas con nuevos valores en cualquier momento. El tipo de la variable también puede cambiar con una nueva asignación.

    # Reasignación de variables
    edad = 30           # edad ahora es 30
    nombre = "Ana"      # nombre ahora es "Ana"
    altura = "1.75"     # altura ahora es una cadena de texto

### Reglas para Nombres de Variables
- Deben comenzar con una letra (a-z, A-Z) o un guion bajo (_)
- No pueden comenzar con un número
- Solo pueden contener caracteres alfanuméricos y guiones bajos
- Python es sensible a mayúsculas y minúsculas, por lo tanto, `edad` y `Edad` son variables diferentes.

    # Nombres de variables válidos
    nombre_completo = "Pedro López"
    Edad = 20
    _es_casado = False

    # Nombres de variables no válidos
    # 2nombre = "María"  # No puede comenzar con un número
    # nombre-apellido = "Luis Pérez"  # No se permiten guiones

## Entrada de Datos
En Python, podemos solicitar al usuario que ingrese datos utilizando la función `input()`. Esta función siempre devuelve los datos como una cadena de texto (str), por lo que si necesitamos otro tipo de dato, como un número, debemos convertirlo utilizando las funciones `int()`, `float()`, etc.

### Ejemplo de uso de `input()`

    # Solicitando una cadena de texto al usuario
    nombre = input("Introduce tu nombre: ")
    print("Hola, " + nombre + "!")

    # Solicitando un número entero al usuario
    edad = input("Introduce tu edad: ")  # Esto devuelve una cadena de texto
    edad = int(edad)  # Convertimos la cadena a un entero
    print("Tienes", edad, "años.")

    # Solicitando un número flotante al usuario
    altura = float(input("Introduce tu altura en metros: "))
    print("Tu altura es:", altura, "metros.")

### Entrada y Salida de Datos en un Solo Paso

    # Pedir y convertir a entero en una sola línea
    edad = int(input("Introduce tu edad: "))
    altura = float(input("Introduce tu altura en metros: "))

    # Mostrando los datos ingresados
    print("Tienes", edad, "años y mides", altura, "metros.")

## Conclusión
En Python, las variables son flexibles y no requieren declaración explícita de tipo. La entrada de datos siempre se recibe como texto, y es posible convertir ese texto a otros tipos de datos según lo necesitemos. La interacción con el usuario a través de `input()` es muy sencilla y se puede integrar fácilmente en cualquier programa.
