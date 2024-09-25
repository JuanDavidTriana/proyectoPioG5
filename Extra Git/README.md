# Git y GitHub: Introducción y Herramientas

## ¿Qué es Git?

**Git** es un sistema de control de versiones distribuido que permite a los desarrolladores llevar un seguimiento de los cambios en el código fuente a lo largo del tiempo. Facilita la colaboración entre múltiples desarrolladores y permite mantener un historial detallado de todas las modificaciones realizadas en un proyecto.

### Características Clave de Git:

- **Control de Versiones**: Permite volver a versiones anteriores del proyecto.
- **Colaboración**: Facilita el trabajo en equipo mediante ramas y fusiones.
- **Ramas**: Posibilidad de crear ramas para desarrollar nuevas características sin afectar la versión principal.
- **Desempeño**: Git es eficiente y rápido, incluso en proyectos grandes.

## ¿Qué es GitHub?

**GitHub** es una plataforma basada en la web que utiliza Git para el control de versiones. Proporciona una interfaz gráfica para gestionar repositorios de Git, facilitando la colaboración entre desarrolladores.

### Características de GitHub:

- **Almacenamiento en la Nube**: Almacena repositorios en línea, accesibles desde cualquier lugar.
- **Colaboración**: Permite a múltiples usuarios trabajar en el mismo proyecto y realizar contribuciones a través de "pull requests".
- **Integraciones**: Ofrece herramientas y aplicaciones para integrarse con otros servicios, como CI/CD.
- **Gestión de Proyectos**: Herramientas para gestionar tareas y seguimiento de problemas (issues).

## Herramientas para Usar GitHub

### 1. Visual Studio Code (VS Code)

**Visual Studio Code** es un editor de código fuente ligero y potente que admite extensiones para mejorar la funcionalidad, incluido el soporte para Git.

#### Características de VS Code:

- **Integración de Git**: Permite realizar operaciones de Git directamente desde el editor (commits, merges, branches).
- **Extensiones**: Hay múltiples extensiones disponibles para personalizar tu entorno de desarrollo.
- **Terminal Integrado**: Puedes ejecutar comandos de Git en la terminal integrada sin salir del editor.
  
#### Ejemplo de Uso de Git en VS Code:

1. Abre el terminal integrado (`` Ctrl + ` ``).
2. Clona un repositorio:
   ```bash
   git clone https://github.com/usuario/repo.git
   ```
3. Realiza cambios en tu código y guarda los archivos.
4. Realiza un commit:
   ```bash
   git add .
   git commit -m "Descripción del cambio"
   ```
5. Envía los cambios al repositorio remoto:
   ```bash
   git push origin main
   ```

### 2. GitHub Desktop

**GitHub Desktop** es una aplicación de escritorio que facilita la gestión de repositorios de GitHub sin necesidad de utilizar la línea de comandos.

#### Características de GitHub Desktop:

- **Interfaz Gráfica**: Proporciona una interfaz intuitiva para gestionar tus repositorios.
- **Sincronización**: Facilita la sincronización entre tu repositorio local y el remoto.
- **Gestión de Pull Requests**: Puedes ver y gestionar pull requests directamente desde la aplicación.

#### Ejemplo de Uso de GitHub Desktop:

1. Descarga e instala GitHub Desktop desde [su sitio oficial](https://desktop.github.com/).
2. Inicia sesión con tu cuenta de GitHub.
3. Clona un repositorio existente o crea uno nuevo.
4. Realiza cambios en tu código.
5. Usa el panel de cambios para añadir y confirmar tus modificaciones.
6. Sincroniza tus cambios con el repositorio remoto haciendo clic en "Push origin".

## Resumen

Git y GitHub son herramientas esenciales para el desarrollo moderno. Git permite el control de versiones, mientras que GitHub proporciona una plataforma para colaborar y gestionar proyectos. Con herramientas como Visual Studio Code y GitHub Desktop, trabajar con Git se vuelve más accesible y eficiente, permitiendo a los desarrolladores enfocarse en crear código de calidad.


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
