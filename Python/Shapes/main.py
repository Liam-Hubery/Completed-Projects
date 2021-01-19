##Try typing in length and width at when the program has finished

import random
import sys
from time import sleep
import math

f=open("shapes.txt", "r")
found_user=f.readline()
found_pass=f.readline()
found_score=f.readline()
real_user=found_user[:-1]
real_pass=found_pass[:-1]
lines=f.readlines()
with open("shapes.txt", "r") as f:
    ##score = f.read(lines[1])
    global score_ints
    score_ints = [ int(x) for x in found_score.split() ]
    global the_score
    the_score=score_ints[0]
    ##print("Current Score:",score_ints)
with open("shapes.txt", "w+") as f:
                f.write(real_user)
                f.write("\n"+real_pass)
#with open("shapes.txt", "w+") as f:
neworold=int(input("Would you like to create a new account? 1 for new, 0 for sign in to original.\n>"))
if neworold==1:
        confirmation=int(input("This will overwrite previous data, are you sure? 1 for yes, 0 for no.\n>"))
        if confirmation==1:
            #f.truncate(0)
            username=input("Please type in your new username \n>")
            password=input("Please type in your new password \n>")
            with open("shapes.txt", "w+") as f:
                f.write(username)
                f.write("\n"+password)
                f.write("\n0")
            print("The program will now terminate. Please restart the program and sign in.")
            sleep(3)
            sys.exit()
        elif confirmation==0:
            exit()

elif neworold==0:
    guess_user=input("Please type in the username \n>")
    guess_pass=input("Please type in the password \n>")
    #found_user=f.readlines()
    if guess_user==(real_user):
        print("Correct Username")
    else:
        print("Incorrect Username")
        sys.exit()
    if guess_pass==real_pass:
        print("Correct Pass")
    else:
        print("Incorrect Password")
        sys.exit()
def main():
        global the_score
        print("Current Score=",the_score)
        print("\nPlease choose the shape number you would like to practice:\n1. Rectangle or Square\n2.Triangle (Isosceles)\n3.Paralellogram or Rhombus\n4.Trapezium\n5.Circle\n6. Sector\n7.Circle with diameter\n8.Quit")
        request=int(input("\n>"))
        length=random.randint(2, 12)
        width=random.randint(2, 12)
        height=random.randint(2, 12)
        ##sleep(3)
        if request==8:
                final_add=str(the_score)
                with open("shapes.txt", "w+") as f:
                        f.write(real_user)
                        f.write("\n"+real_pass)
                        f.write("\n"+final_add)
                sys.exit()
        if request==1:
                area=length*width
        if request==2:
                slope=math.sqrt(((width/2)**2)+(length)**2)
                area=(length*width)/2
                slant=round(slope)
        if request==3:
                area=length*width
                slope=math.sqrt(((width/2)**2)+(length)**2)
                slant=round(slope)
        if request==4:
                area=(length+width)/2*height
        if request==5:
                radius=random.randint(1,1200)/100
                area=round((math.pi*((radius)**2)), 2)
        if request ==6:
                angle=random.randint(1, 360)
                multiplier=360/angle
                radius=random.randint(1,1200)/100
                area=round((math.pi*((radius)**2))/multiplier, 2)
        if request==7:
                diameter=random.randint(2, 2400)/100
                radius=diameter/2
                area=round((math.pi*((diameter/2)**2)), 2)
        i=0
        correct_value=random.randint(0, 3)
        print("Please select the correct value")
        if request==1:
                print("Length =", length)
                print("Width =", width)
        if request==2 or request==3:
                print("Base =", width)
                print("Height =", length)
                print("Sloped side=", slant)
        if request==4:
                print("Length 1 =",width)
                print("Length 2 =",length)
                print("Height =",height)
        if request==5:
                print("Radius =",radius)
        if request==6:
                print("Radius =",radius)
                print("Angle =",angle)
        if request==7:
                print("Diameter =",diameter)
        while i<correct_value:
                operation=random.randint(0, 1)
                if request<5:
                        if operation==0:
                                option=area+random.randint(1,20)
                        if operation==1:
                                option=area-random.randint(1,20)
                if request>4:
                        if operation==0:
                                option=(area+random.randint(1,120)/100)
                        if operation==1:
                                option=(area-random.randint(1,120)/100)
                print("\n",i,".  ",option)
                i+=1
        print("\n",i,".  ",area)
        correct_answer=i
        i+=1
        while i<4:
                operation=random.randint(0, 1)
                if operation==0:
                        option=area+random.randint(1,20)
                if operation==1:
                        option=area-random.randint(1,20)
                print("\n",i,".  ",option)
                i+=1
        answer_input=int(input("\n>"))
        if answer_input==correct_answer:
                print("Correct")
                the_score+=2
                sleep(2)
                main()
        else:
                print("Incorrect")
        sleep(2)
        answer_input=int(input("\n>"))
        if answer_input==correct_answer:
                print("Correct")
                the_score+=1
        else:
                print("Incorrect")
        print("Correct answer was:",area)
        sleep(2)
        main()
while True:
        main()
                
f.close()
