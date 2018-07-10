from Functionalities import login
from Functionalities import signup
from Utility.Menu import Menus
'''--------------------------------------------Displays the Menu--------------------------------------'''
choice=1
while(int(choice)!=3):
    choice = Menus.display_main_menu('Welcome to PySpace','Login,Sign Up,Exit')
    if int(choice)==1:
        login.logindetails()
    elif int(choice)==2:
        signup.signup()
    elif int(choice)==3:
        print('See You Soon!!')
    else:
        print("Enter valid choice")
