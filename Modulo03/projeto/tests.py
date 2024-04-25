import pytest
import requests


# CRUD
BASE_URL = "http://127.0.0.1:5000"
tasks = []


def test_create_task():
    new_task_data = {
        "title": "Nova Tarefa",
        "description": "Descrição da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 201
    response_json = response.json()
    assert "message" in response_json
    assert "task" in response_json
    createdTask = response_json["task"]
    tasks.append(createdTask)


def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total" in response_json
    assert len(response_json["tasks"]) == len(tasks)


def test_get_task():
    if tasks:
        task = tasks[0]
        print(task)
        task_id = task["id"]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json == task
