"""
Enunciado:
Desarrolla una aplicación web con Flask que demuestre diferentes formas de pasar parámetros a una API.
La aplicación debe implementar los siguientes endpoints:

1. `GET /search`: Acepta parámetros de consulta (query parameters) en la URL.
   Ejemplo: `/search?q=flask&category=tutorial`
   Debe devolver los parámetros recibidos en formato JSON.

2. `POST /form`: Acepta datos de formulario (form data) en el cuerpo de la petición.
   Debe devolver los datos recibidos en formato JSON.

3. `POST /json`: Acepta datos JSON en el cuerpo de la petición.
   Debe devolver los datos recibidos en formato JSON.

Esta actividad te enseñará las diferentes formas de recibir parámetros en una aplicación Flask:
- Parámetros de consulta en la URL (query parameters)
- Datos de formulario (form data)
- Datos JSON en el cuerpo de la petición

Estos métodos son fundamentales para construir APIs web interactivas que puedan recibir información del cliente.
"""

from flask import Flask, jsonify, request

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/search', methods=['GET'])
    def search():
        """
        Maneja parámetros de consulta (query parameters) en la URL
        Ejemplo: /search?q=flask&category=tutorial

        Acceso mediante request.args (diccionario con los parámetros de la URL)
        """
        # Implementa este endpoint para obtener los parámetros de consulta
        # y devolverlos en formato JSON
        pass

    @app.route('/form', methods=['POST'])
    def form_handler():
        """
        Maneja datos de formulario enviados mediante POST

        Acceso mediante request.form (para datos de formulario)
        """
        # Implementa este endpoint para obtener los datos del formulario
        # y devolverlos en formato JSON
        pass

    @app.route('/json', methods=['POST'])
    def json_handler():
        """
        Maneja datos JSON enviados en el cuerpo de la petición

        Acceso mediante request.get_json() (para datos JSON)
        """
        # Implementa este endpoint para obtener los datos JSON
        # y devolverlos en formato JSON
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

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
    Prueba el endpoint / search con parámetros de consulta en la URL
    """
    # Prueba con múltiples parámetros de consulta
    response = client.get("/search?q=flask&category=tutorial")
    assert response.status_code == 200, "El código de estado debe ser 200."
    data = response.json
    assert data["q"] == "flask", "El parametro 'q' debe estar en la respuesta" 
    assert data["category"] == "tutorial", "El parámetro 'category' debe esta en la respuesta."

    # Prueba con un sólo parámetro
    response = client.get("/search?q=python")
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.json["q"] == "python", "El parametro 'q' debe estar en la respuesta" 
    assert response.json.get["category"] is None, "El parámetro 'category' debe existir."

def test_form_handler(client):
    """
    Prueba el endpoint / json con datos JSON en el cuerpo
    """
  # Prueba con múltiples parámetros de consulta
    response = client.get("/search?q=flask&category=tutorial")
    assert response.status_code == 200, "El código de estado debe ser 200."
    data = response.json
    assert data["q"] == "flask", "El parametro 'q' debe estar en la respuesta" 
    assert data["category"] == "tutorial", "El parámetro 'category' debe esta en la respuesta."

    # Prueba con un sólo parámetro
    response = client.get("/search?q=python")
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.json["q"] == "python", "El parametro 'q' debe estar en la respuesta" 
    assert response.json.get["category"] is None, "El parámetro 'category' debe existir."

def test_jason_handler(client):
    """
    Prueba el endpoint / json con datos JSON en el cuerpo
    """
    # Prueba con objteto JSON simple
    json_data = {"menssage": "Hola, "priority": "high" 
    response = client.post("/json=json_data")
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.json["name"] == "Maria", "El nombre debe estar en la respuesta" 
    assert response.json.get("email") is None, "El email no debe existir o debe ser None."

    # Prueba con un objeto JSON complejo
    json_data = {
        "user": {
           "name": "Maria",
           "roles": ["admin", "editor"]
         },
         "settings": {
            "theme": "dark",
            "notifications": True
         }
    }
    response = client.post("/json", json=json_data)
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.json,["user"]["name"] == "Maria", "El nombre del usuario debe estar en la respuesta." 
    assert "admin" in response.json["user"]["roles"], El rol 'admin'debe estar en la respuesta."
    assert response.json.get["setting"]["theme"] == "dark", "El tema debe estar en la respuesta."
