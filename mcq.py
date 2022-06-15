from tkinter import*
import tkinter as Tk
from tkinter import messagebox as mb

class Ques():
    def __init__(self):
        self.question=["Total number of states in India? ",
                       "Total number of Wonders? ",
                      ]
        self.choices=[[28,30,40,50],
                      [7,8,9,10],
                     ]

        self.root=Tk.Tk()
        self.root.geometry('1300x1500')
        self.root.title("Niharika-Multiple Choice Question")


        self.label_0=Tk.Label(self.root,text="Answer the question given below: ",width=50,font=("bold",18))
        self.label_0.place(x=90,y=53)

        self.label_1=Tk.Label(self.root,text="Enter your Question:",width=20,font=("bold",10))
        self.label_1.place(x=80,y=130)

        self.entry_1=Tk.Entry(self.root)
        self.entry_1.place(x=240,y=130,width=320)
    
        self.label_2=Tk.Label(self.root,text="First Choice: ",width=20,font=("bold",10))
        self.label_2.place(x=80,y=180)

        self.entry_2=Tk.Entry(self.root)
        self.entry_2.place(x=240,y=180)

        self.label_3=Tk.Label(self.root,text="Second Choice: ",width=20,font=("bold",10))
        self.label_3.place(x=80,y=230)

        self.entry_3=Tk.Entry(self.root)
        self.entry_3.place(x=240,y=230)
                    
        self.label_4=Tk.Label(self.root,text="Third Choice: ",width=20,font=("bold",10))
        self.label_4.place(x=80,y=275)

        self.entry_4=Tk.Entry(self.root)
        self.entry_4.place(x=240,y=280)

        self.label_5=Tk.Label(self.root,text="Fourth Choice: ",width=20,font=("bold",10))
        self.label_5.place(x=80,y=325)

        self.entry_5=Tk.Entry(self.root)
        self.entry_5.place(x=240,y=330)

        self.label_6=Tk.Label(self.root,text="Correct Choice: ",width=20,font=("bold",10))
        self.label_6.place(x=80,y=375)

        self.entry_6=Tk.Entry(self.root)
        self.entry_6.place(x=240,y=380)

        Tk.Button(self.root,text="SUBMIT",width=20,command=self.Submit).place(x=370,y=450)


    def Submit(self):
        mb.askquestion('Niharika-Multiple Choice Question','Do you want to submit?')

        self.root.mainloop()
        print("End Program")

Ques()






