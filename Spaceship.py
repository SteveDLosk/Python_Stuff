# Spaceship program from Introduction to Interactive Programming in Python, part 2
# About half this is template code from the class, and about half is my code
# You can copy the url below to run the app in a browser

#http://www.codeskulptor.org/#user40_7epauiPSob_1.py
#http://www.codeskulptor.org/#user40_uuggZG7LLZ_10.py

# program template for Spaceship
import simplegui
import math
import random

# globals for user interfacegod
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
started = False
#rock_group = set([])
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def set_center(self, posx, posy):
        self.center = [posx, posy]
    
        
    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
asteroid_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_brown.png")
asteroid_image3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

def group_collide(group, other_object):
    ''' Checks for a collision between a single object and a group'''
    remove = set([])
    for item in set(group):
        if item.collide(other_object):
            remove.add(item)
    for item in remove:
        group.remove(item)
        
    if len (remove) > 0:
        return True
    else:
        return False

def group_group_collide(group1, group2):
    collided = set([])
    for item in set(group1):
        if group_collide(group2, item):
            collided.add(item)
    for item in collided:
        group1.discard(item) 
    return collided    

def restart():
    global lives, score, rock_group
    lives = 3
    score = 0
    
#    #clear rocks
#    remove = set(rock_group)
#    for rock in remove:
#        rock_group.remove(rock)
        
# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.set_center = info.set_center(135, 45)
    def draw(self,canvas):
        if self.thrust:
            
            self.set_center
            canvas.draw_image(self.image, (self.image_center[0] + self.image_size[0], self.image_center[1]),
                              self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, 
                          self.pos, self.image_size, self.angle)
        
    def update(self):
        
        FRICTION = .014
        
        self.pos[0] += self.vel[0] 
        self.pos[1] += self.vel[1] 
        self.angle += self.angle_vel

        forward = angle_to_vector(self.angle)
        
        self.vel[0] *= (1.0 - FRICTION)  # slow ship down
        self.vel[1] *= (1.0 - FRICTION)
        
        #Accelerate while thrusting
        if self.thrust:
            ACCEL_CONSTANT = .21
            self.vel[0] += forward[0] * ACCEL_CONSTANT
            self.vel[1] += forward[1] * ACCEL_CONSTANT
        
        #Screen edge wrap around
        if self.pos[0] < 0:
            self.pos[0] += WIDTH
        if self.pos[0] > WIDTH:
            self.pos[0] -= WIDTH
        if self.pos[1] < 0:
            self.pos[1] += HEIGHT
        if self.pos[1] > HEIGHT:
            self.pos[1] -= HEIGHT
            
    def shoot(self):
        
        
        MISSILE_SPEED = 7
        pos = [self.pos[0] + angle_to_vector(self.angle)[0] * self.radius, 
               self.pos[1] + angle_to_vector(self.angle)[1] * self.radius]
        vel = [self.vel[0] + angle_to_vector(self.angle)[0] * MISSILE_SPEED, 
               self.vel[1] + angle_to_vector(self.angle)[1] * MISSILE_SPEED]
        missile = Sprite(pos, vel, 0, 0, missile_image, missile_info, missile_sound)
        missile_group.add(missile)
    def get_position(self):
        return self.pos
    def get_radius(self):
        return self.radius    
            
    def turn_left(self):
        angle_constant = .11
        self.angle_vel = -1 * angle_constant
    def turn_right(self):
        angle_constant = .11
        self.angle_vel = angle_constant

    def zoom(self):
        self.thrust = True
        ship_thrust_sound.play()
    def coast(self):
        self.thrust = False
        ship_thrust_sound.rewind()
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos,
                         self.image_size, self.angle)
    def get_position(self):
        return self.pos
    def get_radius(self):
        return self.radius
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.angle += self.angle_vel

        #Screen edge wrap around
        if self.pos[0] < 0:
            self.pos[0] += WIDTH
        if self.pos[0] > WIDTH:
            self.pos[0] -= WIDTH
        if self.pos[1] < 0:
            self.pos[1] += HEIGHT
        if self.pos[1] > HEIGHT:
            self.pos[1] -= HEIGHT
            
        #update lifespan
        self.age += 1
        if self.age >= self.lifespan:
            return True
        else:
            return False
    def collide(self, other_object):
        distance = dist(self.get_position(), other_object.get_position())
        if distance < self.get_radius() + other_object.get_radius():
            return True
        else:
            return False
        
def draw(canvas):
    global time, lives, score
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    
    # draw lives and score counters 
    
    canvas.draw_text(("Lives: " + str(lives)), [WIDTH / 15, HEIGHT / 10], 24, "white")
    canvas.draw_text("Score: " + str(score), [WIDTH * .83, HEIGHT / 10], 24, "white")
    
    # draw ship and sprites
    my_ship.draw(canvas)
    
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    #a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    #rock_group.update()
    #a_missile.update()
    
    #Check for collision with ship
    if group_collide(rock_group, my_ship):
        lives -= 1
    #Check for collision of missile with rock
    if group_group_collide(rock_group, missile_group):
        score += 1
        
    #check for game over
    if lives <= 0:
        global started
        started = False
   #clear rocks
        remove = set(rock_group)
        for rock in remove:
            rock_group.remove(rock)
   # Draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
        
        
    
            
#handler for keyboard user controls:
def keydown(key):
    
    inputs = {37: my_ship.turn_left, 39: my_ship.turn_right, 
              38: my_ship.zoom, 32: my_ship.shoot}
    if key in inputs.keys():
        inputs[key]()
def keyup(key):
    if key == 37 or key == 39:
        my_ship.angle_vel = 0
    if key == 38:
        my_ship.coast()
def click(pos):
    global started
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        soundtrack.rewind()
        soundtrack.play()
        
        restart()

        
        
 # timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    if started:
        if len(rock_group) <= 11: #generates random rock data:
        
            pos = [random.random() * WIDTH, random.random() * HEIGHT]
            vel = [(random.random() -.5) * 3, (random.random() - .5) * 3]
            ang = random.randrange(0, 7)
            rot = random.choice([-.12, -.105, .09, -.07, .07, .09, .105, .12])
            image = random.choice([asteroid_image1, asteroid_image2, asteroid_image3])
        
            #Check for safe spawn distance, cancel spawn otherwise
            if dist(pos, my_ship.get_position()) > 200:  
                rock_group.add (Sprite(pos, vel, ang, rot, image, asteroid_info))
    
# handler for drawing sprite groups
def process_sprite_group(group, canvas):
    remove = set([])
    for sprite in group:
        sprite.update()
        sprite.draw(canvas)
        if sprite.update():  #check to see if sprite past lifespan
            remove.add(sprite)
    for sprite in remove:
        group.remove(sprite)
    
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set([])
missile_group = set([])
#Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
#a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)
timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()





