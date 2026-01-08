"""
Enunciado:
Desarrolla una aplicación web con Flask que utilice la función abort() para devolver
diferentes códigos de estado HTTP según ciertas condiciones.

La función abort() de Flask permite terminar prematuramente una solicitud con un código
de estado HTTP específico. Esto es útil para indicar errores como recurso no encontrado (404),
acceso prohibido (403), etc.

Tu tarea es implementar los siguientes endpoints:

1. `GET /resource/<id>`: Debe devolver un mensaje con el ID solicitado si el ID es un número positivo.
   Si el ID es 0 o negativo, debe abortar la solicitud con código 400 (Bad Request).
   Si el ID es mayor que 100, debe abortar la solicitud con código 404 (Not Found).

2. `GET /admin`: Debe verificar si existe un parámetro de consulta 'key'.
   Si 'key' no está presente, debe abortar la solicitud con código 401 (Unauthorized).
   Si 'key' no es igual a 'secret123', debe abortar la solicitud con código 403 (Forbidden).

Esta actividad te enseñará a utilizar la función abort() de Flask para manejar
situaciones de error comunes en aplicaciones web.
"""

from flask import Flask, request, abort, jsonify

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/resource/<int:resource_id>', methods=['GET'])
    def get_resource(resource_id):
        """
        Devuelve información sobre un recurso según su ID.
        Utiliza abort() en casos de error:
        - Si el ID es <= 0: abort con código 400 (Bad Request)
        - Si el ID es > 100: abort con código 404 (Not Found)
        """
        # Implementa este endpoint utilizando abort() según las condiciones
        pass

    @app.route('/admin', methods=['GET'])
    def admin():
        """
        Endpoint protegido que requiere una clave de acceso.
        Utiliza abort() en casos de error:
        - Si no se proporciona el parámetro 'key': abort con código 401 (Unauthorized)
        - Si la clave no es 'secret123': abort con código 403 (Forbidden)
        """
        # Implementa este endpoint utilizando abort() según las condiciones
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

import pytest
import flask.testing import FlaskClient
from ej2d2 import create_app

@pytest.fixture 
def client() -> FlaskClient:
   app = create_app()
   app.testing = True
   with app.test_client() as client:
      yield client

def test_resource_valid_id(client)
   """
   Prueba el endpoint / resource/<id> con un ID válido (positivo y ≤ 100)
   Debe devolver un código 200 y alguna información sobre el recurso
   """
   response = client.get("/resource/42")
   assert response.status_code == 200, "El código de estado debe ser 200 para un ID válido"
   assert "42" in response.get_data(as_text=True), "La respuesta debe incluir el ID solicitado"

def test_resource_negative_id(client):
    """
   Prueba el endpoint / resource/<id> con un ID negativo
   Debe abortar con código 400 (Bad Request)
   """
   response = client.get("/resource/-5")
   assert response.status_code == 400, "El código de estado debe ser 400 para un ID negativo"

def test_resource_zero_id(client):
   """
   Prueba el endpoint / resource/<id> con un ID = 0
   Debe abortar con código 400 (Bad Request)
   """
   response = client.get("/resource/0")
   assert response.status_code == 400, "El código de estado debe ser 400 para un ID = 0"

def test_resource_large_id(client):
      """
   Prueba el endpoint / resource/<id> con un ID > 100
   Debe abortar con código 400 (Not Found)
   """
   response = client.get("/resource/101")
   assert response.status_code == 404, "El código de estado debe ser 404 para un ID > 100"

def test_admin_no_key(client):
   """
   Prueba el endpoint / admin sin proporcionar una clave
   Debe abortar con código 401 (Unauthorized)
   """
   response = client.get("/admin")
   assert response.status_code == 401, "El código de estado debe ser 401 cuando no se proporciona la clave"

def test_admin_wrong_key(client):
      """
   Prueba el endpoint /admin con una clave incorrecta
   Debe abortar con código 403 (Forbidden)
   """
   response = client.get("/admin?key=wrong")
   assert response.status_code == 403, "El código de estado debe ser 403 cuando la clave es incorrecta"

def test_admin_correct_key(client):
      """
   Prueba el endpoint /admin con la clave correcta
   Debe devolver un código 200 
   """
   response = client.get("/admin?key=secret123")
   assert response.status_code == 200, "El código de estado debe ser 200 cuando la clave es correcta"
   
