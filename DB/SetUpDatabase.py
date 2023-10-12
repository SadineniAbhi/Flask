from BasicModel import db, Student

db.create_all()

abhi = Student("Abhi",19)
uma = Student("Uma",19)


print(abhi.id)
print(uma.id)

db.session.add_all([abhi,uma])

db.session.commit()

print(abhi.id)
print(uma.id)