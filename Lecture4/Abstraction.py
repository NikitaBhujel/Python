#Hiding internal details and showing only essential features
'''
We use abstract classes : Blueprint for other classes
abc module:abstraction based module
Modules are codes written by other programmers
'''
from abc import ABC,abstractmethod  #Abstraction Based Classes
class Animal(ABC):
    @abstractmethod
    def make_sound():  #So implementation details is hidden here, other classes get permisison,blueprint to implement abstract method as they like.
        pass #Represents null value
class Lion(Animal):
    def make_sound(self):
        print("Roar")
        
l1=Lion()
l1.make_sound()

