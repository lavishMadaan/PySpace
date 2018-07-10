'''
Created on May 3, 2016

@author: kundhuru.shireesha
'''
from Database import viewDB
from Database import insertDB

'''-------------------------------------Below Function to approve friend requests-----------------------------------'''

def approve(username4):
    list1=[]
    list2=viewDB.approvelist(username4)
    n=0
    print('----------------------------')
    print('      Approve REQUESTS      ')
    print('----------------------------')
    for i in list2:
        n=n+1
        print(n,'. ',i.get_name(),'(',i.get_username(),')',' ',i.get_city())
        list1.append(i.get_username())
    v1=input('Select Request (Press x to return to Home):')
    if(v1!='x'):
        v2=input('\n1.Approve\n2.Reject\n\nChoice:')
        if int(v2)==1:
            insertDB.approve(username4,list1[int(v1)-1])
            print('Request Approved')
        elif int(v2)==2:
            insertDB.reject(username4,list1[int(v1)-1])
            print('Request Rejected')
        else:
            print('Invalid Choice')
    else:
        return

        