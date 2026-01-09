"""
Enunciado:
Desarrolla una aplicación web con Flask que procese diferentes tipos MIME (Multipurpose Internet Mail Extensions)
recibidos en solicitudes HTTP. Esta aplicación te permitirá entender cómo recibir y procesar
diferentes formatos de datos enviados por los clientes.

Los tipos MIME son fundamentales en el desarrollo web ya que indican cómo interpretar los datos
recibidos en las solicitudes HTTP. Una API robusta debe poder manejar diversos formatos de entrada.

Tu aplicación debe implementar los siguientes endpoints:

1. `POST /text`: Recibe un texto plano con el tipo MIME `text/plain` y lo devuelve en la respuesta.
   - Ejemplo de uso: Procesar mensajes simples o logs enviados por el cliente.

2. `POST /html`: Recibe un fragmento HTML con el tipo MIME `text/html` y lo devuelve en la respuesta.
   - Ejemplo de uso: Recibir contenido HTML para almacenar o procesar.

3. `POST /json`: Recibe un objeto JSON con el tipo MIME `application/json` y lo devuelve en la respuesta.
   - Ejemplo de uso: Procesar datos estructurados en APIs RESTful.

4. `POST /xml`: Recibe un documento XML con el tipo MIME `application/xml` y lo devuelve en la respuesta.
   - Ejemplo de uso: Procesar configuraciones o datos estructurados en formato XML.

5. `POST /image`: Recibe una imagen con el tipo MIME `image/png` o `image/jpeg` y la guarda en el servidor.
   - Ejemplo de uso: Subir imágenes para un perfil de usuario o una galería.

6. `POST /binary`: Recibe datos binarios con el tipo MIME `application/octet-stream` y confirma su recepción.
   - Ejemplo de uso: Recibir archivos genéricos como PDFs o archivos comprimidos.

Tu tarea es completar la implementación de la función create_app() y de los endpoints solicitados,
asegurándote de identificar correctamente el tipo MIME de cada solicitud y procesarla adecuadamente.

Esta actividad te enseñará cómo recibir y manejar diferentes tipos de datos en solicitudes HTTP,
una habilidad esencial para desarrollar APIs web que interactúan con diversos clientes.
"""

from flask import Flask, jsonify, request, Response
import os

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    # Crear un directorio para guardar archivos subidos si no existe
    uploads_dir = os.path.join(app.instance_path, 'uploads')
    os.makedirs(uploads_dir, exist_ok=True)

    @app.route('/text', methods=['POST'])
    def post_text():
        """
        Recibe un texto plano con el tipo MIME `text/plain` y lo devuelve en la respuesta.
        """
        # Implementa este endpoint:
        # 1. Verifica que el Content-Type sea text/plain
        # 2. Lee el contenido de la solicitud usando request.data
        # 3. Devuelve el mismo texto con Content-Type text/plain
        pass

    @app.route('/html', methods=['POST'])
    def post_html():
        """
        Recibe un fragmento HTML con el tipo MIME `text/html` y lo devuelve en la respuesta.
        """
        # Implementa este endpoint:
        # 1. Verifica que el Content-Type sea text/html
        # 2. Lee el contenido de la solicitud
        # 3. Devuelve el mismo HTML con Content-Type text/html
        pass

    @app.route('/json', methods=['POST'])
    def post_json():
        """
        Recibe un objeto JSON con el tipo MIME `application/json` y lo devuelve en la respuesta.
        """
        # Implementa este endpoint:
        # 1. Accede al contenido JSON usando request.get_json()
        # 2. Devuelve el mismo objeto JSON usando jsonify()
        pass

    @app.route('/xml', methods=['POST'])
    def post_xml():
        """
        Recibe un documento XML con el tipo MIME `application/xml` y lo devuelve en la respuesta.
        """
        # Implementa este endpoint:
        # 1. Verifica que el Content-Type sea application/xml
        # 2. Lee el contenido XML de la solicitud
        # 3. Devuelve el mismo XML con Content-Type application/xml
        pass

    @app.route('/image', methods=['POST'])
    def post_image():
        """
        Recibe una imagen con el tipo MIME `image/png` o `image/jpeg` y la guarda en el servidor.
        """
        # Implementa este endpoint:
        # 1. Verifica que el Content-Type sea image/png o image/jpeg
        # 2. Lee los datos binarios de la imagen
        # 3. Guarda la imagen en el directorio 'uploads' con un nombre único
        # 4. Devuelve una confirmación con el nombre del archivo guardado
        pass

    @app.route('/binary', methods=['POST'])
    def post_binary():
        """
        Recibe datos binarios con el tipo MIME `application/octet-stream` y confirma su recepción.
        """
        # Implementa este endpoint:
        # 1. Verifica que el Content-Type sea application/octet-stream
        # 2. Lee los datos binarios de la solicitud
        # 3. Guarda los datos en un archivo o simplemente verifica su tamaño
        # 4. Devuelve una confirmación con información sobre los datos recibidos
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

import pytest
from flask.testing import FlaskClient
from ej2e3 import create_app
import io
import os

@pytest.fixture
def client() -> FlaskClient:
   app = create_app()
   with app.test_client() as client:
      yield client

def test_post_text(client):
    response = client.post("/text", data="Este es un texto de prueba", content_type="text/plain")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Este es un texto de prueba"
    assert response.content_type == "text/plain"

def test_post_html(client):
    response = client.post("/html", data="<h1>Prueba HTML<H1>", content_type="text/html")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "<h1>Prueba HTML<H1>"
    assert response.content_type == "text/html"

def test_post_json(client):
    response = client.post("/json", json={"key": "value"})  
    assert response.status_code == 200
    assert response.json == {"key": "value"})
    assert response.content_type == "application/json"

def test_post_xml(client):
    xml_data = "<root><key>value</key></root>"
    response = client.post("/xml", data=xml_data, content_type="application/xml")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == xml_data
    assert response.content_type == "application/xml"

def test_post_image(client):
   """
   Test POST/ image endpoint -should accept an image file and save it
   """
   # Create a test image using scipy.misc.face()
   from scipy import misc
   import numpy as np
   from PIL import Image

   # Get the face image from scipy
   face = misc.face()

   # Convert to bytes in PNG format
   img = Image.fromarray(face)
   img_bytes_io = io.BytesIO()
   img.save(img_bytes_io, format='PNG')
   img_bytes = img_bytes_io_getvalue()

   #Send image
   response = client.post(
      "/image",
      data=img_bytes,
      content_type="image/png"

   # Check response
    assert response.status_code == 200
    assert response.is_json
    assert "mensaje" in response.json
    assert "archivo" in response.json

def test_post_binary(client):
   # Create some binary data
   binary_data = os.urandom(64) # 64 random bytes

   # Send the binary data
   response = client.post(
      "/binary",
      data=binary_data,
      content_type="application/octet-stream"
   )

   # Check response
    assert response.status_code == 200
    assert response.is_json
    assert "mensaje" in response.json
    assert "tamaño" in response.json
    assert response.json["tamaño"] == 64  # Should match the size of our test data
