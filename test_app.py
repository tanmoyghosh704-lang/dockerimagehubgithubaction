from fastapi.testclient import TestClient
from app import app
import json

client=TestClient(app)

def test_server():
    response=client.get("/")
    assert response.status_code==200
    assert response.json()=="hello!"
    