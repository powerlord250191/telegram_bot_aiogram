import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
    )

    bot_token: str
    admin_id: frozenset[int] = frozenset({42, 287612289})


settings = Settings()

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_KEY = "c7ca9cdd48msh13b9bab2e4955ffp1b87f9jsncf0790864cbc"
