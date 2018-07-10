
from Database import insertDB
from Functionalities import edit_profile
from Classes import user_details
from Database import viewDB
from Functionalities import approve_request
from Functionalities import showfeeds
from Functionalities import find_friends
user1=user_details.updates()

'''-------------------------------Display homescreen,take choices and invoke respective functions------------------------'''

def home_screen(username):
    try:
        print('---------------------------')
        print('           HOME            ')
        print('---------------------------')
    
        value=input('1.View profile\n2.Status update\n3.Approve Request\n4.Show Feeds\n5.Change Password\n6.Find Friends\n7.Exit\n\nEnter Your choice:')
        if int(value)==1:
            list1=viewDB.get_profile(username)
            print('----------------------')
            print('     VIEW PROFILE     ')
            print('----------------------')
            for i in list1:
                print('Username:',i.get_username(),'\nName:',i.get_name(),'\nSurname:',i.get_surname(),'\nGender:',i.get_gender(),'\nCity:',i.get_city(),'\nRelationship Status:',i.get_relationship_status())
                a=input('\n1.Edit Profile\n2.View Friends\n\nEnter choice:')
                if int(a)==1:
                    edit_profile.profile(username)
                if int(a)==2:
                    list2=viewDB.viewfriends(username)
                    n=0
                    print('----------------------------')
                    print('        VIEW FRIENDS        ')
                    print('----------------------------')
                    for j in list2:
                        n=n+1
                        print(n,'. ',j.get_name(),'(',j.get_username(),')',' ',j.get_city())
    
        if int(value)==5:
            edit_profile.change_pwd(username)
        if int(value)==2:
            print('----------------------------')
            print('        Status Update       ')
            print('----------------------------')
            v1=input('\nEnter status:')
            user1.set_updates(v1)
            user1.set_username(username)
            v2=input('\nConfirm (y/n):')
            if(v2.lower()=='y'):
                insertDB.status_update(user1)
                print('Status Updated successfully!!!')
            elif (v2.lower()=='n'):
                print('Status not updated')
        if int(value)==3:
            approve_request.approve(username)
        if int(value)==4:
            showfeeds.feeds(username)
        if int(value)==6:
            find_friends.search_friends(username)
        if int(value)==7:
            pass
    finally:
        v1=input('Press x to return to Home or 7 to exit:') 
        if v1=='x':
            home_screen(username)
        if v1=='7':
            print('EXIT')