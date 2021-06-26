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
    thestr=str(thenum)
    while thestr in codes:
        thenum=random.randint(0,9)
        thestr=str(thenum)
    codes.append(thestr)

title=Label(entry_frame, text="Bull=Correct Position. Cow=Correct Number, Wrong Place. There are NO duplicates. There are 4 numbers.")
title.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
guess_box=Entry(entry_frame)
guess_box.grid(row=1, column=0, padx=10, pady=15)
global result
result=Label(entry_frame, text="Result", bg="black", fg="white")
result.grid(row=2, column=0, columnspan=1, padx=10, pady=5)
answer=Label(entry_frame)
answer.grid(row=1, column=1)
theguesses=Label(entry_frame)
theguesses.grid(row=3, column=0)

def submitter():
    global cows
    global bulls
    cows=0
    bulls=0
    global guess
    guess=guess_box.get()
    global n
    n=0
    global guess_list
    guess_list=[]
    for n in range(0, len(guess)):
        guess_list.append(guess[n])
    global b
    b=0
    if len(guess_list)!=set(guess_list):
        cows-=(len(guess_list)-len(set(guess_list)))
    for b in range(0, len(guess_list)):
        if guess_list[b] in codes:
            cows+=1
                
    for a in range(0, len(guess_list)):
        if guess_list[a]==codes[a]:
            cows-=1
            bulls+=1
    result.config(text="Cows: "+str(cows)+"Bulls: "+str(bulls))
    if bulls==4:
        result.config(text="4 Bulls! Well Done!")
    theguesses['text'] += guess+" Cows: "+str(cows)+" Bulls: "+str(bulls)+"\n"
theanswer=codes[0]+codes[1]+codes[2]+codes[3]
def givein():
    answer.config(text="Answer: "+str(theanswer))
submit=Button(entry_frame, text="Submit", command=submitter)
submit.grid(row=2, column=1, columnspan=1, padx=10, pady=5)
give_up=Button(entry_frame, text="Give Up", command=givein)
give_up.grid(row=2, column=2)
root.mainloop()
