'''
Created on May 2, 2016

@author: kundhuru.shireesha
'''
from Validations import validate_signup
from Database import insertDB
from Classes import user_details
from Exceptions.user_exceptions import Invalid_string

user=user_details.user_details()

'''------------------------------Below function is for Signup and invoke validate functions----------------------------'''

def signup():
    try:
        list1=['Single','Divorced','Married']
        print('----------------------------')
        print('          SIGN UP           ')
        print('----------------------------')
        print('\n')
        status1=username()
        print('\nPassword must contain a digit, a special character and should be at least 8 chars long')
        status2=password()
        user.set_password(status2)
        name=input('\nEnter name:')
        try:
            user.set_name(name)
            validate_signup.name(name)
        except Invalid_string as e:
            print(e)
            return signup()
        surname=input('\nEnter surname:')
        try:
            user.set_surname(surname)
            validate_signup.name(surname)
        except Invalid_string as e:
            print(e)
            return signup()
        status3=gender()
        user.set_gender(status3)
        city=input('\nEnter city:')
        try:
            user.set_city(city)
            validate_signup.name(city)
        except Invalid_string as e:
            print(e)
            return signup()
        rstatus=input('\nEnter relationship status:') 
        if(rstatus not in list1):
            print("Invalid relationship status")
            return signup()
        user.set_relationship_status(rstatus)
        if(status1==True):
            insertDB.insert_details(user)
            print("Sign up Successfull!!")
            return
    finally:
        pass 

'''------------------------------------------Below function To accept username and invoke validate function--------------------'''
   
def username():
    try:
        username1=input('\nEnter Username:')
        user.set_username(username1)
        status1=validate_signup.username(username1)
        return status1
    except Exception as e:
        print(e)
        return username()

'''------------------------------------------Below function To accept password and invoke validate function--------------------'''
   
def password():
    try:
        password1=input('\nEnter password:') 
        status2=validate_signup.passwords(password1)
        return status2
    except Exception as e:
        print(e)
        return password()

'''------------------------------------------Below function To accept Gender and invoke validate function--------------------'''
   
def gender():
    try:
        gender1=input('\nEnter gender(m/f):')
        status3=validate_signup.gender(gender1)
        return status3
    except Exception as e:
        print(e)
        return gender()
            
    