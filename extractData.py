from nbtHandle import run as nbtHandle
from nbtHandle import by_user as nbtHandleByUser
from create import reeplacePort
import sys
import os
import pandas as pd

def run(userName):
    path_worlds = os.listdir(r'.')
    path_world = r'./Doordash'
    # df=pd.DataFrame()
    df = pd.read_excel('wave.xlsx', header=0)
    filtro_usuario = df['netUser'] == userName
    if filtro_usuario.any():
        # Obtener la fila completa para el usuario dado
        fila_usuario = df[filtro_usuario]

        # Obtener el valor de la columna "puerto" para esa fila
        port = fila_usuario['Port'].values[0]
        port = str(port)
        performance = get_data_by_user(path_world,port.split('.')[0],userName)
        return performance
    return False


def get_data(world_path,port,df):
    
    data = nbtHandle(world_path,port)
    
    data_concat = pd.concat([df,data],ignore_index=True)
    
    return data_concat

def get_data_by_user(world_path,port,userName):
    data =nbtHandleByUser(world_path,port,userName)  
    list_dict = []

    for index, row in list(data.iterrows()):
        list_dict.append(dict(row))
    return list_dict
    
    



if __name__ == "__main__":
    run(sys.argv[1])
