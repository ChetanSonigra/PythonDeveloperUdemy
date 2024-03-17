# instance, class, static methods.
# instance method:
    # self as instance parameter
    # access and modify object attributes
    # access other methods.
    # modify class state.
# class method:
    # @classmethod
    # cls as class parameter
    # can be called on class/instance. 
    # can't access instance attributes. only class attributes.
    
# static method:
    # @staticmethod
    # no class/instance parameter
    # can't access instance / class attributes.
    # normal functions but linked to class.
class Bird():
    wings = True        # class variable
    # constructor initialize or constructs a object.
    # It defines state of object at time of creation.
    def __init__(self,color,species ) -> None:
        self.color = color
        self.species= species
    def chirp(self):
        print('tweet')
    def fly(self,feet):      # instance method
        print(f"{self.color} {self.species} flies {feet} meters high.")
        self.chirp()          # access others methods.
    def paint_black(self):    # instance method
        self.color='black'    # access/modify instance attributes.
    @classmethod
    def lay_eggs(cls,number):
        print(f'It laid {number} eggs.')
        # print(self.color) will throw error
        cls.wings = False
        print(cls.wings)
    @staticmethod
    def look():
        #cls.wings or self.color not accesible
        print('The bird looks.')
tweetie = Bird('Pink','Canary')
tweetie.wings = False
print(tweetie.wings)

Bird.lay_eggs(2)
tweetie.lay_eggs(4)
print(Bird.wings,tweetie.wings)

Bird.look()
tweetie.look()