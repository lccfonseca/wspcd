from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pcd_api.core.config import Settings

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

@app.get("/", tags=["Root"])
async def read_root():
    return {"mensagem": "WSPcd API!"}