import os
from contextlib import asynccontextmanager

import boto3
from context import aws_clients
from fastapi import FastAPI, Depends
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from mangum import Mangum

from router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    session = boto3.Session()
    aws_clients['ssm_client'] = session.client("ssm")
    yield

app = FastAPI(
    root_path='/core',
    docs_url='/docs',
    openapi_url='/openapi.json',
    lifespan=lifespan
)

@app.get("/docs")
async def get_documentation():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.get("/openapi.json")
async def openapi():
    return get_openapi(title="App API",
                       version="0.1.0",
                       routes=app.routes,
                       description="<br>".join(["Use with care"])
                       )

app.include_router(router)

handler = Mangum(app, api_gateway_base_path=os.getenv('ROOT_PATH'))
