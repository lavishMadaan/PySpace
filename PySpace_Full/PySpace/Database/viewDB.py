
from Utility.DatabaseConnection import DBConnectivity
#from Database import insertDB
from Classes.user_details import user_details

'''--------------------------------All select functions for database is done below---------------------------'''

def get_username(username):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select username from user_details where username=:username",{"username":username})
        for i in cur:
            return 1
        return 0
    finally:
        cur.close()
        con.close()
        
def get_username_password(username1,password1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select username,password from user_details where username=:username and password=:password",{"username":username1,"password":password1})
        for i,j in cur:
            return 1
        return 0
    finally:
        cur.close()
        con.close()
        
def get_profile(username2):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list1=[]
        cur.execute("select username,name,surname,gender,city,relationship_status from user_details where username=:username",{"username":username2})
        for i,j,k,l,m,n in cur:
            user2=user_details()
            user2.set_username(i)
            user2.set_name(j)
            user2.set_surname(k)
            user2.set_gender(l)
            user2.set_city(m)
            user2.set_relationship_status(n)
            list1.append(user2)
        return list1
    finally:
        cur.close()
        con.close()

def viewfriends(username3):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list1=[]
        cur.execute("select u.username,u.name,u.city from user_details u inner join request_status r on r.friend_username=u.username and r.username=:username and r.status='Approved'",{"username":username3})
        for i,j,k in cur:
            user3=user_details()
            user3.set_username(i)
            user3.set_name(j)
            user3.set_city(k)
            list1.append(user3) 
        return list1         
    finally:
        cur.close()
        con.close()
        
def approvelist(username4):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list2=[]
        cur.execute("select u.username,u.name,u.city from user_details u inner join request_status r on r.friend_username=u.username and r.username=:username and r.status='Pending'",{"username":username4})
        for i,j,k in cur:
            user4=user_details()
            user4.set_username(i)
            user4.set_name(j)
            user4.set_city(k)
            list2.append(user4)
        return list2
    finally:
        cur.close()
        con.close()
        
def getupdates(username5):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list1=[]
        cur.execute("select nvl(updateid,0) from updates where username=:username",{"username":username5})
        for i in cur:
            list1.append(int(i[0]))
        return list1
    finally:
        cur.close()
        con.close()
        
def showupdates(updateid1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select updates,nvl(likes,0),nvl(dislike,0),u1.name,u1.username from updates u inner join user_details u1 on u.username=u1.username and updateid=:updateid",{"updateid":updateid1})
        for i,j,k,l,m in cur:
            list1=[i,j,k,l,m]
        return list1
    finally:
        cur.close()
        con.close()
        
def showcomments(updateid2):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list1=[]
        cur.execute("select u.username,u.name,c.comments from comments c inner join user_details u on u.username=c.username and updateid=:updateid",{"updateid":updateid2})
        for i,j,k in cur:
            list1.append(i)
            list1.append(j)
            list1.append(k)
        return list1
    finally:
        cur.close()
        con.close()
        
def getlike(username1,updateid1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select count(*) from like_dislike where username=:username and updateid=:updateid",{"username":username1,"updateid":updateid1})
        for i in cur:
            return int(i[0])
    finally:
        cur.close()
        con.close()
        
def getlikecount(updateid2):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select nvl(likes,0),nvl(dislike,0) from updates where updateid=:updateid",{"updateid":updateid2})
        for i,j in cur:
            list1=[i,j]
        return list1
    finally:
        cur.close()
        con.close()
        
def getlikestatus(username3,updateid3):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select likestatus from like_dislike where username=:username and updateid=:updateid",{"username":username3,"updateid":updateid3})
        for i in cur:
            return i[0]
    finally:
        cur.close()
        con.close()
        
def checkusername(updateid4):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select username from updates where updateid=:updateid",{"updateid":updateid4})  
        for i in cur:
            return i[0]
    finally:
        cur.close()
        con.close()
        
def search_friends(value1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list2=[]
        value1=value1.lower()
        cur.execute("select username,name,surname,city from user_details where lower(username) like '%"+value1+"%' or lower(name) like '%"+value1+"%' or lower(surname) like '%"+value1+"%'")
        for i,j,k,l in cur:
            user5=user_details()
            user5.set_username(i)
            user5.set_name(j)
            user5.set_surname(k)
            user5.set_city(l)
            list2.append(user5)
        return list2
    finally:
        cur.close()
        con.close()
