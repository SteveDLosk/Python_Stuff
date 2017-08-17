#http://www.codeskulptor.org/#user40_7s0FisNdxj_3.py
# This one is all me 

# simple times sevens quiz ##

import simplegui
import random

numlist = list(range(0,12))
num = random.choice(numlist)
message = 0
score = 0

def new_problem():
    ''' Makes a new *7 problem '''

    # either 7 * something, OR something * 7
    a = random.choice([False, True])
    global message, product
    num = random.choice(numlist)
    
    if a: 
        message = "7 X " + str(num) + " = "
    else:
        message = str(num) + " X 7 = "
    product = num * 7

new_problem()
# Handler for mouse click
def click():
    global message
    new_problem()
def input_handler(text_input):
    ''' takes user input, checks if correct '''
    global product, message, score
    a = int(text_input)
    if a == product:
        message = "Correct!"
        score += 1
        label.set_text("Score = " + str(score))
    else:
        message = "Sorry, it was " + str(product) + "."
        score -= 1
        label.set_text("Score = " + str(score))
# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Cyan")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 600, 200)
frame.add_button("New Problem", click)
frame.set_draw_handler(draw)
#frame.add_input("Number of sides:", num_diagonals, 100)
frame.add_input('Answer', input_handler, 50)
label = frame.add_label("Score " + str(score))

label.set_text("Score = " + str(score))

# Start the frame animation
frame.start()




