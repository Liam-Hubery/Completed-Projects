from tkinter import*
import random
import time
import sys
root=Tk()
i=0
codes=[]
    
entry_frame=Frame(root)
entry_frame.grid(row=0, column=0, columnspan=2, padx=30, pady=5)
entry_frame.config(bg="deep sky blue")
for i in range(0, 4):
    thenum=random.randint(0, 9)
    while thenum in codes:
        thenum=random.randint(0,9)
    codes.append(thenum)

title=Label(entry_frame, text="Bull=Correct Position. Cow=Correct Number, Wrong Place.")
title.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
guess_box=Entry(entry_frame)
guess_box.grid(row=1, column=0, padx=10, pady=15)
title=Label(entry_frame, text="Result")
title.grid(row=2, column=0, columnspan=1, padx=10, pady=5)

cows=0
bulls=0
def submitter():
    global guess
    guess=guess_box.get()
    n=0
    global guess_list
    guess_list=[]
    for n in range(0, len(guess)):
        guess_list.append(guess[n])
    n=0
    for n in range(0, len(guess)):
        if guess_list[n] in code:
            cows+=1
            
submit=Button(entry_frame, text="Submit", command=submitter)
submit.grid(row=2, column=1, columnspan=1, padx=10, pady=5)

root.mainloop()
