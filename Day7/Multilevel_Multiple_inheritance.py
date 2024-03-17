class Father:
    def __init__(self,age) -> None:
        self.age = age
    def talk(self):
        print('Hello')
    
class Mother:
    def __init__(self,age,name) -> None:
        super.__init__(age)
        self.name = name
    def talk(self):
        print('Hellow 2')
    def laugh(self):
        print('Haha')
class Child(Father,Mother):      # Method resolution order: left to right.
    def __init__(self, age,play) -> None:
        super().__init__(age)
        self.play = play
class GrandChild(Child):
    pass

my_grandchild = GrandChild(34,True)
my_grandchild.talk()
my_grandchild.laugh()
print(my_grandchild.play)
print(GrandChild.__mro__)
