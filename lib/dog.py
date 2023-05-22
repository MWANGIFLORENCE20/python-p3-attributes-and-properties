#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    
    
    def __init__(self,breed="Human",name="fido"):
        self.name = name
        self.breed = breed
        

    def get_name(self):
        return self._name
        
    
    def set_name(self,name):
        if not isinstance(name,str):
            print("Name must be string between 1 and 25 characters.")
        elif len(name) < 1 or len(name) >25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name =  name.title()

    def get_breed (self):
        return self._breed

    def set_breed(self,value):
        if  not isinstance in self.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed 

    name = property(get_name,set_name,get_breed,set_breed)

