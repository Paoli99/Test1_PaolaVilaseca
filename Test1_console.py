import queue
import requests 
import subprocess
import time
import os

API_URL = 'http://127.0.0.1:5000/'

# Funcion para verificar que el servidor funcione correctamente
def check_server_status():
    for _ in range (5):
        try: 
            response = requests.get(API_URL)
            if response.status_code == 200:
                print("Servidor funcionando correctamente")
                return True
        except requests.exceptions.ConnectionError:
            print("Esperando a que el servidor Flask se inicie...")
            time.sleep(1)

    return False 

# Funcion para mostrara el menu principal
def start_program(inputQueue):
    print("")
    print("========================================")
    print("=============BIENVENIDO=================")
    print("========================================")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Marcar tarea como completada")
    print("4. Listar tareas pendientes")
    print("5. Guardar las tareas en un archivo de texto")
    print("6. Salir")
    print("========================================")

    input_str = input("Por favor, seleccione una opcion: " )
    inputQueue.put(input_str)

def main():
    tasks = []
    inputQueue = queue.Queue()

    # Ciclo while para que el usuario agregue multiples tareas si quiere
    while True:
        start_program(inputQueue)
        option = inputQueue.get()

        # El usuario escribe el nombre de la tarea para agregarla 
        if option == "1":
            print("========================================")
            print("===========Agregar tarea================")
            print("===(Escriba 'atras' para volver atras)===")
            print("========================================")
            print("")
            new_task = input("Ingrese la tarea: ")
            print("========================================")

            #Usuario escribe atrs para volver al menu
            if new_task == "atras":
                continue
            else: 
                try:
                    response = requests.post(f"{API_URL}/tareas", json={"task": new_task})
                
                    if response.status_code == 201:
                        created_task = response.json()["task"]
                        tasks.append(created_task) # guardar la tare localmente
                        print(f"La tarea '{created_task['id']}' '{created_task['task']}' fue creado exitosamente.")
                    else:
                        print("Error al agregar la tarea.")

                except requests.exceptions.ConnectionError:
                    print("Error: No se pudo conectar al servidor Flask.")

        # El usuario puede borrar tareas 
        elif option == "2":
            # Ciclo while para que el usuario borrar multiples tareas si quiere
            while True:
                print("========================================")
                print("===========Eliminar tarea===============")
                print("===(Escriba 'atras' para volver atras)===")
                print("========================================")
                print("")
                task_id  = input("Ingrese el id de la tarea: ")
                print("========================================")

                if task_id == "atras":
                    break  
                else:
                    try:
                        response = requests.delete(f"{API_URL}/tareas/{task_id}")
                        if response.status_code == 200:
                            print(f"Tarea con ID {task_id} eliminada correctamente.")
                        elif response.status_code == 404:
                            print(f"No se encontró ninguna tarea con ID {task_id}.")
                        else:
                            print("Error al eliminar la tarea.")
                    except requests.exceptions.ConnectionError:
                        print("Error: No se pudo conectar al servidor Flask.")

        # El usuario marca tareas como completadas 
        elif option == "3":
            # Ciclo while para que el usuario marcar multiples tareas como completadas
            while True:
                print("========================================")
                print("=====Marcar tarea como completada=======")
                print("===(Escriba 'atras' para volver atras)===")
                print("========================================")
                print("")
                task_id = input("Ingrese el id de la tarea: ")
                print("========================================")

                if task_id == "atras":
                    break
                else:
                    try:
                        response = requests.put(f"{API_URL}/tareas/{task_id}/completada")
                        if response.status_code == 200:
                            print(f"Tarea con ID {task_id} marcada como completada correctamente.")
                        elif response.status_code == 404:
                            print(f"No se encontró ninguna tarea con ID {task_id}.")
                        else:
                            print("Error al marcar la tarea como completada.")
                    except requests.exceptions.ConnectionError:
                        print("Error: No se pudo conectar al servidor Flask.")

                    print("========================================")

            
        # El usuario ve laa lista de tareas
        elif option == "4":
            print("========================================")
            print("===== Lista de tareas pendientes =======")
            print("========================================")
            try:
                response = requests.get(f"{API_URL}/tareas/pendientes")
                if response.status_code == 200:
                    pending_tasks = response.json()["tasks"]
                    if pending_tasks:
                        for task in pending_tasks:
                            print(f"ID: {task['id']} - Tarea: {task['task']} - Estado: Pendiente")
                    else:
                        print("No hay tareas pendientes.")
                else:
                    print("Error al obtener las tareas pendientes.")
            except requests.exceptions.ConnectionError:
                print("Error: No se pudo conectar al servidor.")
            
            print("========================================")


        # El usuario debe escribir guardar para que las tareas se guarden
        elif option == "5":
            # Ciclo while para que el usuario solo pueda volver atras si ingresa el comando correcto
            while True:
                print("========================================")
                print("======== Guardar tareas en txt =========")
                print("=====(Presione 6 para volver atras)=====")
                print("========================================")
                print("")
                keyboard = input("Escriba 'guardar' para guardar las tareas: ")

                if keyboard.lower() == "guardar":
                    try:
                        response = requests.post(f"{API_URL}/guardar")
                        if response.status_code == 200:
                            print("Tareas guardadas")
                            break  
                        else:
                            print("Error al guardar las tareas.")
                    except requests.exceptions.ConnectionError:
                        print("Error: No se pudo conectar al servidor Flask.")
                        break  

                elif keyboard == "atras":
                    continue

                else:
                    print("Por favor, ingrese el comando correcto")
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

    if check_server_status():
        main()

    else:
        print("Error: No se pudo iniciar el servidor Flask.")
    
    flask_process.terminate()




