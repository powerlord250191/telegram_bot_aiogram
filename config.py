import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
    )

    bot_token: str
    admin_id: frozenset[int] = frozenset({42, 287612289})


current_dir = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(current_dir, "config_data", "config.txt")

with open(config_path, encoding="utf-8") as file:
    api_key = file.read()


settings = Settings()

BOT_TOKEN = os.getenv('BOT_TOKEN')
