# 

def start_progrm(inputQueue):
    print("========================================")
    print("=============BIENVENIDO=================")
    print("========================================")
    print("Por favor, seleccione una opcion: ")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Marcar tarea como completada")
    print("4. Listar tareas pendientes")
    print("5. Guardr las tareas en un archivo de texto")
    print("6. Salir")
    print("========================================")

    input_str = input()
    inputQueue.put(input_str)




