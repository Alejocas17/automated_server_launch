import os, sys, shutil

def run(n):
    path_worlds = os.listdir(r'.')
    path_world = r'./world'
        
    for i in range(n):
        try:
            shutil.rmtree(path_world + str(i))
        except:
            continue
    ruta_archivo = "echo_file.bat"
    
    with open(ruta_archivo, "w") as archivo:
        archivo.write("@echo off\n")
    
if __name__ == "__main__":
    run(int(sys.argv[1]))