class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hi, my name is {self.name} and I am {self.age} years old')

me = Person("Theo", 26)

my_baby = Person("Qetusi", 31)

my_baby.greet()

