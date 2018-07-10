'''
Created on May 3, 2016

@author: kundhuru.shireesha
'''
from Database import insertDB
from Database import viewDB

'''------------------------------------below function is to update like count and like status---------------------------'''

def update_like(username1,updateid2):            
    value=viewDB.getlike(username1,updateid2)  
    if(int(value)==0):
        list1=viewDB.getlikecount(updateid2)
        insertDB.insertlikestatus(username1,updateid2,'Liked')
        insertDB.updatelikecount(int(list1[0]+1),int(list1[1]),updateid2)
    else:
        val=viewDB.getlikestatus(username1,updateid2)
        if(val=='Unliked'):
            list1=viewDB.getlikecount(updateid2)
            insertDB.updatelike(username1,updateid2,'Liked')
            insertDB.updatelikecount(int(list1[0]+1),int(list1[1]-1),updateid2)
        else:
            print("Already LIKED!!")
            
'''------------------------------------below function is to update dislike count and like status---------------------------'''
            
def update_unlike(username1,updateid2):            
    value=viewDB.getlike(username1,updateid2)  
    if(int(value)==0):
        list1=viewDB.getlikecount(updateid2)
        insertDB.insertlikestatus(username1,updateid2,'Unliked')
        insertDB.updatelikecount(int(list1[0]),int(list1[1]+1),updateid2)
    else:
        val=viewDB.getlikestatus(username1,updateid2)
        if(val=='Liked'):
            list1=viewDB.getlikecount(updateid2)
            insertDB.updatelike(username1,updateid2,'Unliked')
            insertDB.updatelikecount(int(list1[0]-1),int(list1[1]+1),updateid2)
        else:
            print("Already UNLIKED!!")
            
'''----------------------below function is to view feeds,invoke respective functions and for choice(like,unlike,comments)---------------------------------'''
            
def feeds(username1):
    try:
        list1=viewDB.viewfriends(username1)
        list2=[]
        list3=[]
        list8=[]
        for i in range(0,len(list1)):
            list2.append(list1[i].get_username())
        list2.append(username1)
        for j in range(0,len(list2)):
            list4=viewDB.getupdates(list2[j])
            for k in list4:
                list3.append(k)
        list3.sort()
        list3.reverse()
        print('--------------------------')
        print('           FEEDS          ')
        print('--------------------------')
        if(len(list3)>=20):
            for i in range(0,20):
                list5=viewDB.showupdates(list3[i])
                print('\n',i+1,'.',list5[3],' (',list5[4],'): ',list5[0])
                print('Likes:',list5[1],', Dislikes:',list5[2])
                list6=viewDB.showcomments(list3[i])
                list8.append(i+1)
                list8.append(list3[i])
                for i in range(0,len(list6),3):
                    print("\n   >",list6[i+1],"(",list6[i],")",": ",list6[i+2])
                print('-----------------------------------------')
        elif(len(list3)<20):
            for i in range(0,len(list3)):
                list5=viewDB.showupdates(list3[i])
                print('\n',i+1,'.',list5[3],' (',list5[4],'): ',list5[0])
                print('Likes:',list5[1],', Dislikes:',list5[2])
                list6=viewDB.showcomments(list3[i])
                list8.append(i+1)
                list8.append(list3[i])
                for i in range(0,len(list6),3):
                    print("\n   >",list6[i+1],"(",list6[i],")",": ",list6[i+2])
                print('-----------------------------------------')
        val=input("Select feed (Press x to return to Home):")
        if(val!='x'):
            if(int(val)<=(len(list8)/2) and int(val)!=0):
                for i in range(0,len(list8),2):
                    if(list8[i]==int(val)):
                        updateid2=list8[i+1]
                        break
            else:
                print('Invalid Choice')
                return
        else:
            return
        choice=input("\n1.Like\n2.Unlike\n3.Comment\n\nEnter your choice:")
        if(int(choice)==1):
            value=viewDB.checkusername(updateid2)
            if(value!=username1):
                update_like(username1,updateid2)
            else:
                print("Cannot LIKE your own update")
        elif(int(choice)==2):
            value1=viewDB.checkusername(updateid2)
            if(value1!=username1):
                update_unlike(username1,updateid2)
            else:
                print("Cannot UNLIKE your own update")
        elif(int(choice)==3):
            comment1=input("\ncomment:")
            insertDB.insert_comment(username1,updateid2,comment1)
            return feeds(username1)
        elif(choice.lower()=='x'):
            return 
    
    finally:
        pass

    
    