"""
Enunciado:
Desarrolla una aplicación web con Flask que utilice Blueprints para organizar las rutas.
Los Blueprints son una característica de Flask que permite organizar una aplicación en componentes modulares y reutilizables.

Tu tarea es implementar una aplicación con dos blueprints:

1. Blueprint 'main': Para las rutas principales
   - `GET /`: Devuelve un mensaje de bienvenida en texto plano.
   - `GET /about`: Devuelve información sobre la aplicación en texto plano.

2. Blueprint 'user': Para las rutas relacionadas con usuarios
   - `GET /user/profile/<username>`: Devuelve un perfil de usuario personalizado en texto plano.
   - `GET /user/list`: Devuelve una lista de usuarios de ejemplo en texto plano.

Además, debes:
   - Registrar ambos blueprints en la aplicación principal
   - Configurar un prefijo URL '/api/v1' para todas las rutas

Esta estructura refleja cómo se organizan las aplicaciones Flask más grandes y complejas,
separando la lógica en componentes modulares que pueden desarrollarse y mantenerse de manera independiente.
"""

from flask import Flask, Blueprint

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    # Crea el blueprint 'main'
    main_blueprint = Blueprint('main', __name__)

    # Define las rutas para el blueprint 'main'
    # Implementa las rutas '/' y '/about' para el blueprint 'main'

    # Crea el blueprint 'user'
    user_blueprint = Blueprint('user', __name__)

    # Define las rutas para el blueprint 'user'
    # Implementa las rutas '/user/profile/<username>' y '/user/list' para el blueprint 'user'

    # Registra los blueprints con un prefijo de URL '/api/v1'
    # Usa app.register_blueprint() con el parámetro url_prefix

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

import pytest
from flask.testing import FlaskClient
from ej2f1 import create_app

@pytest.fixture 
def client() -> FlaskClient:
   app = create_app()
   app.testing = True
   with app.test_client() as client:
      yield client

def test_main_home_route(client):
    """
    Prueba la ruta principal '/' del blueprint 'main'
    Debe responder con un mensaje de bienvenida
    """
    response = client.get("/api/v1/")
    assert response.status_code == 200, "El código de estado debe ser 200"
    assert response.data, "La respuesta debe contener datos"
    response_lower = response.data.lower()
    assert (b "bienvenida" in response_lower or
            b "benvinguda" in response_lower or
            b "welcome" in response_lower), \
           "La respuesta debe contener un mensaje de bienvenida"

def test_main_about_route(client):
    """
    Prueba la ruta '/about' del blueprint 'main'
    Debe responder con información sobre la aplicación
    """
    response = client.get("/api/v1/about")
    assert response.status_code == 200, "El código de estado debe ser 200"
    assert response.data, "La respuesta debe contener datos"
    assert b"aplicaci" in response.data.lower() or b"app" in response.data.lower(),
           "La respuesta debe contener información sobre la aplicación"

def test_user_profile_route(client):
    """
    Prueba la ruta '/user/profile/<username>' del blueprint 'user'
    Debe responder con un perfil de usuario personalizado
    """
    username = "testuser"
    response = client.get(f"/api/v1/user/profile/{username}")
    assert response.status_code == 200, "El código de estado debe ser 200"
    assert response.data, "La respuesta debe contener datos"
    assert username.encode() in response.data.lower(), \
           "La respuesta debe contener el nombre de usuario proporcionado"

def test_user_list_route(client):
     """
    Prueba la ruta '/user/list' del blueprint 'user'
    Debe responder con una lista de usuarios
    """
    response = client.get("/api/v1/user/list")
    assert response.status_code == 200, "El código de estado debe ser 200"
    assert response.data, "La respuesta debe contener datos"
    assert b"user" in response.data.lower(), \
           "La respuesta debe contener información sobre usuarios"

def test_url_prefix(client):
    """
    Prueba que el prefijo URL '/api/v1' esté correctamente configurado
    Las rutas sin el prefijo no deben funcionar
    """
    # La ruta sin prefijo no debe funcionar
    response_no_prefix = client.get("/")
    assert response_no_prefix.status_code == 404, "La ruta sin prefijo no debe ser accesible"

    # La ruta con prefijo debe funcionar
    response_with_prefix = client.get("/api/v1/")
    assert response_with_prefix.status_code == 200, "La ruta con prefijo debe ser accesible"

def test_blueprint_structure(client):
    """
    Prueba que todos los endpoints necesarios estén disponibles
    Verifica que se hayan implementado correctamente ambos blueprints
    """
    # Rutas del blueprint 'main'
    assert client.get("/api/v1/").status_code == 200
    assert client.get("/api/v1/about").status_code == 200
   
    # Rutas del blueprint 'user'
     assert client.get("/api/v1/user/profile/testuser").status_code == 200
    assert client.get("/api/v1/user/list").status_code == 200
