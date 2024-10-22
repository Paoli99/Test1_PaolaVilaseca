import queue
import requests 
import subprocess
import time

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
                try:
                    response = requests.post(f"{API_URL}/tareas", json={"task": new_task})
                
                    if response.status_code == 201:
                        created_task = response.json()["task"]
                        print(f"La tarea '{created_task['id']}' '{created_task['task']}' fue creado exitosamente.")
                    else:
                        print("Error al agregar la tarea.")

                except requests.exceptions.ConnectionError:
                    print("Error: No se pudo conectar al servidor Flask.")

        elif option == "2":
            print("========================================")
            print("===========Eliminar tarea===============")
            print("=====(Presione 6 para volver atras)=====")
            print("========================================")
            print("")
            new_task = input("Ingrese el id de la tarea: ")
            print("========================================")

        elif option == "3":
            print("========================================")
            print("=====Marcar tarea como completada=======")
            print("=====(Presione 6 para volver atras)=====")
            print("========================================")
            print("")
            new_task = input("Ingrese el id de la tarea: ")
            print("========================================")

        elif option == "4":
            print("========================================")
            print("===== Lista de tareas pendientes =======")
            print("=====(Presione 6 para volver atras)=====")
            print("========================================")
            print("")


        elif option == "5":
            print("========================================")
            print("======== Guardar tareas en txt =========")
            print("=====(Presione 6 para volver atras)=====")
            print("========================================")
            print("")
            new_task = input("Escriba 'guardar' para guardar las tareas: ")
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




