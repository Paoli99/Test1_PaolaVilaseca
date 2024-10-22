# Funcion para mostrara el menu principal

import queue
import requests 
import subprocess

API_URL = 'http://127.0.0.1:5000/tareas'

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
            print("=========(Presione 6 para salir)========")
            print("========================================")
            print("")
            new_task = input("Ingrese la tarea: ")
            print("========================================")

            if new_task == "6":
                continue
            else: 
                response = requests.post(API_URL, json={"task": new_task})
                if response.status_code == 201:
                    created_task = response.json()["task"]
                    print(f"La tarea '{created_task['id']}' '{created_task['task']}' fue creada exitosamente.")
                else:
                    print("Error al agregar la tarea.")


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
    flask_process = subprocess.Popen(['python', 'Test1_apis.py'])

    try: 
        main()
    
    finally:
        flask_process.terminate()




