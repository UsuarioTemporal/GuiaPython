# from io import open
import json

with open('archvo.json') as file:
    dato= json.load(file)
print(dato)