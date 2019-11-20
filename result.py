from tkinter import *
import matplotlib.pyplot as plt


def veiew_result(marks, name):
    res = Tk()
    L1 = Label(res, text="***RESULT***", bg="green", fg="white", font=("bold", 30,), padx=180, pady=5)
    L1.grid(row=0, column=0, columnspan=8, rowspan=3)
    # blank_label
    L2 = Label(res)
    L2.grid(row=4, column=0)
    x = ("HELLO !!!!! " + name + " YOUR MARKS IS --->  " + str(marks)).upper()
    y = x + "/10"
    L3 = Label(res, text=y, font=("bold", 14,), pady=5)
    L3.grid(row=5, column=3)
    L4 = Label(res)
    L4.grid(row=6, column=0)
    M = ["Correct", "WRONG"]
    C = ["red", "yellow"]
    p=10-marks
    me=[marks,p]
    plt.pie(me, labels=M, colors=C)
    plt.axis('equal')
    plt.show()

    res.mainloop()


#veiew_result(7, "ayush")
