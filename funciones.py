from pydantic import BaseModel

# Entidad User
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [
            User(id=1,name="Jose Alfonso",surname="Castro Cantillo",url="http://",age=33),
            User(id=2,name="Maria Luisa",surname="Castro Toncel",url="http://",age=2),
            User(id=3,name="Natalia Milena",surname="Toncel Gonzalez",url="http://",age=28)
        ]

def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error": "User not found"}