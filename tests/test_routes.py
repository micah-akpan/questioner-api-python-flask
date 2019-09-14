import pytest
from app import app

@pytest.fixture
def client():
  app.config['TESTING'] = True
  with app.test_client() as client:
    yield client

def test_home_route_a(client):
  response = client.get('/')
  assert b'Welcome to Questioner API v1' in response.data

def test_home_route_b(client):
  response = client.get('/api/v1')
  assert b'Welcome to Questioner API v1' in response.data
