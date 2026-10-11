class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_postion(position):
        valid_positions = ['Manager', "Cook", "AI Engineer"]
        return position in valid_positions

print(Employee.is_valid_postion("AI Engineer"))


employee = Employee("ayaan","AI Engineer")

print(employee.get_info())