from fastapi import HTTPException, status
from fastapi import FastAPI
from fastapi import APIRouter,Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
import subprocess
import time
import os
import pandas as pd
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db.models import Agent as agentModel
from app.db import models
from sqlalchemy.sql.expression import func

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
async def getData(n:int,route_map:str,db:Session=Depends(get_db)):
    
    path_extract = './extractData.py'
    args = [n,"./"+route_map]
    subprocess.run(f'python {path_extract} {n} {str(args[1])}')
    df = pd.read_csv('./results.csv',index_col=None)
    df=df.astype({'Score': str})

    data_json=jsonable_encoder(df)
    print(df)
    
    
    
    
    
    for i in range(len(df['User'].tolist())):
        data = db.query(agentModel).all()
        response=[item for item in data if item.name == df['User'][i]]
        response1=[item for item in data if item.Kpis == df['KPI'][i]]
        if response==[]:
                        
            new_user = agentModel(               
                        
                    name = df['User'][i],
                    UserNt = "working..",
                    Kpis = [df['KPI'][i]],
                    Scores = [df['Score'][i]]

            )
            print(new_user.Kpis)
            db.add(new_user)
            db.commit()
            db.close()
            data = db.query(agentModel).all()
        
        elif response1==[]:
            agent = db.query(agentModel).filter_by(name=df['User'][i])
            new_user = agentModel(               
                        
                    Kpis = [df['KPI'][i]],
                    Scores = [df['Score'][i]]
            )
            print("angus")
            # models.Agent.Kpis = func.concat(models.Agent.Kpis,new_user.Kpis)
            # models.Agent.Scores = func.concat(models.Agent.Kpis,new_user.Scores)
            agent.update({models.Agent.Kpis:new_user.Kpis},synchronize_session = False,)
            agent.update({models.Agent.Scores:new_user.Scores},synchronize_session = False)
            # agent.append(new_user.Kpis)
            # agent.append(new_user.Scores)
            db.commit()
            db.close()
            
            
    
    return data_json


@router.get("/deleteAll/{id}")
async def deleteAll(id:int,db:Session=Depends(get_db)):
    data = db.query(agentModel).filter_by(id=id).first()
    db.delete(data)
    db.commit()
    
    

