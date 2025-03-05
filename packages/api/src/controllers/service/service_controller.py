from fastapi import APIRouter

from controllers.service.dto.status_rersponse_dto import StatusResponseDto

router = APIRouter()

@router.get("/status", description="Status check", response_model=StatusResponseDto)
async def status():

    return StatusResponseDto(
        status="ok"
    )