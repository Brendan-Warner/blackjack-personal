# -*- coding: utf-8 -*-


import numpy as np

class player:
  def __init__(self, name, age, bet):
    self.name = name
    self.age = age
    self.bet = bet
    self.winings = 0
    self.hand1 = {}
    self.hand2 = {}
    self.hand3 = {}
    self.hand4 = {}
    self.hands = {1: hand1, 2: hand2, 3: hand3, 4: hand4}
    self.scores=[0,0,0,0]
    self.winnings = [0,0,0,0]


    self.hand_play = [1,0,0,0]

    self.double_down = false
    
    self.stand[0,0,0,0]

  def return_name(self):
    return self.name

  def return_age(self):
    return self.age
  
  def return_bet(self):
    return self.bet

  def return_hand(self):
    hand = ""
    num = 1
    for x in self.hands:#this loops through the hands dictionary and every individual value of the dictionarys in hands. 
      for y in self.hands[x]:
        hand = hand + " " y
      print("Your hand " + num + " is " hand + " the value of this hand is " + return_score(num))
      num++

  def return_score(self, num):
    return self.scores[num]

  def return_playable_hand(self, num):
    return self.hand_play[num]
  
  def update_score(self, num):
    sum = 0
    for y in self.hands[num]:
      sum += self.hands[num][y]
    self.scores[num] = sum

  def update_hand(self, card_type, card_num, num):
    self.hands[num].update({card_type, card_num})
    update_score(num)

  def set_winnings(self, outcomes):
    for x in range(0,4):
      self.winings += self.bet * outcomes[x]
  def return_winnings(self):
    return self.winings

  def update_playable_hands(self, num, change_to):
    self.hand_play[num] = change_to

  def update_stands(self, num):
    self.stand[num] = 1
  
  def update_double_down(self, num):
    self.double_down = true

  def can_split(self, num):
    if(len(self.hands[num]) != 2 && self.double_double_down == false):
      return false
    num1 = []
    for x in self.hands[num]:
      num1.append(self.hands[num][x])

    if(num1[0] == num1[1]):
      return true

    return false

  def can_double_down(self, current):
    if(current != 1):
      return false
    return true

  def hand_bust(self, num):
    if(scores[num] > 21):
      self.hand_play[num] = -1
  

class dealer:
  def __init__(self):
    self.dealer_hand = {}
    self.dealer_score = 0
    self.dealer_stand = false
    self.dealer_bust = false

  def return_dealer_hand(self):
    hand = ""
    for x in dealer_hand:
      hand = hand + " " + x
    print("The dealers hand is " + hand + " their score is " + self.dealer_score)

  def return_dealer_score(self):
    return self.dealer_score

  def return_dealer_stand(self):
    return self.dealer_stand

  def return_dealer_bust(self):
    return self.dealer_bust

  def set_dealer_stand(self):
    self.dealer_stand = true

  def set_dealer_bust(self):
    self.dealer_bust = true

  def update_dealer_stand(self):
    if(dealer_score == 17):
      for x in dealer_hand:
        if(dealer_hand[x] == 1 || dealer_hand[x] == 11):
          self.dealer_stand = 1
          return

  def update_dealer_hand(self, card_type, card_number):
    if(dealer_stand!= 1):
      self.dealer_hand.update(card_type: card_number)
      update_dealer_hand()
  def update_dealer_score(self):
    sum = 0
    for x in dealer_hand:
      sum += dealer_hand
    self.dealer_score = sum

class deck:
  def __init__(self):
    self.deck={'ace of clubs': 1, '2 of clubs' : 2,  '3 of clubs': 3,  '4 of clubs' : 4,  '5 of clubs': 5,  '6 of clubs' : 6,  '7 of clubs' : 7,  '8 of clubs' : 8,  '9 of clubs' : 9,  '10 of clubs' : 10,  "jack of clubs" : 10,  "queen of clubs" : 10, "king of clubs" : 10, 'ace of diomands' : 1, '2 of diomands' : 2, '3 of diomands' : 3,  '4 of diomands' : 4, '5 of diomands': 5, '6 of diomands': 6, '7 of diomands': 7, '8 of diomands' : 8, '9 of diomands': 9, '10 of diomands': 10, "jack of diomands" : 10,  "queen of diomands": 10, "king of diomands" : 10, 'ace of hearts': 1, '2 of hearts': 2, '3 of hearts': 3, '4 of hearts': 4, '5 of hearts': 5, '6 of hearts': 6,'7 of hearts': 7,'8 of hearts': 8,'9 of hearts': 9,'10 of hearts': 10, "jack of hearts": 10, "queen of hearts" : 10,"king of hearts": 10, 'ace of spades':1, '2 of spades': 2, '3 of spades': 3, '4 of spades': 4, '5 of spades': 5, '6 of spades': 6, '7 of spades': 7, '8 of spades': 8,  '9 of spades': 9, '10 of spades':10,"jack of spades":10, "queen of spades": 10, "king fo spades": 10}
    self.all_cards = []
    self.current = 0
    

  def return_current(self):
      return this.current

  def shuffle_deck(self):
    
    for x in deck:
      self.all_cards.append(x)
      
    np.random.shuffle(self.all_cards)

  
  
  def return_card(self):
    card = {self.all_cards[current]: self.deck[self.all_cards[current]}
    current++
    return card


name = input("Please enter your name")
age = int(input("Please enter your age"))
bet = int(input("Please enter your bet in dollers"))

deck1 = deck()
player1 = player(name, age, bet)
dealer1 = dealer()

card = deck1.return_card()

for x in card:
  player1.update_hand(x, card[x], 0)
  break

card = return_card()

for x in card:
  dealer1.update_hand(x, card[x])
  break

bool game = true

while game:
  dealer1.return_dealer_hand()
  player1.return_hand()

  for x in range(0, 5):
    if(player1.return_playable_hand(x) != 1):
      continue

    stand = input("Would you like to stand on hand " + x "? enter y to stand or anything else to hit.")
    if(stand == "y"):
      continue
    if(player1.can_double_down(deck1.return_current())):
      dd = input("you can double down, would you like to? enter y for yes and anything else for no.")
      if(dd == "y"):
        player1.update_double_down()

    
    
    card = deck1.return_card()

    

    for y in card:

      if(card[y] == 1):
        ace = int(input("You got an ace, would you like it to be valued at 1 or 11? enter the number you would prefer"))
        card[y] = ace #this may not work due to scoping rules, we shall soon see.
      player1.update_hand(y, card[y], x)

    if(player1.return_score(x) >21):
      player1.hand_bust(x)
      continue

    if(player1.can_split(x) != true || x == 4):
      continue
    
    split = input("You can split this hand into a new one, would you like to?")

    if(split == "y"):
      player1.split_hand(num)

  if(dealer1.return_dealer_stand() != true && dealer1.return_dealer_bust):

    card = deck1.return_card()
    for y in card:
      if(card[y] == 1 && dealer1.return_score() + 11 > 21):
        dealer1.set_soft()
        card[y] = 11
      dealer1.update_hand(y, card[y])
    if((dealer1.return_score() == 17 && dealer1.return_soft() != true) || (dealer1.return_score() >=18 && dealer1.return_score() <=21):
      dealer1.set_dealer_stand()
    elif(dealer1.return_score() > 21):
      dealer1.set_dealer_bust()

  player_can_play = false
  for x in rang(0,5):
    if(player1.return_playable_hand(x) == 1):
      player_can_play = true
       break
  if(player_can_play == true && (dealer1.return_bust == true ||dealer1.return_stand == true):
    game = false
sum = 0     
for x in rand(0,5):
  if(player1.return_playable_hand(num) ==0):
    break
  if((player1.return_score(num) > dealer1.return_score && player1.return_playable_hand(num) != -1) || (player1.return_playable_hand(num) ==2 && dealer1.return_bust == true)):
    sum += (player1.return_bet() *2)
  else:
    sum -= player1.return_bet();
    
print("Here is what you one/Lost in this game" + sum)