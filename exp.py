# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 12:31:33 2022

@author: HP
"""
import datetime
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='library')
mycursor=mydb.cursor()

from tkinter import *
from tkinter.ttk import *


r=Tk()
r.geometry("600x400")
r.title("login window")
lab=Label(r,text="Library Management System").pack()
x=StringVar()
y=StringVar()


def c11():
    nw=Toplevel(r)
    nw.geometry("600x400")
    nw.title("based on book name")
    tv=StringVar(nw)
    l=Label(nw,text="book name").pack()
    e=Entry(nw,textvariable=tv).pack()
    def c11sub():
        book_name=tv.get()
        mycursor.execute("select * from book_details where book='"+book_name+"'")
        for x in mycursor:
            T.insert(END,str(x))
    b=Button(nw,text="submit",command=c11sub)
    b.pack()
    T=Text(nw)
    T.pack()
    

            
def c12():
    nw=Toplevel(r)
    nw.geometry("600x400")
    nw.title("based on category")
    tv=StringVar()
    l=Label(nw,text="Catagory").pack()
    e=Entry(nw,textvariable=tv).pack()
    def c12sub():
        category=tv.get()
        mycursor.execute("select * from book_details where category='"+category+"'")
        for x in mycursor:
            T.insert(END,str(x))
    b=Button(nw,text="submit",command=c12sub)
    b.pack()
    T=Text(nw)
    T.pack()
    

      
def c14():
    nw=Toplevel(r)
    nw.geometry("600x400")
    tv=StringVar(nw)
    nw.title("based on publication")
    l=Label(nw,text="publication").pack()
    e=Entry(nw,textvariable=tv).pack()
    def c14sub():
        publication=tv.get()
        mycursor.execute("select * from book_details where publication='"+publication+"'")
        for x in mycursor:
            T.insert(END,str(x))
    b=Button(nw,text="submit",command=c14sub)
    b.pack()
    T=Text(nw)
    T.pack()    

def c13():
    nw=Toplevel(r)
    nw.geometry("600x400")
    nw.title("based on author name")
    tv=StringVar(nw)
    l=Label(nw,text="author").pack()
    e=Entry(nw,textvariable=tv).pack()
    def c13sub():
        author=tv.get()
        mycursor.execute("select * from book_details where author='"+author+"'")
        for x in mycursor:
            T.insert(END,str(x))
    b=Button(nw,text="submit",command=c13sub)
    b.pack()
    T=Text(nw)
    T.pack()

def c15():
    nw=Toplevel(r)
    nw.geometry("600x400")
    nw.title("alphabetical order")
    T=Text(nw)
    T.pack()
    mycursor.execute("select * from book_details order by book")
    for x in mycursor:
        T.insert(END,str(x)+'\n')

def c1():
    nw=Toplevel(r)
    nw.geometry("600x400")
    nw.title("1. VIEWING BOOK RECORDS")
    but1=Button(nw,text="1. by giving book name",command=c11)
    but2=Button(nw,text="2. based on catagory",command=c12)
    but3=Button(nw,text="3. based on author",command=c13)
    but4=Button(nw,text="4. based on publcation",command=c14)
    but5=Button(nw,text="5. alphabetical order",command=c15)
    but1.pack()
    but2.pack()
    but3.pack()
    but4.pack()
    but5.pack()

def c3():
    nw=Toplevel(r)
    nw.geometry("600x400")
    nw.title("3. VIEWING BOOK STATUS")
    tv=StringVar(nw)
    l=Label(nw,text="Book Name").pack()
    e=Entry(nw,textvariable=tv).pack()
    def c3sub():
        book_name=tv.get()
        mycursor.execute("select * from book_status WHERE BOOK='"+book_name+"'")
        for x in mycursor:
            T.insert(END,str(x))
    b=Button(nw,text="submit",command=c3sub)
    T=Text(nw)
    b.pack()
    T.pack()

def c2():
    nw=Toplevel(r)
    nw.geometry("600x400")
    a=StringVar(nw)
    b=StringVar(nw)
    c=StringVar(nw)
    d=StringVar(nw)
    nw.title("2. ADDING BOOK RECORDS")
    mycursor.execute("create table if not exists book_details (sno int NOT NULL AUTO_INCREMENT PRIMARY KEY, book VARCHAR(50) NOT NULL, author VARCHAR(30), publication VARCHAR(40), category varchar(20))")
    mycursor.execute("create table if not exists book_status (sno int not null auto_increment primary key, book varchar(50) not null, status char(1) not null, name varchar (30), date_of_issuing date, contact char(10))")
    l1=Label(nw,text="book name").pack()
    e1=Entry(nw,textvariable=a).pack()
    l2=Label(nw,text="author").pack()
    e2=Entry(nw,textvariable=b).pack()
    l3=Label(nw,text="publication").pack()
    e3=Entry(nw,textvariable=c).pack()
    l4=Label(nw,text="category").pack()
    e4=Entry(nw,textvariable=d).pack()
    def c2sub():
        book_name=a.get()
        author=b.get()
        publication=c.get()
        category=d.get()
        mycursor.execute("INSERT INTO book_details(book,author,publication,category) VALUES('{}','{}','{}','{}')".format(book_name,author,publication,category))
        mydb.commit()
        mycursor.execute("insert into book_status(book,status) values('{}','{}')".format(book_name,'n'))
        mydb.commit()
        l=Label(nw,text="succesfully added").pack()
        mycursor.execute("select * from book_details")
        for x in mycursor:
            T.insert(END,str(x)+'\n')

    button=Button(nw,text="submit",command=c2sub)
    button.pack()
    T=Text(nw)
    T.pack()    

def c4():
    nw=Toplevel(r)
    nw.geometry("600x400")
    nw.title("4. CHANGING BOOK STATUS")
    x=StringVar(nw)
    y=StringVar(nw)
    z=StringVar(nw)
    a=StringVar(nw)
    b=StringVar(nw)
    c=StringVar(nw)
    d=StringVar(nw)
    def c42():
        l=Label(nw,text="book name").pack()
        entry=Entry(nw,textvariable=d).pack()
        def c42sub():
            book_name=d.get()
            mycursor.execute("update book_status set status='n', date_of_issuing=NULL, contact=NULL, name=NULL where BOOK='"+book_name+"'")
            mydb.commit()
            label=Label(nw,text="successfully returned").pack()
        button=Button(nw,text="submit",command=c42sub).pack()
    def c41():
        l=Label(nw,text="book name").pack()
        e=Entry(nw,textvariable=y).pack()
        l1=Label(nw,text="name").pack()
        e1=Entry(nw,textvariable=x).pack()
        l2=Label(nw,text="date_of_issuing").pack()
        d=Spinbox(nw,from_=1,to=31,textvariable=a).pack()
        m=Spinbox(nw,from_=1,to=12,textvariable=b).pack()
        y1=Spinbox(nw,from_=2021,to=3000,textvariable=c).pack()
        l3=Label(nw,text="contact").pack()
        e3=Entry(nw,textvariable=z).pack()
        def c41sub():
            book_name=y.get()
            name=x.get()
            year=c.get()
            month=b.get()
            date=a.get()
            contact=z.get()
            doi=datetime.date(int(year),int(month),int(date))
            mycursor.execute("update book_status set status='y', contact='"+contact+"', name='"+name+"' WHERE BOOK='"+book_name+"'")
            mydb.commit()
            mycursor.execute("update book_status set date_of_issuing='{}' where BOOK='{}'".format(str(doi),book_name))
            mydb.commit()
            label=Label(nw,text="successfully changed").pack()  
        but=Button(nw,text="submit",command=c41sub).pack()
    issue=Button(nw,text="issue",command=c41).pack()
    returns=Button(nw,text="return",command=c42).pack()

def c5():
    nw=Toplevel(r)
    nw.geometry("600x400")
    nw.title("5.PENALTY RECORD")
    x=StringVar(nw)
    y=StringVar(nw)
    z=StringVar(nw)
    a=StringVar(nw)
    b=StringVar(nw)
    c=StringVar(nw)
    mycursor.execute("create table if not exists penalty_record(book varchar(20), name varchar(20), weeks int, penalty int)")
    def c51():
        l=Label(nw,text="book name").pack()
        e=Entry(nw,textvariable=x).pack()
        l1=Label(nw,text="name").pack()
        e1=Entry(nw,textvariable=y).pack()
        l2=Label(nw,text="weeks").pack()
        e2=Entry(nw,textvariable=z).pack()
        def c51sub():
            book_name=x.get()
            name=y.get()
            weeks=z.get()
            penalty=10*(int(weeks))
            mycursor.execute("insert into penalty_record(book,name,weeks,penalty) values('{}','{}','{}',{})".format(book_name,name,weeks,penalty))
            mydb.commit()
            label=Label(nw,text="successfully added").pack()
        but=Button(nw,text="submit",command=c51sub).pack()
    def c52():
        l1=Label(nw,text="name").pack()
        e1=Entry(nw,textvariable=b).pack()
        l=Label(nw,text="weeks").pack()
        e=Entry(nw,textvariable=a).pack()
        def c52sub():
            name=b.get()
            weeks=a.get()
            penalty=10*(int(weeks))
            mycursor.execute("update penalty_record set weeks='{}', penalty={} where name='{}'".format(weeks,penalty,name))
            mydb.commit()
            label=Label(nw,text="successfully changed").pack()            
        but=Button(nw,text="submit",command=c52sub).pack()
    def c53():
        def c53sub1():
            nw1=Toplevel(r)
            nw1.geometry("600x400")
            T=Text(nw1)
            mycursor.execute("select * from penalty_record")
            for x in mycursor:
                T.insert(END,str(x)+'\n')
            T.pack()
        def c53sub2():
            l1=Label(nw,text="book name").pack()
            e1=Entry(nw,textvariable=c).pack()
            def c53sub21():
                book=c.get()
                mycursor.execute("select * from penalty_record where book='"+book+"'")
                for x in mycursor:
                    T.insert(END,str(x)+'\n')
            but=Button(nw,text="submit",command=c53sub21)
            T=Text(nw)
            but.pack()
            T.pack()
        but1=Button(nw,text="all",command=c53sub1).pack()
        but2=Button(nw,text="by book name",command=c53sub2).pack()
    b1=Button(nw,text="add record",command=c51).pack()
    b2=Button(nw,text="change record",command=c52).pack()
    b3=Button(nw,text="view record",command=c53).pack()
    
def submit():
    username=x.get()
    password=y.get()
    mycursor.execute("select * from login")
    c=0
    for a in mycursor:
        if a[0]==username:
            c+=1
            if a[1]==eval(password):
                button=Button(r,text="click to proceed",command=choices).pack()
               
            else:
                label=Label(r,text="wrong password").pack()
    if c==0:
        label=Label(r,text="no such username").pack()
    x.set("")
    y.set("")
    
labe1=Label(r,text="username").pack()
e1=Entry(r,textvariable=x).pack()
label2=Label(r,text="password").pack()
e2=Entry(r,textvariable=y).pack()
b=Button(r,text="Submit",command=submit).pack()

def choices():
    nw1=Toplevel(r)
    nw1.geometry("600x400")
    nw1.title("CHOICES")
    b1=Button(nw1,text="1. VIEWING BOOK RECORDS",command=c1)
    b2=Button(nw1,text="2. ADDING BOOK RECORDS",command=c2)
    b1.pack()
    b2.pack()
    b3=Button(nw1,text="3. VIEWING BOOK STATUS",command=c3).pack()
    b4=Button(nw1,text="4. CHANGING BOOK STATUS",command=c4).pack()
    b5=Button(nw1,text="5.PENALTY REPORT",command=c5).pack()

r.mainloop()
