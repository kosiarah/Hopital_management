class User:

    name = ""
    age = 0
    email = ""
    address = ""
    gender = ""


class Student(User):
    def __init__(self, score):
        self.score = score

class Teacher(User):
    pass

kosi = Student(score = 1)

kosi.age = 19
kosi.name = "Kosi"
kosi.email = "ksoisos"
kosi.address = "Address"
kosi.gender = "Male"

print(f"Student Name: {kosi.name}\nAge: {kosi.age}\nEmail: {kosi.email}\nAddress: {kosi.address}\nGender: {kosi.gender}\nScore: {kosi.score}")

print("")

austin = Teacher()

austin.age = 35
austin.name = "Austin"
austin.email = "djdkddkd"
austin.address = "Address_again"
austin.gender = "Male"
austin.score = 100
print(f"Teacher Name: {austin.name}\nAge: {austin.age}\nEmail: {austin.email}\nAddress: {austin.address}\nGender: {austin.gender}")