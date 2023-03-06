
import nbtlib
import pandas as pd
import os


def run(ruta_world,port):
    import pandas as pd

    # leer archivo excel
    df = pd.read_excel('wave.xlsx', header=6)

    # extraer dos columnas a partir de la fila 2
    columnas = df[['Nombre', 'Puerto']].dropna()
    columnas['Puerto'] = columnas['Puerto'].astype(int)
    
    nombre=columnas['Nombre'].values
    puerto = columnas['Puerto'].values
    # data = { : columnas['Puerto'].values}
    agent = {}
    for i in range(len(nombre)):
        if int(port) == puerto[i]:
            agent=nombre[i]
    
    
    
        
    # ruta_player = f"{ruta_world}\playerdata"
    ruta_score = f"{ruta_world}\data\scoreboard.dat"
    
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
            data[kpi] = value
    
    data = dict(sorted(data.items()))

        
        
    

    df_data = pd.DataFrame(data.items(), columns=["KPI", "Score"])
    df_data["User"] = agent
    df_data=df_data.iloc[:,[2,0,1]]
    # print(df_data)
    return df_data

if __name__ == "__main__":
    run()