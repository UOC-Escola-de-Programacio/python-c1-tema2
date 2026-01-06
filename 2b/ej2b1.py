"""
Enunciado:
Desarrolla una aplicación web básica con Flask que responda a una petición GET.
La aplicación debe tener un único endpoint:

1. `GET /`: Devuelve un mensaje de saludo en texto plano con el contenido "¡Hola mundo!".

Esta es una introducción simple a Flask para entender cómo crear una aplicación web básica y responder
a solicitudes HTTP.

Tu tarea es completar la implementación de la función create_app() y del endpoint solicitado.

Nota: Si deseas cambiar el idioma del ejercicio, edita el archivo de test correspondiente (ej1a1_test.py).
"""

from flask import Flask

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    # Aquí debes implementar el endpoint solicitado

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


import pytest
from flask.testing import FlaskClient
from ej2b1 import create_app

@pytest.fixture
def client() -> FlaskClient:
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_root_endpoint(client)
    """
    Prueba el endpoint / para validar que devuelve el mensaje correcto.
    Si deseas cambiar el idioma del ejercicio, edita este archivo.
    """
    response = client.get("/")
    assert response.status_code == 200, "El código debe ser 200."
    assert response.data.decode("utf-8") == "¡Hola mundo!", "El mensaje debe ser '¡Hola mundo!' en texto plano."
