from fastapi import HTTPException, status
from fastapi import FastAPI
from fastapi import APIRouter,Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
import subprocess
import time
import os
import pandas as pd
from pydantic import BaseModel
from extractData import run as findUserKpis


router = APIRouter(
    prefix="/api",
    tags = ["MCweb"],
)

class UserData(BaseModel):
    userName: str



############################### Endpoints for MCWEB #############################


#Endpoint for Get one user filtered by id
# @router.get("/createServers/{n}/{route_map}")
# async def createServers(n,route_map:str):
#     path_create = './create.py'
#     path_remove = './remove.py'
#     args = [n,"./"+route_map]
#     subprocess.run(['python',path_remove]+args)
#     time.sleep(5)
#     subprocess.run(['python',path_create]+args)
    
# @router.get("/createServers/{n}/{route_map}")
# async def createServers(n:int,route_map:str):
#     path_create = './create.py'
#     path_remove = './remove.py'
#     args = [n,"./"+route_map]
#     comando = f'python {path_remove} {n} {str(args[1])} && timeout /t 1 && python {path_create} {n} {str(args[1])}'

#     # Especifica el nombre del archivo batch y la ruta donde se guardará
#     nombre_archivo = 'init_servers.bat'
#     ruta_archivo = './'

#     # Crea el archivo batch
#     with open(os.path.join(ruta_archivo, nombre_archivo), 'w') as archivo:
#         archivo.write(comando)
#     subprocess.run('init_servers.bat')

@router.post("/getPerformance")
async def getPerformance(userData:UserData):
    performance = findUserKpis(userData.userName)
    
    if (performance == False):
        return {[]}
    else :
        print("este es el performance: ",performance)

        # performance = [i["kpi"].replace("kpi", "") for i in performance]            
        for i in performance:
            for key in list(i.keys()):
                i[key.lower()] = i.pop(key).replace("kpi", "")

        return performance    