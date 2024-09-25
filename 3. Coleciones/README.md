# Variables de Colecciones en Python

Las **variables de colección** son contenedores que permiten almacenar múltiples valores en una sola variable. En Python, los tipos más comunes de colecciones son:

## 1. Listas

Las listas son colecciones ordenadas y modificables que pueden contener elementos de diferentes tipos. Se definen utilizando corchetes `[]`.

### Ejemplo de Lista
```python
frutas = ["manzana", "naranja", "plátano"]
```

### Acceso a Elementos
Puedes acceder a los elementos de una lista utilizando índices (comenzando desde 0).
```python
print(frutas[0])  # Salida: manzana
```

### Métodos Comunes de Listas
- **Agregar un elemento**: 
  ```python
  frutas.append("fresa")  # Añade "fresa" al final
  ```

- **Eliminar un elemento**:
  ```python
  frutas.remove("naranja")  # Elimina "naranja"
  ```

- **Ordenar la lista**:
  ```python
  frutas.sort()  # Ordena alfabéticamente
  ```

## 2. Tuplas

Las tuplas son colecciones ordenadas e inmutables. Se definen utilizando paréntesis `()`.

### Ejemplo de Tupla
```python
coordenadas = (10.0, 20.0)
```

### Acceso a Elementos
Puedes acceder a los elementos de una tupla de la misma manera que en las listas.
```python
print(coordenadas[1])  # Salida: 20.0
```

### Métodos Comunes de Tuplas
- **Contar elementos**:
  ```python
  print(coordenadas.count(10.0))  # Salida: 1
  ```

- **Encontrar el índice de un elemento**:
  ```python
  print(coordenadas.index(20.0))  # Salida: 1
  ```

## 3. Conjuntos

Los conjuntos son colecciones desordenadas de elementos únicos. Se definen utilizando llaves `{}` o la función `set()`.

### Ejemplo de Conjunto
```python
numeros = {1, 2, 3, 4, 4}  # El número 4 solo se incluirá una vez
```

### Acceso a Elementos
No se puede acceder a los elementos de un conjunto por índice, ya que son desordenados. En su lugar, puedes verificar si un elemento está en el conjunto.
```python
print(2 in numeros)  # Salida: True
```

### Métodos Comunes de Conjuntos
- **Agregar un elemento**:
  ```python
  numeros.add(5)  # Añade 5 al conjunto
  ```

- **Eliminar un elemento**:
  ```python
  numeros.remove(2)  # Elimina 2 del conjunto
  ```

- **Unir dos conjuntos**:
  ```python
  otro_conjunto = {5, 6, 7}
  union = numeros.union(otro_conjunto)  # Unión de conjuntos
  ```

## 4. Diccionarios

Los diccionarios son colecciones de pares clave-valor. Se definen utilizando llaves `{}` con una sintaxis de `clave: valor`.

### Ejemplo de Diccionario
```python
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
```

### Acceso a Valores
Puedes acceder a los valores utilizando sus claves.
```python
print(persona["nombre"])  # Salida: Juan
```

### Métodos Comunes de Diccionarios
- **Agregar o actualizar un par clave-valor**:
  ```python
  persona["ocupacion"] = "Estudiante"  # Agrega ocupación
  ```

- **Eliminar un par clave-valor**:
  ```python
  del persona["edad"]  # Elimina la edad
  ```

- **Obtener todas las claves**:
  ```python
  claves = persona.keys()  # Obtiene todas las claves
  ```

## Resumen

- Las **listas** son ordenadas y modificables, ideales para almacenar múltiples elementos.
- Las **tuplas** son ordenadas pero inmutables, útiles cuando no se quiere modificar el conjunto de datos.
- Los **conjuntos** son colecciones de elementos únicos y desordenados, ideales para operaciones de conjunto.
- Los **diccionarios** son útiles para almacenar datos en forma de pares clave-valor, permitiendo acceso rápido a los valores.

Las colecciones en Python son herramientas poderosas que permiten manejar datos de manera eficiente y flexible.
