class User:
    def __init__(self, name, age, email, nationality, gender):
        self.name = name
        self.age = age
        self.email = email
        self.nationality = nationality
        self.gender = gender
    
 #   def Display(self):
  #      print(f"Name: {self.name}\nAge: {self.age}\nemail: {self.email}\nNationality: {self.nationality}\nGender: {self.gender}")
    

class Patient(User):
    def __init__(self, name, age, email, nationality, gender, marital_status, weight):
        super().__init__(self, name, age, email, nationality, gender)
        self.marital_status = marital_status
        self.weight = weight

class Doctor(User):
    def __init__(self, name, age, email, nationality, gender, id_number, department):
        super().__init__(self, name, age, email, nationality, gender)
        self.id_number = id_number
        self.department = department

class Receptionist(User):
    def __init__(self, name, age, email, nationality, gender, username, date_of_birth):
        super().__init__(self, name, age, email, nationality, gender)
        self.username = username
        self.date_of_birth = date_of_birth


kosi = Patient 
kosi.name = "Kosi"
kosi.age = 19
kosi.email = "kosiarah@gmail.com"
kosi.nationality = "Nigerian"
kosi.gender = "Male"
kosi.marital_status = "Single"
kosi.weight = "180LBS"

print(f"Name: {kosi.name}\nAge: {kosi.age}\nemail: {kosi.email}\nNationality: {kosi.nationality}\nGender: {kosi.gender}\nMarital Status: {kosi.marital_status}\nWeight: {kosi.weight}\n")

chisom = Doctor
chisom.name = "Chisom"
chisom.age = 32
chisom.email = "chisomohams@gmail.com"
chisom.nationality = "Nigerian"
chisom.gender = "Female"
chisom.id_number = 1013245632
chisom.department = "Dental Unit"

print(f"Name: {chisom.name}\nAge: {chisom.age}\nemail: {chisom.email}\nNationality: {chisom.nationality}\nGender: {chisom.gender}\nID number: {chisom.id_number}\nDepartment: {chisom.department}\n")

david = Receptionist
david.name = "David"
david.age = 22
david.email = "davidb@gmail.com"
david.nationality = "Ghanaian"
david.gender = "Male"
david.username = "davidb"
david.date_of_birth = "12/08/2002"

print(f"Name: {david.name}\nAge: {david.age}\nemail: {david.email}\nNationality: {david.nationality}\nGender: {david.gender}\nUsername: {david.username}\nDepartment: {david.date_of_birth}")