# Test 1 - Paola Vilaseca 

## Funcionalidades

### Aplicación de Consola:
1. **Agregar tarea**: Permite al usuario agregar nuevas tareas con un estado inicial de "Pendiente".
2. **Eliminar tarea**: Permite al usuario eliminar tareas por ID.
3. **Marcar tarea como completada**: Permite al usuario marcar una tarea como completada por ID.
4. **Listar tareas pendientes**: Muestra al usuario todas las tareas que están pendientes.
5. **Guardar las tareas en un archivo de texto**: Permite al usuario guarda las tareas en el archivo `Tareas.txt`.
6. **Salir**: Permite al usuario salir del programa.

### API REST:
- **POST /tareas**: Agregra una nueva tarea.
- **DELETE /tareas/{id}**: Eliminar una tarea por ID.
- **PUT /tareas/{id}/completada**: Marcar una tarea como completada por ID.
- **GET /tareas/pendientes**: Listar todas las tareas pendientes.
- **POST /guardar**: Guarda todas las tareas en el archivo de texto `Tareas.txt`.

## Instalación y Ejecución

### Requisitos:
- Python 3.x
- Bibliotecas: `Flask`, `requests`

### Instrucciones para ejecutar:
1. Clonar el repositorio o descargar los archivos.
2. Instalar las dependencias necesarias:
   ``pip install flask requests``

3.  La aplicación ejecuta automáticamente el servidor Flask (la API REST) en segundo plano. Para ejecutar el programa y el servidor juntos, simplemente ejecute el siguiente comando:
    ``python Test1_console.py``

4. El servidor API estará corriendo en http://127.0.0.1:5000/ mientras el programa esté activo.
