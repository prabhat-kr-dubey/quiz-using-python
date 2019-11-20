import sqlite3
from tkinter import *
def insert_into_db(name,email,password):
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute('create table if not exists users (user_id integer primary key autoincrement, username text, email text, password text)')
    query = """INSERT INTO users (username,email,password) VALUES (?,?,?)"""
    c.execute(query,(name,email,password))
    conn.commit()
    c.execute('select * from users')
    print(c.fetchall())
    conn.close()
def check_login(Email,Pwd):
    #print(Email,'   ',Pwd)
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    select_query = """SELECT * FROM users WHERE email = ? AND password= ? """
    c.execute(select_query,(Email,Pwd))
    record = c.fetchone()
    print(record)
    conn.close()
    if type(record) is tuple:
        return True
    else:
        return False

#print(check_login('fghj','dfvbnm'))

    
    
    
