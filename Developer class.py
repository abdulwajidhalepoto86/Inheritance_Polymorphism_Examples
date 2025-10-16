class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id

class Developer(Person, Employee):
    def __init__(self, name, emp_id, language):
        Person.__init__(self, name)
        Employee.__init__(self, emp_id)
        self.language = language

    def show_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Language: {self.language}")

dev = Developer("ABDUL WAJID", 786, "Python")
dev.show_details()