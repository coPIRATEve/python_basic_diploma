import os
from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr

load_dotenv()

class SiteSettings(BaseSettings):
    site_api: SecretStr = os.getenv("API_KEY", None)
    tg_api: SecretStr = os.getenv("BOT_TOKEN", None)
