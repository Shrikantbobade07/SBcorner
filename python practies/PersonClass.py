class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introdce(self):
        print(f"my name is {self.name} and I am {self.age} years old")


person = Person("Shrikant", 30)
person.introdce()
