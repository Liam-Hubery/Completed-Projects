import random
import time
import sys

f=open("dogs.txt", "r")
linet=f.readline(-1)
thedogs=linet.split(";")
##print(thedogs)
value_cards={}

n=0
stats=[]

def main():
    card_amount=float(input("How many cards should be used? \n >"))
    i=0
    my_cards=[]
    if card_amount%2!=0:
        print("Invalid! Please type in an EVEN number between 4 and 30")
        sys.exit()
    if card_amount<4:
        print("Invalid! Please type in an EVEN number between 4 and 30")
        sys.exit()
    if card_amount>30:
        print("Invalid! Please type in an EVEN number between 4 and 30")
        sys.exit()

    while i<card_amount/2:
        card_given=random.choice(thedogs)

        i+=1
        my_cards.append(card_given)
    com_cards=[]
    while i<card_amount:
        card_given_c=random.choice(thedogs)

        i+=1
        com_cards.append(card_given_c)

    while True:
        print("\n", my_cards[0])
        h_exercise=random.randint(1, 5)
        h_intelligence=random.randint(1, 100)
        h_friendliness=random.randint(1, 10)
        h_drool=random.randint(1, 10)
        time.sleep(0.2)
        print("Exercise:", h_exercise)
        time.sleep(0.2)
        print("Intelligence:", h_intelligence)
        time.sleep(0.2)
        print("Friendliness:", h_friendliness)
        time.sleep(0.2)
        print("Drool:", h_drool)
        time.sleep(0.4)

        c_exercise=random.randint(1, 5)
        c_intelligence=random.randint(1, 100)
        c_friendliness=random.randint(1, 10)
        c_drool=random.randint(1, 10)

        choice=input("Which category would you like to use? \n >")

        print("The computer had: ")
        time.sleep(2)
        print(com_cards[0])
        print("Exercise:", c_exercise)
        time.sleep(0.2)
        print("Intelligence:", c_intelligence)
        time.sleep(0.2)
        print("Friendliness:", c_friendliness)
        time.sleep(0.2)
        print("Drool:", c_drool)
        time.sleep(0.4)



        if choice=="exercise" or choice=="Exercise":
            if h_exercise>=c_exercise:
                print("You win this round!")
                my_cards.append(com_cards[0])
                del com_cards[0]
                my_cards.append(my_cards[0])
                del my_cards[0]
            elif h_exercise<c_exercise:
                print("You lose this round!")
                com_cards.append(my_cards[0])
                del my_cards[0]
                com_cards.append(com_cards[0])
                del com_cards[0]

        elif choice=="intelligence" or choice=="Intelligence":
            if h_intelligence>=c_intelligence:
                print("You win this round!")
                my_cards.append(com_cards[0])
                del com_cards[0]
                my_cards.append(my_cards[0])
                del my_cards[0]
            elif h_intelligence<c_intelligence:
                print("You lose this round!")
                com_cards.append(my_cards[0])
                del my_cards[0]
                com_cards.append(com_cards[0])
                del com_cards[0]
                
        elif choice=="friendliness" or choice=="Friendliness":
            if h_friendliness>=c_friendliness:
                print("You win this round!")
                my_cards.append(com_cards[0])
                del com_cards[0]
                my_cards.append(my_cards[0])
                del my_cards[0]
            elif h_friendliness<c_friendliness:
                print("You lose this round!")
                com_cards.append(my_cards[0])
                del my_cards[0]
                com_cards.append(com_cards[0])
                del com_cards[0]
                

        elif choice=="drool" or choice=="Drool":
            if h_drool<=c_drool:
                
                print("You win this round!")
                my_cards.append(com_cards[0])
                del com_cards[0]
                my_cards.append(my_cards[0])
                del my_cards[0]
            elif h_drool>c_drool:
                
                print("You lose this round!")
                com_cards.append(my_cards[0])
                del my_cards[0]
                com_cards.append(com_cards[0])
                del com_cards[0]
                
        if len(my_cards)<1:
            stars=0
            while stars<5:
                print("\n\n *")
                time.sleep(0.2)
                print("*")
                time.sleep(0.2)
                print("*")
                time.sleep(0.2)
                print("*")
                time.sleep(0.2)
                print("*")
                time.sleep(0.4)
                print("YOU LOSE")
                playing=input("Do you want to play or leave?")
                if playing=="play" or playing=="Play":
                    main()
                elif playing=="leave" or playing=="Leave":
                    sys.exit()
        if len(com_cards)<1:
            stars=0
            while stars<5:
                print("\n\n *")
                time.sleep(0.2)
                print("*")
                time.sleep(0.2)
                print("*")
                time.sleep(0.2)
                print("*")
                time.sleep(0.2)
                print("*")
                time.sleep(0.4)
                print("YOU WIN")
                playing=input("Do you want to play or leave?")
                if playing=="play" or playing=="Play":
                    main()
                elif playing=="leave" or playing=="Leave":
                    sys.exit()



playing=input("Do you want to play or leave?")
if playing=="play" or playing=="Play":
    main()
elif playing=="leave" or playing=="Leave":
    sys.exit()
    
