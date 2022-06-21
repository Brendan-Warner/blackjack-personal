# -*- coding: utf-8 -*-



import numpy as np




deck={1: 'ace of clubs', 2: '2 of clubs', 3: '3 of clubs', 4: '4 of clubs', 5: '5 of clubs', 6: '6 of clubs', 7: '7 of clubs', 8: '8 of clubs', 9: '9 of clubs', 10: '10 of clubs', 11: "jack of clubs", 12: "queen of clubs", 13: "king of clubs", 14: 'ace of diomands', 15: '2 of diomands', 16: '3 of diomands', 17: '4 of diomands', 18: '5 of diomands', 19: '6 of diomands', 20: '7 of diomands', 21: '8 of diomands', 22: '9 of diomands', 23: '10 of diomands', 24: "jack of diomands", 25: "queen of diomands", 26: "king of diomands", 27: 'ace of hearts', 28: '2 of hearts', 29: '3 of hearts', 30: '4 of hearts', 31: '5 of hearts', 32: '6 of hearts', 33: '7 of hearts', 34: '8 of hearts', 35: '9 of hearts', 36: '10 of hearts', 37: "jack of hearts", 38: "queen of hearts", 39: "king of hearts", 40: 'ace of spades', 41: '2 of spades', 42: '3 of spades', 43: '4 of spades', 44: '5 of spades', 45: '6 of spades', 46: '7 of spades', 47: '8 of spades', 48: '9 of spades', 49: '10 of spades', 50: "jack of spades", 51: "queen of spades", 52: "king fo spades"}
  #this is the referance for the entire deck

numbers = [] #this is used for shuffling, each number one threw 52 represents a card in the dictionary above.

#add functionality for keeping track of what cards each player/dealer has, so this way we can add deck splitting and soft 17's

for x in range(52):
  numbers.append(x + 1)


np.random.shuffle(numbers)#shuffels the numbers in the array for adding randomness to the deck.

pos_arr = 0 

#base scores for the player and dealer
num_dealer = 0
num_player = 0

#used later to determine which suit the card comes from
suit_dealer = 0
suit_player = 0

#used to hold the value that comes from the numbers array, both for determined which card just came from the deck, which suit its from, and what number to add to the player/dealer
current_player = 0
current_dealer = 0

#bools for the game, done is for the game being done, player hit and dealer hit are used for the player and ai for standing or hitting. double down is not used currently, but will be in future versions.
done = False
player_hit = True
dealer_hit = True
double_down = False

while done == False:
  

  if player_hit ==True:#if the player is choosing to hit, then give them the next number in the deck
    current_player = numbers[pos_arr]
    pos_arr+= 1

  
    suit_player = current_player/13 #this helps us find which suit the player drew
    if suit_player <= 1:#if the suit value is one or less, then we are in the clubs
      if current_player > 10:#if the player draws a jack, king or queen set the value to 10
        num_player += 10

      elif current_player == 1:#for if the player draws an ace, let them decide if its worth a 1 or 11
        ace = input("would you like your ace to be worth one or 11 points? enter one or eleven")
        if ace == 'one':
          num_player += current_player
        else:
          num_player += 11
      else:#if nether of the above, then the card is simply worth whatever the value says it is.
        num_player += current_player
      print("The players next card is", deck[current_player], " their total is", num_player)

    elif suit_player <= 2:#if suit value is 2 or less, down to one, then we are in diomands, here, we sub 13 from current value to get the actual value of the card
      if current_player - 13 > 10:
        num_player += 10

      elif current_player - 13 == 1:
        ace = input("would you like your ace to be worth one or 11 points? enter one or eleven")
        if ace == 'one':
          num_player += current_player - 13
        else:
          num_player += 11
      else:
        num_player += current_player - 13
      print("The players next card is", deck[current_player], " their total is", num_player)
  
    elif suit_player <=3:#if the suit is 3 or less, down to 2, then we are in hearts, here we sub 26 from current to get the actual value of the cards
      if current_player - 26 > 10:
        num_player += 10

      elif current_player - 26 == 1:
        ace = input("would you like your ace to be worth one or 11 points? enter one or eleven")
        if ace == 'one':
          num_player += current_player - 26
        else:
          num_player += 11
      else:
        num_player += current_player - 26
      print("The players next card is", deck[current_player], " their total is", num_player)

    elif suit_player <=4:#if the suit is less then 4, down to three, then we are in spades, here we sub 39 from the current to get the actual value of the cards.
      if current_player - 39 > 10:
        num_player += 10

      elif current_player - 39 == 1:
        ace = input("would you like your ace to be worth one or 11 points? enter one or eleven")
        if ace == 'one':
          num_player += current_player - 39
        else:
          num_player += 11
      else:
        num_player += current_player - 39
      print("The players next card is", deck[current_player], " their total is", num_player)

  if dealer_hit == True:
    current_dealer = numbers[pos_arr]
    pos_arr+= 1
    suit_dealer = current_dealer/13#this helps us find which suit the dealer drew

    if suit_dealer < 1:
      if current_dealer > 10:
        num_dealer += 10

      elif current_dealer == 1:#the dealer will always choose to hav ethe ace be 1 if they are over 11
        if num_dealer >=11:
          num_dealer += 1
        else:# if they are below 11, then its a 50/50 on if the value will be worth 11 or 1
          r = np.random.randint(2)
          if r == 0:
            num_dealer += 11
          else:
            num_dealer += 1
      else:
        num_dealer += current_dealer
      print("The dealers next card is", deck[current_dealer], " their total is", num_dealer)

    elif suit_dealer <= 2:
      if current_dealer - 13 > 10:
        num_dealer += 10

      elif current_dealer - 13 == 1:
        if num_dealer >=11:
          num_dealer += 1
        else:
          r = np.random.randint(2)
          if r == 0:
            num_dealer += 11
          else:
            num_dealer += 1
      else:
        num_dealer += current_dealer - 13
      print("The dealers next card is", deck[current_dealer], " their total is", num_dealer)
  
    elif suit_dealer <=3:
      if current_dealer - 26 > 10:
        num_dealer += 10

      elif current_dealer - 26 == 1:
        if num_dealer >=11:
          num_dealer += 1
        else:
          r = np.random.randint(2)
          if r == 0:
            num_dealer += 11
          else:
            num_dealer += 1
      else:
        num_dealer += current_dealer - 26
      print("The dealers next card is", deck[current_dealer], " their total is", num_dealer)

    elif suit_dealer <=4:
      if current_dealer - 39 > 10:
        num_dealer += 10

      elif current_dealer - 39 == 1:
        if num_dealer >=11:
          num_dealer += 1
        else:
          r = np.random.randint(2)
          if r == 0:
            num_dealer += 11
          else:
            num_dealer += 1
      else:
        num_dealer += current_dealer - 39
      print("The dealers next card is", deck[current_dealer], " their total is", num_dealer)

  if num_player == 21 and num_dealer == 21: #first check for a draw
    print('draw')
    done = True
  elif num_player >21 and num_dealer > 21:
    print('You lost, both you and the dealer busted')
    done = True

  elif num_player == 21 and dealer_hit == False:#check if the player won
      print("You have won, Blackjack!")
      done = True

  elif num_dealer == 21 and player_hit == False:#check if the dealer won
      print("You have lost, the dealer hit 21")
      done = True

  elif num_player > 21:#check if the player busted
      print("You have lost, you have gone bust")
      done = True

  elif num_dealer > 21:#check if the deasler busted
      print("You have won, the dealer has gone bust")
      done = True

  if player_hit == False and dealer_hit == False and done == False:# if both the player and dealer are standing, then check who has the larger number
    if num_player > num_dealer:
      print("You have won")
      done = True
    else:
      print("You have lost")
      done = True

  option = False
  while option == False and done == False and player_hit == True:#if the player has decided to hit last time, and the game has not ended, then the player can choose to hit or stand
    if double_down == True:
      player_hit = False
    else:
      user_input = input("Would you like to hit? enter y for yes and n for no and d for double down:")
      if user_input == 'y':
      
        option = True
      elif user_input == 'n' or double_down == True:
        player_hit = False
        option = True
      elif user_input == 'd':
      
        option = True
        double_down = True
      else:
        print("That is not a valid option, please try again")

  if dealer_hit == True:
    if num_dealer >= 17:
      dealer_hit = False
    else:
      dealer_hit = True


    
