
import nbtlib
import pandas as pd
import os


def run(ruta_world,port):
    import pandas as pd

    # leer archivo excel
    df = pd.read_excel('wave.xlsx', header=1)

    # extraer dos columnas a partir de la fila 2
    columnas = df[['netUser', 'Port']].dropna()
    columnas['netUser'] = columnas['Port'].astype(int)
    
    nombre=columnas['netUser'].values
    puerto = columnas['Port'].values
    # data = { : columnas['Puerto'].values}
    agent = {}
    for i in range(len(nombre)):
        if int(port) == puerto[i]:
            agent=nombre[i]
    
    
    
        
    # ruta_player = f"{ruta_world}\playerdata"
    # ruta_score = f"{ruta_world}\world\data\scoreboard.dat" 
    ruta_score = f"{ruta_world}/world/data/scoreboard.dat" 
        # Crear un objeto de archivo NBT
    score_nbt = nbtlib.load(ruta_score)
    # player_nbt = nbtlib.load(ruta_player)

    # Obtener los datos del archivo NBT
    data_score = score_nbt
    # data_player = player_nbt
    score_player = data_score.get("data").get("PlayerScores")

    data = {}
    
    for i in score_player:
        kpi = str(i.get("Name"))
        if "trainee" not in kpi and "Trainee" not in kpi:
            value = int(i.get("Score"))
            data[kpi] = str(value)
    
    data = dict(sorted(data.items()))

        
        
    

    df_data = pd.DataFrame(data.items(), columns=["KPI", "Score"])
    df_data["User"] = agent
    df_data=df_data.iloc[:,[2,0,1]]
    # print(df_data)
    return df_data

def by_user(ruta_world:str,port:str,username:str):
    import pandas as pd
    ##path for winodows
    # ruta_score = f"{ruta_world}{port}\world\data\scoreboard.dat"
    ##path for macos
    ruta_score = f"{ruta_world}{port}/world/data/scoreboard.dat"
        # Crear un objeto de archivo NBT
    score_nbt = nbtlib.load(ruta_score)
    # player_nbt = nbtlib.load(ruta_player)

    # Obtener los datos del archivo NBT
    data_score = score_nbt
    # data_player = player_nbt
    score_player = data_score.get("data").get("PlayerScores")

    data = {}
    
    for i in score_player:
        kpi = str(i.get("Name"))
        if "kpi" in kpi:
            value = int(i.get("Score"))
            data[kpi] = str(value)
    
    data = dict(sorted(data.items()))
    print("los kpis son:",data)

    df_data = pd.DataFrame(data.items(), columns=["kpi", "score"])
    df_data["GameName"] = ruta_world.split('/')[1]
    df_data=df_data.iloc[:,[0,1,2]]
    # print(df_data)
    return df_data
    
if __name__ == "__main__":
    run()
