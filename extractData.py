from nbtHandle import run as nbtHandle
from create import reeplacePort
import sys
import os
import pandas as pd

def run(n,path_world):
    path_worlds = os.listdir(r'.')
    #path_world = r'./world'
    df=pd.DataFrame()
        
    for i in range(1,n):
        new_path = path_world + str(i)
        try:
            df = get_data(new_path, reeplacePort(i,new_path),df)
        except ValueError as e:
            print(e)
            pass
    # print(df)
    
    df.to_csv('results.csv',index=False)
    return df


def get_data(world_path,port,df):
    
    data = nbtHandle(world_path,port)
    
    data_concat = pd.concat([df,data],ignore_index=True)
    
    return data_concat
    
    
    



if __name__ == "__main__":
    run(int(sys.argv[1]),str(sys.argv[2]))
