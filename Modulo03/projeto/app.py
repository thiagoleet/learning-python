from flask import Flask, request, jsonify
from models.task import Task
import uuid
app = Flask(__name__)

tasks = []

# CRUD

# Create


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = Task(id=uuid.uuid4(),
                    title=data["title"],
                    description=data.get("description", ""))

    print(new_task.to_dict())
    tasks.append(new_task)

    output = {"message": "Nova tarefa criada com sucesso!",
              "task": new_task.to_dict()}
    return jsonify(output), 201


# Read
@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {"tasks": task_list, "total": len(task_list)}
    return jsonify(output), 200


@app.route("/tasks/<uuid:id>", methods=["GET"])
def get_task(id):

    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict()), 200

    return jsonify({"message": "Tarefa não encontrada"}), 404


@app.route("/tasks/<uuid:id>", methods=["PUT"])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if not task:
        return jsonify({"message": "Tarefa não encontrada"}), 404
    else:
        data = request.get_json()
        task.title = data.get("title", task.title)
        task.description = data.get("description", task.description)
        task.completed = data.get("completed", task.completed)
        output = {"message": "Tarefa atualizada com sucesso!",
                  "task": task.to_dict()}

        return jsonify(output), 202


@app.route("/tasks/<uuid:id>", methods=["DELETE"])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if not task:
        return jsonify({"message": "Tarefa não encontrada"}), 404
    else:
        tasks.remove(task)
        return jsonify({"message": "Tarefa removida com sucesso!"}), 204


if __name__ == "__main__":
    app.run(debug=True)
else:
    app.run(debug=False)
