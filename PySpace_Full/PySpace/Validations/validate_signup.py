from Database import viewDB
from Exceptions.user_exceptions import Invalid_password_sp
from Exceptions.user_exceptions import Invalid_password_digit
from Exceptions.user_exceptions import Invalid_password_len
from Exceptions.user_exceptions import Invalid_gender
from Exceptions.user_exceptions import Invalid_username
from Exceptions.user_exceptions import Invalid_string

'''-----------------------------------Validate username------------------------------------'''

def username(username):
    value=viewDB.get_username(username)
    if value==1:
        raise Invalid_username()
    else:
        return True
'''-------------------------------------Validate Password-----------------------------------'''
def passwords(password):
        list1=['0','1','2','3','4','5','6','7','8','9']
        list2=['@','#','$','%','&','*']
        counter1=0
        counter2=0
        for i in range(0,len(password)):
            if(password[i] in list1):
                counter1+=1
        for j in range(0,len(password)):
            if(password[j] in list2):
                counter2+=1
   
        if(len(password)>=8):
            if(counter1!=0):
                if(counter2!=0):
                    return password
                else:
                    raise Invalid_password_sp()
            else:
                raise Invalid_password_digit()
        else:
            raise Invalid_password_len()

'''------------------------------------------Validate Gender---------------------------------------'''       

def gender(gender1):
    gender1=gender1.lower()
    if(gender1 in ['m','f']):
        return gender1
    else:
        raise Invalid_gender()

'''-------------------------------------------Validate name,surname and city--------------------------------'''
       
def name(name1):
    if name1.isalpha():
        return name1
    else:
        raise Invalid_string()
        