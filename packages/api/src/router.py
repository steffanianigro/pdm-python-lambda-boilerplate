from fastapi import APIRouter

from controllers.user import user_controller
from controllers.service import service_controller

router = APIRouter()

router.include_router(service_controller.router, prefix="/service", tags=["Service"],
                      dependencies=[])
router.include_router(user_controller.router, prefix="/users", tags=["Users"],
                      dependencies=[])