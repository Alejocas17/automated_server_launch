@echo on

python .\remove.py 2 "./Doordash" && timeout /t 1 && python .\create.py 2 "./Doordash"