import random
import time
catch=random.randint(1, 10)
flee=random.randint(1,10)
rocks=0
bait=0
print('A wild chansey appeared!')
print('''________________________________________
|   Pokeball                           | Bait                                   |
|-----------------------------------------------------------------------|
|   Rock                                 |  Run                                  |
|_______________________________________|''')
while True:
    option=input('What would you like to use?>')
    if option=='pokeball':
        if catch<=(3+rocks-bait):
            print('Shake... Shake... Shake... Gotcha! Chansey was caught!')
            break
        else:
            print('Shake... Shake... Shake... Awwww, it wasn\'t caught!')
            catch=random.randint(1, 10)
    elif option=='rock':
        print('You threw a rock.')
        time.sleep(2)
        print('Chansey is getting annoyed!')
        rocks+=1
    elif option=='bait':
        print('You threw some bait.')
        time.sleep(2)
        print('Chansey is eating the bait')
        bait+=1
    elif option=='run':
        break
    if flee<=(5+rocks-bait):
        print('The wild Chansey fled!')
        break
        
    
