class Parent:
    def greet(self):
        print("Hello from Parent class!")

class Child(Parent):
    def greet(self):
        super().greet()   
        print("Hello from Child class!")

c = Child()
c.greet()