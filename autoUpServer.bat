@echo on

python .\remove.py 21 "./Doordash" && timeout /t 1 && python .\create.py 21 "./Doordash"