import json

# with open('db.json') as file :
#     data=json.load(file)
data=[dic for dic in json.load(open('db.json'))]
print(data)