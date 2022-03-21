import os
import sys
if sys.platform == "win32":
    os.system('color')  # enable ANSI terminal colors on Windows platforms

from dotenv import load_dotenv
load_dotenv("./.env")

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

# Setup database
from app.db.init_db import init_db
init_db()

from app.api.api_v1.api import api_router
from app.api import security

# Start app
app = FastAPI(
    title="DS-AI API",
    description="DS-AI Team algorithm library API",
    version="0.1.0"
)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    api_router,
    prefix="/api",
    dependencies=[Depends(security.api_key_security)]
)

app.include_router(
    security.api_management_router,
    prefix="/auth",
    tags=["_management_auth"]
)
