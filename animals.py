import time
class Animals():
    
    alive = True
    hungry = True

    def __init__(self,name,gender,height,weight):
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight

    def drink(self):
        print(f"{self.name} is drinking water at  !!")
        time.sleep(3)
        print(f"the {self.name} has finished drinking ! ")
        return self


    def eat(self,food):
        print(f"{self.name} is eating {food}!")
        time.sleep(5)
        print(f"the {self.name} has finished eating ! ")
        hungry = False
        
        return self
   
        





        
