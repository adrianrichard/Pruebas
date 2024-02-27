#class module

#parent class
class Animal_Kingdom:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age =  age
        
#method to combine first name and last name
    def full_name(self):
        return self.fname + ' ' + self.lname
    
#child class       
class Human(Animal_Kingdom):
    pass

#subclass
class Pets(Human):
    #this inherits from all the way to animal kingdom, because we passed through human
    def __init__(self,fname, lname, age, pet_type):
        super().__init__(fname, lname, age)
        self.pet_type = pet_type
