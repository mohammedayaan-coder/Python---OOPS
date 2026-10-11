class Student:

    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    
    def get_info(self):
        return f"{self.name} = {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

student1 = Student("Ayaan", 8.5)
student2 = Student("Alice", 8.5)
student3 = Student("Bob", 8.5)
student4 = Student("Alex", 8.5)
student5 = Student("Charli", 8.5)



print(Student.get_count())

print(student1.gpa)