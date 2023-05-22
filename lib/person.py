#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,name='Guido'):
        self.name = name
        self.job = None

    
    def get_name(self):
        return self._name

    
    def set_name(self, name):
          if not isinstance(name,str):
            print("Name must be string between 1 and 25 characters.")
          elif len(name) < 1 or len(name) >25:
            print("Name must be string between 1 and 25 characters.")
          else:
            self._name =  name.title()

    name = property(get_name,set_name)

