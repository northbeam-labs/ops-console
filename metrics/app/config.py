from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "metrics"
    env: str = "local"
    db_url: str = "postgresql://app:app@localhost/app"
    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"
    access_ttl_min: int = 30
    page_size: int = 50

    class Config:
        env_file = ".env"


settings = Settings()
