from typing import Annotated

from clients.auth.models.auth_user import AuthUser

from exceptions import UNAUTHORISED_EXCEPTION
from fastapi import Header


class JWTAuthorizer:

    def __call__(self, authorization: Annotated[str | None, Header()] = None):

        if not authorization:
            raise UNAUTHORISED_EXCEPTION
        split_authorization_tokens: list[str] = authorization.split("Bearer ")

        if len(split_authorization_tokens) < 2:
            raise UNAUTHORISED_EXCEPTION

        token: str = split_authorization_tokens[1]
        print(token)

        # TODO validate token
        return AuthUser(
            id='',
            email='',
        )


jwt_authorizer = JWTAuthorizer()