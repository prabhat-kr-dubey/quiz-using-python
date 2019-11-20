from tkinter import *
score__=0
poi=""
#from result_page import *
def easy(name):
    global sore__
    score=0
    global poi
    poi=name
    questions= [
                 [
                     "What will be the output of the following Python code? \nl=[1, 0, 2, 0, 'hello', '', []] \nlist(filter(bool, nl))",
                     "[1, 0, 2, [], '', ‘hello’]",
                     "Error",
                     "[1, 2, ‘hello’]",
                     "[1, 0, 2, 0, ‘hello’, '', []]" 
                 ] ,
                 [
                     "What will be the output of the following Python expression if the value of x is 34? \nprint(“%f”%x)" ,
                    "34.00",
                    "34.000000",
                    "34.0000",
                    "34.00000000"
                     
                 ],
                [
                    "What will be the value of X in the following Python expression? \nX = 2+9*((3*12)-8)/10" ,
                    "30.8",
                    "27.2",
                    "28.4",
                    "30.0"
                ],
                [
                    "Which of these in not a core data type?" ,
                    "Tuples",
                    "Dictionary",
                    "Lists",
                    "Class"
                ],
                [
                    "Which of the following represents the bitwise XOR operator?" ,
                    "&",
                    "!",
                    "^",
                    "|"
                ],
                 ["raining'. find('z') ?",
                  "Type error",
                  "' '",
                  "-1",
                  " Not found"
                  ],
                 ["How can we swap two numbers a = 10, b = 20 in python without using third variable?",
                  "- a = b and b = a",
                  "-a.b=b.a",
                  "-b=a",
                  "a=b",
                     ],
                 ["s = 0 \nfor d in range(0, 5, 0.1):\ns += s\nprint(s)",
                  "syntax error",
                  "type error",
                  "run time error",
                  "both b & c"],
                 ["suppose we have to set a and b, then a<b is",
                  "True if len(A) is less than len(B)",
                  "True if A is a proper subset of B",
                  "True if the elements in A when compared are less than the elements in B",
                  "True if A is a proper superset of B"
                     ],
                 ["What is the out of thr following\n print('any'.encode())",
                  "any",
                  "yan",
                  "b'any'",
                  "x'any'"
                     ]
            ]
    answer = [
                "[1, 0, 2, [], '', ‘hello’]",
                "34.000000",
                "27.2",
                "Class",
                "^",
                "-1",
                "-b=a",
                "both b & c",
                "True if A is a proper subset of B",
                "b'any'"]
    i=0
    #p=name
    def show_question(i,nam):
        root=Tk()
        def get_i():
            return i
        def get_nam():
            return nam
        

        def next_question():
            xyz=get_i()
            root.destroy()
            xyz=xyz+1
            #global nme
            nme=get_nam()
            if(xyz<len(questions)):
                show_question(xyz,nme)
            else:
                end_test(score__)
        def end_test1():
            end_test(score__)
            
        def end_test(score1):
            l=get_nam()
            try:
                root.destroy()
            except:
                pass
            import result
            result.veiew_result(score1,l)
        def scores():
            z=get_i()
            value=v.get()

            if(value==answer[z]):
                global score__
                score__=score__+1
                print(score__)
            return score__
        
            
            
            
        root.title("QUESTIION")
        L1=Label(root,text="QUESTION BANK  ",bg="green",fg="white",font=("bold",30,),padx=150)
        L1.grid(row=0,column=0,rowspan=3,columnspan=8)
        #black label
        L2=Label(root,pady=15)
        L2.grid(row=4,column=0)
        
        x=("WELCOME "+nam).upper()
        L3=Label(root,text=x,font=("bold",30,))
        L3.grid(row=5,column=3)
        #black label
        L4=Label(root,pady=15)
        L4.grid(row=6,column=0)

        L5=Label(root,text="QUESTION --->",bg="yellow",fg="black",font=("bold",18,))
        L5.grid(row=7,column=3)
        #black label
        L6=Label(root,pady=15)
        L6.grid(row=8,column=0)

        L7=Label(root,text=questions[i][0],font=("bold",15,))
        L7.grid(row=9,column=3)
        L8=Label(root,pady=10)
        L8.grid(row=10,column=0)

        

        #radio_button
        v=StringVar()
        R1=Radiobutton(root,text=questions[i][1],variable=v,value=questions[i][1],font=("bold",12,))
        R1.grid(row=11,column=3)
        R2=Radiobutton(root,text=questions[i][2],variable=v,value=questions[i][2],font=("bold",12,))
        R2.grid(row=12,column=3)
        R3=Radiobutton(root,text=questions[i][3],variable=v,value=questions[i][3],font=("bold",12,))
        R3.grid(row=13,column=3)
        R4=Radiobutton(root,text=questions[i][4],variable=v,value=questions[i][4],font=("bold",12,))
        R4.grid(row=14,column=3)

        L9=Label(root,pady=10)
        L9.grid(row=15,column=0)

        #buttons
        B1=Button(root,text="SAVE",fg="white",bg="red",font=("bold",14,),padx=5,pady=5,command=scores)
        B1.grid(row=16,column=2)
        B2=Button(root,text="NEXT",fg="white",bg="red",font=("bold",14,),padx=5,pady=5,command=next_question)
        B2.grid(row=16,column=4)
        lbl=Label(root,pady=10)
        lbl.grid(row=17,column=0)
        B3=Button(root,text="END",fg="white",bg="red",font=("bold",14,),padx=5,pady=5,command=end_test1)
        B3.grid(row=18,column=2)
        B4=Button(root,text="FLAG",fg="white",bg="red",font=("bold",14,),padx=5,pady=5)
        B4.grid(row=18,column=4)    

        root.mainloop()
        #print('Hello World')
    show_question(i,poi)        
        
        
#easy('ayush')
print(score__)

