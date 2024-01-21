__all__ = ("router",)
from aiogram import Router
from .comands_start import router as base_commands_router
from .user_comands import router as user_commands_router

router = Router(name=__name__)
router.include_routers(
    base_commands_router,
    user_commands_router,
)

