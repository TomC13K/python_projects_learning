from datetime import date

from pydantic import BaseModel

# Declare a variable as a str
# and get editor support inside the function
def main(user_id: str):
    return user_id


# A Pydantic model
class User(BaseModel):
    id: int
    name: str
    joined: date


my_user: User = User(id=3, name="John Doe", joined="2018-07-19")

second_user_data = {
    "id": 4,
    "name": "Mary",
    "joined": "2018-11-30",
}

# **second_user_data means:
# Pass the keys and values of the second_user_data dict directly as key-value arguments, equivalent
# to: User(id=4, name="Mary", joined="2018-11-30")
my_second_user: User = User(**second_user_data)

print(my_second_user.model_dump())
