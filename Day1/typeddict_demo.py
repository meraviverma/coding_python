from typing import TypedDict
class User(TypedDict):
    name: str
    age: int
def greet_user(user: User) -> str:
    return f"Hello, {user['name']}! You are {user['age']} years old."   
# Example usage
user_info = User(name="Alice", age=30)
greeting = greet_user(user_info)
print(greeting)