class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
    def start(self):
        print(f"my car model is {self.model}, and brand is {self.brand}.")
    

frnd = Car("2k26", "BMW")
frnd.start()