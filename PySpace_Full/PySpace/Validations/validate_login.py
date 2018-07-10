'''
Created on May 2, 2016

@author: kundhuru.shireesha
'''
from Database import viewDB
from Exceptions.user_exceptions import Invalid_combination

'''------------------This is for validating login credentials---------------------------'''

def validate_login_details(uname,pwd):
    value=viewDB.get_username_password(uname,pwd)
    if value==1:
        return value
    else:
        raise Invalid_combination()