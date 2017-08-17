#http://www.codeskulptor.org/#user40_88G3kdIGtb_22.py

# Implementation of classic arcade game Pong
# From IIPP1

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400  	 
BALL_RADIUS = 17
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = 160
paddle2_pos = 160
paddle1_vel = 0
paddle2_vel = 0
ball_pos = [300, 200]
ball_vel = [3, 3]
score1 = 0
score2 = 0
rebounds = 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
	global ball_pos, ball_vel # these are vectors stored as lists
	ball_pos = [WIDTH/2, HEIGHT/2]
	ball_vel[1] = - random.randrange(10,30) / 10
	if LEFT == True:
    	ball_vel[0] = random.randrange(20,40) / 10
    	ball_vel[0] = ball_vel[0] * -1
	elif LEFT == False:
    	ball_vel[0] = random.randrange(2,4)
# define event handlers
def new_game():
	global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
	global score1, score2  # these are ints
	spawn_ball(1)
def draw(canvas):
	global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, LEFT, paddle1_vel, paddle2_vel, rebounds
    
   	 
	# draw mid line and gutters
	canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
	canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
	canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
   	 
	# update ball
	ball_pos[0] = ball_pos[0] + ball_vel[0]
	ball_pos[1] = ball_pos[1] + ball_vel[1]
	## ceiling/floor rebound
	if ball_pos[1] < BALL_RADIUS:
    	ball_vel [1] = - ball_vel [1]
	if ball_pos[1] > (HEIGHT - BALL_RADIUS):
    	ball_vel [1] = - ball_vel [1]
	## check for hitting gutters
	if ball_pos[0] <= (PAD_WIDTH):
    	LEFT = False
    	spawn_ball(RIGHT)
    	score2 += 1
	if ball_pos[0] >= (WIDTH - PAD_WIDTH):
    	LEFT = True
    	spawn_ball (LEFT)
    	score1 += 1
	# draw ball
	canvas.draw_circle((ball_pos), BALL_RADIUS, 1, "White", "White")
	# update paddle's vertical position, keep paddle on the screen
	global paddle1_vel, paddle2_vel
	paddle1_pos = paddle1_pos - paddle1_vel
	if paddle1_pos <= 0 or paddle1_pos >= (HEIGHT - PAD_HEIGHT):
    	paddle1_vel = 0
    
	paddle2_pos = paddle2_pos - paddle2_vel
	if paddle2_pos <= 0 or paddle2_pos >= (HEIGHT - PAD_HEIGHT):
    	paddle2_vel = 0
   	 
	# draw paddles
	canvas.draw_polygon([[0, paddle1_pos], [PAD_WIDTH, paddle1_pos], [PAD_WIDTH, paddle1_pos + PAD_HEIGHT], [0, paddle1_pos + PAD_HEIGHT]], 1, "white", "white")
	canvas.draw_polygon([[WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT], [WIDTH, paddle2_pos + PAD_HEIGHT]], 1, "white", "white")
	# determine whether paddle and ball collide    
	if ball_pos [1] > paddle1_pos and ball_pos[1] < paddle1_pos + PAD_HEIGHT:
    	if ball_pos [0] <= PAD_WIDTH + BALL_RADIUS:
    	#if ball_pos[1] < paddle1_pos + PAD_HEIGHT:
        	ball_vel[0] = - ball_vel [0]
       	 
        	paddle_strike_speedup()
	if ball_pos [1] > paddle2_pos and ball_pos[1] < paddle2_pos + PAD_HEIGHT:
    	if ball_pos [0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
    	#if ball_pos[1] < paddle1_pos + PAD_HEIGHT:
        	ball_vel[0] = - ball_vel [0]
       	 
        	paddle_strike_speedup()
	# draw scores
	canvas.draw_text (str(score1), [240, 100], 30, "Cyan")
	canvas.draw_text (str(score2), [340, 100], 30, "Cyan")             	 
def keydown(key):
	global paddle1_vel, paddle2_vel
	if key == simplegui.KEY_MAP["w"]:
    	paddle1_vel = 4
	if key == simplegui.KEY_MAP["s"]:
    	paddle1_vel = -4
	if key == simplegui.KEY_MAP["up"]:
    	paddle2_vel = 4
	if key == simplegui.KEY_MAP["down"]:
    	paddle2_vel = -4
def keyup(key):
	global paddle1_vel, paddle2_vel
	if key == simplegui.KEY_MAP["w"]:
    	paddle1_vel = 0
	if key == simplegui.KEY_MAP["s"]:
    	paddle1_vel = 0
	if key == simplegui.KEY_MAP["up"]:
    	paddle2_vel = 0
	if key == simplegui.KEY_MAP["down"]:
    	paddle2_vel = 0
def reset_button():
	global score1, score2
	score1 = 0
	score2 = 0
	new_game()
def paddle_strike_speedup():
	global ball_vel
	ball_vel[0] = ball_vel[0] * 1.1
	ball_vel[1] = ball_vel[1] * 1.1
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
reset_button = frame.add_button("Reset", reset_button, 150)

# start frame
new_game()
frame.start()


