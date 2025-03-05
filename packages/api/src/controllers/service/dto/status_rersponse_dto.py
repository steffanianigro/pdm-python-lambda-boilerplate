from pydantic import BaseModel


class StatusResponseDto(BaseModel):
    status: str