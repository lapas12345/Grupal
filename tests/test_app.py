"""
Tests para la aplicación Flask
"""
import pytest
from src.app import app

@pytest.fixture
def client():
    """Cliente de prueba"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    """Test del endpoint principal"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Hello, Secure World!"

def test_data_endpoint(client):
    """Test del endpoint de datos"""
    response = client.get('/api/data?query=test')
    assert response.status_code == 200
    data = response.get_json()
    assert 'Processed: test' in data['data']

def test_data_endpoint_long_query(client):
    """Test de validación de entrada"""
    long_query = 'a' * 101  # Query muy larga
    response = client.get(f'/api/data?query={long_query}')
    assert response.status_code == 400
