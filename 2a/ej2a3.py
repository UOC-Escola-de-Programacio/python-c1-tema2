"""
Enunciado:
Desarrolla una API REST básica utilizando la biblioteca http.server de Python con un endpoint que devuelve información sobre productos en formato XML.

Tu tarea es implementar el siguiente endpoint:

`GET /product/<id>`: Devuelve información sobre un producto específico por su ID.
- Si el producto existe, devuelve los datos del producto en formato XML con código 200 (OK).
- Si el producto no existe, devuelve un mensaje de error con código 404 (Not Found).

Requisitos:
- Utiliza la lista de productos proporcionada.
- Devuelve las respuestas en formato XML.
- Asegúrate de utilizar los códigos de estado HTTP apropiados.

Ejemplo:
1. Una solicitud `GET /product/1` debe devolver los datos del producto con ID 1 en formato XML y código 200.
2. Una solicitud `GET /product/999` debe devolver un mensaje de error con código 404.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Lista de productos predefinida
products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 699.99},
    {"id": 3, "name": "Tablet", "price": 349.99}
]

def dict_to_xml(tag, d):
    """
    Convierte un diccionario en un elemento XML
    """
    elem = ET.Element(tag)
    for key, val in d.items():
        child = ET.SubElement(elem, key)
        child.text = str(val)
    return elem

def prettify(elem):
    """
    Devuelve una cadena XML formateada bonita
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ").encode()

class ProductAPIHandler(BaseHTTPRequestHandler):
    """
    Manejador de peticiones HTTP para la API de productos en XML
    """

    def do_GET(self):
        """
        Método que se ejecuta cuando se recibe una petición GET.
        Debes implementar la lógica para responder a la petición GET en la ruta /product/<id>
        con los datos del producto en formato XML si existe, o un error 404 si no existe.
        """
        # Implementa aquí la lógica para responder a las peticiones GET
        # 1. Usa una expresión regular para verificar si la ruta coincide con /product/<id>
        # 2. Si coincide, extrae el ID del producto de la ruta
        # 3. Busca el producto en la lista
        # 4. Si el producto existe:
        #    a. Convierte el producto a XML usando dict_to_xml y prettify
        #    b. Devuelve el XML con código 200 y Content-Type application/xml
        # 5. Si el producto no existe, devuelve un mensaje de error XML con código 404
        pass

def create_server(host="localhost", port=8000):
    """
    Crea y configura el servidor HTTP
    """
    server_address = (host, port)
    httpd = HTTPServer(server_address, ProductAPIHandler)
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
import xml.etree.ElementTree as ET
from ej2a3 import create_server

@pytest.fixture
def server():
    """
    Fixture para iniciar y detener el servidor HTTP durante las pruebas
    """
    # Crear el servidor en un puerto específico para pruebas
    server = create_server(host="localhost", port=8890)

    # Iniciar el servidor en un hilo separado
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start(9
    # Esperar un momento para que el servidor se inicie
    time.sleep(0.5)
    # Detener el servidor después de las pruebas
    server.shutdown()
    server.server_close()
    thread.join(1)
                 
def test_get_product_exists(server):
    """
    Prueba obtener otro producto existente (ID 1)
    Debería devolver datos del producto XML con código 200
    """
    response = requests.get("http://localhost:8890/product/1")
    assert response.status_code == 200, "El código de estado debe ser 200 para un producto existente."
    assert response.headers['Content-Type'] == "application/xml", "El Content-Type debe ser application/xml"

    # Pasear la respuesta XML
    root = ET.fromstring(responde.content)

    # Verificar los valores del producto
    assert root.tag == "product", "El elemento raíz debe ser 'product'"
    assert root.find("id").text == "1"
    assert root.find("name").text == "Laptop"
    assert root.find("price").text == "999.99"

def test_get_product_exists_2(server):
    """
    Prueba obtener otro producto existente (ID 2)
    Debería devolver datos del producto XML con código 200
    """
    response = requests.get("http://localhost:8890/product/2")
    assert response.status_code == 200, "El código de estado debe ser 200 para un producto existente."
    assert response.headers['Content-Type'] == "application/xml", "El Content-Type debe ser application/xml"

    # Pasear la respuesta XML
    root = ET.fromstring(responde.content)

    # Verificar los valores del producto
    assert root.tag == "product", "El elemento raíz debe ser 'producr'"
    assert root.find("id").text == "2"
    assert root.find("name").text == "Smartphone"
    assert root.find("price").text == "699.99"

def test_get_product_not_found(server):
    """
    Prueba obtener un producto que no existe (ID 999)
    Debería devolver un mensaje de error XML con código 404
    """
    response = requests.get("http://localhost:8890/product/999")
    assert response.status_code == 404, "El código de estado debe ser 404 para un producto que no existe."
    assert response.headers['Content-Type'] == "application/xml", "El Content-Type debe ser application/xml"

    # Verificar que sea un XML de error
    assert "<error>" in response.text, "El XML debe contener un elemento 'error'"

def test_invalid_route(server):
    """
    Prueba una ruta inválida
    Debería devolver un mensaje de error XML con código 404
    """
    response = requests.get("http://localhost:8890/invalid")
    assert response.status_code == 404, "El código de estado debe ser 404 para rutas inválidas."
    assert response.headers['Content-Type'] == "application/xml", "El Content-Type debe ser application/xml"

    # Verificar que sea un XML de error
    assert "<error>" in response.text, "El XML debe contener un elemento 'error'"

