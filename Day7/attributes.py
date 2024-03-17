
# Attributes:
class Bird():
    wings = True        # class variable
    # constructor initialize or constructs a object.
    # It defines state of object at time of creation.
    def __init__(self,color,species ) -> None:
        self.color = color
        self.species= species
        
my_bird = Bird('black','tucan')           
# throws error if arguments are not given as per parameters defined in __init__ method.
print(f"My bird is {my_bird.color} {my_bird.species}.")      
print(Bird.wings,my_bird.wings)  
my_bird.wings = False
# class variable can be changed for individual object if needed.
print(Bird.wings,my_bird.wings)

Bird.wings= False
print(Bird.wings,my_bird.wings)
bird1 = Bird('white','tucan')
Bird.wings = True
print(Bird.wings,my_bird.wings,bird1.wings)
bird2 = Bird('green','tucan')
print(Bird.wings,my_bird.wings,bird1.wings,bird2.wings)
# unless specifically changed for specific object, class variable will be same for all object.

