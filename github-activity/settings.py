from dotenv import load_dotenv
import os

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "production")
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")
GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
