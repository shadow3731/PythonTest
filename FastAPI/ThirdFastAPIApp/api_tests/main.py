from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    id: int | None = 0
    login: str | None
    password: str | None
    
user_dict = {
    'id': 1,
    'login': 'admin',
    'password': 'pass',
}
user: User = User(**user_dict)
users: list[User] = [user]

fail_message = {'message': 'User not found.'}
new_id = 2

async def check_user_existence(user_id: int) -> User | int | None:
    for i in range(len(users)):
        if users[i].id == user_id:
            return users[i], i
        
    return None, None


@app.get('/')
async def read_index():
    return {'message': 'Hello, World!'}


@app.get('/users/{user_id}')
async def read_user(user_id: int):
    user_result, index = await check_user_existence(user_id)
    return user_result if user_result is not None else fail_message
    
    
@app.get('/users')
async def read_users():
    return users
    
    
@app.post('/users/')
async def create_user(user: User):
    global new_id
    user.id = new_id
    users.append(user)
    new_id += 1
    return user


@app.put('/users/{user_id}')
async def update_user(user_id: int, user: User):
    user_result, index = await check_user_existence(user_id)
    
    if user_result is None:
        return fail_message
    
    user_result = user
    users[index] = user_result
    return user_result


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    user_result, index = await check_user_existence(user_id)
    
    if user_result is None:
        return fail_message
    
    users.pop(index)
    return {}