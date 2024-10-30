class Animal:
    def __init__(self) -> None:
        self.__name = "Car"
    
    
    @property
    def name(self):
        return self.__name
   
        
animal1 = Animal()

# animal1.name = "sssssssss"

print(animal1.name)
