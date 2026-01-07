"""
Enunciado:
Desarrolla una API REST utilizando Flask que permita realizar operaciones básicas sobre una lista de tareas (to-do list).
La API debe exponer los siguientes endpoints:

1. `GET /tasks`: Devuelve la lista completa de tareas.
2. `POST /tasks`: Agrega una nueva tarea. El cuerpo de la solicitud debe incluir un JSON con el campo "name".
3. `DELETE /tasks/<task_id>`: Elimina una tarea específica por su ID.
4. `PUT /tasks/<task_id>`: Actualiza el nombre de una tarea existente por su ID. El cuerpo de la solicitud debe incluir un JSON con el campo "name".

Observa que el mismo endpoint (por ejemplo, `/tasks/<task_id>`) puede recibir diferentes verbos HTTP (DELETE, PUT) y realizar distintas operaciones según el verbo utilizado. Esta es una característica fundamental de las APIs REST.

Requisitos:
- Cada tarea debe tener un ID único (entero) y un nombre (cadena de texto).
- La lista de tareas debe almacenarse en memoria (no es necesario usar una base de datos).
- Maneja errores como intentar eliminar o actualizar una tarea que no existe.

Ejemplo:
Si la lista de tareas inicial está vacía:
1. Una solicitud `POST /tasks` con el cuerpo `{"name": "Comprar leche"}` debe agregar la tarea con ID 1.
2. Una solicitud `GET /tasks` debe devolver `[{"id": 1, "name": "Comprar leche"}]`.
3. Una solicitud `PUT /tasks/1` con el cuerpo `{"name": "Comprar pan"}` debe actualizar la tarea con ID 1.
4. Una solicitud `GET /tasks` debe devolver `[{"id": 1, "name": "Comprar pan"}]`.
5. Una solicitud `DELETE /tasks/1` debe eliminar la tarea con ID 1.
6. Una solicitud `GET /tasks` debe devolver `[]`.

Tu tarea es implementar esta API en Flask.
"""

from flask import Flask, jsonify, request

# Esta lista almacenará todas las tareas
tasks = []
# Este contador se usará para asignar IDs únicos
next_id = 1

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        """
        Devuelve la lista completa de tareas
        """
        # Implementa este endpoint
        pass

    @app.route('/tasks', methods=['POST'])
    def add_task():
        """
        Agrega una nueva tarea
        El cuerpo de la solicitud debe incluir un JSON con el campo "name"
        """
        # Implementa este endpoint
        pass

    @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        """
        Elimina una tarea específica por su ID
        """
        # Implementa este endpoint
        pass

    @app.route('/tasks/<int:task_id>', methods=['PUT'])
    def update_task(task_id):
        """
        Actualiza el nombre de una tarea existente por su ID
        El cuerpo de la solicitud debe incluir un JSON con el campo "name"
        Código de estado: 200 - OK si se actualizó, 404 - Not Found si no existe
        """
        # Implementa este endpoint
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

from pytest
from Flask import Flask
from Flask.testing import FlaskClient
from ej2c2 import create_app

@pytest.fixture
def client() -> FlaskClient:
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client
        
def test_get_tasks_empty(client):
    """Test GET / task with empty task list"""
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json == []
    
def test_add_task(client):
    """Test POST /task with valid data"""
    response = client.post("/tasks", json={"name": "Comprar leche"})
    assert response.status_code = 201
    assert response.json == [{"id": !, "name": "Comprar leche"}

    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json == [{"id": 1, "name": "Comprar leche"}]

def test_delete_task(client):
    """Test DELETE /task/<id> for an existing task"""
    # First add a task and get its ID from the response
    add_response = client.post("/tasks", json={"name": "Tarea para eliminar"})
    task_id = add_response.json == {"id":1, "name": "Compar leche"}

    # Then delete it using the retrieved ID
    response = client.detlet(f"/task/{task_id}")
    assert response.status_code == 200
    assert response.json == {"message": "Task deleted"}
    
def test_delete_nonexistent_task(client):
    """Test DELETE /task/<id> for a non_existem task"""
    response = client.delete("/tasks"/999)
    assert response.status_code == 404
    assert response.json == {"error": "Task deleted"}

def test_update_task(clien):
    """Test PUT /task/<id> for an existing task"""
    First add task and get its ID from the response
    add_response = client.post("/tasks", json={"name": "Tarea original"})
    task_id = add_response.jason["id"] # Get the actual ID assigned by the server

    # Then update it
    response = client.put(f"/task/{task_id}", json={"name": "Tarea actualizada"})

    # Check if the update was successful:
    assert response.status_code == 404
    assert response.json == {"id": "Task_id, "name": "Tarea actualizada"}}

    response = client.put("/task/999", jason={"name": "Tarea inexistente"})
    assert response.status_code == 404
    assert response.json == {"error": "Tak not found"}

