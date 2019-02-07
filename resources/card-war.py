import random
diamonds = ['ace','two','three','four','five','six','seven','eight','nine','ten','Jack','Queen','King']
spades = ['ace','two','three','four','five','six','seven','eight','nine','ten','Jack','Queen','King']
hearts = ['ace','two','three','four','five','six','seven','eight','nine','ten','Jack','Queen','King']
clubs = ['ace','two','three','four','five','six','seven','eight','nine','ten','Jack','Queen','King']
player = []
computer = []
playerSuit = 0
compSuit = 0
def Computers_Card():
    compSuit = random.randint(1,4)
    if((compSuit == 1) and (len(diamonds) == 0)):
        Comp_Repick()
    elif((compSuit == 1) and (len(diamonds) > 0)):
        compsCard = random.choice(diamonds)
        computer.append(compsCard)
        diamonds.remove(compsCard)

        
    if((compSuit == 2) and (len(spades) == 0)):
        Comp_Repick()
    elif((compSuit == 2) and (len(spades) > 0)):
        compsCard = random.choice(spades)
        computer.append(compsCard)
        spades.remove(compsCard)

        
    if((compSuit == 3) and (len(hearts) == 0)):
        Comp_Repick()
    elif((compSuit == 3) and (len(hearts) > 0)):
        compsCard = random.choice(hearts)
        computer.append(compsCard)
        hearts.remove(compsCard)

        
    if((compSuit == 4) and (len(clubs) == 0)):
        Comp_Repick()
    elif((compSuit == 4) and (len(clubs) > 0)):
        compsCard = random.choice(clubs)
        computer.append(compsCard)
        clubs.remove(compsCard)
def Players_Card():
    playerSuit = random.randint(1,4)
    if((playerSuit == 1) and (len(diamonds) == 0)):
        Player_Repick()
    elif((playerSuit == 1) and (len(diamonds) > 0)):
        playersCard = random.choice(diamonds)
        player.append(playersCard)
        diamonds.remove(playersCard)

    if((playerSuit == 2) and (len(spades) == 0)):
        Player_Repick()
    elif((playerSuit == 2) and (len(spades) > 0)):
        playersCard = random.choice(spades)
        player.append(playersCard)
        spades.remove(playersCard)

    if((playerSuit == 3) and (len(hearts) == 0)):
        Player_Repick()
    elif((playerSuit == 3) and (len(hearts) > 0)):
        playersCard = random.choice(hearts)
        player.append(playersCard)
        hearts.remove(playersCard)

    if((playerSuit == 4) and (len(clubs) == 0)):
        Player_Repick()
    elif((playerSuit == 4) and (len(clubs) > 0)):
        playersCard = random.choice(clubs)
        player.append(playersCard)
        clubs.remove(playersCard)
def Comp_Repick():
    Computers_Card()
def Player_Repick():
    Players_Card()

def Compare_Cards():
    playerFlip = random.choice(player)
    compFlip = random.choice(computer)
    print("You flipped "+playerFlip+", the computer flipped "+compFlip+".")
    if(playerFlip == compFlip):
        print("It was a tie re-flip")
    elif((playerFlip == 'ace') and (compFlip != 'ace')):
        print("The computer wins.")
        computer.append(playerFlip)
        player.remove(playerFlip)
    elif((playerFlip != 'ace') and (compFlip == 'ace')):
        print("You win.")
        player.append(compFlip)
        computer.remove(compFlip)
    elif(playerFlip == 'two'):
        if(compFlip != 'ace'):
            print("The computer wins.")
            computer.append(playerFlip)
            player.remove(playerFlip)
        else:
            print("You win.")
            player.append(compFlip)
            computer.remove(compFlip)
    elif(playerFlip == 'three'):
        if((compFlip != 'ace') and (compFlip != 'two')):
            print("The computer wins.")
            computer.append(playerFlip)
            player.remove(playerFlip)
        else:
            print("You win.")
            player.append(compFlip)
            computer.remove(compFlip)
    elif(playerFlip == 'four'):
        if((compFlip != 'ace') and(compFlip != 'two')and (compFlip != 'three')):
            print("The computer wins.")
            computer.append(playerFlip)
            player.remove(playerFlip)
        else:
            print("You win.")
            player.append(compFlip)
            computer.remove(compFlip)
    elif(playerFlip == 'five'):
        if((compFlip != 'ace') and (compFlip != 'two')and (compFlip != 'three') and (compFlip != 'four')):
            print("The computer wins.")
            computer.append(playerFlip)
            player.remove(playerFlip)
        else:
            print("You win.")
            player.append(compFlip)
            computer.remove(compFlip)
    elif(playerFlip == 'six'):
        if((compFlip != 'ace') and(compFlip != 'two')and (compFlip != 'three') and (compFlip != 'four') and (compFlip != 'five')):
            print("The computer wins.")
            computer.append(playerFlip)
            player.remove(playerFlip)
        else:
            print("You win.")
            player.append(compFlip)
            computer.remove(compFlip)
    elif(playerFlip == 'seven'):
        if((compFlip != 'ace') and(compFlip != 'two')and (compFlip != 'three') and (compFlip != 'four') and (compFlip != 'five') and (compFlip != 'six')):
            print("The computer wins.")
            computer.append(playerFlip)
            player.remove(playerFlip)
        else:
            print("You win.")
            player.append(compFlip)
            computer.remove(compFlip)
    elif(playerFlip == 'eight'):
        if((compFlip != 'ace') and(compFlip != 'two')and (compFlip != 'three') and (compFlip != 'four') and (compFlip != 'five') and (compFlip != 'six') and (compFlip != 'seven')):
            print("The computer wins.")
            computer.append(playerFlip)
            player.remove(playerFlip)
        else:
            print("You win.")
            player.append(compFlip)
            computer.remove(compFlip)
    elif(playerFlip == 'nine'):
        if((compFlip != 'ace') and(compFlip != 'two')and(compFlip != 'three') and (compFlip != 'four') and (compFlip != 'five') and (compFlip != 'six') and (compFlip != 'seven') and (compFlip != 'eight')):
            print("The computer wins.")
            computer.append(playerFlip)
            player.remove(playerFlip)
        else:
            print("You win.")
            player.append(compFlip)
            computer.remove(compFlip)
    elif(playerFlip == 'ten'):
        if((compFlip != 'ace') and(compFlip != 'two')and (compFlip != 'three') and (compFlip != 'four') and (compFlip != 'five') and (compFlip != 'six') and (compFlip != 'seven') and (compFlip != 'eight') and (compFlip != 'nine')):
            print("The computer wins.")
            computer.append(playerFlip)
            player.remove(playerFlip)
        else:
            print("You win.")
            player.append(compFlip)
            computer.remove(compFlip)
    elif(playerFlip == 'Jack'):
        if((compFlip != 'ace') and(compFlip != 'two')and (compFlip != 'three') and (compFlip != 'four') and (compFlip != 'five') and (compFlip != 'six') and (compFlip != 'seven') and (compFlip != 'eight') and (compFlip != 'nine') and (compFlip != 'ten')):
            print("The computer wins.")
            computer.append(playerFlip)
            player.remove(playerFlip)
        else:
            print("You win.")
            player.append(compFlip)
            computer.remove(compFlip)
    elif(playerFlip == 'Queen'):
        if((compFlip != 'ace') and(compFlip != 'two')and (compFlip != 'three') and (compFlip != 'four') and (compFlip != 'five') and (compFlip != 'six') and (compFlip != 'seven') and (compFlip != 'eight') and (compFlip != 'nine') and (compFlip != 'ten') and (compFlip != 'Jack')):
            print("The computer wins.")
            computer.append(playerFlip)
            player.remove(playerFlip)
        else:
            print("You win.")
            player.append(compFlip)
            computer.remove(compFlip)
    elif(playerFlip == 'King'):
        if((compFlip != 'ace') and(compFlip != 'two') and (compFlip != 'three') and (compFlip != 'four') and (compFlip != 'five') and (compFlip != 'six') and (compFlip != 'seven') and (compFlip != 'eight') and (compFlip != 'nine') and (compFlip != 'ten') and (compFlip != 'Jack') and (compFlip != 'Queen')):
            print("The computer wins.")
            computer.append(playerFlip)
            player.remove(playerFlip)
        else:
            print("You win.")
            player.append(compFlip)
            computer.remove(compFlip)

for x in range(26):
    Computers_Card()
    Players_Card()

while((len(player) > 0) and (len(computer) > 0)):
    flip = input("type flip to flip the top of your deck. ").lower()
    while(flip != ""):
        if(flip == 'flip'):
            Compare_Cards()
            print("player",len(player))
            print("computer",len(computer))
            flip = input("Type flip to flip the top of your deck. ").lower()
        elif(flip == 'quit' ):
            quit
        else:
            flip = input("There was an error type 'flip' to flip the top of your deck or 'quit' to quit. ").lower()
#if(len(player) == 0):
    #print("The computer wins!")
#else:
    #print("You win!")
    
