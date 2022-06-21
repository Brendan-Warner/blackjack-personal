# -*- coding: utf-8 -*-


import numpy as np


class player:
  def __init__(self, name, age, bet):
    self.name = name
    self.age = age
    self.bet = bet
    self.winings = 0

  def return_name(self):
    return self.name

  def return_age(self):
    return self.age
  
  def return_bet(self):
    return self.bet

  def set_winnings(self, outcomes):
    for x in range(0,4):
      self.winings += self.bet * outcomes[x]
  def return_winnings(self):
    return self.winings



class game:
  def __init__(self):
    self.deck={1: 'ace of clubs', 2: '2 of clubs', 3: '3 of clubs', 4: '4 of clubs', 5: '5 of clubs', 6: '6 of clubs', 7: '7 of clubs', 8: '8 of clubs', 9: '9 of clubs', 10: '10 of clubs', 11: "jack of clubs", 12: "queen of clubs", 13: "king of clubs", 14: 'ace of diomands', 15: '2 of diomands', 16: '3 of diomands', 17: '4 of diomands', 18: '5 of diomands', 19: '6 of diomands', 20: '7 of diomands', 21: '8 of diomands', 22: '9 of diomands', 23: '10 of diomands', 24: "jack of diomands", 25: "queen of diomands", 26: "king of diomands", 27: 'ace of hearts', 28: '2 of hearts', 29: '3 of hearts', 30: '4 of hearts', 31: '5 of hearts', 32: '6 of hearts', 33: '7 of hearts', 34: '8 of hearts', 35: '9 of hearts', 36: '10 of hearts', 37: "jack of hearts", 38: "queen of hearts", 39: "king of hearts", 40: 'ace of spades', 41: '2 of spades', 42: '3 of spades', 43: '4 of spades', 44: '5 of spades', 45: '6 of spades', 46: '7 of spades', 47: '8 of spades', 48: '9 of spades', 49: '10 of spades', 50: "jack of spades", 51: "queen of spades", 52: "king fo spades"}
    self.all_cards = [] #an array for numbers, each of these represents a card from the deck, and is sued so we can simulate a shuffle
    self.pos = 0 #the current position in the array
    self.hand1 = {} #a dictionary for the first hand of the player, used to hold whatever cards they get in their first hand throughout the game, same for the three next variables but for hands 2, 3, and 4
    self.hand2 = {}
    self.hand3 = {}
    self.hand4 = {}
    self.score1 = 0
    self.score2 = 0
    self.score3 = 0
    self.score4 = 0
    self.dealer_hand = {}#used to the hand of the dealer, the dealer can only have one hand
    self.hands = {1: self.hand1, 2: self.hand2, 3: self.hand3, 4: self.hand4} #used to hold all the hands of the player, this is done to make it easier to acces and minipulated the various hands without needing checks later on, will be explained more then
    self.scores = {1: self.score1, 2: self.score2, 3: self.score3, 4: self.score4}#same idea as the hands
    self.num_hands = 1 #used to denote the total number of hands in play
    self.dealer_score = 0 #used to denote dealer score
    self.hand1 = False #these bools are used to denote which hands are still in play, false means the hand is still in play, true means the hand is not in play, since hands 2,3,and 4 can only come into play through splitting, they are set as not in play at the start
    self.hand2 = True
    self.hand3 = True
    self.hand4 = True
    self.hands_left = {1: self.hand1, 2: self.hand2, 3: self.hand3, 4: self.hand4} #same idea as the to other ditonaries above
    self.double_down1 = False #double down bools are used to determine which hands are currently under the effect of double down, mainly used to auto stand them after they recive their next card
    self.double_down2 = False
    self.double_down3 = False
    self.double_down4 = False
    self.double_downs = {1: self.double_down1, 2: self.double_down2, 3: self.double_down3, 4: self.double_down4}#same idea as the above dictionaries
    self.stand1 = False#used to denote when a player is standing on a hand.
    self.stand2 = False
    self.stand3 = False
    self.stand4 = False
    self.dealer_stand = False#used to denote a dealer standing.
    self.stands = {1: self.stand1, 2: self.stand2, 3: self.stand3, 4: self.stand4}
    self.options = True
    self.check_list = [0,0,0,0]#used for when the program is done to figure out how much a player has won/lost in the game

  def shuffle_deck(self):#sets up the all cards list and shuffles it.
    for x in range(52):
      self.all_cards.append(x + 1)
      np.random.shuffle(self.all_cards)

  # updates both the players hand(s) and the dealers hand. this is done through the dictionary of dictionaries made above. The x value denotes which hand we are on, with the limit being self.num_hands +1 since range is not inclusive.
  #using this, we can access each of the players hand without needing to check how many hands we have or which hand we are one, we simply loop through all possible hands using the self.hands dictionary. we can also use this
  #to accuess the values of each hand and add to them using the self.hands dicitonary.
  def update_hands_scores(self): 
    for x in range(1,self.num_hands +1):#this for loop will loop through all potential hands for the player
      if self.stands[x] == False:#if the player is stanidng on this hand, then dont try to update it
        self.hands[x].update({self.all_cards[self.pos]: self.deck[self.all_cards[self.pos]]}) #we add the number from the all_cards list and the corrisbonding card from the deck to the currently selected hand
      
        if self.all_cards[self.pos] - (self.all_cards[self.pos] // 13) * 13 > 10 or self.all_cards[self.pos] - (self.all_cards[self.pos] // 13) * 13 ==0:#checks to see if we have a jack, queen, or king, if so, make their value 10
          self.scores[x] += 10

        else:
          self.scores[x] += self.all_cards[self.pos] - (self.all_cards[self.pos] // 13) * 13

        if self.double_downs[x] == True:#set the hand stand state to true if the hand was double downed on
          self.stands[x] = True
        
        self.pos += 1


    if self.dealer_stand == False:
      self.dealer_hand.update({self.all_cards[self.pos]: self.deck[self.all_cards[self.pos]]})
      if self.all_cards[self.pos] - (self.all_cards[self.pos] // 13) * 13 > 10 or self.all_cards[self.pos] - (self.all_cards[self.pos] // 13) * 13 ==0:
          self.dealer_score += 10
      else:
        self.dealer_score += self.all_cards[self.pos] - (self.all_cards[self.pos] // 13) * 13

      if self.dealer_score >= 17 and len(self.dealer_hand) != 2:#if the dealer is on 17 or above, they must stand, unless the 17 they have is a soft 17, in which case they must hit, this is denoted by checking if their hand size is 2
        self.dealer_stand = True
      
      self.pos += 1



  def return_hands(self):
    for x in range(1, self.num_hands +1):
      print("Hand ", x, "value is ", self.scores[x], "Your hand is ", list(self.hands[x].values()))

      while self.options == True and self.stands[x] == False:#this option affects the currently selected hands stand and dobuel down state
        userin = input("Would you like to hit, stand, or dobule down? enter yes or y, no or n, double or d for the options")
        if userin == "no" or userin == 'n':
          self.stands[x] = True
          self.options = False
        elif userin == 'double' or userin == 'd':
          self.double_downs[x] = True
          self.options = False
        elif userin == 'yes' or userin == 'y':
          self.options = False

      self.options = True


    print("The dealers score is ", self.dealer_score, " Their hand is ", list(self.dealer_hand.values()))


  def splits(self):
    for x in range(1, self.num_hands+1):#loop through all avalible hands
      if len(self.hands[x]) == 2:#if the hand is not size 2, then its not possible to split
          
        hold = list(self.hands[x].keys())#get the keys of the current hand to figure out of the two values are equal to each other
        y = hold[0] - (hold[0] //13)  * 13
        z = hold[1] - (hold[1] //13)  * 13
          

        if y == z:#if the two cards are of equal value, then ask the user if they want to split the hand
          userin = input("Would you like to split your hand enter y/yes for yes or enter n/no for no")
          if userin == 'yes' or userin == 'y':
            self.num_hands += 1#increase the number of hands
            key = list(self.hands[x].keys())
            self.hands[self.num_hands].update({key[1]: self.hands[x][key[1]]})#add the second card 
            self.hands[x].popitem()
            self.scores[self.num_hands] = z
            self.scores[x] = z
            self.hands_left[self.num_hands] = False


  def win_loss(self):
    for x in range(1, self.num_hands+1):
      if  self.hands_left[x] == False:
        if self.scores[x] == 21:
          print("Hand ", x, " won by blackjack!")
          self.check_list[x-1] = 2.5
          self.stands[x] = True
          self.hands_left[x] = True
        elif self.scores[x] < 21 and self.scores[x] < self.dealer_score and self.stands[x] == True and self.dealer_stand == True:
          if self.dealer_score == 21:
            print("Hand ", x, " lost, the dealer got blackjack")
            self.check_list[x-1] = 1
            self.hands_left[x] = True
          elif self.dealer_score < 21:
            print("Hand ", x," lost")
            self.check_list[x-1] = 0
            self.hands_left[x] = True
          elif self.dealer_score > 21:
            print("Hand ", x," won, the dealer went but")
            self.check_list[x-1] = 2
            self.hands_left[x] = True


        elif self.scores[x] < 21 and self.scores[x] > self.dealer_score and self.stands[x] == True and self.dealer_stand == True:
          print("Hand ", x, " Won!")
          self.check_list[x-1] = 2
          self.hands_left[x] = True

        elif self.scores[x] > 21:
          print("Hand ", x, " Went bust")
          self.check_list[x-1] = 0
          self.stands[x] = True
          self.hands_left[x] = True

        

        else:
          self.check_list[x-1] = 6

        if self.check_list[x-1] == 2 and self.double_downs[x] == True:
          self.check_list[x-1] = 4
        elif self.check_list[x-1] == 2.5 and self.double_downs[x] == True:
          self.check_list[x-1] = 4.5



    return self.check_list

name = input("Please enter your name ")
age = int(input("Please enter you age "))
bet = int(input("Please enter your bet in dollers "))


player1 = player(name, age, bet)
game1 = game()
done = False
game1.shuffle_deck()
while done == False:
  game1.update_hands_scores()
  game1.return_hands()
  game1.splits()
  check = game1.win_loss()

  if check[0] < 6 and check[1] < 6 and check[2] < 6 and check[3] < 6:
    done = True
  
player1.set_winnings(check)


print(player1.return_name(), " your winnings are ", player1.return_winnings())