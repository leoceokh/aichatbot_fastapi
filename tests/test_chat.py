from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat():
    response = client.post("/chat", json={"messages": [{"role": "user", "content": "안녕하세요"}]})
    assert response.status_code == 200
    assert "response" in response.json()
    assert "videos" in response.json()
