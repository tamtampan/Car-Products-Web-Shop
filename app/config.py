"""Config module"""

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Class settings"""

    DB_HOST: str
    DB_HOSTNAME: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    USER_SECRET: str
    ALGORITHM: str

    DB_NAME_TEST: str
    USE_TEST_DB: bool

    """Config class"""

    class Config:
        env_file = "./.env"


settings = Settings()
