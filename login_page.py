from tkinter import *
import random
from db import *
from main_page import *
from tkinter import messagebox
def captcha_generater():
    capta=[]
    j=0
    for i in range(0,5):
        x=random.randint(69,122)
        d=chr(x)
        if d.isalpha()==False:
            capta.insert(i,str(i))
        else:
            capta.insert(i,d)
        j+=1
        #print(capta)   
    chapta1=("").join(capta)
    return(chapta1)
def login():        
    top=Tk()
    
    def sinup1():
        top.destroy()
        sinup()
    def login1():
        x=E1.get()
        y=E2.get()
        if(x=="" or y==""):
            L3.config(text="Plese enter all values")
        else:
            k=check_login(x,y)
            if k==True:
                top.destroy()
                mains_page()
            else:
                b=messagebox.showwarning("Warning","INVALID EMAIL or PASSWORD")
                    
            
            
    top.title("QUIZ")
    photo = PhotoImage(file = 'quiz-png-3.png')
    photo = photo.subsample(1)
    lbl = Label(top,image = photo)
    lbl.image = photo
    lbl.grid(row=0,column=0, columnspan=8,rowspan=10)
    #rest labels
    L1=Label(top,text="EMAIL  :",font = ( "bold" , 14 , ))
    L1.grid(row=12,column=1, columnspan=3)
    E1=Entry(top,bd=5)
    E1.grid(row=12,column=4,columnspan=3)
    L2=Label(top,text="PASSWORD  :",font = ( "bold" , 14 , ))
    L2.grid(row=13,column=1,columnspan=3)
    E2=Entry(top,bd=5)
    E2.grid(row=13,column=4,columnspan=3)
    L3=Label(top,bd=5)
    L3.grid(row=14,column=3)
    B1=Button(top,text="LOGIN",bg="green",fg="white",command=login1)
    B1.grid(row=15,column=3)
    B2=Button(top,text="SIGN UP",bg="green",fg="white",command=sinup1)
    B2.grid(row=15,column=4)
    top.mainloop()

def sinup():
    sin=Tk()
    captchs=captcha_generater()
    def go_back():
        name = E0.get()
        email= E1.get()
        cap=E3.get()
        password = E2.get()
        if cap!=captchs:
            b=messagebox.showwarning("Warning","INVALID CHAPTA")
        elif name!='' and email!='' and password!='':
            insert_into_db(name,email,password)   
            sin.destroy()
            login()
    sin.title("SIGN UP")
    photo1=PhotoImage(file="Reg-online.png")
    photo1=photo1.subsample(1)
    lan=Label(sin,image=photo1)
    lan.image=photo1
    lan.grid(row=0,column=0,rowspan=5,columnspan=8)
    #labels start from here
    lost=Label(sin,padx=10,pady=10)
    lost.grid(row=6,column=0)
    L0=Label(sin,text="NAME : ",font=("bold",14,))
    L0.grid(row=7,column=3)
    E0=Entry(sin,bd=5)
    E0.grid(row=7,column=4)
    L1=Label(sin,text="EMAIL :",font=("bold",14,))
    L1.grid(row=8,column=3)
    E1=Entry(sin,bd=5)
    E1.grid(row=8,column=4)
    L2=Label(sin,text="PASSWORD :",font=("bold",14,))
    L2.grid(row=9,column=3)
    E2=Entry(sin,bd=5)
    E2.grid(row=9,column=4)
    L3=Label(sin,text="CAPTCHA : ",font=("bold",14,))
    L3.grid(row=10,column=3)
    L4=Label(sin,text=captchs,bg="grey",padx=20,pady=6,font=("bold",14,))
    L4.grid(row=10,column=4)
    #buttons
    L5=Label(sin,text="ENTER CAPTCHA:",font=("bold",14,))
    L5.grid(row=11,column=3)
    E3=Entry(sin,bd=5)
    E3.grid(row=11,column=4)
    B1=Button(sin,text="SIGN UP",bg="green",fg="white",command=go_back)
    B1.grid(row=12,column=3)

    #comparing capta 

    
        
    
    sin.mainloop()
    
login()
