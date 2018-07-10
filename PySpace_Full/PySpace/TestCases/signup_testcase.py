'''
Created on May 4, 2016

@author: kundhuru.shireesha
'''
from Validations.validate_signup import passwords
from Validations.validate_signup import gender
from Validations.validate_signup import username
from Validations.validate_signup import name
from Exceptions.user_exceptions import Invalid_password_sp,Invalid_password_digit,Invalid_password_len,Invalid_gender,Invalid_username,Invalid_string

'''
positive test cases
'''
vlue1=username('Suraj1')
value=passwords('welcome@123')
value2=gender('f')
value2=gender('m')
print('Sign up successful!!!')



'''
negative test cases
'''
try:
    value1=username('Shireesha1')
    value2=passwords('welcomegth')
    value3=passwords('welcomegth12')
    value4=passwords('welco')
    value5=gender('t')
    value6=name('sagar123')
    value7=name('talwar123')
    value8=name('mumbai07')

except Invalid_username as e:
    print(e)
except Invalid_gender as e:
    print(e)
except Invalid_password_sp as e:
    print(e)
except Invalid_password_digit as e:
    print(e)
except Invalid_password_len as e:
    print(e)
except Invalid_string as e:
    print(e)
