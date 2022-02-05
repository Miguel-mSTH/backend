import email
from pydoc import cli
from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

db=cliente ['codigog11']

colAlumnos=db["alumnos"]

#alumnoId=colAlumnos.insert_one({"nombre":"JUAN MENENDEZ","email":"juan@gmail.com","nota":7})

#print("NUEVO ALUMNO CREADO ID : ",alumnoId)

#consultar datos

for a in colAlumnos.find():
    print(a["nombre"]+"~"+a["email"])