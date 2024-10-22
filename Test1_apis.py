from flask import Flask, request, jsonify
import os

app = Flask(__name__)

tasks = []
task_id = 0 # contador para asignar los ids

# Funcion para cargar las tareas guardadas y evitar que estas se sobre escriban 
def load_tasks():
    global task_id, tasks

    if os.path.exists("Tareas.txt"):
        with open("Tareas.txt", "r") as file:
            for line in file:
                task_data = line.strip().split(" - ")
                task = {
                    "id": int(task_data[0].split(": ")[1]),
                    "task": task_data[1].split(": ")[1],
                    "completed": task_data[2].split(": ")[1] == "Completada"
                }
                tasks.append(task)
                task_id = max(task_id, task["id"] + 1)  # Actualizar el task_id para que continue desde el último ID
        print(f"Se cargaron {len(tasks)} tareas desde 'Tareas.txt'.")

@app.route('/')
def home():
    return"Bienvenido"

# Opcion 1: Agregar tareas
@app.route('/tareas', methods=['POST'])
def add_task():
    global task_id 
    task_data = request.get_json()
    new_task = {
        "id": task_id,
        "task": task_data.get("task"),
        "completed": False # La tarea se creara con estado "pendiente"
    }

    task_id += 1 #incrementar el numero de id por 1
    tasks.append(new_task)

    return jsonify({
        "message": "Tarea agregada exitosamente",
        "task": new_task
    }), 201

#Opcion 5: Gurdar tareas

@app.route('/guardar', methods=['POST'])
#Funcion para que se guarden las tareas
def save_tasks():
    with open("Tareas.txt", "w") as file:
        for task in tasks:
            status = "Completada" if task["completed"] else "Pendiente"
            file.write(f"ID: {task['id']} - Tarea: {task['task']} - Estado: {status}\n")
    return jsonify({"message": "Tareas guardadas en 'Tareas.txt'."}), 200

if __name__ == '__main__':
    load_tasks()
    app.run(debug=False, use_reloader=False)