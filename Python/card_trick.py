import random
import sys
import time

#SYMBOL BANK: DIAMOND ♦ HEART ♥ CLUBS ♣ SPADES ♠

#i=0
n=0
the_values=[]
the_suits=[]
pile_1=[]
pile_2=[]
pile_3=[]
every_card=[]

i=0
the_values.clear()
the_suits.clear()
pile_1.clear()
pile_2.clear()
pile_3.clear()

i=0
potential_value=['A♦', '2♦', '3♦', '4♦', '5♦', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', 'A♣', '2♣', '3♣', '4♣', '5♣', 'A♠', '2♠', '3♠', '4♠', '5♠']

n=0
while n<21:
    every_card.extend(potential_value)
    n+=1
n=0
i=0
while i<7:
    pile_1.append(every_card[3*i])
    pile_2.append(every_card[3*i+1])
    pile_3.append(every_card[3*i+2])
    i+=1
#print(card_value[3*i]+ card_suit[3*i]+"    " + card_value[(3*i)+1]+ card_suit[(3*i)+1]+"    " +card_value[(3*i)+2]+ card_suit[(3*i)+2])
i=0
while i<7:
    #print(the_values[3*i]+ the_suits[3*i]+"    " + the_values[(3*i)+1]+ the_suits[(3*i)+1]+"    " +the_values[(3*i)+2]+ the_suits[(3*i)+2])
    print(pile_1[i]+"    " + pile_2[i]+"    " +pile_3[i])
    i+=1
the_pile=int(input("Please pick a card and type the pile it is in (1, 2 or 3) \n >"))
all_cards=[]
if the_pile == 1:
    all_cards.extend(pile_2)
    all_cards.extend(pile_1)
    all_cards.extend(pile_3)
if the_pile == 2:
    all_cards.extend(pile_1)
    all_cards.extend(pile_2)
    all_cards.extend(pile_3)
if the_pile == 3:
    all_cards.extend(pile_1)
    all_cards.extend(pile_3)
    all_cards.extend(pile_2)

i=0

while i<7:
    print(all_cards[3*i]+"    " + all_cards[(3*i)+1]+"    " +all_cards[(3*i)+2])
    i+=1
i=0
pile_1.clear()
pile_2.clear()
pile_3.clear()
while i<7:
    pile_1.append(all_cards[3*i])
    pile_2.append(all_cards[3*i+1])
    pile_3.append(all_cards[3*i+2])
    i+=1
new_pile=int(input("Which pile is it in now? \n >"))
n=0
all_cards_2=[]

if new_pile == 1:
    all_cards_2.extend(pile_2)
    all_cards_2.extend(pile_1)
    all_cards_2.extend(pile_3)
if new_pile == 2:
    all_cards_2.extend(pile_1)
    all_cards_2.extend(pile_2)
    all_cards_2.extend(pile_3)
if new_pile == 3:
    all_cards_2.extend(pile_1)
    all_cards_2.extend(pile_3)
    all_cards_2.extend(pile_2)

n=0
while n<7:
    print(all_cards_2[3*n]+"    " + all_cards_2[(3*n)+1]+"    " +all_cards_2[(3*n)+2])
    n+=1
final_pile=int(input("Which pile is your card in now? (I promise this is the last time) \n >"))


pile_1.clear()
pile_2.clear()
pile_3.clear()

i=0

while i<7:
    pile_1.append(all_cards_2[3*i])
    pile_2.append(all_cards_2[3*i+1])
    pile_3.append(all_cards_2[3*i+2])
    i+=1

all_cards_2.clear()
    
if final_pile == 1:
    all_cards_2.extend(pile_2)
    all_cards_2.extend(pile_1)
    all_cards_2.extend(pile_3)
if final_pile == 2:
    all_cards_2.extend(pile_1)
    all_cards_2.extend(pile_2)
    all_cards_2.extend(pile_3)
if final_pile == 3:
    all_cards_2.extend(pile_1)
    all_cards_2.extend(pile_3)
    all_cards_2.extend(pile_2)

n=0

print(all_cards_2[10])




##the_pile=input("Please pick a card and type the pile it is in (1, 2 or 3) \n >")
##all_cards=[]
##if the_pile == 1:
##    all_cards.extend(pile_2)
##    all_cards.extend(pile_1)
##    all_cards.extend(pile_3)
##if the_pile == 2:
##    all_cards.extend(pile_1)
##    all_cards.extend(pile_2)
##    all_cards.extend(pile_3)
##if the_pile == 3:
##    all_cards.extend(pile_1)
##    all_cards.extend(pile_3)
##    all_cards.extend(pile_2)
##print(all_cards)
    
