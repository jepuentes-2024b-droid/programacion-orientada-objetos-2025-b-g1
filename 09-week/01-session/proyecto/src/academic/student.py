# Student class
from typing import List
from security.user import User

class Student:
	def __init__(self, grade_level: str, subjects_academic: List[str], user: User):
		self.grade_level = grade_level
		self.subjects_academic = subjects_academic
		self.user = user

	def __str__(self):
		subjects = ', '.join(self.subjects_academic)
		return f"Student: {self.user.person.first_name} {self.user.person.last_name} - Grade: {self.grade_level} - Subjects: {subjects}"