# -*- coding: utf-8 -*-
"""module containing all people.

"""


import datetime
# The Person class is the parent class of all the people
class Person:
	
    #initialize the common attributors that can be inherited
    def __init__(self, name, age, gender, emailadress, birthdate, phone):
        self.name = name 
        self.age = age
        self.gender = gender
        self.emailadress = emailadress
        self.birthdate = birthdate
        self.phone = phone

    # calculate age by using birthdate and date of today
    def age(self):
    	today = datetime.date.today()                    #get date of today
    	month, day, year = self.birthdate.split("/")     #format the input
    	age = today.year - int(year)                     #calculate years old
    	if (today.month, today.day) < (int(month), int(day)):   
    		age-=1

    	return age

    def email(self):
    	return ("The request email address is", emailadress)



class Customer(Person):
    pass

class Staff(Person):
    pass

class Assistant(Person):
    pass

class Manager(Person):
    pass




