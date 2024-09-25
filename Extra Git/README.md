## Guía de Comandos de Git

Aquí tienes una lista de los comandos de Git más utilizados, junto con sus descripciones y ejemplos de uso.

### Configuración Inicial

- **Configurar el nombre de usuario**:
    ```bash
    git config --global user.name "Tu Nombre"
    ```
  
- **Configurar el correo electrónico**:
    ```bash
    git config --global user.email "tu.email@example.com"
    ```

### Crear y Clonar Repositorios

- **Crear un nuevo repositorio**:
    ```bash
    git init nombre_del_repositorio
    ```

- **Clonar un repositorio existente**:
    ```bash
    git clone https://github.com/usuario/repo.git
    ```

### Estado del Repositorio

- **Ver el estado de los cambios**:
    ```bash
    git status
    ```

### Gestionar Cambios

- **Añadir archivos al área de preparación (staging)**:
    ```bash
    git add nombre_del_archivo
    ```
  
- **Añadir todos los archivos**:
    ```bash
    git add .
    ```

- **Hacer un commit (guardar cambios)**:
    ```bash
    git commit -m "Mensaje del commit"
    ```

- **Ver el historial de commits**:
    ```bash
    git log
    ```

### Ramas

- **Crear una nueva rama**:
    ```bash
    git branch nombre_de_la_rama
    ```

- **Cambiar a otra rama**:
    ```bash
    git checkout nombre_de_la_rama
    ```

- **Crear y cambiar a una nueva rama**:
    ```bash
    git checkout -b nombre_de_la_rama
    ```

- **Fusionar una rama**:
    ```bash
    git merge nombre_de_la_rama
    ```

### Sincronización

- **Enviar cambios al repositorio remoto**:
    ```bash
    git push origin nombre_de_la_rama
    ```

- **Actualizar el repositorio local con cambios del remoto**:
    ```bash
    git pull origin nombre_de_la_rama
    ```

### Deshacer Cambios

- **Deshacer cambios no confirmados**:
    ```bash
    git checkout -- nombre_del_archivo
    ```

- **Deshacer el último commit (sin eliminar los cambios)**:
    ```bash
    git reset --soft HEAD~1
    ```

- **Eliminar el último commit (y también los cambios)**:
    ```bash
    git reset --hard HEAD~1
    ```

### Comandos Útiles

- **Ver la configuración actual**:
    ```bash
    git config --list
    ```

- **Ver las diferencias entre commits**:
    ```bash
    git diff
    ```

- **Ver las diferencias entre archivos en el área de preparación y el último commit**:
    ```bash
    git diff --cached
    ```

### Resumen

Esta guía de comandos de Git te proporciona una referencia rápida para las operaciones más comunes. Familiarizarte con estos comandos te ayudará a gestionar tus proyectos de manera más efectiva y colaborativa.
