class Cow:
    def __init__(self,name) -> None:
        self.name = name
    def talk(self):
        print(self.name + ' moos')
class Sheep:
    def __init__(self,name) -> None:
        self.name =name
    def talk(self):
        print(self.name + ' bleats')
        
cow1 = Cow('Mandy')
sheep1 = Sheep('Cloud')
cow1.talk()
sheep1.talk()

animals = [cow1,sheep1]
for a in animals:
    a.talk()                  # we can iterate through different object if they share same method.