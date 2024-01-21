__all__ = ("router",)

from aiogram import Router
from .comands import router as commands_router
from .generals import router as generals_router
from .media_handlers import router as media_router
from .admin_handler import router as admin_router

router = Router(name=__name__)
router.include_routers(
    commands_router,
    media_router,
    admin_router,
)
router.include_router(generals_router)  # этот роутер всегда должен оставаться последним в очереди на обработку!
