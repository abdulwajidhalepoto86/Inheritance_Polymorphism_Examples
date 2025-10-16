class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
        
class Motorcycle(Vehicle):
    def __init__(self, brand, model, has_sidecar):
        super().__init__(brand, model)
        self.has_sidecar = has_sidecar

    def show_info(self):
        super().show_info()
        print(f"Has Sidecar: {self.has_sidecar}")

bike = Motorcycle("Honda", "125cc", False)
bike.show_info()