'''
Created on May 2, 2016

@author: kundhuru.shireesha
'''
'''
This class represents user details
'''
class user_details:
    def __init__(self):
        self.__username=None
        self.__password=None
        self.__name=None
        self.__surname=None
        self.__gender=None
        self.__city=None
        self.__relationship_status=None

    def get_password(self):
        return self.__password


    def set_password(self, value):
        self.__password = value


    def del_password(self):
        del self.__password



    def get_username(self):
        return self.__username


    def get_name(self):
        return self.__name


    def get_surname(self):
        return self.__surname


    def get_gender(self):
        return self.__gender


    def get_city(self):
        return self.__city


    def get_relationship_status(self):
        return self.__relationship_status


   
    def set_username(self, value):
        self.__username = value


    def set_name(self, value):
        self.__name = value


    def set_surname(self, value):
        self.__surname = value


    def set_gender(self, value):
        self.__gender = value


    def set_city(self, value):
        self.__city = value


    def set_relationship_status(self, value):
        self.__relationship_status = value
    

class updates:
    def __init__(self):
        self.__updateid=None
        self.__updates=None
        self.__username=None
        self.__time=None
        self.__likes=None
        self.__dislike=None

    def get_username(self):
        return self.__username


    def set_username(self, value):
        self.__username = value


    def get_updateid(self):
        return self.__updateid


    def get_updates(self):
        return self.__updates


    def get_time(self):
        return self.__time


    def get_likes(self):
        return self.__likes


    def get_dislike(self):
        return self.__dislike


    def set_updateid(self, value):
        self.__updateid = value


    def set_updates(self, value):
        self.__updates = value


    def set_time(self, value):
        self.__time = value


    def set_likes(self, value):
        self.__likes = value


    def set_dislike(self, value):
        self.__dislike = value

class comments:
    def __init__(self):
        self.__comments=None

    def get_comments(self):
        return self.__comments


    def set_comments(self, value):
        self.__comments = value

        
            
