import pytest
from flask.testing import FlaskClient
from ej2b3 import create_app

@pytest.fixture
def client() -> FlaskClient:
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_search_with_parameters(client):
    """
    Prueba el endpoint /search con parámetros de consulta en la URL
    """
    # Prueba con múltiples parámetros de consulta
    response = client.get("/search?q=flask&category=tutorial")
    assert response.status_code == 200, "El código de estado debe ser 200."
    data = response.json
    assert data["q"] == "flask", "El parámetro 'q' debe estar en la respuesta."
    assert data["category"] == "tutorial", "El parámetro 'category' debe estar en la respuesta."

    # Prueba con un solo parámetro
    response = client.get("/search?q=python")
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.json["q"] == "python", "El parámetro 'q' debe estar en la respuesta."
    assert response.json.get("category") is None, "El parámetro 'category' no debe existir o debe ser None."

def test_form_handler(client):
    """
    Prueba el endpoint /form con datos de formulario
    """
    # Prueba con datos de formulario completos
    form_data = {"name": "Juan Pérez", "email": "juan@example.com"}
    response = client.post("/form", data=form_data)
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.json["name"] == "Juan Pérez", "El nombre debe estar en la respuesta."
    assert response.json["email"] == "juan@example.com", "El email debe estar en la respuesta."

    # Prueba con datos parciales
    response = client.post("/form", data={"name": "María"})
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.json["name"] == "María", "El nombre debe estar en la respuesta."
    assert response.json.get("email") is None, "El email no debe existir o debe ser None."

def test_json_handler(client):
    """
    Prueba el endpoint /json con datos JSON en el cuerpo
    """
    # Prueba con objeto JSON simple
    json_data = {"message": "Hola", "priority": "high"}
    response = client.post("/json", json=json_data)
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.json["message"] == "Hola", "El mensaje debe estar en la respuesta."
    assert response.json["priority"] == "high", "La prioridad debe estar en la respuesta."

    # Prueba con objeto JSON complejo
    json_data = {
        "user": {
            "name": "Ana",
            "roles": ["admin", "editor"]
        },
        "settings": {
            "theme": "dark",
            "notifications": True
        }
    }
    response = client.post("/json", json=json_data)
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.json["user"]["name"] == "Ana", "El nombre del usuario debe estar en la respuesta."
    assert "admin" in response.json["user"]["roles"], "El rol 'admin' debe estar en la respuesta."
    assert response.json["settings"]["theme"] == "dark", "El tema debe estar en la respuesta."
