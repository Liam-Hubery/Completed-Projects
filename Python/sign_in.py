from tkinter import*
root=Tk()
root.geometry("500x400")
root.title("Your Personal Info Stolen!")
root.resizable(False, False)
root.configure(background="MediumPurple4")
frame_heading=Frame(root)

#Frames
frame_heading.grid(row=0, column=0, columnspan=2, padx=30, pady=5)
frame_heading.config(bg="Mediumpurple1")
frame_entry=Frame(root)
frame_entry.grid(row=1, column=0, columnspan=2, padx=25, pady=10)

#Labels
Label(frame_heading, text="Your Personal Information Stolen!", font=('Arial', 16)).grid(row=0, column=0, padx=5, pady=5)
Label(frame_entry, text="Username: ").grid(row=0, column=0, padx=10, pady=5)
Label(frame_entry, text="Password: ").grid(row=1, column=0, padx=10, pady=10)
Label(frame_entry, text="PIN Number: ").grid(row=2, column=0, padx=10, pady=10)
Label(frame_entry, text="Website used ").grid(row=3, column=0, padx=10, pady=10)

#Input boxes
username=Entry(frame_entry, width=15, bg="yellow2")
username.grid(row=0, column=1, padx=25, pady=5)
password=Entry(frame_entry, width=15, bg="yellow2", show="*")
password.grid(row=1, column=1, padx=25, pady=5)
pinnum=Entry(frame_entry, width=15, bg="yellow2", show="*")
pinnum.grid(row=2, column=1, padx=25, pady=5)
website=Entry(frame_entry, width=15, bg="yellow2")
website.grid(row=3, column=1, padx=25, pady=5)

#Thank you message
thank_mess=Label(frame_entry, text="Thank You", fg="Red")
thank_blank=Label(frame_entry, text=" ", fg="Red")
thank_blank.grid(row=5, column=1, padx=25, pady=5)
def show_thank():
    thank_mess.grid(row=5, column=0, padx=25, pady=5)
'''def clear_it():
    username.delete('start', "end")
    password.delete("1.0", "end")
    pinnum.delete("1.0", "end")
    social.delete("1.0", "end")'''
    

#Submit Button
submitter=Button(frame_entry, text="Submit", font=("Arial", 16), command=show_thank)
submitter.grid(row=4, column=1, padx=25, pady=5)
'''clearer=Button(frame_entry, text="Clear", font=("Arial", 16), command=clear_it)
clearer.grid(row=4, column=0, padx=25, pady=5)'''

#Review box
reviews=Label(frame_entry, fg="Green", text="I'm so glad this program stole my information.\n Now other people can hack into my account and\n steal valuable stuff! ☆☆☆☆☆", font=("Arial", 10))
reviews.grid(row=6, column=0, padx=10, pady=5)

