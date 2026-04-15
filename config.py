import os
from dotenv import load_dotenv

# Load local .env file if it exists (for local testing)
load_dotenv()

class Config(object):
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    # Add other variables here...
  
