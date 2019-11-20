from tkinter import *
from sampel import *
from tkinter import messagebox
def mains_page():
    #top.destroy()
    mains=Tk()
    def select_level():
        
        x=v.get()
        nme=E1.get()
        print(x)
        if x==1:
            print(nme)
            mains.destroy()
            easy(nme)
        elif x==2:
            import medium
            mains.destroy()
            medium.easy(nme)
        else:
            import hard
            mains.destroy()
            hard.easy(nme)
            
    mains.title("MAIN_PAGE")
    L1=Label(mains,text="QUIZ",bg="green",fg="white",font=("bold",40,),padx=20,pady=20)
    L1.grid(row=0,column=0,rowspan=3,columnspan=15)
    L0=Label(mains,padx=20,pady=20)
    L0.grid(row=5,column=0)
    L2=Label(mains,text="NAME  : ",font=("bold",20,))
    L2.grid(row=6,column=3)
    E1=Entry(mains,bd=5)
    E1.grid(row=6,column=6)
    L3=Label(mains,text="REGISTRATION NO  : ",font=("bold",20,))
    L3.grid(row=7,column=3)
    E2=Entry(mains,bd=5)
    E2.grid(row=7,column=6)
    L4=Label(mains,text="SECTION  : ",font=("bold",20,))
    L4.grid(row=8,column=3)
    E3=Entry(mains,bd=5)
    E3.grid(row=8,column=6)
    L5=Label(mains,text="LEVEL :",font=("bold",18,))
    L5.grid(row=9,column=3)
    #CREATING RADIO BUTTONS
    v=IntVar()
    opt1=Radiobutton(mains,text="EASY",variable=v,value=1,font=("lora",15))
    opt1.grid(row=9,column=6)
    opt2=Radiobutton(mains,text="MEDIUM",variable=v,value=2,font=("lora",15))
    opt2.grid(row=10,column=6)
    opt2=Radiobutton(mains,text="HARD",variable=v,value=3,font=("lora",15))
    opt2.grid(row=11,column=6)
    #CREATING BUTTON
    L6=Label(mains,padx=5,pady=5)
    L6.grid(row=12,column=0)
    B1=Button(mains,text="SUBMIT",bg="green",fg="white",padx=10,pady=10,font=("bold",14,),command=select_level)
    B1.grid(row=13,column=3)
    
    mains.mainloop()
    


#mains_page()
