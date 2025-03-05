import pytest
from clients.auth.models.auth_user import AuthUser
from middleware.jwt_authorizer import JWTAuthorizer

TEST_TOKEN = "Bearer test_token"

@pytest.fixture(name="jwt_authorizer", scope='function')
def jwt_authorizer_fixture():
    yield JWTAuthorizer()

class TestJWTAuthorizer:

    def test_jwt_authorizer(self, jwt_authorizer: JWTAuthorizer):
        print(jwt_authorizer)

        result = jwt_authorizer(TEST_TOKEN)
        assert result == AuthUser(
            id="",
            email=""
        )
