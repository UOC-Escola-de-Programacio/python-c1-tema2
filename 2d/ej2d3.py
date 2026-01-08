"""
Enunciado:
Desarrolla una API REST utilizando Flask que gestione un catálogo de animales e implemente
manejo de errores personalizado con el decorador @app.errorhandler.

La API debe exponer los siguientes endpoints:

1. `GET /animals`: Devuelve la lista completa de animales.
2. `GET /animals/<animal_id>`: Devuelve la información de un animal específico por su ID.
3. `POST /animals`: Agrega un nuevo animal. El cuerpo debe incluir JSON con campos "name" y "species".
4. `DELETE /animals/<animal_id>`: Elimina un animal específico por su ID.

Además, debes implementar manejadores personalizados para los siguientes errores HTTP:

- 400 (Bad Request): Cuando faltan datos necesarios o tienen formato incorrecto.
- 404 (Not Found): Cuando se solicita un animal que no existe.
- 405 (Method Not Allowed): Cuando se utiliza un método HTTP no permitido.
- 500 (Internal Server Error): Para errores internos del servidor.

Requisitos:
- Implementar los manejadores de errores utilizando el decorador @app.errorhandler.
- Cada manejador debe devolver una respuesta JSON con un mensaje descriptivo y el código de estado correspondiente.
- Asegúrate de que la función delete_animal lance un error 404 cuando se intenta eliminar un animal que no existe.
- Implementa un manejador para el error 500 que registre el error en los logs de la aplicación.

Ejemplo:
- Una solicitud a un endpoint inexistente debe activar el manejador de error 404.
- Una solicitud POST sin los campos requeridos debe activar el manejador de error 400.
- Intentar eliminar un animal inexistente debe activar el manejador de error 404.

Tu tarea es implementar esta API en Flask con el manejo adecuado de errores.
"""

from flask import Flask, jsonify, request, abort
import logging

# Configuración del registro (logging)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Lista de animales predefinida
animals = [
    {"id": 1, "name": "León", "species": "Panthera leo"},
    {"id": 2, "name": "Elefante", "species": "Loxodonta africana"},
    {"id": 3, "name": "Jirafa", "species": "Giraffa camelopardalis"}
]

# Este contador se usará para asignar IDs únicos
next_id = 4

def create_app():
    """
    Crea y configura la aplicación Flask con manejadores de errores personalizados
    """
    app = Flask(__name__)
    
    # Manejador de errores 400 - Bad Request
    @app.errorhandler(400)
    def bad_request(error):
        """
        Maneja errores de solicitud incorrecta (400)
        Devuelve un JSON con mensaje de error y código de estado 400
        """
        # Implementa este manejador de errores
        # 1. Registra el error usando app.logger.warning() con un mensaje descriptivo
        # 2. Devuelve un JSON con un mensaje descriptivo y el código de estado 400
        pass

    # Manejador de errores 404 - Not Found
    @app.errorhandler(404)
    def not_found(error):
        """
        Maneja errores de recurso no encontrado (404)
        Devuelve un JSON con mensaje de error y código de estado 404
        """
        # Implementa este manejador de errores
        # 1. Registra el error usando app.logger.info() con un mensaje descriptivo
        # 2. Devuelve un JSON con un mensaje descriptivo y el código de estado 404
        pass

    # Manejador de errores 405 - Method Not Allowed
    @app.errorhandler(405)
    def method_not_allowed(error):
        """
        Maneja errores de método no permitido (405)
        Devuelve un JSON con mensaje de error y código de estado 405
        """
        # Implementa este manejador de errores
        # 1. Registra el error usando app.logger.warning() con un mensaje descriptivo
        # 2. Devuelve un JSON con un mensaje descriptivo y el código de estado 405
        pass

    # Manejador de errores 500 - Internal Server Error
    @app.errorhandler(500)
    def internal_error(error):
        """
        Maneja errores internos del servidor (500)
        Registra el error en los logs y devuelve un JSON con mensaje de error
        """
        # Implementa este manejador de errores
        # 1. Registra el error usando app.logger.error() con los detalles del error
        # 2. Incluye información adicional como la ruta que causó el error utilizando request.path
        # 3. Devuelve un JSON con un mensaje descriptivo y el código de estado 500
        pass

    @app.route('/animals', methods=['GET'])
    def get_animals():
        """
        Devuelve la lista completa de animales
        """
        # Implementa este endpoint para devolver la lista de animales
        pass

    @app.route('/animals/<int:animal_id>', methods=['GET'])
    def get_animal(animal_id):
        """
        Devuelve la información de un animal específico por su ID
        Si el animal no existe, debe activar un error 404
        """
        # Implementa este endpoint para devolver un animal por su ID
        # si no existe, usa abort(404) para lanzar un error 404
        pass

    @app.route('/animals', methods=['POST'])
    def add_animal():
        """
        Agrega un nuevo animal
        El cuerpo debe incluir JSON con campos "name" y "species"
        Si falta algún campo, debe activar un error 400
        """
        # Implementa este endpoint
        # 1. Verifica que el cuerpo de la solicitud contenga JSON
        # 2. Verifica que los campos "name" y "species" estén presentes
        # 3. Si falta algún campo, usa abort(400) para lanzar un error
        # 4. Si todo está correcto, agrega el nuevo animal a la lista y devuelve una respuesta adecuada (código 201)
        pass

    @app.route('/animals/<int:animal_id>', methods=['DELETE'])
    def delete_animal(animal_id):
        """
        Elimina un animal específico por su ID
        Si el animal no existe, debe activar un error 404
        """
        # Implementa este endpoint
        # 1. Verifica si el animal existe
        # 2. Si no existe, usa abort(404) para lanzar un error 404
        # 3. Si existe, elimínalo de la lista y devuelve una respuesta adecuada
        pass

    # Endpoint adicional que lanza un error 500 para probar el manejador
    @app.route('/test-error', methods=['GET'])
    def test_error():
        """
        Endpoint de prueba que lanza un error 500 intencionalmente
        """
        # Lanza una excepción para probar el manejador de error 500
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

from pytest
from Flask import Flask
from Flask.testing import FlaskClient
from ej2d3 import create_app
import logging
from io import StringIO

class LogCaptureHandler(logging.Handler):
    """
    Manejador personalizado para capturar mensajes de log durante las pruebas
    """
    def __init__(self):
        super():__init__()
        self.logs = StringIO()
        self.setLevel(logging.INFO)
        self.setFormatter(logging.Formatter('%levelname)s: %(message)'s))

    def emit(self, record):
        """Añade un mensaje de log a los logs capturados"""
        self.logs.write(self.format(record) + '/n')

    def get_logs(self):
        """Devuelve los logs capturados y reinicia"""
        logs = self.logsgetvalue()
        self.logs = StringIO()
        return logs

@pytest.fixture
def client() -> FlaskClient:
    app: Flask = create_app()
    app.testing = True

    # Configurar el capturador de logs
    log_capture = LogCaptureHandler()
    app.logger.addHandler(log_capture)
    app.logger.setLevel(logging.INFO)

     with app.test_client() as client:
        client.log_capture = log_capture
        yield client

def test_get_animal(client):
    """Test GET/animals - should return all animals"""
    response = client.get("/animals")
    assert response.status_code == 200
    assert len(response.json) == 3
    assert response.json[0]["name"] == "León"


def test_get_animal_exists(client):
    """Test GET/animals - should return all animals"""
    response = client.get("/animals/1")
    assert response.status_code == 200
    assert response.json["name"] == "León"
    assert response.json["species"] == "Panthera leo"

def test_get_animal_not_found(client):
    """Test GET/animals/999 - should return 404 error"""
    response = client.get("/animals/999")
    assert response.status_code == 404
    assert "error" in response.json or "message" in response.json

    # Verificar que se registro el error en los logs
    logs = client.log_capture.get_logs()
    assert "INFO:" in logs, "Debe registrarse un mensaje de nivel INFO para errores 404"

def test_add_animal(client):
    """Test POST/animals - with valid data - should add new animal"""
    response = client.post("/animals", json{"name": "Tigre", "species": "Panthera"}) 
    assert response.status_code == 201
    assert response.json["name"] == "Tigre"
    assert response.json["id"] == 4

def test_add_animal_invalid(client):
    """Test POST/animals - with invalid data - should return 400 error"""
    response = client.get("/animals", json{"name": "Tigre"}) # Missing specie
    assert response.status_code == 400
    assert "error" in response.json or "message" in response.json

    # Verificar que se registro el error en los logs
    logs = client.log_capture.get_logs()
    assert "WARNING:" in logs, "Debe registrarse un mensaje de nivel WARNING para errores 400"

def test_delete_animal(client):
    """Test DELETE / animals/2 - should delete the animal with ID 2"""
    response = client.delete)"/animals/2")
    assert response.status_code == 204

    # Verify animal was deleted
    respose = client.get("/animals/2")
    assert response.status_code == 404

def test_delete_animal_not_found(client):
    """Test DELETE /animals/999 - should return 404 error"""
    response = client.delete("/animals/999")
    assert response.status_code == 404
    assert "error" in response.json or "Message" in response.json

    # Verificar que se registró el error en los logs
    logs = client.log_capture.get_logs()
    assert "INFO" in logs, "Debe resgistrarse un mesanje de nivel INFO para errores 404"

def test_method_not_allowed(client):
    """ Test PUT/animals -should return 405 error"""
    response = client.put("/animals")
    assert response.status_code == 405
    assert "error" in response.json or "Message" in response.json

    # Verificar que se registró el error en los logs
    logs = client.log_capture.get_logs()
    assert "WARNING" in logs, "Debe resgistrarse un mesanje de nivel WARNING para errores 405"

# def test_internal_server_error(client):
#    """Test GET /test-error - should return 500 error"""
#    response = client.get("/test-error")
#    assert response.status_code == 500
#    assert "error" in response.json or "message" in response.json
#
#    # Verificar que se registro el error en los logs
#    logs = client.log_capture.get_logs()
#    assert "ERROR": in logs, "Debe registrarse un mensaje de nivel ERROR para errores 500"
#    assert "test-error" in logs, "El log debe incluir información de la ruta que causó el error"
