
from fastapi import FastAPI
import uvicorn
from models import User, Gender, Role

app = FastAPI()

db : list[User] = [
    User(
        id = 1,
        first_name = "Naeem",
        last_name = "Goraya",
        gender = Gender.male,
        role = [Role.admin]
    ),
    User(
        id = 2,
        first_name = "Muhammad",
        last_name = "Goraya",
        gender = Gender.male,
        role = [Role.student]
    ),
    User(
        id = 3,
        first_name = "Mr.",
        last_name = "Goraya",
        gender = Gender.male,
        role = [Role.student]
    )
]

@app.get("/", tags = ['Home'])

async def Home():
    return {"Name" : "Naeem Goraya"}
    


@app.get("/users")
async def user_list():
    return db


@app.post("/users")
async def add_user(user: User):
    db.append(user)
    return {"db": "New user has been added successfully"}






if __name__ == "__main__":
    uvicorn.run("main:app", port = 9000, reload = True)