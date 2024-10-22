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
    inputQueue = queue.Queue()

    while True:
        start_program(inputQueue)
        option = inputQueue.get()

        if option == "1":
            print("========================================")
            print("===========Agregar tarea================")
            print("========================================")
            print("")
            new_task = input("Ingrese la tarea: ")
            print("========================================")
            print("=========Presione 6 para salir==========")
            print("========================================")

            if new_task == "6":
                continue
            else: 
                print("Tarea: ", new_task, "agregada")

        elif option == "2":
            print("========================================")
            print("===========Eliminar tarea===============")
            print("========================================")
            print("")
            print("========================================")
            print("=========Presione 6 para salir==========")
            print("========================================")

        elif option == "3":
            print("========================================")
            print("=====Marcar tarea como completada=======")
            print("========================================")
            print("")
            print("========================================")
            print("=========Presione 6 para salir==========")
            print("========================================")

        elif option == "4":
            print("========================================")
            print("===== Lista de tareas pendientes =======")
            print("========================================")
            print("")
            print("========================================")
            print("=========Presione 6 para salir==========")
            print("========================================")

        elif option == "5":
            print("========================================")
            print("======== Guardar tarea en txt ==========")
            print("========================================")
            print("")
            print("========================================")
            print("=========Presione 6 para salir==========")
            print("========================================")

        elif option == "6":
            print("========================================")
            print("=========Saliendo del programa==========")
            print("========================================")
            break

        else:
            print("Por favor, ingrese una opcion valida.")

if __name__ == "__main__":
    main()




