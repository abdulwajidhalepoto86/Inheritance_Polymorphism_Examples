class Animal:
    def eat(self):
        print("The animal is eating.")

class Bird(Animal):
    def eat(self):
        print("The bird is pecking seeds.")
    
    def fly(self):
        print("The bird is flying in the sky.")

sparrow = Bird()
sparrow.eat()   
sparrow.fly()  