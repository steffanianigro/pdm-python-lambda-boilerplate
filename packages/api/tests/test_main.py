from fastapi.testclient import TestClient

class TestMainController:

    def test_docs_endpoint(self, client: TestClient):
        response = client.get(url="/docs")
        assert response.status_code == 200

