"""
Enunciado:
Desarrolla un servidor web básico utilizando la biblioteca http.server de Python.
El servidor debe responder a una petición GET en la ruta raíz.

1. `GET /`: Devuelve un mensaje de saludo en texto plano con el contenido "¡Hola mundo!".

Esta es una introducción simple a los servidores HTTP en Python para entender cómo crear
una aplicación web básica sin usar frameworks y responder a solicitudes HTTP.

Tu tarea es completar la implementación de la clase MyHTTPRequestHandler.

Nota: Si deseas cambiar el idioma del ejercicio, edita el archivo de test correspondiente (ej2a1_test.py).
"""

from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Manejador de peticiones HTTP personalizado
    """

    def do_GET(self):
        """
        Método que se ejecuta cuando se recibe una petición GET.
        Debes implementar la lógica para responder a la petición GET en la ruta raíz ("/")
        con el mensaje "¡Hola mundo!" en texto plano.

        Para otras rutas, devuelve un código de estado 404 (Not Found).
        """
        # Implementa aquí la lógica para responder a las peticiones GET
        # 1. Verifica la ruta solicitada (self.path)
        # 2. Si la ruta es "/", envía una respuesta 200 con el mensaje "¡Hola mundo!"
        # 3. Si la ruta es cualquier otra, envía una respuesta 404
        pass


def create_server(host="localhost", port=8000):
    """
    Crea y configura el servidor HTTP
    """
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    return httpd

def run_server(server):
    """
    Inicia el servidor HTTP
    """
    print(f"Servidor iniciado en http://{server.server_name}:{server.server_port}")
    server.serve_forever()

if __name__ == '__main__':
    server = create_server()
    run_server(server)

import pytest
import threading
import request
import time
from ej1a1 import create_server

@pytest.fixture
def server():
    """
    Fixture para iniciar y detener el servidor HTTP durante las pruebas.
    """
    # Crear el servidor en un puerto específico para pruebas
    server = create_server(host="localhost", port=8888)

    # Iniciar el servidor en un hilo separado
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

    # Esperar un momento para el servidor se inicie
    time.sleep(0.5)

    yield server

    # Detener el servidor después de las pruebas
    server.shutdown()
    server.server_close()
    thread.join(1)

def test_root_endpoint(server):
    """
    Prueba el endpoint / para validar que devuelve el mensaje correcto.
    """
    response = requests.get("http://localhost:8888/")
    assert response.status_code == 200, "El código de estado debe ser 200."
    # Comparing the exact bytes representation rather than the the string
    assert "Hola mundo" in response.text, "El mensaje debe contener 'Hola mundo'"

def test_nonexistent_endpoint(server):
    """
    Prueba un endpoint que no existe para validar que devuelve un código de error 404.
    response = requests.get("http://localhost:8888/nonexistent")
    assert response.status_code == 404, "El código de estado debe ser 404 para rutas inexistentes."
