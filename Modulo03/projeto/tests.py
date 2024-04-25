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
        task_id = task["id"]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json == task


def test_update_task():
    if tasks:
        task = tasks[0]
        task_id = task["id"]
        payload = {
            'completed': True,
            'description': 'Nova descrição',
            'title': 'Título Atualizado'
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        assert response.status_code == 202
        response_json = response.json()
        assert "message" in response_json
        assert "task" in response_json

        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        response_json = response.json()
        assert response_json["completed"] == payload["completed"]
        assert response_json["description"] == payload["description"]
        assert response_json["title"] == payload["title"]


def test_delete_task():
    if tasks:
        task = tasks[0]
        task_id = task["id"]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 204
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404
