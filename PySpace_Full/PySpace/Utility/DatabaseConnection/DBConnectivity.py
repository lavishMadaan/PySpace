'''
Created on Nov 11, 2015
 
@author: Yashwant.Sagar
'''
 
 
import cx_Oracle

def create_connection():
    return cx_Oracle.Connection('T728295/T728295@10.123.79.57/GEORLI02')

def create_cursor(con):
    return cx_Oracle.Cursor(con)