import json
from functools import reduce
# with open('db.json') as file :
#     data=json.load(file)
data=[dic for dic in json.load(open('db.json'))]
# print(data)

def makeHash(users,key):
    def analyzing(dic,person):
        dic[person[key]]=person
        return dic
    return reduce(analyzing,users,{})

hashMap= makeHash(data,'id')
print(hashMap)