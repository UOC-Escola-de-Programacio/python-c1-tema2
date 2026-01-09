"""
Enunciado:
Desarrolla una aplicación web con Flask que demuestre diferentes formas de acceder a la
información enviada en las solicitudes HTTP. Esta aplicación te permitirá entender cómo
procesar diferentes tipos de datos proporcionados por los clientes.

Tu aplicación debe implementar los siguientes endpoints:

1. `GET /headers`: Devuelve los encabezados (headers) de la solicitud en formato JSON.
   - Muestra información como User-Agent, Accept-Language, etc.

2. `GET /browser`: Analiza el encabezado User-Agent y devuelve información sobre:
   - El navegador que está usando el cliente
   - El sistema operativo
   - Si es un dispositivo móvil o no

3. `POST /echo`: Acepta cualquier tipo de datos y devuelve exactamente los mismos datos
   en la misma forma que fueron enviados. Debe manejar:
   - JSON
   - Datos de formulario (form data)
   - Texto plano

4. `POST /validate-id`: Valida un documento de identidad según estas reglas:
   - Debe recibir un JSON con un campo "id_number"
   - El ID debe tener exactamente 9 caracteres
   - Los primeros 8 caracteres deben ser dígitos
   - El último carácter debe ser una letra
   - Devuelve JSON indicando si es válido o no

Esta actividad te enseñará cómo acceder y manipular datos de las solicitudes HTTP,
una habilidad fundamental para crear APIs robustas y aplicaciones web interactivas.
"""

from flask import Flask, jsonify, request
import re

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/headers', methods=['GET'])
    def get_headers():
        """
        Devuelve los encabezados (headers) de la solicitud en formato JSON.
        Convierte el objeto headers de la solicitud en un diccionario.
        """
        # Implementa este endpoint:
        # 1. Accede a los encabezados de la solicitud usando request.headers
        # 2. Convierte los encabezados a un formato adecuado para JSON
        # 3. Devuelve los encabezados como respuesta JSON



    @app.route('/browser', methods=['GET'])
    def get_browser_info():
        """
        Analiza el encabezado User-Agent y devuelve información sobre el navegador,
        sistema operativo y si es un dispositivo móvil.
        """
        # Implementa este endpoint:
        # 1. Obtén el encabezado User-Agent de request.headers
        # 2. Analiza la cadena para detectar:
        #    - El nombre del navegador (Chrome, Firefox, Safari, etc.)
        #    - El sistema operativo (Windows, macOS, Android, iOS, etc.)
        #    - Si es un dispositivo móvil (detecta cadenas como "Mobile", "Android", "iPhone")
        # 3. Devuelve la información como respuesta JSON
        pass

    @app.route('/echo', methods=['POST'])
    def echo():
        """
        Devuelve exactamente los mismos datos que recibe.
        Debe detectar el tipo de contenido y procesarlo adecuadamente.
        """
        # Implementa este endpoint:
        # 1. Detecta el tipo de contenido de la solicitud con request.content_type
        # 2. Según el tipo de contenido, extrae los datos:
        #    - Para JSON: usa request.get_json()
        #    - Para form data: usa request.form
        #    - Para texto plano: usa request.data
        # 3. Devuelve los mismos datos con el mismo tipo de contenido
        pass

    @app.route('/validate-id', methods=['POST'])
    def validate_id():
        """
        Valida un documento de identidad según reglas específicas:
        - Debe tener exactamente 9 caracteres
        - Los primeros 8 caracteres deben ser dígitos
        - El último carácter debe ser una letra
        """
        # Implementa este endpoint:
        # 1. Obtén el campo "id_number" del JSON enviado
        # 2. Valida que cumpla con las reglas especificadas
        # 3. Devuelve un JSON con el resultado de la validación
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

import pytest
from flask.testing import FlaskClient
from ej2e1 import create_app
import json

@pytest.fixture
def client() -> FlaskClient:
   app = create_app()
   app.testing = True
   with app.test_client() as client
      yield client

def test_headers_endpoint(client):
   """
   Prueba el endpoint / headers para verificar que devuelve los encabezados HTTP.
   """
   # Envía una solicitud con encabezados personalizados
   headers = {
      'X-Test-Header': 'test-value'
      'User-Agent': 'Test-Browser/1.0'
      'Acceot-Language': 'es-ES, es;q=0.9, en;q=0.8'
   }
   response = client.get("/headers", headers=headers)

   # Verifica la respuesta
   assert response.status_code == 200, "El código de estado debe ser 200"
   assert response.is_json, "La respuesta debe ser JSON"

   # Verifica que los encabezos enviados estén presentes en la respuesta
   response_data = response.get_json()
   assert 'X-Test-Header' in response_data, "El encabezado personalizado debe estar en la respuesta"
   assert response_data['X-Test-Header'] == 'test-value', "El valor del encabezado debe ser correcto"
   assert 'User-Agent' in response_data, "El encabezado User-Agent debe estar en la respuesta"
   assert 'Accept-Language' in response_data, "El encabezado Accept-Language debe estar en la rspuesta"

def test_browser_info_endpoint(client):
   """ 
   Prueba  el endpoint /browser para verifcar que analiza
   correctamente el encabezado User-Agent.
   """
   # Caso 1: Un navegador Chrone en WINDOWS
   headers = {
      'User-Agent': 'Mozila/5.0 (Windows NT 10.0; Wind64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
   }
   response = client.get("/browser", headers=headers)

   # Verifica la respuesta 
   assert response.status_code == 200, "El código de estado debe ser 200"
   assert response.is_json, "La respuesta debe ser JSON"

   # Verifica que la información del navegadro sea correcta
   browser_info = response.get_json()
   assert 'browser' in browser_info, "La respuesta debe incluir información del navegador"
   assert 'Chrome' in browser_info['browser'], "Debe detectar Chrome como navegador"
   assert 'os' in browser_info, "La respuesta debe incluir información del sistema operativo"
   assert 'Windows' in browser_info['os'], "Debe detectar Windows como sistema operativo"
   assert 'is_mobile' in browser_info, "La respuesta debe indicar si es un dispositivo móvil" 
   assert browser_info['is_mobile'] == False, "Debe detectar que no es un dispositivo móvil"

   # Caso 2: Un navegador en iPhone (móvil)
   headers = {
      'Usert-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
    }
   response = client.get("/browser", headers= headers)
   browser_info = response.get_json()

   assert 'Safari' in browser_info['browser'] "Debe detectar Safari como navegador"
   assert 'iPhone' in browser_info['os'] or 'iOS' in browser_info['os'] "Debe detectar iPhone/iOS como sistema operativo"
   assert browser_info['is_mobile'] == True,  "Debe detectar que es un dispositivo móvil"

def test_echo_endpoint_json(client):
   """
   Prueba el endpoint /echo con datos JSON.
   """
   test_data =  {"message": "Hola Mundo", "value": 42, "list": [1, 2, 3]}
   response = client.post("/echo", json=test_data)

   # Verifica la respuesta
   assert response.status_code == 200, "El código de estado debe ser 200"
   assert response.is_json, "La respuesta debe ser JSON"
   assert response.get_json() == "Los datos devueltos deben ser idénticos a los enviados"

def test_echo_endpoint_form(client)
    """
    Prueba el endpoint /echo con datos de formulario.
    """
    form_data = {"name": "Juan Pérez", "email": "juan@example.com"}

    response = client.post("/echo", data=form_data)

    # Verifica la respuesta
    assert response.status_code == 200, "El código de estado debe ser 200"
    # La respuesta debe contener los datos del formulario
    # Nota: la respuesta podría ser JSON o form-urlencoded, aceptamos ambos
    if response.is_json:
       assert response.get_json() == form_data, "Los datos devueltos deben ser idénticos a los enviados"
    else:
       for key, value in form_data.items():
       assert key in response.data.decode(), "La clave debe estar en la respuesta"
       assert value in response.data.decode(), "El valor debe estar en la respuesta"

def test_echo_endpoint_plain_test(client):
    """
    Prueba el endpoint /echo con texto plano.
    """
    plain_text = "Este es un texto de prueba"

    response = client.post(
        "/echo",
        data=plain_text,
        headers={"Content-Type": "text/plain"}
    )

    # Verifica la respuesta
    assert response.status_code == 200, "El código de estado debe ser 200"
    assert response.data.decode() == plain_text, "El texto devuelto debe ser idéntico al enviado"

def test_validate_id_valid(client):
    """
    Prueba el endpoint /validate-id con un ID válido.
    """
    # ID válido: 8 dígitos + 1 letra
    valid_id = {"id_number": "12345678A"}

    response = client.post("/validate-id", json=valid_id)

    # Verifica la respuesta
    assert response.status_code == 200, "El código de estado debe ser 200"
    assert response.is_json, "La respuesta debe ser JSON"

    result = response.get_json()
    assert "valid" in result, "La respuesta debe indicar si el ID es válido"
    assert result["valid"] == True, "El ID debe considerarse válido"

def test_validate_id_invalid_length(client):
    """
    Prueba el endpoint /validate-id con un ID de longitud incorrecta.
    """
    # ID demasiado corto
    short_id = {"id_number": "1234567A"}

    response = client.post("/validate-id", json=short_id)
    assert response.status_code == 200
    assert response.get_json()["valid"] == False

    # ID demasiado largo
    long_id = {"id_number": "123456789A"}

    response = client.post("/validate-id", json=long_id)
    assert response.status_code == 200
    assert response.get_json()["valid"] == False


def test_validate_id_invalid_format(client):
    """
    Prueba el endpoint /validate-id con un ID en formato incorrecto.
    """
    # Primeros caracteres no son dígitos
    non_digit_id = {"id_number": "1234567XA"}

    response = client.post("/validate-id", json=non_digit_id)
    assert response.status_code == 200
    assert response.get_json()["valid"] == False

    # Último carácter no es letra
    non_letter_id = {"id_number": "123456789"}

    response = client.post("/validate-id", json=non_letter_id)
    assert response.status_code == 200
    assert response.get_json()["valid"] == False


def test_validate_id_missing_field(client):
 """
    Prueba el endpoint /validate-id con datos incompletos.
    """
    # JSON sin el campo requerido
    incomplete_data = {"some_other_field": "value"}

    response = client.post("/validate-id", json=incomplete_data)
    assert response.status_code == 400, "Debe devolver 400 Bad Request cuando falta el campo requerido"
    assert response.is_json, "La respuesta debe ser JSON"
    assert "error" in response.get_json(), "La respuesta debe incluir un mensaje de error"

   
