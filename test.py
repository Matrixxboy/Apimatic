from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Create the FastAPI app
app = FastAPI()

# Mock database
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

# Pydantic model for request validation
class User(BaseModel):
    name: str


# Route to get all users
@app.get("/users", response_model=List[dict])
def get_users():
    hello = "hello"
    print(hello)
    return users


# Route to get a single user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((item for item in users if item["id"] == user_id), None)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


# Route to create a new user
@app.post("/users")
def create_user(user: User):
    new_user = {"id": len(users) + 1, "name": user.name}
    users.append(new_user)
    return new_user


# Another POST route (/user2)
@app.post("/user2")
def create_user2():
    new_user = {"id": len(users) + 1, "name": "New User"}
    users.append(new_user)
    return new_user
