import uvicorn
from app.db.pg_connection import postgres_connection
from app.db.redis_connection import redis_connection

from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging

logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def life_span(app: FastAPI):
    logging.info("Server is starting...")

    try:
        await postgres_connection.init_db()
        await redis_connection.connect()
        yield
    except Exception as e:
        logging.error(f"Error during startup: {e}")
        raise e
    finally:
        logging.info("Server has been stopped...")
        await postgres_connection.close_db()
        await redis_connection.disconnect()

app = FastAPI(
    title="Current-ly API",
    version="1.0.0",
    description="An API for discovering and reporting outages for utilities.",
    debug=True,
    contact={
        "name": "API Support",
        "email": "support@support.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url=None,
    lifespan=life_span,
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Current-ly API!"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
