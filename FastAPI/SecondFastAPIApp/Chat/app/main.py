from app.configurations import configuration
from app.routers import index

from fastapi import FastAPI


app = FastAPI()
configuration.mount_static(app)

app.include_router(index.router)