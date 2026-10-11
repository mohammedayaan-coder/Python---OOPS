class Car:
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def drive(self):
        print(f"you are driving {self.name}")

    def stop(self):
        print(f"you stoped the {self.name}")

class Student:
    colleg = "SCET"
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no


        