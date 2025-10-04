# type_document,
# number_document,
# first_name,
# last_name,
# birth_date,
# email

class Person:
    def __init__(self, type_document, number_document, first_name, last_name, birth_date, email):
        self.type_document = type_document
        self.number_document = number_document
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.type_document}: {self.number_document}"