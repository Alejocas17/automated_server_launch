import os, sys, shutil

##Main function
def run(n,path_world):    
    path_worlds = os.listdir(r'.')
    #path_world = r'./world'
    
    for i in range(n):
        new_path = path_world + str(i)
        print(f'Creadondo {new_path} ...')
        shutil.copytree(path_world, new_path)
        reeplacePort(i, new_path)
        create_executable(i, new_path)
##Replacing ports in each server
def reeplacePort(n,new_path):
    ruta_archivo = new_path+"/server.properties"
    if len(str(n))==1:
        nuevo_puerto = "2560"+str(n)
    if len(str(n))==2:
        nuevo_puerto = "256"+str(n)

    # Leer el contenido del archivo
    with open(ruta_archivo, "r") as archivo:
        lineas = archivo.readlines()

    # Buscar la línea que contiene la propiedad "puerto" y reemplazarla con el nuevo puerto
    for i, linea in enumerate(lineas):
        if "server-port" in linea:
            lineas[i] = f"server-port={nuevo_puerto}\n"

    # Escribir el contenido actualizado en el archivo
    with open(ruta_archivo, "w") as archivo:
        archivo.writelines(lineas)

    print(f"Puerto actualizado a {nuevo_puerto}")
    return nuevo_puerto
    
##appending .bat executions for each server in order to start it
def create_executable(n,new_path):
    ruta_archivo = "echo_file.bat"
    
    # Leer el contenido del archivo
    with open(ruta_archivo, "r") as archivo:
        contenido = archivo.readlines()

    # Agregar las líneas n veces
    
    contenido.extend([f"\n cd "f"{new_path}"" \n",
                    "start Start.bat\n",
                    "timeout /t 3 /nobreak\n",
                    "cd ..\n"])

    # Escribir el contenido actualizado en el archivo con la extensión .bat
    # print(ruta_archivo)
    ruta_archivo = ruta_archivo.split(".")[0] + ".bat"
    # print(ruta_archivo)
    with open(ruta_archivo, "w") as archivo:
        archivo.writelines(contenido)

##entrypoint
if __name__ == '__main__':
    run(int(sys.argv[1]),str(sys.argv[2]))
    


    
    
    

    

