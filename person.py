# -*- coding: utf-8 -*-
"""module containing all people.

"""


import datetime
# The Person class is the parent class of all the people
class Person:

    #initialize the common attributors that can be inherited
    def __init__(self, name, gender, email_address, birthdate, phone):
        self.name = name 
        self.age = self.get_age()
        self.gender = gender
        self.email_address = email_address
        self.birthdate = birthdate
        self.phone = phone

    # calculate age by using birthdate and date of today
    def get_age(self):
        today = datetime.date.today()                    #get date of today
        month, day, year = self.birthdate.split("/")  
        #format the input
        age = today.year - int(year)               
        #calculate years old
        if (today.month, today.day) < (int(month), int(day)):   
            age-=1

        return age

    # get email address of this person
    def get_email(self):
        return ("The request email address is", self.email_address)


# The Customer class will inherit attributors in Person class
class Customer(Person):

    # 
    def __init__(self, name, gender, email_address, birthdate, phone):
        Person.__init__(self, name, gender, email_address, birthdate, phone)

    #
#    def create_account(self, balance_saving, balance_checking, account_number):




class Staff(Person):
    pass

class Assistant(Staff):
    pass

class Teller(Staff):
    pass

class Manager(Staff):
    pass




