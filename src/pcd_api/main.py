from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pcd_api.core.config import Settings
from pcd_api.api.v1.api import api_router

app = FastAPI(title=Settings.project_name)
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router, prefix=Settings.api_v1_str)

@app.get("/", tags=["Root"])
async def read_root():
    return {"mensagem": "WSPcd API!"}

