from fastapi import APIRouter, FastAPI
from routers import routes

router = APIRouter(prefix='/api')
for route in routes:
    router.include_router(route)

app = FastAPI(title='Documentation', version='0.0.1')
app.include_router(router)