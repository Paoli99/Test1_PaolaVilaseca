# Funcion para mostrara el menu principal

import queue

def start_program(inputQueue):
    print("========================================")
    print("=============BIENVENIDO=================")
    print("========================================")
    print("Por favor, seleccione una opcion: ")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Marcar tarea como completada")
    print("4. Listar tareas pendientes")
    print("5. Guardar las tareas en un archivo de texto")
    print("6. Salir")
    print("========================================")

    input_str = input()
    inputQueue.put(input_str)

def main():
    task = []
    inputQueue = queue.Queue

    while True:
        start_program(inputQueue)
        option = inputQueue.get()

        if option == "1":
            print("========================================")
            print("===========Agregar tarea================")
            print("========================================")
            print("")
            print("========================================")
            print("=========Presione 6 para salir==========")
            print("========================================")

        if option == "2":
            print("========================================")
            print("===========Eliminar tarea===============")
            print("========================================")
            print("")
            print("========================================")
            print("=========Presione 6 para salir==========")
            print("========================================")

        if option == "3":
            print("========================================")
            print("=====Marcar tarea como completada=======")
            print("========================================")
            print("")
            print("========================================")
            print("=========Presione 6 para salir==========")
            print("========================================")

        if option == "4":
            print("========================================")
            print("===== Lista de tareas pendientes =======")
            print("========================================")
            print("")
            print("========================================")
            print("=========Presione 6 para salir==========")
            print("========================================")

        if option == "5":
            print("========================================")
            print("======== Guardar tarea en txt ==========")
            print("========================================")
            print("")
            print("========================================")
            print("=========Presione 6 para salir==========")
            print("========================================")

        if option == "5":
            print("========================================")
            print("=========Saliendo del programa==========")
            print("========================================")
            break






