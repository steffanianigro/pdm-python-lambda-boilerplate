from fastapi.testclient import TestClient

class TestServiceController:

    def test_status_endpoint(self, client: TestClient):

        response = client.get(url="/service/status")
        json_response = response.json()
        assert response.status_code == 200
        assert json_response['status'] == 'ok'
