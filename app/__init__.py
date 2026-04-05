from fastapi import FastAPI

from app.routes import events, health, urls, users


def create_app() -> FastAPI:
    app = FastAPI(title="Hackathon URL Shortener")
    app.include_router(health.router)
    app.include_router(users.router)
    app.include_router(urls.router)
    app.include_router(events.router)
    return app
