# -*- coding: utf-8 -*-
"""module containing all people.

"""


import datetime
# The Person class is the parent class of all the people
class Person:

    #initialize the common attributors that can be inherited
    def __init__(self, name,
                 gender, email_address,
                 birthdate, phone):
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
    def __init__(self, name,
                 gender, email_address,
                 birthdate, phone):
        Person.__init__(self, name,
                        gender, email_address,
                        birthdate, phone)
        # The account is a list containing the strings of the account number
        # of every account the customer has
        self.account = [] 
        self.num_of_account = len(self.account)
        # get last for digits of the account numbers
        self.account_tails = [word[-4:] for word in self.account]

    # This will call the request_new_account method of Manager whose 
    # variable/reference by default is default
    def create_account(self, balance_saving,
                       balance_checking, account_number,
                       manager=default):
        manager.request_new_account(self.name, balance_saving,
                                    balance_checking, account_number)
        
        self.account.append(manager.get_account(account_number))
    
    # This method returns a string containing the basic information of the customer
    def __format__(self):
        result = "Name: {} \nGender: {} \nEmail: {}\nBirthday: {}\nPhone: {}\n".format(
            self.name, self.gender, self.email_address, self.birthdate, self.phone
        )
        result += "Accounts: {}\n".format(self.num_of_account)

        # Loop through the account list and return all 
        # the account number of the cutomer
        # If the customer does not have any account yet, no account number returned
        if self.num_of_account == 0:
            return result
        else:
            for account_string in self.account:
                result += "Account Number: XXXX-XXXX-XXXX-{}"\
                .format(account_string[-4:]) + "\n"
            return result

    def get_account_balance_saving(self, account_tail):
        if num_of_account == 0:
            return None
        else if account_tail not in 

    # Return if the tail is in the name of any account
    def 








class Staff(Person):
    pass

class Assistant(Staff):
    pass

class Teller(Staff):
    pass

class Manager(Staff):
    def request_new_account(self, name,
                            balance_saving, balance_checking,
                            account_number):




