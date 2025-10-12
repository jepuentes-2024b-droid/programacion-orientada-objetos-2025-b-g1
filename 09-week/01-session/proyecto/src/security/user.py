# username,
# password,
# person: Person
from .person import Person
class User:
    def __init__(self, username, password, person: Person):
        self.username = username
        self.password = password
        self.person = person

    def __str__(self):
        return f"User: {self.username}, Person: [{self.person}]"