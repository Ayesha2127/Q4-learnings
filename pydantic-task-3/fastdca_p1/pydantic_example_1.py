from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None

user_data = {"id": 1, "name": "Ayesha Waseem", "email": "ayeshawaseem30@gmail.com", "age": 20}   
user = User(**user_data)
print(user)
print(user.model_dump()) 

try:
    invalid_user = User(id="not an int", name="Arisha Saleem", email="arishasaleem20@gmail.com", age=20)
except ValidationError as e:
    print(e)