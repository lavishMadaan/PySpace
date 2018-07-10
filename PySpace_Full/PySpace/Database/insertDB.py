'''
Created on May 2, 2016

@author: kundhuru.shireesha
'''
from Utility.DatabaseConnection import DBConnectivity  

'''--------------------------------All insert and update functions for database is done below---------------------------'''
 
def insert_details(user1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("insert into user_details values('"+user1.get_username()+"','"+user1.get_password()+"','"+user1.get_name()+"','"+user1.get_surname()+"','"+user1.get_gender()+"','"+user1.get_city()+"','"+user1.get_relationship_status()+"')")
    finally:
        cur.close()
        con.commit()
        con.close()
        
def edit_profile(username,user):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("update user_details set name='"+user.get_name()+"',surname='"+user.get_surname()+"',gender='"+user.get_gender()+"',city='"+user.get_city()+"',relationship_status='"+user.get_relationship_status()+"' where username='"+username+"'" )
    finally:
        cur.close()
        con.commit()
        con.close()
        
def chng_pwd(username,new_password):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("update user_details set password='"+new_password +"'where username='"+username+"'" )
    finally:
        cur.close()
        con.commit()
        con.close()
        
def status_update(user1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur2=DBConnectivity.create_cursor(con)
        cur.execute("select nvl(max(updateid),0) from updates")
        for i in cur:
            v1=int(i[0])+1
        user1.set_updateid(v1)   
        cur2.execute("insert into updates(updateid,updates,username) values('"+str(user1.get_updateid())+"',:updates1,'"+user1.get_username()+"')",{"updates1":user1.get_updates()})
    finally:
        cur.close()
        cur2.close()
        con.commit()
        con.close()
        
def approve(username1,username2):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur2=DBConnectivity.create_cursor(con)
        cur.execute("update request_status set status='Approved' where username=:username and friend_username=:friendname",{"username":username1,"friendname":username2})
        cur2.execute("insert into request_status values('"+username2+"','"+username1+"','Approved')")
    finally:
        cur.close()
        cur2.close()
        con.commit()
        con.close()
        
def reject (username1,username2):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("delete from request_status where username=:username and friend_username=:friendname",{"username":username1,"friendname":username2})
    finally:
        cur.close()
        con.commit()
        con.close()
        
def updatelike(username2,updateid2,status2):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("update like_dislike set likestatus='"+status2+"' where username='"+username2+"' and updateid='"+str(updateid2)+"'")
    finally:
        cur.close()
        con.commit()
        con.close()
        
def updatelikecount(a,b,updateid1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("update updates set likes='"+str(a)+"',dislike='"+str(b)+" 'where updateid='"+str(updateid1)+"'")
    finally:
        cur.close()
        con.commit()
        con.close()
        
def insertlikestatus(username3,updateid3,status1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("insert into like_dislike(updateid,username,likestatus) values('"+str(updateid3)+"','"+username3+"','"+status1+"')")
    finally:
        cur.close()
        con.commit()
        con.close()
        
def insert_comment(username4,updateid4,comment1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("insert into comments(username,updateid,comments) values('"+username4+"','"+str(updateid4)+"',:comment2)",{"comment2":comment1})
    finally:
        cur.close()
        con.commit()
        con.close()
        
def add_friend(username1,username2):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("insert into request_status(username,friend_username,status) values('"+username1+"','"+username2+"','Pending')")
    finally:
        cur.close()
        con.commit()
        con.close()

