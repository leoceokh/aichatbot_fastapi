from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "DRO Chatbot"
    OPENAI_API_KEY: str
    YOUTUBE_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
