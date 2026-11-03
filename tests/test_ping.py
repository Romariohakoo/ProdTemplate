from fastapi.testclient import TestClient


def test_ping(client: TestClient) -> None:
    response = client.get("/api/ping")
    assert response.status_code == 200
    assert response.text == "ok"


def test_unknown_route_uses_error_format(client: TestClient) -> None:
    response = client.get("/api/unknown")
    assert response.status_code == 404
    assert "reason" in response.json()