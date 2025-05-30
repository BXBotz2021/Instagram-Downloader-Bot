import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Telegram API
    API_ID = int(os.getenv("API_ID", 7813390))
    API_HASH = os.getenv("API_HASH", "1faadd9cc60374bca1e88c2f44e3ee2f")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "8168394361:AAHO-V1bqMutW-DZrSUW5d0wgMm6_MSOS88")
    
    # Redis
    REDIS_HOST = os.getenv("REDIS_HOST", "redis-16415.c228.us-central1-1.gce.redns.redis-cloud.com")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 16415))
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "lpyhkguL4VmjkU8hyF8MHmbzmsDbE7RL")
    REDIS_DB = int(os.getenv("REDIS_DB", 0))  # Usually DB index is 0 unless you're using multiple Redis databases

    # Instagram (optional)
    INSTA_USERNAME = os.getenv("INSTA_USERNAME", None)
    INSTA_PASSWORD = os.getenv("INSTA_PASSWORD", None)
    
    @property
    def has_insta_creds(self):
        return bool(self.INSTA_USERNAME and self.INSTA_PASSWORD)
