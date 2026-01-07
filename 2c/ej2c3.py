"""
Enunciado:
Desarrolla una API REST utilizando Flask que permita filtrar productos según diferentes criterios.

En APIs REST, es común necesitar obtener subconjuntos de datos basados en ciertos criterios.
Esto se implementa habitualmente mediante parámetros de consulta (query parameters) en la URL.
Por ejemplo: /products?min_price=500&category=electronics

Tu tarea es implementar el siguiente endpoint con capacidades de filtrado:

`GET /products`: Devuelve una lista de productos que se puede filtrar según diferentes criterios.
Debe admitir los siguientes parámetros de consulta:
- `category`: Filtrar productos por categoría
- `min_price`: Filtrar productos con precio igual o mayor al valor especificado
- `max_price`: Filtrar productos con precio igual o menor al valor especificado
- `name`: Filtrar productos cuyo nombre contenga la cadena especificada (búsqueda parcial)

Si no se proporciona ningún parámetro, debe devolver todos los productos.

Requisitos:
- Utiliza la lista de productos proporcionada.
- Los filtros deben poder combinarse entre sí (por ejemplo, filtrar por categoría Y precio mínimo).
- Devuelve las respuestas en formato JSON utilizando la función jsonify() de Flask.
- Asegúrate de devolver un código 200 (OK) incluso si no hay productos que cumplan los filtros.

Ejemplos:
1. `GET /products` debe devolver todos los productos.
2. `GET /products?category=electronics` debe devolver solo productos de categoría "electronics".
3. `GET /products?min_price=500&max_price=1000` debe devolver productos con precio entre 500 y 1000.
4. `GET /products?name=pro` debe devolver productos cuyo nombre contenga "pro" (como "Laptop Pro").
"""

from flask import Flask, jsonify, request

# Lista de productos predefinida con categorías
products = [
    {"id": 1, "name": "Laptop Pro", "price": 999.99, "category": "electronics"},
    {"id": 2, "name": "Smartphone X", "price": 699.99, "category": "electronics"},
    {"id": 3, "name": "Tablet Mini", "price": 349.99, "category": "electronics"},
    {"id": 4, "name": "Office Desk", "price": 249.99, "category": "furniture"},
    {"id": 5, "name": "Ergonomic Chair", "price": 189.99, "category": "furniture"},
    {"id": 6, "name": "Coffee Maker Pro", "price": 89.99, "category": "appliances"},
    {"id": 7, "name": "Wireless Headphones", "price": 129.99, "category": "electronics"},
    {"id": 8, "name": "Smart Watch", "price": 199.99, "category": "electronics"}
]

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/products', methods=['GET'])
    def get_products():
        """
        Devuelve una lista de productos filtrada según los parámetros de consulta.
        Parámetros admitidos:
        - category: Filtrar por categoría
        - min_price: Precio mínimo
        - max_price: Precio máximo
        - name: Buscar por nombre (coincidencia parcial)
        """
        # Implementa aquí el filtrado de productos según los parámetros de consulta
        # 1. Obtén los parámetros de consulta usando request.args
        # 2. Filtra la lista de productos según los parámetros proporcionados
        # 3. Devuelve la lista filtrada en formato JSON con código 200
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True

import pytest
from flask.testing import FlaskClient
from ej2c3 import create_app

@pytest.fixture
del client() -> FlaskClient:
app = create_app()
app.testing = True
with app.test_client() as client:
    yield client

def test_get_all_products(client):
    """
    Prueba obtener todos los productos sin filtros
    """
    response = client.get("/products")
    assert response.status_code == 200
    data = response.json
    assert len(data) == 8 # Verifica que se devuelven todos los productos

def test_filter_by_category(client):
    """
    Prueba filtrar productos por categoría
    """
    # Filtrar por categoría "electronics"
    response = client.get ("/products?category=electronics")
    assert response.status_code == 200
    data = response.json
    assert len(data) == 4 # Debería haber 4 productos electrónicos
    for product in data:
        assert product ["category"] == "electronics"
    
    # Filtrar por categoría "furniture"
    response = client.get ("/products?category=furniture")
    assert response.status_code == 200
    data = response.json
    assert len(data) == 2 # Debería haber 2 productos de mobiliario
    for product in data:
        assert product ["category"] == "furniture"


def test_filter_by_price_range(client):
    """
    Prueba filtrar productos por rango de precios
    """
    # Filtrar productos con precio >= 500
    response = client.get("products?min_price=500")
    assert response.status_code == 200
    data = response.json
    assert len(data) == 2 # Debería haber 2 productos con precio >= 500
    for product in data:
        assert product["price"] >= 500
        
    # Filtrar productos con precio <= 200
    response = client.get("products?max_price=200")
    assert response.status_code == 200
    data = response.json
    assert len(data) == 4 # Debería haber 4 productos con precio <= 200
    for product in data:
        assert product["price"] <= 200
    
    # Filtrar productos con precio entre 200 y 700
    response = client.get("/products?min_price=200&max_price=700")
    assert response.status_code == 200
    data = response.json
    assert len(data) == 3 # Debería haber 3 productos en ese rango
    for product in data:
        assert product["price"] >= 200 and product["price"] <= 700


def test_filter_by_name(client):
    """
    Prueba filtrar productos por nombre (búsqueda parcial)
    """
    # Filtrar productos que contengan "Pro" en el nombre
    response = client.get("/products?name=Pro")
    assert response.status_code == 200
    data = response.json
    assert len(data) == 2 # Debería haber 2 productos con "Pro" en el nombre
    for product in data:
        assert "Pro" in product["name"]
        
def test_combined_filters(client):
    """
    Prueba combinar varios filtros
    """
    # Filtrar productos electrónicos con precio >= 500
    response = client.get("/products?category=electronics&min_price=500")
    assert response.status_code == 200
    data = response.json
    assert len(data) == 2 # Debería haber 2 productos que cumplan ambos criterios
    for product in data:
        assert product["category"] == "electronics"
        assert product["price"] >= 500

    # Filtrar productos con "Pro" en el nombre y precio <= 100
    response = client.get("/products?name=Pro&max_price=100")
    assert response.status_code == 200
    data = response.json
    assert len(data) == 1 # Debería haber 1 producto que cumplan ambos criterios
    assert data[0]["name"] == "Coffe Maker Pro"
    assert data[0]["price"] <= 100

def test_filter_no_results(client):
    """
    Prueba filtrar con criterios que no devuelven resultados
    """
    # Filtrar con una categoría que no existe
    response = client.get("/products?category=nonexistent")
    assert response.status_code == 200
    data = response.json
    assert len(data) == 0 # No debería haber productos

    # Filtrar con un rango de precios imposible
    response = client.get("/products?min_price=2000")
    assert response.status_code == 200
    data = response.json
    assert len(data) == 0 # No debería haber productos 


    
