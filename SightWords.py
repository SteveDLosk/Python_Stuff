#Sight words testing program 
# http://www.codeskulptor.org/#user40_zieZB3w45c_3.py

# This one is all me, though it does use the codeskulptor platform / api

import simplegui
import random

FRAME_WIDTH = 400
FRAME_HEIGHT = 200

current_word = ""
current_list = 1
vocab_dict = {1: ["see", "my", "said", "is", "do", "in", "me", "the", "can", "for"],
              2: ["to", "here", "look", "up", "we", "and", "it", "play", "so", "she"],
              3: ["am", "at", "he", "an", "go", "are", "like", "have", "has", "no"]
             }

# Handler for mouse click
def click():
    global current_word
    current_word = random.choice(vocab_dict[current_list])
def change_list(num):
    global current_list
    if num in vocab_dict.keys():
        current_list = num
# Handler to draw on canvas
def draw(canvas):
    
    canvas.draw_text(current_word, [FRAME_WIDTH / 2 - 20, FRAME_HEIGHT / 2], 48, "Yellow")
    list_label.set_text ("List " + str(current_list))
# Handlers to change word list
def key_handler(key):
    pass
def next_list():
    global current_list
    change_list(current_list + 1)
    
def last_list():
    global current_list
    change_list(current_list - 1)
    
    
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", FRAME_WIDTH, FRAME_HEIGHT)
frame.add_button("New Word", click)
frame.add_button("Next List", next_list)
frame.add_button("Previous List", last_list)
frame.add_label ("")
list_label = frame.add_label ("List " + str(current_list))
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_handler)

# Start the frame animation
frame.start()


