from fastapi import FastAPI
from app.api.recsys import recsys
import app.db.db as db
from fastapi.middleware.cors import CORSMiddleware

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

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


app.include_router(recsys, prefix='/api/v1/recsys')
