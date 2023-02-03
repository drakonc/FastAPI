from fastapi import FastAPI
from funciones import *

app = FastAPI()

@app.get("/users")
async def users():
    return users_list

@app.get("/user/{id}")
async def user(id:int):
    return search_user(id)

@app.get("/user/")
async def user(id:int):
    return search_user(id)

@app.post("/user")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"Error": "User found"}
        
    users_list.append(user)
    return user

@app.put("/user")
async def user(user: User):
    found = False

    for index,item in enumerate(users_list):
        if(item.id == user.id):
            users_list[index] = user
            found = True

    if not found:
        return {"Error": "Usuario no Actualizado"} 
    return {"Éxito": "Usuario Actualizado"} 

@app.delete("/user/{id}")
async def user(id: int):
    found = False
    
    for index,item in enumerate(users_list):
        if(item.id == user.id):
            del users_list[index]
            found = False

    if not found:
        return {"Error": "Usuario no Eliminado"} 
    return {"Éxito": "Usuario Eliminado"} 