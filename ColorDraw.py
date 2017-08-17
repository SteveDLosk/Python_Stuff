## Simple color dot drawing program
# This one is all me.  My kids call it the drawing circle game

import simplegui

# Globals
active_color = "Red"
active_size = 16
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 450
CANVAS_TITLE = "Circle Drawing"

ball_list = []   #stores a list of balls, including pos, size, color
color_dict = {1: "Red", 2: "Orange", 3: "Yellow", 4: "Green", 5: "Blue", 6: "Purple"}
color_dict2 = {"Red": 1, "Orange": 2, "Yellow": 3, "Green": 4, "Blue": 5, "Purple": 6}
def click(pos):
    ## creates a ball data structure with active color and size at mouse click
    global ball_list
    pos = list(pos)
    ball = [pos[0], pos[1], active_size, active_color, active_color]
    ball_list.append(ball)
def drag(pos):
    ## creates a ball at each position dragged to
    global ball_list
    pos = list(pos)
    ball = [pos[0], pos[1], active_size, active_color]
    ball_list.append(ball)
def draw(canvas):
    ## draws balls from the ball_list on canvas
    for ball in ball_list:
        if ball[2] > 0:
            canvas.draw_circle([ball[0], ball[1]], ball[2], 1, ball[3], ball[3])

def color_change():
    ## picks next color in color list
    global active_color
    current_color = color_dict2.get(active_color) #lookup current color number
    current_color += 1    #increase current color
    if current_color > 6:
        current_color = 1  #roll over to start
    active_color = color_dict.get(current_color)  #reset current color
def input_handler(text_input):
    ### takes string input for new brush size
    global active_size
    text_input = int(text_input)
    active_size = text_input
def keydown(key):
    ### uses up and down to change ball size
    global active_size
    if key == 38:
        active_size += 2
        if active_size > 100:
            active_size = 100
    if key == 40:
        active_size -= 2
        if active_size < 3:
            active_size = 3

def undo():
    if len(ball_list) > 0:
        ball_list.pop()
            
def brown():
    global active_color
    active_color = "Brown"
def red():
    global active_color
    active_color = "Red"
def orange():
    global active_color
    active_color = "Orange"
def yellow():
    global active_color
    active_color = "Yellow"
def green():
    global active_color
    active_color = "Green"
def blue():
    global active_color
    active_color = "Blue"
def purple():
    global active_color
    active_color = "Purple"
def pink():
    global active_color
    active_color = "Pink"
def white():
    global active_color
    active_color = "White"
def grey():
    global active_color
    active_color = "Grey"
def black():
    global active_color
    active_color = "Black"
frame = simplegui.create_frame (CANVAS_TITLE, CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_canvas_background("white")


#color buttons
buttonBrown = frame.add_button("Brown", brown)
buttonRed = frame.add_button("Red", red)
buttonOrange = frame.add_button("Orange", orange)
buttonYellow = frame.add_button("Yellow", yellow)
buttonGreen = frame.add_button("Green", green)
buttonBlue = frame.add_button("Blue", blue)
buttonPurple = frame.add_button("Purple", purple)
buttonPink = frame.add_button("Pink", pink)
buttonWhite = frame.add_button("White", white)
buttonGrey = frame.add_button("Grey", grey)
buttonBlack = frame.add_button("Black", black)

buttonUndo = frame.add_button("Undo", undo)
size_input = frame.add_input('Brush Size', input_handler, 50)

frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(click)
frame.set_mousedrag_handler(drag)
frame.set_draw_handler(draw)
frame.start()



