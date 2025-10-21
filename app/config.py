import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    DATABASE_URL = os.getenv("DATABSE_URL", "postgresql://user:password@db:5432/hh_agent")
    REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
    
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smpt.gmail.com")
    SMTP_PORT = os.getenv("SMTP_PORT", "587")
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    
    HH_BASE_URL = "https://api.hh.ru"
    
    RESUME_FILE_PATH = "/app/data/resume.txt"
    VACANCIES_LIMIT = 50
    
    
settings = Settings()