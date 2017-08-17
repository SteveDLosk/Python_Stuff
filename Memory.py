#http://www.codeskulptor.org/#user40_WpdIBDsjZP_12.py
# IIPP2

# implementation of card game - Memory

import simplegui
import random

#Globals
lista = [0, 1, 2, 3, 4, 5, 6, 7]
card_list = lista + lista
exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
state = 0
card_a = 8768768
card_b = 87689	# hold active card values; check them for match
exposed_a = 72136
exposed_b = 23879	#hold active card positions
counter = 0
# helper function to initialize globals
def new_game():
	global state, exposed, counter
	random.shuffle(card_list)
	state = 0
	exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
	counter = 0
# define event handlers
def mouseclick(pos):
	# add game state logic here
	global exposed, state, card_a, card_b, exposed_a, exposed_b, counter
	card_clicked = pos[0] / 50  # floor division; selects card
	if exposed[card_clicked] == False:
    	exposed[card_clicked] = True
    	if state == 0:
        	state = 1
        	card_a = card_list[card_clicked]
        	exposed_a = card_clicked
    	elif state == 1:
        	state = 2
        	card_b = card_list[card_clicked]
        	exposed_b = card_clicked
        	counter += 1
       	 
    	elif state == 2:
        	if card_a == card_b:
            	state = 1
            	card_a = card_list[card_clicked]
            	exposed_a = card_clicked
        	else:
            	exposed[exposed_a] = False
            	exposed[exposed_b] = False
            	state = 1
            	card_a = card_list[card_clicked]
            	exposed_a = card_clicked
# cards are logically 50x100 pixels in size    
def draw(canvas):
	global exposed
	label.set_text("Turns = " + str(counter))
	pos = 0
	for card in exposed:
    	if card == True:
        	canvas.draw_text(str(card_list[pos/50]), ((pos + 6), 80), 80, "Yellow")  # Draws exposed card
    	else:
        	canvas.draw_polygon([(pos, 0), (pos, 100), ((pos + 50), 100),  # Draws card back
                             	(pos + 50, 0)], 1, "white", "green")
    	pos += 50	# Moves to next card physical position       	 

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(counter))
label.set_text("Turns = " + str(counter))
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
