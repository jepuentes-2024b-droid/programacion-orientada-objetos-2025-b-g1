# Registrar personas
# Asignar usuarios a personas
# Registrar estudiantes y profesores

# Nota: Cargar y mostar los datos del profesor, estudiante.
#  Se conoce que el estudiante tiene materias asociadas {subject_academic}.
#  Y Un profesor orienta materias {subject_academic}. 

# Proceder con registar y mostrar los datos de un usuario
from security.user import User
from security.person import Person
from academic.teacher import Teacher
from academic.student import Student

# Allow running this file directly as a script: ensure the `src` directory
# is on sys.path so absolute imports like `security` and `academic` resolve.
import os
import sys
src_dir = os.path.dirname(__file__)
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

# Nota: Person.__init__(type_document, number_document, first_name, last_name, birth_date, email)
# Añadimos el tipo de documento (ej: 'CC' - cédula de ciudadanía) y usamos los nombres de atributos definidos en la clase Person
User1 = User("juandavid21", "password123", Person("CC", "123456789", "Juan David", "Perez", "1990-01-01", "jdoe@example.com"))
User2 = User("asmith", "securepass", Person("CC", "987654321", "Alice", "Smith", "1992-02-02", "asmith@example.com"))
User3 = User("bwayne", "darkknight", Person("CC", "555666777", "Bruce", "Wayne", "1985-03-03", "bwayne@example.com"))
User4 = User("ckent", "superman", Person("CC", "444555666", "Clark", "Kent", "1980-04-04", "ckent@example.com"))


for user in [User1, User2, User3, User4]:
    print(f"Username: {user.username}")
    print(f"Full Name: {user.person.first_name} {user.person.last_name}")
    print(f"Document: {user.person.type_document} {user.person.number_document}")
    print(f"Date of Birth: {user.person.birth_date}")
    print(f"Email: {user.person.email}")
    print("-" * 40)

# Teacher constructor: Teacher(type_contract, area_academic, user)
Teacher1 = Teacher("Permanent", "Mathematics", User1)
print(f"Teacher: {Teacher1.user.person.first_name} {Teacher1.user.person.last_name} \nUsuario: {User1.username} \nArea: {Teacher1.area_academic}")

print("-" * 40)

# Student constructor: Student(grade_level, subjects_academic, user)
Student1 = Student("10th Grade", ["Math", "Science", "History"], User1)
print(f"Student: {Student1.user.person.first_name} {Student1.user.person.last_name} \nUsuario: {User1.username} \nGrade Level: {Student1.grade_level} \nSubjects: {', '.join(Student1.subjects_academic)}")