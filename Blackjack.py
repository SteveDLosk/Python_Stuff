#http://www.codeskulptor.org/#user40_GKhLSR6rUG_13.py
# Another project from Introduction to Interactive Programming in Python part 2 (IIPP2)

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
	def __init__(self, suit, rank, face_up):
    	if (suit in SUITS) and (rank in RANKS):
        	self.suit = suit
        	self.rank = rank
        	self.face_up = face_up
       	 
    	else:
        	self.suit = None
        	self.rank = None
        	print "Invalid card: ", suit, rank

	def __str__(self):
    	return self.suit + self.rank

	def get_suit(self):
    	return self.suit

	def get_rank(self):
    	return self.rank

	def draw(self, canvas, pos, face_up):
    	card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                	CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
    	if face_up == True:
        	canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    	else:
        	canvas.draw_image(card_back, (36,48), CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
       	 
# define hand class
class Hand:
	def __init__(self):
    	self.cards = []

	def __str__(self):
    	output = []
    	for Card in self.cards:
        	output.append(Card.suit + Card.rank)
    	return "hand contains " + str(output)
   	 
	def add_card(self, card):
    	self.cards.append(card)

	def get_value(self):
    	net_value = 0  #sum of cards
    	card_value = 0  #currently iterated card
    	has_ace = False
    	for Card in self.cards:
        	card_value = VALUES[Card.rank]
        	net_value += VALUES[Card.rank]
        	if card_value == 1:
            	has_ace = True
       	 
    	if has_ace == True:
        	if (net_value + 10) < 22:
            	return net_value + 10
        	else:
            	return net_value	 
    	else:
        	return net_value
   	 
	def is_busted(self):
    	i = False
    	val = self.get_value()
    	if val > 21:
        	return True
    	else:
        	return False
    
	def draw(self, canvas, pos, i):
    	# i is number of face-down cards
    	for card in self.cards:
        	if i > 0:   
            	card.draw(canvas, [pos[0] + (CARD_SIZE[0] + 12) * i, pos[1]], True)
            	i += 1    # draw a hand on the canvas, use the draw method for cards
        	else:
            	card.draw(canvas, [pos[0] + (CARD_SIZE[0] + 12) * i, pos[1]], False)
            	i += 1
# define deck class
class Deck:
	def __init__(self):
    	self.contents = []
    	for suit in SUITS:
        	for rank in RANKS:
            	self.contents.append(Card(str(suit), str(rank), False))
           	 
            	#print Card.get_suit(self) + Card.get_rank(self)
	def shuffle(self):
    	i = 0
    	while i < 11:	#Shuffles the deck thoroughly
        	random.shuffle(self.contents)
        	i += 1
	def deal_card(self):
    	return self.contents.pop()
	def deal_from_bottom(self):
    	return self.contents.pop(-1)
	def pick_a_card(self, suit, rank):
    	#Supposedly picks a card from the deck by suit and rank
    	## not yet tested
    	return self.contents.remove(str(suit)+str(rank))
    
	def __str__(self):
    	s = []
    	for Card in self.contents:
        	s.append (Card.get_suit() + Card.get_rank ())
    	return str(s)    

the_deck = Deck()
player_hand = Hand()
dealer_hand = Hand()
#define event handlers for buttons
def deal():
	global outcome, score, in_play, the_deck, player_hand, dealer_hand, prompt
	outcome = ""
    
	the_deck = Deck()  #re-instates a full 52 card deck
	the_deck.shuffle()
	dealer_hand = Hand()
	player_hand = Hand()
	dealer_hand.add_card(the_deck.deal_card())  #deals one card
	dealer_hand.add_card(the_deck.deal_card())  #deals one card
    
	player_hand.add_card(the_deck.deal_card())  #deals one card
	player_hand.add_card(the_deck.deal_card())  #deals one card
    
	prompt = "Hit or stand?"
	if in_play == True:
    	score -= 1
    
	else:
    	in_play = True
    
def hit():
	global in_play, score, outcome, prompt, player_hand, dealer_hand, the_deck# replace with your code below
	if in_play == False:
    	pass
	# if the hand is in play, hit the player
	if in_play == True:
    	if player_hand.is_busted() == False:
        	player_hand.add_card(the_deck.deal_card())
        	###print player_hand.get_value()
        	prompt = "Hit or stand?"
       	 
        	if player_hand.is_busted() == True:   #check to see if just now busted
            	#inputString.splitlines(True)  # --> ['Line 1\n', 'Line 2\n',
            	outcome = "Unfortunately, you have busted."
            	prompt = "New deal?"
            	in_play = False
            	score -= 1
    
	# if busted, assign a message to outcome, update in_play and score
    	else:
        	outcome = "Unfortunately, you have busted."
        	prompt = "New deal?"
        	print player_hand.get_value()
       	 
        	print outcome	#### testing ####
        	in_play = False
        	score -= 1
def stand():
	global in_play, outcome, prompt, player_hand, dealer_hand, score
	if player_hand.is_busted == True:
    	outcome = "You have busted"
    	prompt = "New deal?"
    	print outcome #### testing ####
	# if hand is in play, repeatedly hit dealer until his hand has value 17 or more
	if in_play == True:
    	while dealer_hand.get_value() < 17:
        	dealer_hand.add_card(the_deck.deal_card())
        	##print dealer_hand #### testing ####
    	if dealer_hand.is_busted() == True:
        	outcome = "You Win! Dealer has busted!"
        	prompt = "New deal?"
        	###print outcome #### testing ####
        	in_play = False
        	score += 1
    	elif dealer_hand.get_value() > player_hand.get_value():
        	outcome = "You Lose! Dealer scores higher."
        	prompt = "New deal?"
        	###print outcome #### testing ####
        	in_play = False
        	score -= 1
    	elif dealer_hand.get_value() == player_hand.get_value():
        	outcome = "You Lose! Dealer wins ties."
        	prompt = "New deal?"
        	###print outcome #### testing ####
        	in_play = False
        	score -= 1
    	else:
        	outcome = "You Win!"
        	prompt = "New deal?"
        	###print outcome #### testing ####
        	in_play = False
        	score += 1
	# assign a message to outcome, update in_play and score
   	 
# draw handler    
def draw(canvas):
	canvas.draw_text("Blackjack", (220, 75), 30, "White")  #Title
	canvas.draw_text(str(outcome), (90, 310), 28, "White") #outcome
	canvas.draw_text(str(prompt), (120, 340), 24, "White")  #prompt
	canvas.draw_text(("Score: " + str(score)), (480, 40), 24, "White")  #score
    
	player_hand.draw(canvas, [20, 400], 1 ) #last parameter hides first dealder card
	if in_play == True:
    	dealer_hand.draw(canvas, [20, 110], 0)
	else:
    	dealer_hand.draw(canvas, [20, 110], 1)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
