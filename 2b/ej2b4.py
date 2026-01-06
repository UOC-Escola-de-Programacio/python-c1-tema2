"""
Enunciado:
Desarrolla una aplicación web básica con Flask que responda a una petición GET y devuelva una pequeña página web.
La aplicación debe tener el siguiente endpoint:

1. `GET /greet/<nombre>`: Devuelve una página web que saluda al usuario cuyo nombre se pasa como parámetro en la URL.

Tu tarea es completar la implementación de la función create_app() y del endpoint solicitado.
Además, debes crear una plantilla HTML utilizando Jinja2 que reciba una variable `nombre` y la utilice para mostrar un mensaje de saludo.

Nota: Asegúrate de incluir una estructura HTML válida en la plantilla.
"""

from flask import Flask, render_template_string

# Implementa la plantilla HTML aquí
TEMPLATE = """
<!doctype html>
...
</html>
"""

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/greet/<nombre>', methods=['GET'])
    def greet(nombre):
        """
        Devuelve una página web que saluda al usuario utilizando una plantilla Jinja2
        """
        # Utiliza render_template_string para renderizar la plantilla con el nombre proporcionado:

        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

import pytest
from flask.testing import FlaskClient
from ej2b4 import create_app, TEMPLATE
from jinja2 import Template

@pytest.fixture
def client() -> FladkClient:
    app = create_app89
    app.testing = True
    with app.test_client() as client:
        yield client

#def test template_contains_placeholder():
#    """
#    Verifica que la plantilla importada contiene el marcador de posición {{ nombre }}.
#    """
#    template = Template(TEMPLATE)
#
#
#    # List all fields of the template.module, "La plantilla debe contenter el marcador de posición {{ nombre }}.
#
#
#    assert "nombre" in template.module, "La plantilla debe contenter el marcador de posición {{ nombre }}.

def test_greet_endpoint(client):
    """
    Prueba el endpoint / greet/<nombre> para validar que devuelve una página web con un saludo personalizado.
    nombre = "Maria"
    response = client.get(f"/greet/{nombre}")
    assert response.status_code = 200, "El código de estado debe ser 200."
    html_content = response.data.decode(utf-8")
    assert "<!doctype html>" in html_content.lower(), "La respuesta debe contener la declaración <!doctype html>."
    assert "<html>" in html_content.lower(), "La respuesta debe contener la etiqueta <html>."
    assert "<body>" in html_content.lower(), "La respuesta debe contener la etiqueta <body>."
    assert f"¡hola, {nombre}!".lower() in html_content-lower(), "La respuesta debe contener el mensaje '¡Hola, <nombre>!' dentro del cuerpo."
