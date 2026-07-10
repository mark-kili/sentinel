from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    app_name: str = "Sentinel"
    app_version: str = "0.1.0"
    timezone: str = "Africa/Nairobi"
    
    log_level: str = "INFO"

    database_url: str = "sqlite:///data/sentinel.db"

    bot_token: str = ""
    owner_user_id: int = 0
    owner_chat_id: int = 0
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

settings = Settings()