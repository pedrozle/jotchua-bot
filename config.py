import os
from pathlib import Path
from dotenv import load_dotenv

class Settings:
    dotenv_path = Path(".env")
    load_dotenv(dotenv_path=dotenv_path)

    # Database configurations
    DB_USER = os.getenv("DB_USER", "")
    DB_PASS = os.getenv("DB_PASS", "")
    DB_SERVER = os.getenv("DB_SERVER", "")

    # Bot configurations
    DEBUG = bool(os.getenv("DEBUG", "False") == "True")
    print("Serving in: " + ("DEBUG" if DEBUG else "PRODUCTION") + " mode")
    BOT_TOKEN = os.getenv("BOT_TOKEN_DEV") if DEBUG else os.getenv("BOT_TOKEN")

def get_settings():
    return Settings()