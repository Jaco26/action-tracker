from app.main import create_app
from app.config import DevConfig

app = create_app(DevConfig)