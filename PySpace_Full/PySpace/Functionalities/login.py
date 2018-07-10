'''
Created on May 2, 2016

@author: kundhuru.shireesha
'''
from Validations import validate_login
from Functionalities import home
import random
from Exceptions.user_exceptions import Max_attempts, Invalid_combination,Invalid_captcha
count=1

'''------------------This below function is for Login and invoking validate to check login credentials------------------------------'''

def logindetails():
    global count                
    try:
        while(count<=3):
            username=input('\nEnter Username:')
            password=input('\nEnter password:')    
            value=validate_login.validate_login_details(username,password)
            if value==1:
                print('Log in successfull!')
                home.home_screen(username)
                break
        captcha()
    except Exception as e:
        print(e)
        count+=1
        logindetails()

'''-------------This below function is for generationg captcha and invoking validate to check credentials-------------------'''
        
def captcha():
    global count
    try:
        if(count>3):
            list1=['vbjhvc','jkbvek','vehvb','jhvhcv','hvebwc','hvecjhv']
            x=random.randrange(0,len(list1))
            value1=list1[x]
            print('Captcha:',value1)
            value2=input('\nEnter captcha:')
            if(value1==value2):
                username1=input('\nEnter Username:')
                password1=input('\nEnter password:')    
                try:
                    value3=validate_login.validate_login_details(username1,password1)
                except Invalid_combination:
                    value3=0
                if value3==1:
                    print('Log in successfull!!')
                    home.home_screen(username1)
                    return
                else:
                    count=1
                    raise Max_attempts   
            else:
                count=1
                raise Invalid_captcha
    except Max_attempts as e:
        print(e)
    except Invalid_captcha as e:
        print(e)
