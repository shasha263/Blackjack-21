def random_():
    import random
    playercards=[]
    dealercards=[]
    rand_num=[]
    card_types=['Clubs', 'Diamonds', 'Hearts', 'Spades']
    print("""
        Welcome to Blackjack Game
        """)    
    for n in card_types:
        for i in range(1,11):
            rand_num.append(i)
        rand_num.append(10)
        rand_num.append(10)
        rand_num.append(10)    
    #print(rand_num) #test purpose
    for i in range(1,3):
        playercards.append(random. choice(rand_num))        
    print(f"Player's cards are {playercards}")
    for i in range(1,3):
        dealercards.append(random. choice(rand_num))        
    print(f"Dealer's one card is {dealercards[0]}")

    while True:  
        #blck.rand_num()
        begin=input("What do you want to do? Hit or Stand? /n Please enter H for Hit and S for Stand.")
        if begin=="H".lower():
            if sum(playercards) >= 21:
                print("Player Busted") 
            elif sum(playercards) < 21:
                playercards.append(random.choice(rand_num))  
                print(f"Player's cards are: {playercards}")                 
            else:
                print("Player Busted")                    
        elif begin=="S".lower():
            print(f"Player's cards are: {playercards}") 
            print(f"Dealer's cards are: {dealercards}")  
            if sum(playercards) > sum(dealercards):
                print('Blackjack :-)')
                break            
            elif sum( dealercards) < 17:
                dealercards.append(random.choice(rand_num))  
                print(f"Dealer's cards are: {dealercards}") 
                break
            elif sum(dealercards) > sum(playercards):
                print('Busted!!!')       
                break       
            else:
                print("Dealer Busted")
                break
        else:
            print("Invalid Input. Please enter only H or S")          

random_()