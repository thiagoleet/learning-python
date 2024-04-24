from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

# CRUD

# Create


@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control,
                    title=data["title"],
                    description=data.get("description", ""))
    task_id_control += 1

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


@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if task:
        return jsonify(task.to_dict()), 200
    else:
        return jsonify({"message": "Tarefa não encontrada"}), 404


if __name__ == "__main__":
    app.run(debug=True)
else:
    app.run(debug=False)
