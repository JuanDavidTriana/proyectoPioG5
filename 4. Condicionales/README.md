# Condicionales, Operadores Lógicos y Operadores Relacionales en Python

Los **condicionales** en Python permiten ejecutar diferentes bloques de código según si una condición es verdadera o falsa. Los **operadores lógicos** se utilizan para combinar condiciones, mientras que los **operadores relacionales** permiten comparar valores. A continuación, se describen estos conceptos.

## 1. Estructura Básica de un Condicional

La estructura básica de un condicional en Python se realiza utilizando la palabra clave `if`, seguida de una condición y un bloque de código que se ejecuta si la condición es verdadera.

### Ejemplo
```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad.")
```

## 2. Condicionales `else`

El bloque `else` se utiliza para ejecutar un bloque de código alternativo cuando la condición del `if` es falsa.

### Ejemplo
```python
edad = 16

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

## 3. Condicionales `elif`

La palabra clave `elif` (que significa "else if") permite comprobar múltiples condiciones. Si la condición del `if` es falsa, se evalúan las condiciones en los bloques `elif`.

### Ejemplo
```python
edad = 20

if edad < 13:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
else:
    print("Eres un adulto.")
```

## 4. Operadores Relacionales

Los operadores relacionales se utilizan para comparar dos valores y devuelven un valor booleano (`True` o `False`). Aquí están los operadores relacionales más comunes:

| Operador | Descripción                  | Ejemplo          |
|----------|------------------------------|------------------|
| `==`     | Igual a                      | `a == b`         |
| `!=`     | Diferente de                 | `a != b`         |
| `>`      | Mayor que                    | `a > b`          |
| `<`      | Menor que                    | `a < b`          |
| `>=`     | Mayor o igual que            | `a >= b`         |
| `<=`     | Menor o igual que            | `a <= b`         |

### Ejemplo de Uso de Operadores Relacionales
```python
a = 10
b = 20

if a < b:
    print("a es menor que b.")
```

## 5. Operadores Lógicos

Los operadores lógicos permiten combinar varias condiciones en una sola expresión.

### 5.1 Operador `and`

El operador `and` devuelve `True` si ambas condiciones son verdaderas.

### Ejemplo con `and`
```python
edad = 25
licencia = True

if edad >= 18 and licencia:
    print("Puedes conducir.")
else:
    print("No puedes conducir.")
```

### 5.2 Operador `or`

El operador `or` devuelve `True` si al menos una de las condiciones es verdadera.

### Ejemplo con `or`
```python
dia = "domingo"

if dia == "sábado" or dia == "domingo":
    print("Es fin de semana.")
else:
    print("Es un día laboral.")
```

### 5.3 Operador `not`

El operador `not` invierte el valor de la condición; es decir, devuelve `True` si la condición es falsa y viceversa.

### Ejemplo con `not`
```python
es_noche = False

if not es_noche:
    print("Es de día.")
else:
    print("Es de noche.")
```

## 6. Condiciones Múltiples

Puedes combinar varios operadores lógicos y relacionales para crear condiciones más complejas.

### Ejemplo con Condiciones Combinadas
```python
edad = 22
licencia = True
estudiante = True

if (edad >= 18 and licencia) or estudiante:
    print("Tienes acceso a la tarifa reducida.")
else:
    print("No tienes acceso a la tarifa reducida.")
```

## 7. Anidación de Condicionales

Los condicionales pueden anidarse, lo que significa que puedes colocar un `if` dentro de otro `if`.

### Ejemplo
```python
edad = 20
socio = True

if edad >= 18:
    if socio:
        print("Tienes un descuento.")
    else:
        print("No tienes descuento.")
else:
    print("Eres menor de edad.")
```

## Resumen

- Los **condicionales** permiten el control del flujo de ejecución en un programa.
- Los **operadores relacionales** se utilizan para comparar valores y determinan si una expresión es verdadera o falsa.
- Los **operadores lógicos** (`and`, `or`, `not`) permiten evaluar múltiples condiciones.
- Puedes combinar y anidar condiciones para lógica más compleja.

Los condicionales, operadores lógicos y relacionales son componentes fundamentales en la programación, permitiendo que tu código tome decisiones basadas en diferentes condiciones.
