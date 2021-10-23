from fastapi import FastAPI
from app.api.recsys import recsys
from app.db.db import metadata, database, engine
from fastapi.middleware.cors import CORSMiddleware

metadata.create_all(engine)

app = FastAPI(
    openapi_url="/api/v1/recsys/openapi.json",
    docs_url="/api/v1/recsys/docs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(recsys, prefix='/api/v1/recsys')
