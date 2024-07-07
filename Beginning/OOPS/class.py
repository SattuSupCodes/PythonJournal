'''A class contains the blueprints or the prototype from which the objects are being created. 
It is a logical entity that contains some attributes and methods.'''

# Class is always written with first letter in caps and ends with parethesis
# Building a class

class class_name():
    def __init__(self, parameter):
        self.property=parameter
        
    def class_details(self):
        print("show me the details: ", self, property)
        
object=class_name(argument) #type: ignore

# example
class agent():
    def __init__(self, name, health, car):
        self.name=name
        self.health=health
        self.car=car
        
    def player_info(self):
        print("welcome" , self.name)
        print("your health", self.health)
        print("your car", self.car)
    
spy=agent("james bond", 100 , "Porche")
spy.player_info()

        