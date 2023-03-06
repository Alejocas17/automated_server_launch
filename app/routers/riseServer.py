from fastapi import HTTPException, status
from fastapi import FastAPI
from fastapi import APIRouter,Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
import subprocess
import time
import os
import pandas as pd

router = APIRouter(
    prefix="/server",
    tags = ["MCweb"],
)



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
    
@router.get("/createServers/{n}/{route_map}")
async def createServers(n:int,route_map:str):
    path_create = './create.py'
    path_remove = './remove.py'
    args = [n,"./"+route_map]
    comando = f'python {path_remove} {n} {str(args[1])} && timeout /t 1 && python {path_create} {n} {str(args[1])}'

    # Especifica el nombre del archivo batch y la ruta donde se guardará
    nombre_archivo = 'init_servers.bat'
    ruta_archivo = './'

    # Crea el archivo batch
    with open(os.path.join(ruta_archivo, nombre_archivo), 'w') as archivo:
        archivo.write(comando)
    subprocess.run('init_servers.bat')

@router.get("/getData")
async def getData(n:int,route_map:str):
    
    path_extract = './extractData.py'
    args = [n,"./"+route_map]
    subprocess.run(f'python {path_extract} {n} {str(args[1])}')
    df = pd.read_csv('./results.csv',index_col=None)
    df=df.astype({'Score': str})

    data=jsonable_encoder(df)
    return JSONResponse(data)
    
    

