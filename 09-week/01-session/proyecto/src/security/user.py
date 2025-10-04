# username,
# password,
# person: Person
class User:
    def __init__(self, username, password, person):
        self.username = username
        self.password = password
        self.person = person

    def __str__(self):
        return f"User: {self.username}, Person: [{self.person}]"