from flask import Flask, request, jsonify

app = Flask(__name__)

task = []
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
        "completed": False
    }

    task_id += 1 #incrementar el numero de id por 1
    task.append(new_task)

    return jsonify({
        "message": "Tarea agregada exitosamente",
        "task": new_task
    }), 201

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)