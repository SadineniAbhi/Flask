from BasicModelApp import db,Students


laststudent = Students.query.get(4)
db.session.delete(laststudent)
students = Students.query.all()
print(students)