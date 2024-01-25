"""
Constants for Planetoids

This module global constants for the game Planetoids. These constants need to be used
in the model, the view, and the controller. As these are spread across multiple modules,
we separate the constants into their own module. This allows all modules to access them.

# YOUR NAME- SHRAVAN RAM
# DATE- 09-05-2023
"""
import introcs
import sys

### WINDOW CONSTANTS (all coordinates are in pixels) ###

#: the width of the game display
GAME_WIDTH  = 800
#: the height of the game display
GAME_HEIGHT = 700
# The offscreen dead zone for "wrapping"
DEAD_ZONE = 48

### SHIP CONSTANTS ###

# The image file to use for the ship
SHIP_IMAGE     = 'ship.png'
# The radius of the ship (width/2 and height/2)
SHIP_RADIUS    = 24
# The number of lives a ship has
SHIP_LIVES     = 3
# The maximum ship speed
SHIP_MAX_SPEED = 3.0
# The amount of thrust to apply each frame
SHIP_IMPULSE   = 0.1
# The number of degrees to turn the ship
SHIP_TURN_RATE = 2

# The image file to use for the shield
SHIELD_IMAGE    = 'shield.png'
# The size of the shield in proportion to the ship
SHIELD_SCALE = 78/58
# The number of seconds to deploy the shield
SHIELD_TIME  = 300

### PLANETOID CONSTANTS ###

# The size name of a large planetoid
LARGE_ASTEROID = 'large'
# The size name of a medium planetoid
MEDIUM_ASTEROID = 'medium'
# The size name of a small planetoid
SMALL_ASTEROID = 'small'

# The image file to use for a large planetoid
LARGE_IMAGE  = 'asteroid1.png'
# The radius of a large planetoid (width/2 and height/2)
LARGE_RADIUS = 64
# The speed of a large planetoid
LARGE_SPEED  = 1

# The image file to use for a medium planetoid
MEDIUM_IMAGE  = 'asteroid2.png'
# The radius of a medium planetoid (width/2 and height/2)
MEDIUM_RADIUS = 32
# The speed of a medium planetoid
MEDIUM_SPEED  = 2.0 # DECREASED BY 0.5

# The image file to use for a small planetoid
SMALL_IMAGE  = 'asteroid3.png'
# The radius of a small planetoid (width/2 and height/2)
SMALL_RADIUS = 16
# The speed of a small planetoid
SMALL_SPEED  = 3

### BULLET CONSTANTS ###

# The radius of a bullet (width/2 and height/2)
BULLET_RADIUS = 10
# The speed of a bolt
BULLET_SPEED  = 10
# The number frames that must pass until the player can fire again
BULLET_RATE   = 10
# The color of a bullet
BULLET_COLOR   = 'red'

### GAME CONSTANTS ###

# state before the game has started
STATE_INACTIVE = 0
# state when we are initializing a new wave
STATE_LOADING  = 1
# state when the level is activated and in play
STATE_ACTIVE   = 2
# state when we are are paused between lives
STATE_PAUSED   = 3
# state when we restoring a destroyed ship
STATE_CONTINUE = 4
#: state when the game is complete (won or lost)
STATE_COMPLETE = 5

### FONT CONSTANTS ###

# The font choice for the title
TITLE_FONT = 'Redline-Outline.ttf'
# The font size for the title
TITLE_SIZE = 140
# The y-offset for the title (the value to add to the center y value)
TITLE_OFFSET = 70

# The font choice for messages
MESSAGE_FONT = 'Redline.ttf'
# The font size for messages
MESSAGE_SIZE = 60
# The y-offset for the message (the value to add to the center y value)
MESSAGE_OFFSET = -70


### JSON FILES ###

# The default wave
DEFAULT_WAVE  = 'wave1.json'

### USE COMMAND LINE ARGUMENTS TO CHANGE DEFAULT LEVEL FILE
"""
sys.argv is a list of the command line arguments when you run python. These arguments are
everything after the word python. So if you start the game typing

    python planetoids default.json

Python puts ['planetoids', 'default.json'] into sys.argv. Below, we take advantage of 
this fact to change the constant DEFAULT_LEVEL. This is the level file to be used when 
you start the game.  
"""
try:
    file = sys.argv[1]
    if file[-5:].lower() == '.json':
        DEFAULT_WAVE = file
    else:
        DEFAULT_WAVE = file+'.json'
except:
    pass # Use original value

### ADD MORE CONSTANTS (PROPERLY COMMENTED) AS NECESSARY ###
# ADDED BY SHRAVAN
# screen message font choice
CONTINUE_FONT = 'Arcade.ttf'
# continue message font size
CONTINUE_SIZE = 60

EXPLOSION_IMAGE = 'explosion.png'
# background image
BACKGROUND_IMAGE = 'background.png'

# shield radius
SHIELD_RADIUS = 2*SHIP_RADIUS+20

FONT_COLOR = 'white'
# Flame image or thrusters image
FLAME_IMAGE = 'flames.png'