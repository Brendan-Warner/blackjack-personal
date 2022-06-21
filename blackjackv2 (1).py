# -*- coding: utf-8 -*-


import numpy as np

#add function functionality for stands, including for split hands

#add functionality for  up to four hands for a person

deck={1: 'ace of clubs', 2: '2 of clubs', 3: '3 of clubs', 4: '4 of clubs', 5: '5 of clubs', 6: '6 of clubs', 7: '7 of clubs', 8: '8 of clubs', 9: '9 of clubs', 10: '10 of clubs', 11: "jack of clubs", 12: "queen of clubs", 13: "king of clubs", 14: 'ace of diomands', 15: '2 of diomands', 16: '3 of diomands', 17: '4 of diomands', 18: '5 of diomands', 19: '6 of diomands', 20: '7 of diomands', 21: '8 of diomands', 22: '9 of diomands', 23: '10 of diomands', 24: "jack of diomands", 25: "queen of diomands", 26: "king of diomands", 27: 'ace of hearts', 28: '2 of hearts', 29: '3 of hearts', 30: '4 of hearts', 31: '5 of hearts', 32: '6 of hearts', 33: '7 of hearts', 34: '8 of hearts', 35: '9 of hearts', 36: '10 of hearts', 37: "jack of hearts", 38: "queen of hearts", 39: "king of hearts", 40: 'ace of spades', 41: '2 of spades', 42: '3 of spades', 43: '4 of spades', 44: '5 of spades', 45: '6 of spades', 46: '7 of spades', 47: '8 of spades', 48: '9 of spades', 49: '10 of spades', 50: "jack of spades", 51: "queen of spades", 52: "king fo spades"}
  
  #this is the referance for the entire deck



class player:
  def __init__(self, name, age, bet):
    self.name = name
    self.cards1 = {}
    self.cards2 = {}
    self.cards3 = {}
    self.cards4 = {}
    self.age = age
    self.bet = bet
    self.bet2 = 0
    self.bet3 = 0
    self.bet4 = 0
    self.score1 = 0
    self.score2 = 0
    self.score3 = 0
    self.score4 = 0
    
    self.hand1 = False
    self.hand2 = True
    self.hand3 = True
    self.hand4 = True
    self.stand1 = False
    self.stand2 = False
    self.stand3 = False
    self.stand4 = False
    self.double_down1 = False
    self.double_down2 = False
    self.double_down3 = False
    self.double_down4 = False
    self.split_flag = False#may be able to take out
  

  def add_deck(self, deck, deck_place, flag):
    if flag == 0:
      self.cards1.update({deck_place: deck[deck_place]})
    elif flag == 1:
      self.cards2.update({deck_place: deck[deck_place]})
    elif flag == 2:
      self.cards3.update({deck_place: deck[deck_place]})
    elif flag == 3:
      self.cards4.update({deck_place: deck[deck_place]})

  def update_score(self, num, flag):#split into two updates
    if flag == 0:
      self.score1 += num
    elif flag == 1:
      self.score2 += num
    elif flag == 2:
      self.score3 += num
    elif flag == 3:
      self.score4 += num

  def checkloss1(self):
    if self.score1 >21:
      return 1
    elif self.score1 == 21:
      return 3
    elif self.score1 < 21 and self.stand1 == True:
      return 2

  def checkloss2(self):
    if self.score2 >21:
      return 1
    elif self.score2 == 21:
      return 3
    elif self.score2 < 21 and self.stand2 == True:
      return 2

  def checkloss3(self):
    if self.score3 >21:
      return 1
    elif self.score3 == 21:
      return 3
    elif self.score3 < 21 and self.stand2 == True:
      return 2

  def checkloss4(self):
    if self.score4 >21:
      return 1
    elif self.score4 == 21:
      return 3
    elif self.score4 < 21 and self.stand2 == True:
      return 2

  def double_down(self,num):
    if num == 0:
      self.double_down1 = True
      self.bet *= 2
    elif num == 1:
      self.double_down2 = True
      self.bet2 *= 2
    elif num == 2:
      self.double_down3 = True
      self.bet3 *= 2
    elif num == 3:
      self.double_down4 = True
      self.bet4 *= 2


  def split(self):
    if len(self.cards1) == 2:
      x = list(self.cards1.keys())
      y = x[0] - (x[0]//13) * 13 #this will give us the exact value of the card, with 13 being represented as a 0, this way, we don't need to do something like divide and check to figure out what suit its in to get the card value.
      z = x[1] - (x[1]//13) * 13 
      if y == z:
        user_in = input("You can split your first hand, would you like to? enter y for yes and n for no")
        if user_in == 'y':

          if len(self.cards2) == 0:
            self.cards2.update({x[1]: self.cards1[x[1]]})
            self.cards1.popitem()
            self.bet2 = self.bet
            self.hand2 = False
            self.score2 = y
            self.score1 = y

          elif len(self.cards3) == 0:
            self.cards3.update({x[1]: self.cards1[x[1]]})
            self.cards1.popitem()
            self.bet3 = self.bet
            self.hand3 = False
            self.score3 = y
            self.score1 = y

          elif len(self.cards4) == 0:
            self.cards4.update({x[1]: self.cards1[x[1]]})
            self.cards1.popitem()
            self.bet4 = self.bet
            self.hand4 = False
            self.score4 = y
            self.score1 = y

    if len(self.cards2) == 2:
      x = list(self.cards2.keys())
      y = x[0] - (x[0]//13) * 13 #this will give us the exact value of the card, with 13 being represented as a 0, this way, we don't need to do something like divide and check to figure out what suit its in to get the card value.
      z = x[1] - (x[1]//13) * 13 
      if y == z:
        user_in = input("You can split your second hand, would you like to? enter y for yes and n for no")
        if user_in == 'y':
          if len(self.cards3) == 0:
            self.cards3.update({x[1]: self.cards2[x[1]]})
            self.cards2.popitem()
            self.bet3 = self.bet2
            self.hand3 = False
            self.score3 = y
            self.score2 = y

          elif len(self.cards4) == 0:
            self.cards4.update({x[1]: self.cards2[x[1]]})
            self.cards2.popitem()
            self.bet4 = self.bet2
            self.hand4 = False
            self.score4 = y
            self.score2 = y

    if len(self.cards3) == 2:
      x = list(self.cards3.keys())
      y = x[0] - (x[0]//13) * 13 #this will give us the exact value of the card, with 13 being represented as a 0, this way, we don't need to do something like divide and check to figure out what suit its in to get the card value.
      z = x[1] - (x[1]//13) * 13 
      if y == z:
        user_in = input("You can split your third hand, would you like to? enter y for yes and n for no")
        if user_in == 'y':
          
          self.cards4.update({x[1]: self.cards1[x[1]]})
          self.cards3.popitem()
          self.bet4 = self.bet3
          self.hand4 = False
          self.score4 = y
          self.score3 = y

    


  def set_hand1(self):
    self.hand1 = True
  def set_hand2(self):
    self.hand2 = True
  def set_hand3(self):
    self.hand3 = True
  def set_hand4(self):
    self.hand4 = True

  def set_stand(self):
    self.stand1 = True
  def set_stand2(self):
    self.stand2 = True
  def set_stand3(self):
    self.stand3 = True
  def set_stand4(self):
    self.stand4 = True

  def return_bet1(self):
    return self.bet

  def return_bet2(self):
    return self.bet2
  def return_bet3(self):
    return self.bet3
  def return_bet4(self):
    return self.bet4

  def return_score1(self):
    return self.score1
  def return_score2(self):
    return self.score2
  def return_score3(self):
    return self.score3
  def return_score4(self):
    return self.score4
  
  def return_split(self):
    return self.split_flag

  def return_stand(self, num):
    if num == 0:
      return self.stand1
    elif num == 1:
      return self.stand2
    elif num == 2:
      return self.stand3
    elif num == 3:
      return self.stand4

  def return_name(self):
    return self.name

  def return_deck(self):
    print(self.name, "your score for your hand is ", self.score1, "your cards are ", list(self.cards1.values()))
    if len(self.cards2) > 0:
      print(self.name, "your score for your second hands score is ", self.score2, "your cards are ", list(self.cards2.values()))
    if len(self.cards3) > 0:
      print(self.name, "your score for your second hands score is ", self.score3, "your cards are ", list(self.cards3.values()))
    if len(self.cards4) > 0:
      print(self.name, "your score for your second hands score is ", self.score4, "your cards are ", list(self.cards4.values()))

  def return_hand1(self):
    return self.hand1
  def return_hand2(self):
    return self.hand2
  def return_hand3(self):
    return self.hand3
  def return_hand4(self):
    return self.hand4

  

  def return_double_down1(self):
    return self.double_down1

  def return_double_down2(self):
    return self.double_down2

  def return_double_down3(self):
    return self.double_down3

  def return_double_down4(self):
    return self.double_down4

  #create an update for functions to update stands to treu when called.

class dealer:
  def __init__(self):
    self.name = 'dealer'
    self.score = 0
    self.cards ={}
    self.lost = False
    self.stand = False


  def add_deck(self, deck, deck_place):
    self.cards.update({deck_place: deck[deck_place]})
      

  def update_score(self, num):
    self.score += num

  def soft_17(self):#checks for if the dealer has a one in their collection of cards, if so, then they must hit on a 17
    x = self.cards.values()
    y = 0
    for items in x:
      if x == 'ace of clubs' or x == 'ace of hearts' or x == 'ace of spades' or x == 'ace of diomands':
        y = 1
        
    return y


  def return_score(self):
    return self.score
  
  def return_stand(self):
    return self.stand

  def set_lost(self):
    self.lost = True

  def set_stand(self):
    self.stand = True

  def return_deck(self):
    print(self.name, "your score for your hand is ", self.score, "your cards are ", list(self.cards.values()))

  def checkloss(self):
    if self.score >21:
      return 1
    elif self.score == 21:
      return 3
    elif self.score < 21 and self.stand == True:
      return 2
  



numbers = [] #this is used for shuffling, each number one threw 52 represents a card in the dictionary above.

#add functionality for keeping track of what cards each player/dealer has, so this way we can add deck splitting and soft 17's

for x in range(52):
  numbers.append(x + 1)


np.random.shuffle(numbers)#shuffels the numbers in the array for adding randomness to the deck.



pos_arr = 0 

name = input("Please enter your name ")






bet = int(input("Please enter your bet "))

age = int(input("Please enter your age "))

player1 = player(name, age, bet)


dealer1 = dealer()





#used to hold the value that comes from the numbers array, both for determined which card just came from the deck, which suit its from, and what number to add to the player/dealer
current_player = 0
current_dealer = 0

#bools for the game, done is for the game being done, player hit and dealer hit are used for the player and ai for standing or hitting. double down is not used currently, but will be in future versions.
done = False


while done == False:
  

  if player1.return_stand(0) == False:#updated  player section
    current_player = numbers[pos_arr]
    pos_arr+= 1
    card = current_player - (current_player//13) * 13

    if card == 0 or card >10:#in the equation for card, if card is 13 or devisable by it, then it will equal zero, so to remedy this, we simply assume that if the value is zero, then it must be 13, and any values above ten in the deck are realted to jacks, queens, and kings, so their value is auto set to 10
      player1.update_score(10,0)#the zero here is to denote the flag, telling the function which hand to add it to if their is split hands involved.
    else:#if the card value is not greater then 10, then we can just add the value to the players score directly.
      player1.update_score(card,0)
    player1.add_deck(deck, current_player, 0)
    

  
  if player1.return_hand2() == True and player1.return_stand(1) == False:
    current_player = numbers[pos_arr]
    pos_arr+= 1
    card = current_player - (current_player//13) * 13
    if card == 0 or card >10:
      player1.update_score(10,1)
    else:
      player1.update_score(card,1)
    player1.add_deck(deck, current_player, 1)

  if player1.return_hand3() == True and player1.return_stand(2) == False:
    current_player = numbers[pos_arr]
    pos_arr+= 1
    card = current_player - (current_player//13) * 13
    if card == 0 or card >10:
      player1.update_score(10,2)
    else:
      player1.update_score(card,2)
    player1.add_deck(deck, current_player, 2)

  if player1.return_hand4() == True and player1.return_stand(3) == False:
    current_player = numbers[pos_arr]
    pos_arr+= 1
    card = current_player - (current_player//13) * 13
    if card == 0 or card >10:
      player1.update_score(10,3)
    else:
      player1.update_score(card,3)
    player1.add_deck(deck, current_player, 3)

  player1.return_deck()
      
  if player1.return_double_down1() == True:
    player1.set_stand()
  if player1.return_double_down2() == True:
    player1.set_stand2()

  if player1.return_double_down3() == True:
    player1.set_stand3()

  if player1.return_double_down4() == True:
    player1.set_stand4()


  if dealer1.return_stand() == False:#updated dealer section, mainly relies on new class functions to do the work for the dealers situation.
    current_dealer = numbers[pos_arr]
    pos_arr+= 1
    card = current_dealer - (current_dealer//13) * 13

    if card == 0 or card >10:
      dealer1.update_score(10)
    else:
      dealer1.update_score(card)
    dealer1.add_deck(deck, current_dealer)
    dealer1.return_deck()


  p=player1.checkloss1()
  
  d=dealer1.checkloss()

  if player1.hand2 == False:
    p2 = player1.checkloss2()
  if player1.hand3 == False:
    p3 = player1.checkloss3()
  if player1.hand4 == False:
    p4 = player1.checkloss4()
  

  #standing and 21:3, standing and not 21: 2, bust: 1
  if player1.return_hand1() == False:
    if p == 3 and d <= 3:
      print(player1.return_name(), "Your hand won via blackjack! Your winings are $", player1.return_bet1() * 2.5)
      player1.set_hand1()
      player1.set_stand()
    elif p == 2 and d == 3:
      print(player1.return_name(), "Your hand lost, dealer got blackjack")
      player1.set_hand1()
      player1.set_stand()
    elif p == 1 and d == 1:
      print(player1.return_name(), "Your hand lost, you and the dealer both went bust")
      player1.set_hand1()
      player1.set_stand()

    elif p == 1 and d > 1:
      print(player1.return_name(), "your hand lost, you went bust")
      player1.set_hand1()
      player1.set_stand()

    elif p ==2 and d == 1:
      print(player1.return_name(), "your hand won!, your winnings are $", player1.return_bet1() * 2)
      player1.set_hand1()
      player1.set_stand()

    elif p == 2 and d == 2:
      if player1.return_score1() >= dealer1.return_score():
        print(player1.return_name(), "your hand won!, your winnings are $", player1.return_bet1() * 2)
        player1.set_hand1()
        player1.set_stand()
      else:
        print(player1.return_name(), "Your hand lost")
        player1.set_hand1()
        player1.set_stand()

  if player1.return_hand2() == False:
    if p2 == 3 and d <= 3:
      print(player1.return_name(), "Your second hand won via blackjack! your winnings are $", player1.return_bet2() * 2.5)
      player1.set_hand2()
      player1.set_stand2()
    elif p2 == 2 and d == 3:
      print(player1.return_name(), "Your second hand lost, dealer got blackjack")
      player1.set_hand2()
      player1.set_stan2()
    elif p2 == 1 and d == 1:
      print(player1.return_name(), "Your second hand lost, you and the dealer both went bust")
      player1.set_hand2()
      player1.set_stand2()

    elif p2 == 1 and d > 1:
      print(player1.return_name(), "your second hand lost, you went bust")
      player1.set_hand2()
      player1.set_stand2()

    elif p2 == 2 and d == 1:
      print(player1.return_name(), "your second hand won! your winnings are $", player1.return_bet2() * 2)
      player1.set_hand2()
      player1.set_stand2()


    elif p2 == 2 and d == 2:
      if player1.return_score2() >= dealer1.return_score():
        print(player1.return_name(), "your second hand won! your winnings are $", player1.return_bet2() * 2)
        player1.set_hand2()
        player1.set_stand2()
      else:
        print(player1.return_name(), "Your second hand lost")
        player1.set_hand2()
        player1.set_stand2()

  if player1.return_hand3() == False:
    if p3 == 3 and d <= 3:
      print(player1.return_name(), "Your third hand won via blackjack! your winnings are $", player1.return_bet3() * 2.5)
      player1.set_hand3()
      player1.set_stand3()
    elif p3 == 2 and d == 3:
      print(player1.return_name(), "Your third hand lost, dealer got blackjack")
      player1.set_hand3()
      player1.set_stan3()
    elif p3 == 1 and d == 1:
      print(player1.return_name(), "Your third hand lost, you and the dealer both went bust")
      player1.set_hand3()
      player1.set_stand3()

    elif p3 == 1 and d > 1:
      print(player1.return_name(), "your third hand lost, you went bust")
      player1.set_hand3()
      player1.set_stand3()

    elif p3 == 2 and d == 1:
      print(player1.return_name(), "your third hand won! your winnings are $", player1.return_bet3() * 2)
      player1.set_hand3()
      player1.set_stand3()


    elif p3 == 2 and d == 2:
      if player1.return_score2() >= dealer1.return_score():
        print(player1.return_name(), "your third hand won! your winnings are $", player1.return_bet3() * 2)
        player1.set_hand3()
        player1.set_stand3()
      else:
        print(player1.return_name(), "Your third hand lost")
        player1.set_hand3()
        player1.set_stand3()

    if player1.return_hand4() == False:
    if p4 == 3 and d <= 3:
      print(player1.return_name(), "Your third hand won via blackjack! your winnings are $", player1.return_bet4() * 2.5)
      player1.set_hand4()
      player1.set_stand4()
    elif p4 == 2 and d == 3:
      print(player1.return_name(), "Your third hand lost, dealer got blackjack")
      player1.set_hand4()
      player1.set_stan4()
    elif p4 == 1 and d == 1:
      print(player1.return_name(), "Your third hand lost, you and the dealer both went bust")
      player1.set_hand4()
      player1.set_stand4()

    elif p4 == 1 and d > 1:
      print(player1.return_name(), "your third hand lost, you went bust")
      player1.set_hand4()
      player1.set_stand4()

    elif p4 == 2 and d == 1:
      print(player1.return_name(), "your third hand won! your winnings are $", player1.return_bet4() * 2)
      player1.set_hand4()
      player1.set_stand4()


    elif p4 == 2 and d == 2:
      if player1.return_score4() >= dealer1.return_score():
        print(player1.return_name(), "your third hand won! your winnings are $", player1.return_bet4() * 2)
        player1.set_hand4()
        player1.set_stand4()
      else:
        print(player1.return_name(), "Your third hand lost")
        player1.set_hand4()
        player1.set_stand4()

  

  if player1.return_hand1() == True and player1.return_hand2() == True and player1.return_hand3() == True and player1.return_hand4() == True:
    done = True 

  option = True
  while option == True and done == False:
    if player1.return_hand1() == False and player1.return_stand(0) == False:
      player1.split()
      userin = input("Would you like to hit or stand on your hand? enter y for yes and n for no and d for double down")
      if userin == 'n':
        option = False
        player1.set_stand()
      elif userin == 'd':
        player1.double_down(0)
        option = False
      elif userin == 'y':
        option = False
    else:
      option = False
    

    if player1.return_hand2() == False and player1.return_stand(1) == False:
      option = True
      userin = input("Would you like to hit or stand on your second hand? enter y for yes and n for no and d for double down")
      if userin == 'n':
        option = False
        player1.set_stand2()
      elif userin == 'y':
        option = False
      elif userin == 'd':
        player1.double_down(1)
        option = False
    else:
      option = False

    if player1.return_hand3() == False and player1.return_stand(2) == False:
      option = True
      userin = input("Would you like to hit or stand on your third hand? enter y for yes and n for no and d for double down")
      if userin == 'n':
        option = False
        player1.set_stand3()
      elif userin == 'y':
        option = False
      elif userin == 'd':
        player1.double_down(2)
        option = False
    else:
      option = False

    if player1.return_hand4() == False and player1.return_stand(3) == False:
      option = True
      userin = input("Would you like to hit or stand on your second hand? enter y for yes and n for no and d for double down")
      if userin == 'n':
        option = False
        player1.set_stand4()
      elif userin == 'y':
        option = False
      elif userin == 'd':
        player1.double_down(3)
        option = False
    else:
      option = False

  if dealer1.return_score() == 17:
    if dealer1.soft_17() == 0:
      dealer1.set_stand()
  elif dealer1.return_score() >= 18:
    dealer1.set_stand()