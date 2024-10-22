from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []
task_id = 0 # contador para asignar los ids

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
def save_tasks():
    with open("Tareas.txt", "w") as file:
        for task in tasks:
            status = "Completada" if task["completed"] else "Pendiente"
            file.write(f"ID: {task['id']} - Tarea: {task['task']} - Estado: {status}\n")
    return jsonify({"message": "Tareas guardadas en 'Tareas.txt'."}), 200

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)