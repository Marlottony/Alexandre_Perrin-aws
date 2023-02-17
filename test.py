import json
import pytest

from app import app, employees

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_employees(client):
    response = client.get('/api/v1/employees')
    assert response.status_code == 200
    assert json.loads(response.data) == employees

def test_add_employee(client):
    new_employee = {
        'firstName': 'Test',
        'lastName': 'User',
        'emailId': 'testuser@example.com'
    }
    response = client.post('/api/v1/employees', json=new_employee)
    assert response.status_code == 201
    assert json.loads(response.data)['id'] == len(employees)

