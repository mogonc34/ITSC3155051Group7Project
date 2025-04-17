# Imports

import uvicorn # from code skeleton
from fastapi import Depends, FastAPI, HTTPException # from code skeleton
from fastapi.middleware.cors import CORSMiddleware # from code skeleton
# from api.routers import index as indexRoute
from .models import model_loader # from code skeleton
from .dependencies.config import conf # from code skeleton


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()
# indexRoute.load_routes(app)


if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)