import logging

from fastapi import FastAPI

from .api import search

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def read_root():
    logger.info("Root endpoint accessed.")
    return {"Hello": "World"}


app.include_router(search.router)
