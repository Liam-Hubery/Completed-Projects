import random
import string
import time
allowed=True
t=time.localtime()
print("\n\n=======================Password generator and checker=======================")
print("The date and time is",time.asctime(t))
n=0
number_split=[1,2,3,4,5,6,7,8,9,0]
while n<13:
        bank=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '$', '%', '*', '(', ')', '-', '_', '=', '+', '1' '2', '3', '4', '5', '6', '7', '8', '9', '0']
        n+=1
        bank
def leave():
        print("Shutting Down Program...")
        time.sleep(3)
        quit()

def generate():
    print("=============================Generator===================================")
    i=0
    random_bank=[]
    while i<13:
        random_bank.append(random.choice(bank))
        i+=1
    print("\nPassword characters:",random_bank)

    
while True:
        prompt=input("\nWould you like to check a password, generate a password or leave?\n>")
        if prompt=="leave":
            leave()
        if prompt=="generate":
            generate()
        if prompt=="check":
            print("==============================Checker====================================")
            low_bank=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            my_pass=str(input("What is your password? Allowed symbols: !$%^&*()-_=+. Split each character with a comma.\n>"))
            lines=['qwertyuiop', 'asdfghjkl','zxcvbnm']
            triples=[]
            for line in lines:
                for i in range(len(line)-2):
                    triples.append(line[i:i+3])
            if len(my_pass)>31 or len(my_pass)<11 :
                print("Please make sure your password is between 6 and 16 characters")
                allowed=False
            if ',' not in my_pass:
                print("Please make sure you have a comma between your characters")
            split_pass=my_pass.split(',')
            score=len(split_pass)
            if split_pass==['p','a','s','s','w','o','r','d']:
               print("Password can't be password")
               allowed=False
            if 'a' in split_pass or 'b' in split_pass or 'c' in split_pass or 'd' in split_pass or 'e' in split_pass or 'f' in split_pass or 'g' in split_pass or 'h' in split_pass or 'i' in split_pass or 'j' in split_pass or 'k' in split_pass or 'l' in split_pass or 'm' in split_pass or 'n' in split_pass or 'o' in split_pass or 'p' in split_pass or 'q' in split_pass or 'r' in split_pass or 's' in split_pass or 't' in split_pass or 'u' in split_pass or 'v' in split_pass or 'w' in split_pass or 'x' in split_pass or 'y' in split_pass or 'z' in split_pass:
               print("Lower case letter: +5")
            if '£' in split_pass or '{' in split_pass or '}' in split_pass or '[' in split_pass or ']' in split_pass or ':' in split_pass or ';' in split_pass or "\\" in split_pass or '.' in split_pass or '|' in split_pass or '#' in split_pass or '¬' in split_pass or '`' in split_pass or '¦' in split_pass or '?' in split_pass or '@' in split_pass or '/' in split_pass or "'" in split_pass or '"' in split_pass or '>' in split_pass or '<' in split_pass:
               print("Not allowed")
               allowed=False
            if 'A' in split_pass or 'B' in split_pass or 'C' in split_pass or 'D' in split_pass or 'E' in split_pass or 'F' in split_pass or 'G' in split_pass or 'H' in split_pass or 'I' in split_pass or 'J' in split_pass or 'K' in split_pass or 'L' in split_pass or 'M' in split_pass or 'N' in split_pass or 'O' in split_pass or 'P' in split_pass or 'Q' in split_pass or 'R' in split_pass or 'S' in split_pass or 'T' in split_pass or 'U' in split_pass or 'V' in split_pass or 'W' in split_pass or 'X' in split_pass or 'Y' in split_pass or 'Z' in split_pass:
               print("Upper case letter: +5")
               score+=5
            if '!' in split_pass or '$' in split_pass or '%' in split_pass or '^' in split_pass or '*' in split_pass or '(' in split_pass or ')' in split_pass or '-' in split_pass or '_' in split_pass or '=' in split_pass or '+' in split_pass:
               print ("Special character: +5")
               score+=5
            if '1' in split_pass or '2' in split_pass or '3' in split_pass or '4' in split_pass or '5' in split_pass or '6' in split_pass or '7' in split_pass or '8' in split_pass or '9' in split_pass or '0' in split_pass:
               print ("Number: +5")
               score+=5
            if 'a' not in split_pass and 'b' not in split_pass and 'c' not in split_pass and 'd' not in split_pass and 'e' not in split_pass and 'f' not in split_pass and 'g' not in split_pass and 'h' not in split_pass and 'i' not in split_pass and 'j' not in split_pass and 'k' not in split_pass and 'l' not in split_pass and 'm' not in split_pass and 'n' not in split_pass and 'o' not in split_pass and 'p' not in split_pass and 'q' not in split_pass and 'r' not in split_pass and 's' not in split_pass and 't' not in split_pass and 'u' not in split_pass and 'v' not in split_pass and 'w' not in split_pass and 'x' not in split_pass and 'y' not in split_pass and 'z' not in split_pass:
               print("No lower case letter: -5")
               score-=5
            if 'A' not in split_pass and 'B' not in split_pass and 'C' not in split_pass and 'D' not in split_pass and 'E' not in split_pass and 'F' not in split_pass and 'G' not in split_pass and 'H' not in split_pass and 'I' not in split_pass and 'J' not in split_pass and 'K' not in split_pass and 'L' not in split_pass and 'M' not in split_pass and 'N' not in split_pass and 'O' not in split_pass and 'P' not in split_pass and 'Q' not in split_pass and 'R' not in split_pass and 'S' not in split_pass and 'T' not in split_pass and 'U' not in split_pass and 'V' not in split_pass and 'W' not in split_pass and 'X' not in split_pass and 'Y' not in split_pass and 'Z' not in split_pass:
               print("No upper case letter: -5")
               score-=5
            if '!' not in split_pass and '$' not in split_pass and '%' not in split_pass and '^' not in split_pass  and '*' not in split_pass and '(' not in split_pass and ')' not in split_pass and '-' not in split_pass and '_' not in split_pass and '=' not in split_pass and '+' not in split_pass:
               print ("No special character: -5")
               score-=5
            if '1' not in split_pass and '2' not in split_pass and '3' not in split_pass and '4' not in split_pass  and '5' not in split_pass and '6' not in split_pass and '7' not in split_pass and '8' not in split_pass and '9' not in split_pass and '0' not in split_pass:
               print ("No number: -5")
               score-=5
            input_string=my_pass.strip().lower()
            for triple in triples:
               if triple in input_string:
                   score-=5
                   print("Consecutive letters:-5")
               
            if allowed==True:
               print('\nScore:', score)
               if score<=5:
                   print("Not secure")
               elif score >0 and score<15:
                   print("Okay password")
               else:
                   print("Strong password")
            else:
               print('\n Password not allowed!\n') 
            
