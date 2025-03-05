from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

UNAUTHORISED_EXCEPTION = HTTPException(
    status_code=HTTP_401_UNAUTHORIZED, detail="Unauthorized"
)