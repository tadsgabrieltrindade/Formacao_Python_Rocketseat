from flask import Flask, request, jsonify, Response
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1


@app.route("/tasks", methods=['POST'])
def insert_task():
    global task_id_control
    data = request.get_json()
    title = data.get('title')
    description = data.get('description', "")  #caso a descrição seja vazia, ele será uma string vazia
    
    task = Task(id=task_id_control, title=title, description=description, completed=True)
    tasks.append(task)
    
    task_id_control += 1
    return jsonify({"message": "Nova tarefa criada com sucesso!"})


@app.route("/tasks", methods=['GET'])
def get_tasks():
    tasks_list = [task.to_dict() for task in tasks]
    return jsonify({
        "message": "Segue a lista com todos as tasks", 
        "tasks": tasks_list,
        "total_tasks": len(tasks)
    })

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify({
                'message': "Segue a task",
                'task': t.to_dict()
            })
    # return jsonify({"message": "Não foi possível encontrar a task"})
    return jsonify(msg="Not found"), 404



if __name__ == "__main__":
    app.run(debug=True)