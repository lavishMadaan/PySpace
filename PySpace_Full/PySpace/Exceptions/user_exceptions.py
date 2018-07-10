'''
Created on May 3, 2016

@author: kundhuru.shireesha
'''
class Invalid_password_sp(Exception):
    def __init__(self):
        super().__init__("Password does not have special characters")
        
class Invalid_password_digit(Exception):
    def __init__(self):
        super().__init__("Password does not have digit")
    
class Invalid_password_len(Exception):
    def __init__(self):
        super().__init__("Password does not have required length")
        
class Invalid_gender(Exception):     
    def __init__(self):
        super().__init__("Invalid Gender") 
        
class Invalid_username(Exception):
    def __init__(self):
        super().__init__("sorry!! username already exists") 
        
class Invalid_combination(Exception):
    def __init__(self):
        super().__init__("Invalid Username-Password Combination")
        
class Max_attempts(Exception):
    def __init__(self):
        super().__init__("Maximum no. of attempts done. please log in after sometime")
        
class Invalid_captcha(Exception):
    def __init__(self):
        super().__init__("Captcha entered is wrong!!!")
        
class Invalid_string(Exception):
    def __init__(self):
        super().__init__("Enter only characters")
        