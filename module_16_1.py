from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def main():
    return f'Главная страница'
@app.get("/user")
async def user_info(username: str, age: int):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
@app.get("/user/admin")
async def admin():
    return f'Вы вошли как администратор'
@app.get("/user/{user_id}")
async def userid(user_id):
    return f'Вы вошли как пользователь № {user_id}'