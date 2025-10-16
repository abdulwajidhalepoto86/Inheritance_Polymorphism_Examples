class Swimmer:
    def swim(self):
        print("Swimming in water.")

class Walker:
    def walk(self):
        print("Walking on land.")

class Amphibian(Swimmer, Walker):
    def live(self):
        print("Can live both on land and in water.")

frog = Amphibian()
frog.swim()
frog.walk()
frog.live()