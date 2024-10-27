from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

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


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8015)