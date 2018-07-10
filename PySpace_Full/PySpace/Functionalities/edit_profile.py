
from Database import insertDB
from Validations import validate_signup 
from Classes import user_details
from Database import viewDB
from Exceptions.user_exceptions import Invalid_string
from Database.insertDB import chng_pwd
user=user_details.user_details()

'''-------------------------------------Below function is to edit profile and invoking validate---------------------------------------''' 
def profile(username):
    list1=['Single','Divorced','Married']
    print('----------------------------')
    print('        Edit Profile        ')
    print('----------------------------')
    password1=input('Enter password:')
    value1=viewDB.get_username_password(username,password1)
    if value1==1:
        name1=input("\nEnter name:")
        try:
            user.set_name(name1)
            validate_signup.name(name1)
        except Invalid_string as e:
            print(e)
            return profile(username)
        surname1=input("\nEnter surname:")
        try:
            user.set_surname(surname1)
            validate_signup.name(surname1)
        except Invalid_string as e:
            print(e)
            return profile(username)
        gender1=input("\nEnter gender:")
        gender2=validate_signup.gender(gender1)
        user.set_gender(gender2)
        city1=input('\nEnter city:')
        try:
            user.set_city(city1)
            validate_signup.name(city1)
        except Invalid_string as e:
            print(e)
            return profile(username)
        rstatus1=input('\nEnter relationship status:')
        if(rstatus1 not in list1):
            print("Invalid relationship status")
            return profile(username)
        user.set_relationship_status(rstatus1)
        insertDB.edit_profile(username,user)
        print('\nProfile Updated!!')
        
    else:
        print('\nPassword entered is wrong')
        profile(username)

'''--------------------------------------------Function To change password----------------------------------'''
              
def change_pwd(username):
    print('----------------------------')
    print('       Change Password      ')
    print('----------------------------')
    v1=input('\nEnter your old Password:')
    v2=viewDB.get_username_password(username,v1)
    if v2==1:
        print('\nVerified!!')
        p1=input('\nEnter your new password:')
        try:
            b=validate_signup.passwords(p1)
        except Exception as e:
            print(e)
            return change_pwd(username)
        p2=input('\nConfirm your new Password:')
        if b==p2:
            insertDB.chng_pwd(username, p1)
            print('\nPassword Updated')
        else:
            print('\nPassword doesnot match')
    else:
        print('\nPassword entered is wrong')
    