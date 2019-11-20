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
                 ["Which of the following is a Python tuple?",
                  "[1, 2, 3]",
                  "(1, 2, 3)",
                  "{1, 2, 3}",
                  "{}"
                  ],
                 ["Suppose t = (1, 2, 4, 3), which of the following is incorrect?",
                  "print(t[3])",
                  "t[3] = 45",
                  "print(max(t))",
                  "print(len(t))"
                  ],
                 ["What will be the output of the following Python code?\n>>>t=(1,2,4)\n>>>t[1:3]",
                  "2",
                  "4",
                  "5",
                  "3"
                  ],
                 ["output of the code\n	>>>t = (1, 2, 4, 3, 8, 9)\n>>>[t[i] for i in range(0, len(t), 2)]",
                  "[2, 3, 9]",
                  "[1, 2, 4, 3, 8, 9]",
                  "[1, 4, 8]",
                  "(1, 4, 8)"
                  ],
                 ["What will be the output of the following Python expression if the value of x is 34? \nprint(“%f”%x)" ,
                    "34.00",
                    "34.000000",
                    "34.0000",
                    "34.00000000"],
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
                 ["Which event among them is fired when the right mouse button is released?",
                  "<ButtonReleased>",
                  "<ButtonPressed>",
                  "<ButtonReleased-3>",
                  "<ButtonPressed-3>"
                  ],
                 ["Using the pack manager, how you can you put the components in a container in the same row?",
                  "A - Component.pack(side= ''LEFT'')",
                  "B - Component.pack(''Left '')",
                  "C - Component.pack(side=LEFT)",
                  "D - Component.pack(Left-side)"
                  ],
                 ["Which is the special symbol used in python to add comments?",
                  "A - $",
                  "B - //",
                  "C - /*.... */",
                  "D - #"
                  ]
                 
            ]
    answer = ["(1, 2, 3)",
              "t[3] = 45",
              "4",
              "[1, 4, 8]",
              "34.000000",
              "27.2",
              "Class",
              "<ButtonReleased-3>",
              "C - Component.pack(side=LEFT)",
              "D - #",
              
                ]
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
        B4=Button(root,text="PRE",fg="white",bg="red",font=("bold",14,),padx=5,pady=5)
        B4.grid(row=18,column=4)    

        root.mainloop()
        #print('Hello World')
    show_question(i,poi)        
        
        
#easy('ayush')
print(score__)

