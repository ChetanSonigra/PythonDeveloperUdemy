# magic method or dunder method
# __name__ , __mro__, __init__, __bases__, __subclasses__

my_list = [1,1,1,1,1]; print(len(my_list),my_list)
class Object:
    pass
obj1 = Object(); print(obj1)  
print(len(obj1))

class CD:
    def __init__(self,songwriter,title,songs) -> None:
        self.songwriter = songwriter
        self.songs = songs
        self.title = title
    def __str__(self):
        return f'Album: {self.title} by {self.songwriter}'
    def __len__(self):
        return self.songs
    def __del__(self):
        print(f'CD {self.title} has been deleted.')
my_cd = CD('Pink Floyd', 'The Wall', 34)
print(my_cd,str(my_cd), len(my_cd))
del my_cd           # deletes object.
#print(my_cd)