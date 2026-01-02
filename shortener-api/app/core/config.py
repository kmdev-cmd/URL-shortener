import os

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///urlshortener.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "super-secret-key-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    BASE_URL: str = os.getenv("BASE_URL", "http://localhost:8000")

settings = Settings()
