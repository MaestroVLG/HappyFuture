from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get('/user/{user_id}')
def user(user_id: Annotated[int, Path(title='User ID', description='Enter User ID', gt=0, le=100)]):
    return {'mes': f'Вы вошли как пользователь №{user_id}'}

@app.get("/user/{username}/{age}")
async def info(username: Annotated[str, Path(title="Username", description="Enter username", min_length=5, max_length=20)],
               age: Annotated[int, Path(title="Age", description="Enter age", ge=18, le=120)]) -> dict:
    return {"message":f'Информация о пользователе. Имя:{username}, Возраст:{age}'}

# CRUD операции(функции, главное понять)

@app.get("/users")
async def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(title="Username", description="Enter username", min_length=5, max_length=20)],
                      age: Annotated[int, Path(title="Age", description="Enter age", ge=18, le=120)]) -> str:

    #Находим максимальный ключ в бд и добавляе нового пользователя в бд(в словарь)

    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return f'User {new_id} is registered'

#Обновляем данные словаря и взвращаем информацию об успешном обновлении.
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(title='User ID', description='Enter User ID', gt=0, le=100)],
                      username: Annotated[str, Path(title="Username", description="Enter username", min_length=5, max_length=20)],
                      age: Annotated[int, Path(title="Age", description="Enter age", ge=18, le=120)]) -> str:
    if str(user_id) in users: #Проверяем есть ли такой пользователь в бд
        users[str(user_id)] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    else:
        return f"User {user_id} not found"

#Удаление пользователя из бд(словаря)
@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(title='User ID', description='Enter User ID', gt=0, le=100)]) -> str:
    if str(user_id) in users: #Проверяем есть ли такой пользователь в бд
        del users[str(user_id)]
        return f"User {user_id} has been deleted"
    else:
        return f"User {user_id} not found"

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8015)