import pytest
from clients.auth.models.auth_user import AuthUser
from starlette.testclient import TestClient

from main import app
from middleware.jwt_authorizer import jwt_authorizer

TEST_USER_ID = 'b50a4de4-cafa-4cb4-8e4d-1c5e8a9e1996'
TEST_EMAIL = 'test@service.xyz'

USER = AuthUser(
    id=TEST_USER_ID,
    email=TEST_EMAIL
)

async def override_auth_dependency():
    return USER

@pytest.fixture(name="client", scope='module')
def client_fixture():
    client = TestClient(app)

    app.dependency_overrides[jwt_authorizer] = override_auth_dependency

    yield client

    app.dependency_overrides = {}

@pytest.fixture(name="test_user", scope='session')
def test_user_fixture():

    return USER
