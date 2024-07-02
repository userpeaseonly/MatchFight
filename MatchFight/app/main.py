import logging
from fastapi import FastAPI, Request
from app.api.v1.endpoints import participants
from app.db.session import engine, Base, init_db

init_db()

app = FastAPI()



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app.include_router(participants.router, prefix="/participants", tags=["participants"])



@app.middleware("http")
async def log_requests(request: Request, call_next):  # noqa: F821
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response