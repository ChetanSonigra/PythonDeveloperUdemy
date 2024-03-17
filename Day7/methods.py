class Bird():
    wings = True        # class variable
    # constructor initialize or constructs a object.
    # It defines state of object at time of creation.
    def __init__(self,color,species ) -> None:
        self.color = color
        self.species= species
    def chirp(self):
        print('tweet')
    def fly(self,feet):
        print(f"{self.color} {self.species} flies {feet} meters high.")
        
tweetie = Bird('Pink','Canary')
tweetie.chirp()
tweetie.fly(99)