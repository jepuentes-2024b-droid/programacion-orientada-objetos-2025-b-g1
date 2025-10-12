# code
# type_contract,
# area_academic,
# user: User

from security.user import User
class Teacher:
    def __init__(self, type_contract, area_academic, user: User):
        self.type_contract = type_contract
        self.area_academic = area_academic
        self.user = user

    def __str__(self):
        return f"Teacher: {self.user}, Contract Type: {self.type_contract}, Area: {self.area_academic}"