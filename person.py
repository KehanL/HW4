# -*- coding: utf-8 -*-
"""module containing all people.

"""

# The Person class is the parent class of all the people
class Person:
    
    def __init__(self, name):
        self.name = name

class Customer(Person):
    pass

class Staff(Person):
    pass

class Assistant(Person):
    pass

class Manager(Person):
    pass




