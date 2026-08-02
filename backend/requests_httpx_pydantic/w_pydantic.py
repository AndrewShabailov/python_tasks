from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool


user = User(id=1, name="Andrew", is_active=True)
user2 = User(id="2", name="Bob", is_active=1)

print(user)
print(user2)
