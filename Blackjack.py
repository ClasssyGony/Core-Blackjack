import random, os

deck = []
playerDeck = []
dealersDeck = []

def shuffle(arr):
    global deck
    last_index = len(arr)-1
    while last_index > 0:
        rand_index = random.randint(0,last_index)
        temp = arr[last_index]
        arr[last_index] = arr[rand_index]
        arr[rand_index] = temp
        last_index -= 1
    deck = arr

def reset():
    global deck, playerDeck, dealersDeck

    os.system("clear")

    suits = ["♥","♦","♣","♠"]
    values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    deck = []

    STARTING_CARDS = 2
    playerDeck = []
    dealersDeck = []

    for suit in suits:
        for value in values:
            card = (f"{suit} {value}")
            deck.append(card)

    for x in range(STARTING_CARDS):
        playerDeck.append(deck.pop(0))
        dealersDeck.append(deck.pop(0))

    # # # # # # # # # # # # # # # # # # #
    print("########  ##          ###     ######  ##    ##       ##    ###     ######  ##    ## ")
    print("##     ## ##         ## ##   ##    ## ##   ##        ##   ## ##   ##    ## ##   ##  ")
    print("##     ## ##        ##   ##  ##       ##  ##         ##  ##   ##  ##       ##  ##   ")
    print("########  ##       ##     ## ##       #####          ## ##     ## ##       #####    ")
    print("##     ## ##       ######### ##       ##  ##   ##    ## ######### ##       ##  ##   ")
    print("##     ## ##       ##     ## ##    ## ##   ##  ##    ## ##     ## ##    ## ##   ##  ")
    print("########  ######## ##     ##  ######  ##    ##  ######  ##     ##  ######  ##    ## ")
    print("")
    print("____________________________________________________________________________________")
    print("")

    shuffle(deck)
    print("Shuffling Deck")
    print("")
    
def pick_card(person):
    global deck, playerDeck, dealersDeck

    if person == "player":
        playerDeck.append(deck.pop(0))
    elif person == "dealer":
        dealersDeck.append(deck.pop(0))

def checkCardValue(personsDeck):
    value = 0
    for card in personsDeck:
        cards = card.split()
        try:
            value += int(cards[1])
        except ValueError:
            if cards[1] == "J" or cards[1] == "Q" or cards[1] == "K":
                value += 10
            elif cards[1] == "A":
                value += 1


    return value

def checkWin(personsDeck):
    win = False

    if personsDeck[0].split()[1] == "10" and personsDeck[1].split()[1] == "A":
        win = True
    elif personsDeck[1].split()[1] == "10" and personsDeck[0].split()[1] == "A":
        win = True

    elif personsDeck[0].split()[1] == "J" and personsDeck[1].split()[1] == "A":
        win = True
    elif personsDeck[1].split()[1] == "J" and personsDeck[0].split()[1] == "A":
        win = True

    elif personsDeck[0].split()[1] == "Q" and personsDeck[1].split()[1] == "A":
        win = True
    elif personsDeck[1].split()[1] == "Q" and personsDeck[0].split()[1] == "A":
        win = True

    elif personsDeck[1].split()[0] == "K" and personsDeck[1].split()[1] == "A":
        win = True
    elif personsDeck[1].split()[1] == "K" and personsDeck[0].split()[1] == "A":
        win = True

    elif personsDeck[1].split()[0] == "A" and personsDeck[1].split()[1] == "A":
        win = True
    elif personsDeck[1].split()[1] == "A" and personsDeck[0].split()[1] == "A":
        win = True
    return win

def checkValueWin(playersDeck, dealersDeck):
    playerWin = None

    if checkCardValue(playersDeck) <= 21:
        if checkCardValue(dealersDeck) <= 21:
            if checkCardValue(playersDeck) == checkCardValue(dealersDeck):
                playerWin = None
            elif checkCardValue(playersDeck) > checkCardValue(dealersDeck):
                playerWin = True
            else:
                playerWin = False
        else:
            playerWin = True
    elif checkCardValue(dealersDeck) <= 21:
        playerWin = False
    else:
        playerWin = None
    return playerWin

def askReset(condition):
    global running
    
    print("")
    print(condition)
    print(f"Dealer's cards {dealersDeck}")
    print("")
    if input("Do you want to play again? y/n ") == "y":
        reset()
    else:
        running = False

reset()

running = True
while running:
    if checkWin(playerDeck) == False:
        print(f"Player's cards {playerDeck}")
        if checkWin(dealersDeck) == False:
            Ask_To_Pick_Card = input("Do you want to pick another card? y/n ")
            if Ask_To_Pick_Card == "y":
                pick_card("player")
            elif Ask_To_Pick_Card == "n":
                while checkCardValue(dealersDeck) <= 15:
                    pick_card("dealer")
                if checkValueWin(playerDeck,dealersDeck) == True:
                    askReset("You Won")
                elif checkValueWin(playerDeck,dealersDeck) == False:
                    askReset("You Lost")
                elif checkValueWin(playerDeck,dealersDeck) == None:
                    askReset("You Tied")
            else:
                print("Not Valid Input")
        else:
            askReset("You Lost")
    else:
        askReset("You Won")

os.system("clear")
