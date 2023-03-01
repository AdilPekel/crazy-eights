import random

topCardSuit = ''
topCardNum = ''
winnerWho = ''
winner = False
magicianTurn = False
playerTurn = False
deck = []
playerCards = []
magicianCards = []
suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
nums = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

class Card:
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit

#Method to combine suits and numbers to make a deck of cards
def makeDeck():
    global deck
    global suits
    global nums
    deck = [Card(num, suit) for num in nums for suit in suits]

#Method ot shuffle the deck of cards
def shuffleDeck():
    global deck
    random.shuffle(deck)

#Method to print the deck of cards (Testing purposes)
def printDeck():
    global deck
    for card in deck:
        print(card.num + ' of ' + card.suit)

#Method to deal the deck of cards to both players
def dealCards():
    global deck
    global playerCards
    global magicianCards
    playerCards = deck[0:26]
    magicianCards = deck[26:52]
    deck.clear()

#Method to print the player's cards 
def printPlayerCards():
    global playerCards
    for card in playerCards:
        print()
        print(card.num + ' of ' + card.suit)

#Method to print the magician's cards (Testing purposes)
def printMagicianCards():
    global magicianCards
    for card in magicianCards:
        print()
        print(card.num + ' of ' + card.suit)

#Method to choose the player making the first move
def chooseFirstPlayer():
    firstPlayer = random.randint(1, 2)
    return firstPlayer

#Method to change the format of the player's deck to the same format the player uses to place cards for comparison purposes
def simpleFormat():
    global playerCards
    newFormat = []
    for card in playerCards:
        if card.num == '10':
            nums = card.num
        else:
            nums = card.num[0]
        suits = card.suit[0].upper()
        form = nums + 'o' + suits
        newFormat.append(form)
    return newFormat

#Method to check if any cards can be placed on the top of the deck
def magicianFormat():
    global magicianCards
    newFormat = []
    for card in magicianCards:
        if card.num[0] == topCardNum[0] or card.suit[0].upper() == topCardSuit:
            newFormat.append(card)
    for card in magicianCards:
        if card.num == '8':
            newFormat.append(card)
    return newFormat

#Method to check if any player has placed all their cards
def checkWinner():
    global winner
    global winnerWho
    if len(magicianCards) == 0:
        winner = True
        playerTurn = False
        magicianTurn = False
        winnerWho = 'magician'
    elif len(playerCards) == 0:
        winner = True
        playerTurn = False
        magicianTurn = False
        winnerWho = 'player'

#Method for the magician playing against the player 
def magicianPlays():
    global deck
    global magicianTurn
    global playerTurn
    global magicianCards
    drawnCard = False
    while magicianTurn == True:
        if len(deck) == 0:
            i = random.randint(0, len(magicianCards) - 1)
            print('The magician has placed the ' + magicianCards[i].num + ' of ' + magicianCards[i].suit)
            deck.append(magicianCards[i])
            magicianCards.pop(i)
            magicianTurn = False
            playerTurn = True
        elif len(deck) != 0:
            global topCardSuit
            global topCardNum
            topCardSuit = deck[len(deck) - 1].suit[0].upper()
            if deck[len(deck) - 1].num == '10':
                topCardNum = deck[len(deck) - 1].num
            else:
                topCardNum = deck[len(deck) - 1].num[0]
            formatted = magicianFormat()
            if (len(formatted)) == 0:
                magicianCards.append(deck[0])
                deck.pop(0)
                drawnCard = True
                print('The magician has drawn a card from the bottom of the pile')
                print('The top of the pile is still the ' + deck[len(deck) - 1].num + ' of ' + deck[len(deck) - 1].suit)
                magicianTurn = False
                playerTurn = True
            elif (len(formatted)) != 0:
                i = random.randint(0, len(formatted) - 1)
                j = 0
                for card in magicianCards:
                    if (formatted[i].num == card.num and formatted[i].suit == card.suit):
                        foundCard = True
                        break
                    elif j == (len(magicianCards) - 1):
                        magicianCards.append(0)
                        deck.pop(0)
                        drawnCard = True
                        print('The magician has drawn a card from the bottom of the pile')
                        print('The top of the pile is still the ' + deck[len(deck) - 1].num + ' of ' + deck[len(deck) - 1].suit)
                        magicianTurn = False
                        playerTurn = True
                        break
                    else:
                        j += 1
                if (j != (len(magicianCards) - 1) and drawnCard == False) or foundCard == True:
                    print('The magician has placed the ' + magicianCards[j].num + ' of ' + magicianCards[j].suit)
                    deck.append(magicianCards[j])
                    magicianCards.pop(j)
                    foundCard = False
                    magicianTurn = False
                    playerTurn = True

#Method for the player playing against the magician
def playerPlays():
    global deck
    global playerTurn
    global magicianTurn
    global playerCards
    newFormat = simpleFormat()
    printPlayerCards()
    while playerTurn == True:
        if len(deck) == 0:
            i = 0
            print('Which card would you like to place first? Use the format "8oS" for "8 of Spades" or "JoC"  for "Jack of Clubs"')
            decision = input()
            while decision not in newFormat:
                print('This card is not in your deck. Please select a card from your deck.')
                decision = input()
            for card in newFormat:
                if decision == card:
                    break
                else:
                    i += 1
            print('You have placed the ' + playerCards[i].num + ' of ' + playerCards[i].suit)
            deck.append(playerCards[i])
            playerCards.pop(i)
            playerTurn = False
            magicianTurn = True
        elif len(deck) != 0:
            i = 0
            global topCardSuit
            global topCardNum
            topCardSuit = deck[len(deck) - 1].suit[0].upper()
            if deck[len(deck) - 1].num == '10':
                topCardNum = deck[len(deck) - 1].num
            else:
                topCardNum = deck[len(deck) - 1].num[0]
            print('Choose a card of either the same suit or same number to place OR draw a card from the pile')
            print('Type 1 to place a card OR 2 to draw a card')
            action = input()
            while action != '1' and action != '2':
                print('Only enter the number 1 OR 2')
                action = input()
            if action == '1':
                print('Choose a card of either the same suit or same number to place')
                decision = input()
                while len(decision) < 3:
                    print('Please enter card in correct format')
                    decision = input()
                if decision[0] == '1' and decision[1] == '0':
                    cardNum = '10'
                    cardSuit = decision[3]
                else:
                    cardNum = decision[0]
                    cardSuit = decision[2]
                while (cardNum != str(topCardNum) and cardSuit != str(topCardSuit)) or (decision not in newFormat):
                    if decision not in newFormat:
                        print('This card is not in your deck. Please select a card from your deck.')
                        decision = input()
                        while len(decision) < 3:
                            print('Please enter card in correct format')
                            decision = input()
                        if decision[0] == '1' and decision[1] == '0':
                            cardNum = '10'
                            cardSuit = decision[3]
                        else:
                            cardNum = decision[0]
                            cardSuit = decision[2]
                    elif cardNum != str(topCardNum) and cardSuit != str(topCardSuit):
                        if cardNum == '8' or deck[len(deck) - 1].num == '8':
                            break
                        print('The card you selected does not have the same suit or number as the most recent card')
                        decision = input()
                        while len(decision) < 3:
                            print('Please enter card in correct format')
                            decision = input()
                        if decision[0] == '1' and decision[1] == '0':
                            cardNum = '10'
                            cardSuit = decision[3]
                        else:
                            cardNum = decision[0]
                            cardSuit = decision[2]
                for card in newFormat:
                    if decision == card:
                        break
                    else:
                        i += 1
                print('You have placed the ' + playerCards[i].num + ' of ' + playerCards[i].suit)
                deck.append(playerCards[i])
                playerCards.pop(i)
                playerTurn = False
                magicianTurn = True
            elif action == '2':
                print('You have drawn the ' + deck[0].num + ' of ' + deck[0].suit + ' from the bottom of the pile')
                playerCards.append(deck[0])
                deck.pop(0)
                if len(deck) != 0:
                    print('The top of the pile is still the ' + deck[len(deck) - 1].num + ' of ' + deck[len(deck) - 1].suit)
                playerTurn = False
                magicianTurn = True

def gameRun():
    
    global playerTurn
    global magicianTurn
    global winner
    global winnerWho
    
    makeDeck()
    shuffleDeck()
    dealCards()
    firstPlayer = chooseFirstPlayer()
    if firstPlayer == 1:
        magicianTurn = True
        magicianPlays()
    elif firstPlayer == 2:
        playerTurn = True
        playerPlays()
    while winner == False:
        checkWinner()
        if playerTurn == True:
            playerPlays()
        elif magicianTurn == True:
            magicianPlays()
    print('The winner is the ' + winnerWho + '!')

gameRun()
