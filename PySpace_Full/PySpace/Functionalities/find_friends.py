'''
Created on May 2, 2016

@author: kundhuru.shireesha
'''


from Database import viewDB
from Database import insertDB

'''---------------------------------------Below funcion to find friends----------------------------------'''

def search_friends(username1):
    val=input("\nSearch:")
    list2=[]
    list1=viewDB.search_friends(val)
    n=0
    for i in list1:
        n=n+1
        print(n,'. ',i.get_name()," ",i.get_surname()," (",i.get_username(),")",", ",i.get_city())
        list2.append(n)
        list2.append(i.get_username())
    value2=input("\nSelect Profile (Press x to return to Home): ")
    if(value2!='x'):
        for j in range(0,len(list2),2):
            if(list2[j]==int(value2)):
                username2=list2[j+1]
        view_profile(username1,username2)
    else:
        return

'''------------------------------------------Below function to view Friends profile and iterate-------------------------------------'''
     
def view_profile(username1,username2):
    list5=[]
    list3=viewDB.get_profile(username2)
    print('----------------------')
    print('     ',username2,'     ')
    print('----------------------')
    for i in list3:
        print('Username:',i.get_username(),'\nName:',i.get_name(),'\nSurname:',i.get_surname(),'\nGender:',i.get_gender(),'\nCity:',i.get_city(),'\nRelationship Status:',i.get_relationship_status())
    list4=viewDB.viewfriends(username1)
    for k in list4:
        list5.append(k.get_username())
    if(username2 in list5):
        print("\n(Already in your friend list)\n1. View Friend List")
        val1=input("\nChoice(Press x to return to Home):")
        if int(val1)==1:
            friends(username2)
        elif (val1=='x'):
            return
    else:
        print("\n1. Add Friend\n2. View Friend List")
        val1=input("\nChoice(Press x to return to Home):")
        if int(val1)==1:
            insertDB.add_friend(username1, username2)
        elif int(val1)==2:
            friends(username2)
        elif (val1=='x'):
            return

'''----------------------------------------------Below function to view Friend's friend list-----------------------'''
       
def friends(username2):
    list9=viewDB.viewfriends(username2)
    list6=[]
    n=0
    print('----------------------------------------')
    print('        ',username2,'  Friend List      ')
    print('----------------------------------------')
    for j in list9:
        n=n+1
        print(n,'. ',j.get_name(),'(',j.get_username(),')',' ',j.get_city())
        list6.append(n)
        list6.append(j.get_username())
    value2=input("\nSelect Profile (Press x to return to Home): ")
    if(value2!='x'):
        for k in range(0,len(list6),2):
            if(list6[k]==int(value2)):
                username3=list6[k+1]
        view_profile(username2,username3)
    else:
        return
        
