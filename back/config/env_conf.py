from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DatabaseSettings(BaseModel):
    NAME: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int

class BackendSettings(BaseSettings):
    SECRET: str
    DEBUG: bool = False

    model_config = SettingsConfigDict(
        env_prefix="APP_CONFIG__BACKEND__",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

class Settings(BaseSettings):
    backend: BackendSettings
    db: DatabaseSettings

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__"
    )

# Initialize the settings
config = Settings()

print(config)