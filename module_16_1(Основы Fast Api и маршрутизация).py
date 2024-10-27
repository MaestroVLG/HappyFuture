from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get('/user/{user_id}')
def user(user_id: str):
    return {'mes': f'Вы вошли как пользователь №{user_id}'}

@app.get("/user")
async def info(username: str = 'Federer', age: int = 35) -> dict:
    return {"message":f'Информация о пользователе. Имя:{username}, Возраст:{age}'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8010)