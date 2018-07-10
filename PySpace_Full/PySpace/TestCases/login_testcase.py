'''
Created on May 4, 2016

@author: kundhuru.shireesha
'''
from Validations.validate_login import validate_login_details
from Exceptions.user_exceptions import Invalid_combination
from Functionalities.edit_profile import change_pwd
'''
positive test cases
'''
value=validate_login_details('Shireesha1','welcome@123')
print(value)
print("Log In successful!!!")
value=validate_login_details('Kratika1','welcome@123')
print(value)
print("Log In successful!!!")
value=validate_login_details('Lavish1','welcome@123')
print(value)
print("Log In successful!!!")
value=validate_login_details('Malvika1','welcome@123')
print(value)
print("Log In successful!!!")
value=change_pwd('Shireesha1')
print(value)




'''
negative test cases
'''
try:
    value=validate_login_details('Shirees1','welcome@123')
    value1=validate_login_details('Shireesha1','welcome23')
    value2=validate_login_details('Shireeessss','ygfjsdgfsgfsjd')
    value3=validate_login_details('ShireeesKHJKH','ygfjsdgfsgfDJHJKsjd')
    
except Invalid_combination as e:
    print(e)

