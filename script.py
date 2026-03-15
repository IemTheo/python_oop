class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        
    def bark(self):
        print ("Whoof whoof")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact = contact_number


owner1 = Owner("Theo", "Calle Mar Negro", "+34123456789")

dog1 = Dog("Bolita", "Unknown", owner1)

print(dog1.owner.name)
dog1.bark()