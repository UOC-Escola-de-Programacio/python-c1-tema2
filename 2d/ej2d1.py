"""
Enunciado:
Desarrolla una aplicación web básica con Flask que muestre el uso del sistema de registro (logging).

En el desarrollo web es fundamental tener un buen sistema de registro de eventos,
que permita hacer seguimiento de lo que ocurre en nuestra aplicación. Flask proporciona
un objeto logger integrado (app.logger) que permite registrar mensajes con diferentes
niveles de importancia.

Tu tarea es implementar los siguientes endpoints:

1. `GET /info`: Registra un mensaje de nivel INFO y devuelve un mensaje en texto plano.
2. `GET /warning`: Registra un mensaje de nivel WARNING y devuelve un mensaje en texto plano.
3. `GET /error`: Registra un mensaje de nivel ERROR y devuelve un mensaje en texto plano.
4. `GET /critical`: Registra un mensaje de nivel CRITICAL y devuelve un mensaje en texto plano.

Esta actividad te enseñará a utilizar el sistema de registro de Flask,
una habilidad crucial para el desarrollo y depuración de aplicaciones web.
"""

from flask import Flask, jsonify

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    # Configuración básica del logger
    # Por defecto, los mensajes se registrarán en la consola

    @app.route('/info', methods=['GET'])
    def log_info():
        """
        Registra un mensaje de nivel INFO
        """
        # Implementa este endpoint:
        # 1. Registra un mensaje de nivel INFO usando app.logger.info()
        # 2. Devuelve un mensaje en texto plano indicando que se ha registrado el mensaje
        pass

    @app.route('/warning', methods=['GET'])
    def log_warning():
        """
        Registra un mensaje de nivel WARNING
        """
        # Implementa este endpoint:
        # 1. Registra un mensaje de nivel WARNING usando app.logger.warning()
        # 2. Devuelve un mensaje en texto plano indicando que se ha registrado el mensaje
        pass

    @app.route('/error', methods=['GET'])
    def log_error():
        """
        Registra un mensaje de nivel ERROR
        """
        # Implementa este endpoint:
        # 1. Registra un mensaje de nivel ERROR usando app.logger.error()
        # 2. Devuelve un mensaje en texto plano indicando que se ha registrado el mensaje
        pass

    @app.route('/critical', methods=['GET'])
    def log_critical():
        """
        Registra un mensaje de nivel CRITICAL
        """
        # Implementa este endpoint:
        # 1. Registra un mensaje de nivel CRITICAL usando app.logger.critical()
        # 2. Devuelve un mensaje en texto plano indicando que se ha registrado el mensaje
        pass

    @app.route('/status', methods=['GET'])
    def status():
        """
        Endpoint adicional que registra diferentes mensajes según el parámetro de consulta 'level'
        Ejemplo: /status?level=warning
        """
        # Este endpoint es opcional, puedes implementarlo si quieres practicar
        # con parámetros de consulta y logging condicional
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

from pytest 
from flask.testing import FlaskClient
from ej2d1 import create_app
import logging
import io import Sring IO

class LogCaptureHandler(logging.Handler):
    """
    Manejador personalizado para capturar mensajes de log durante las pruebas
    """
    def __init__(self):
        super().__init__(9
        self.logs = StingIO()
        self.setLevel(logging.INFO)
        self.setFormatter(logging.Formatter('%(levelname)s: %(mensaje)s'))
    
    def emit(self, record):
        """Añade un mensaje de log a los logs capturados"""
        self.logs.write(self.format(record) + '/n')

    def get_logs(self):
        """Devuelve los logs capturados y reinicia"""
        logs = self.logs.getvalue()
        self.logs = StringIO()
        return logs

@pytest.fixture
del client() -> FlaskClient:
    """
    Fixture para configurar el cliente de pruebas y capturar logs
    """
    app = create_app()
    app.testing = True

    # Configurar el capturados de logs
    log_capture = LogCaptureHandler()
    app.logger.addHandler(log_capture)
    app.logger.setLevel(logging.INFO)

    with app.test_client() as client:
        client.log_capture = log_capture
        yield client

def test_ifo_endpoint(client):
    """
    Prueba el endpoint /info
    Verifica que:
    1. Devuelve un mensaja de texto
    2. El código de estado es 200
    3. Se registró un mensaje de nivel INFO
    """
    response = client.get("/info")
    assert response.status_code == 200, "El código de estado debe ser 200"
    assert response.content_type.startswith('text/plain'), "El contenido debe ser texto plano"

    logs = client.log_capture.get_logs()
    assert "INFO:" in logs, "Debe resgistrarase un mensaje de nivel INFO"

def test_warning_endpoint(client):
    """
    Prueba el endpoint /warning
    Verifica que:
    1. Devuelve un mensaja de texto
    2. El código de estado es 200
        3. Se registró un mensaje de nivel WARNING
    """
    response = client.get("/warning")
    assert response.status_code == 200, "El código de estado debe ser 200"
    assert response.content_type.startswith('text/plain'), "El contenido debe ser texto plano"

    logs = client.log_capture.get_logs()
    assert "WARNING:" in logs, "Debe resgistrarase un mensaje de nivel WARNING"

def test_error_endpoint(client):
       """
    Prueba el endpoint /error
    Verifica que:
    1. Devuelve un mensaja de texto
    2. El código de estado es 200
    3. Se registró un mensaje de nivel ERROR
    """
    response = client.get("/error")
    assert response.status_code == 200, "El código de estado debe ser 200"
    assert response.content_type.startswith('text/plain'), "El contenido debe ser texto plano"

    logs = client.log_capture.get_logs()
    assert "ERROR:" in logs, "Debe resgistrarase un mensaje de nivel ERROR"

def test_critical_endpoint(client):
       """
    Prueba el endpoint /critical
    Verifica que:
    1. Devuelve un mensaja de texto
    2. El código de estado es 200
    3. Se registró un mensaje de nivel CRITICAL
    """
    response = client.get("/critical")
    assert response.status_code == 200, "El código de estado debe ser 200"
    assert response.content_type.startswith('text/plain'), "El contenido debe ser texto plano"

    logs = client.log_capture.get_logs()
    assert "CRITICAL:" in logs, "Debe resgistrarase un mensaje de nivel CRITICAL"

def test_status_endpoint_with_level(client):
       """
    Prueba el endpoint /status con parámetro level
    Este test es opcional, solo se ejecutará si el endpoint está implementado
    """
    try:
        # Intentar diferentes niveles
        response = client.get("/status?level=warning")
        assert response.status_code == 200, "El código de estado debe ser 200"
        logs = client.log_capture.get_logs(9    
        assert "WARNING:" in logs
        
    response = client.get("/status?level=warning")
    assert response.status_code == 200
    logs = client.log_capture.get_logs()
    assert "ERROR:" in logs  
except:
    # Si el endpoint no está implementado, la prueba se omite
    pytest.skip("El endpoint / status no está implementado")
