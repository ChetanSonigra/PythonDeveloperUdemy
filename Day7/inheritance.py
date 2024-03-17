# inheritance helps in implementing DRY principle.
class Animal():
    def __init__(self,age, color) -> None:
        self.age = age
        self.color = color
    def born(self):
        print('Animal has been born.')
class Example():
    pass
class Bird(Animal,Example):
    pass
print(Bird.__bases__, Bird.__base__, Animal.__subclasses__())
bird = Bird(2,'Red')
print(type(bird), bird.color)
bird.born()

# Can add extra attributes and methods.

class Animal():
    def __init__(self,age,color) -> None:
        self.color = color
        self.age = age
    def born(self):
        print('Animal has been born.')
    def talk(self):
        print('Animal is talking.')
        
class Bird(Animal):
    def __init__(self, age, color, altitude) -> None:
        super().__init__(age, color)
        self.altitude = altitude
    def talk(self):
        print('chirp')
    def fly(self, feet):
        print(f'Bird flew {feet} feet high.')
        
tweeti = Bird(4,'Pink', 190)
tweeti.fly(56)
tweeti.talk()
print(tweeti.altitude)
