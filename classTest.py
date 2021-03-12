class User: # create parent class 
    name = "Blank"
    email = " "
    password = "Blank"
    account_number = 0
    #create child class
class Teacher(User):
    subject = "History"
    gradelevel = 11
    #create child class
class Student(User):
    GPA = 4.0
    GradYear = 2025
