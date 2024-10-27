from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}

@app.get("/user/A/B")
async def us() -> dict:
    return {"message": f"Hello, Tester!"}

@app.get("/id")
asyns def id_paginator(username: str, age: int): ->dict:
    return {"User": username, "Age": age}


@app.get('/user/{first_name}/{last_name}')
def us(first_name: str, last_name: str ):
    return {'mes': f'{first_name} {last_name}'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8010)