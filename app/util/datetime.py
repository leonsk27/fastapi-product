from datetime import datetime
import pytz
from app.core.config import Config

timezone_app = pytz.FixedOffset(Config.TIME_ZONE * 60)

def get_current_time():
    return datetime.now(timezone_app).replace(tzinfo=None)