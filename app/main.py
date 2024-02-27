import uvicorn
from app.core.app import create_app

app = create_app()


def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=3000, reload=True)
