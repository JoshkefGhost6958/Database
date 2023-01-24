from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_NAME:str 
    USER:str 
    HOST:str
    PASSWORD:str

    class Config:
        env_file = ".env"

settings = Settings()