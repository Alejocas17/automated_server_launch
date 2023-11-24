from fastapi import HTTPException, status
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, Response
from app.routers.riseServer import router as router_server
import uvicorn

# def create_tables():
#     Base.metadata.create_all(bind=engine)

# create_tables()
app = FastAPI()

app.include_router(router_server)
#Allow connections from frontend
@app.middleware("http")
async def add_cors_headers(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

@app.options("/{path:path}")
async def options_handler(path: str, response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"



if __name__=='__main__':
    uvicorn.run("main:app",port=8000,reload=True,host="localhost")