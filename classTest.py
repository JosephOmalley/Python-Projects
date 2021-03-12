class User:
    name = "Blank"
    email = " "
    password = "Blank"
    account_number = 0

class Teacher(User):
    subject = "History"
    gradelevel = 11
    
class Student(User):
    GPA = 4.0
    GradYear = 2025
