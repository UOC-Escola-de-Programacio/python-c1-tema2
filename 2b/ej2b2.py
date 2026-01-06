"""
Enunciado:
Desarrolla una aplicación web básica con Flask que responda a diferentes peticiones GET.
La aplicación debe tener los siguientes endpoints:

1. `GET /hello`: Devuelve un mensaje de saludo en texto plano con el contenido "¡Hola mundo!".
2. `GET /goodbye`: Devuelve un mensaje de despedida en texto plano con el contenido "¡Adiós mundo!".
3. `GET /greet/<nombre>`: Devuelve un mensaje personalizado en texto plano con el contenido "¡Hola, <nombre>!", donde <nombre> es un parámetro dinámico.

Tu tarea es completar la implementación de la función create_app() y de los endpoints solicitados.

Nota: Si deseas cambiar el idioma del ejercicio, edita el archivo de prueba correspondiente.
"""

from flask import Flask

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    # Aquí debes implementar los endpoints solicitados

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

imprt pytest
from flask.testing import FlaskClient
from ej2b2 import create_app

@pixture.fixture
def client() -> FlaskClient:
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    """
    Prueba el endpoint / hello para validar que devuelve el mensaje correcto.
    """
    response = client.get("/hello")
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.data.decode("utf-8") == "¡Hola mundo!", "El mensaje debe ser '¡Hola mundo!' en texto plano."


def test_goodbye_endpoint(client):
    """
    Prueba el endpoint / goodbye para validar que devuelve el mensaje correcto.
    """
    response = client.get("/ goodbye")
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.data.decode("utf-8") == "¡Adiós mundo!", "El mensaje debe ser '¡Adiós mundo!' en texto plano."

def test_greet_endpoint(client):
    """
    Prueba el endpoint / greet/<nombre> para validar que devuelve el mensaje personalizado correcto.
    """
    nombre = "Maria"
    response = client.get(f"/ greet/{nombre}")
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.data.decode("utf-8") == f"¡Hola, {nombre}!", "El mensaje debe ser personalizado con el nombre proporcionado."
    
