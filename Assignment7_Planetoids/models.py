"""
Models module for Planetoids

This module contains the model classes for the Planetoids game. Anything that you
interact with on the screen is model: the ship, the bullets, and the planetoids.

We need models for these objects because they contain information beyond the simple
shapes like GImage and GEllipse. In particular, ALL of these classes need a velocity
representing their movement direction and speed (and hence they all need an additional
attribute representing this fact). But for the most part, that is all they need. You
will only need more complex models if you are adding advanced features like scoring.

You are free to add even more models to this module. You may wish to do this when you
add new features to your game, such as power-ups. If you are unsure about whether to
make a new class or not, please ask on Ed Discussions.

# YOUR NAME- SHRAVAN RAM
# DATE- 09-05-2023
"""
from consts import *
from game2d import *
from introcs import *
import math

# PRIMARY RULE: Models are not allowed to access anything in any module other than
# consts.py. If you need extra information from Gameplay, then it should be a 
# parameter in your method, and Wave should pass it as a argument when it calls 
# the method.

# START REMOVE
# HELPER FUNCTION FOR MATH CONVERSION
def degToRad(deg):
    """
    Returns the radian value for the given number of degrees
    
    Parameter deg: The degrees to convert
    Precondition: deg is a float
    """
    return math.pi*deg/180
# END REMOVE

class Bullet(GEllipse):
    """
    A class representing a bullet from the ship
    
    Bullets are typically just white circles (ellipses). The size of the bullet is 
    determined by constants in consts.py. However, we MUST subclass GEllipse, because 
    we need to add an extra attribute for the velocity of the bullet.
    
    The class Wave will need to look at this velocity, so you will need getters for
    the velocity components. However, it is possible to write this assignment with no 
    setters for the velocities. That is because the velocity is fixed and cannot change 
    once the bolt is fired.
    
    In addition to the getters, you need to write the __init__ method to set the starting
    velocity. This __init__ method will need to call the __init__ from GEllipse as a
    helper. This init will need a parameter to set the direction of the velocity.
    
    You also want to create a method to update the bolt. You update the bolt by adding
    the velocity to the position. While it is okay to add a method to detect collisions
    in this class, you may find it easier to process collisions in wave.py.
    """
    # LIST ANY ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    # HIDDEN ATTRIBUTES
    # Attribute _velocity: The direction and speed the bullet is travelling
    # Invariant: velocity is a float number

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    @property
    def velocity(self):
        """Returns the velocity attribute"""
        return self._velocity

    # INITIALIZER TO SET THE POSITION AND VELOCITY
    def __init__(self, x, y, facing, width=BULLET_RADIUS,height=BULLET_RADIUS,fillcolor=BULLET_COLOR):
        """
        Initializes a particle at (x,y) with given velocity and color.

        Parameter x: the starting x-coordinate
        Precondition: x is a number (int or float)

        Parameter y: the starting y-coordinate
        Precondition: y is a number (int or float)

        Parameter width: width of the bullet
        Precondition: width is a number (int or float)

        Parameter height: height of the bullet
        Precondition: height is a number (int or float)

        Parameter fillcolor: color of the bullet
        Precondition: fillcolor is a number (int or float)
        """
        super().__init__(x=x+(facing.x*SHIP_RADIUS), y=y+(facing.y*SHIP_RADIUS), 
                        width=BULLET_RADIUS, height=BULLET_RADIUS, fillcolor=BULLET_COLOR)
        self._velocity = Vector2(facing.x*BULLET_SPEED, facing.y*BULLET_SPEED)
        pewsound = Sound('pew1.wav')
        pewsound.play()


class Ship(GImage):
    """
    A class to represent the game ship.
    
    This ship is represented by an image. The size of the ship is determined by constants 
    in consts.py. However, we MUST subclass GEllipse, because we need to add an extra 
    attribute for the velocity of the ship, as well as the facing vecotr (not the same)
    thing.
    
    The class Wave will need to access these two values, so you will need getters for 
    them. But per the instructions,these values are changed indirectly by applying thrust 
    or turning the ship. That means you won't want setters for these attributes, but you 
    will want methods to apply thrust or turn the ship.
    
    This class needs an __init__ method to set the position and initial facing angle.
    This information is provided by the wave JSON file. Ships should start with a shield
    enabled.
    
    Finally, you want a method to update the ship. When you update the ship, you apply
    the velocity to the position. While it is okay to add a method to detect collisions 
    in this class, you may find it easier to process collisions in wave.py.
    """
    # LIST ANY ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    # HIDDEN ATTRIBUTES
    # Attribute _velocity: The direction and speed the ship is travelling
    # Invariant: velocity is a float number

    # Attribute _facing: The direction the ship is facing.
    # Invariant: _facing is a unit vector to represent direction.

    # Attribute _shield: for the shield of the ship 
    # Invariant: _shield is a GEllipse object.
    # 
    # Attribute _fire: for the thrust image
    # Invariant: _fire is a GImage object
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    @property
    def facing(self):
        """Returns the facing vector"""
        return self._facing
    @property
    def velocity(self):
        """Returns the velocity  vector"""
        return self._velocity
    @property
    def shield(self):
        """Returns the shield attribute"""
        return self._shield

    @shield.setter
    def shield(self, value):
        """Sets the ship shield attribute value to value
        para value: new ship shield value to be assigned
        precondition: it must be a None"""
        assert value==None, repr(value)+' is not a None'
        self._shield = value
    
    # INITIALIZER TO CREATE A NEW SHIP
    def __init__(self,x, y, angle, source):
        """
        Initializes a ship object at (x,y).

        Parameter x: the starting x-coordinate
        Precondition: x is a number (int or float)

        Parameter y: the starting y-coordinate
        Precondition: y is a number (int or float)

        Parameter angle: angle at which ship is to be drawn
        Precondition: angle is a int 0<=angle<=360

        Parameter width: width of the ship
        Precondition: width is a number (int or float)

        Parameter height: height of the ship
        Precondition: height is a number (int or float)

        Parameter source: source of the ship image
        Precondition: source is a file name in string.
        """
        super().__init__(x=x, y=y, angle=angle, width=2*SHIP_RADIUS, 
                            height=2*SHIP_RADIUS, source=source)
        self._shield = GImage(x=x, y=y, angle=angle, width=SHIELD_RADIUS, 
                            height=SHIELD_RADIUS, source=SHIELD_IMAGE)
        self._velocity = Vector2(0,0)
        self._facing = Vector2(math.cos(degToRad(angle)), math.sin(degToRad(angle)))
        self._fire = GImage(x=x, y=y, angle=angle, width=SHIELD_RADIUS, 
                            height=SHIELD_RADIUS, source=FLAME_IMAGE)

    # ADDITIONAL METHODS (MOVEMENT, COLLISIONS, ETC)
    def _turn(self, inp):
        """Turns the ship according the input

        Parameter inp: inp is the current input by the user
        Precondition: inp is a Planetoid object containing current input.
        """
        da = 0
        if inp.is_key_down('left'):
            da += SHIP_TURN_RATE
        if inp.is_key_down('right'):
            da -= SHIP_TURN_RATE
        self.angle = self.angle+da
        self._fire.angle = self.angle
        # Change the facing vector
        self._facing = Vector2(math.cos(degToRad(self.angle)), math.sin(degToRad(self.angle)))

    def _move(self, inp, view):
        """Moves the ship by the current velocity

        Parameter inp: inp is the current input by the user
        Precondition: inp is a Planetoid object containing current input.

        Parameter view: view is the current view to be drawn
        Precondition: view is a Planetoid object containing view .
        """
        if inp.is_key_down('up'):
            self._fire.draw(view)
            self._velocity += self._impulse_cal()
            if self._velocity.length() > SHIP_MAX_SPEED:   # forward movement with impulse
                self._velocity = self._velocity.normalize()*SHIP_MAX_SPEED
            
        # normal movement
        self.x += self._velocity.x
        self.y += self._velocity.y
        self._fire.x += self._velocity.x
        self._fire.y += self._velocity.y
        if self.shield!=None:
            self._shield.x += self._velocity.x
            self._shield.y += self._velocity.y
        self._wrap_hori('ship')
        self._wrap_vert('ship')

    def _impulse_cal(self):
        """Returns the impulse"""
        return self._facing*SHIP_IMPULSE

    def _wrap_hori(self, other=None):
        """Wraps the horizontal movement

        parameter other: other is to detect that wrapping is of the ship.
        precondition: other is a string"""
        if other=='ship':
            if self.x < (-DEAD_ZONE):
                self.x = GAME_WIDTH + DEAD_ZONE
                self._fire.x = GAME_WIDTH + DEAD_ZONE
            elif self.x > (GAME_WIDTH + DEAD_ZONE):
                self.x = self.x - (GAME_WIDTH + 2*DEAD_ZONE)
                self._fire.x = self._fire.x - (GAME_WIDTH + 2*DEAD_ZONE)
        else:
            if self.x < (-DEAD_ZONE):
                self.x = GAME_WIDTH + DEAD_ZONE
            elif self.x > (GAME_WIDTH + DEAD_ZONE):
                self.x = self.x - (GAME_WIDTH + 2*DEAD_ZONE)

    def _wrap_vert(self, other=None):
        """Wraps the vertical movement
        
        parameter other: other is to detect that wrapping is of the ship.
        precondition: other is a string"""
        if other=='ship':
            if self.y < (-DEAD_ZONE):
                self.y = GAME_HEIGHT + DEAD_ZONE
                self._fire.y = GAME_HEIGHT + DEAD_ZONE
            elif self.y > (GAME_HEIGHT + DEAD_ZONE):
                self.y = self.y - (GAME_HEIGHT + DEAD_ZONE)
                self._fire.y = self._fire.y - (GAME_HEIGHT + DEAD_ZONE)
        else:
            if self.y < (-DEAD_ZONE):
                self.y = GAME_HEIGHT + DEAD_ZONE
            elif self.y > (GAME_HEIGHT + DEAD_ZONE):
                self.y = self.y - (GAME_HEIGHT + DEAD_ZONE)


class Asteroid(GImage):
    """
    A class to represent a single asteroid.
    
    Asteroids are typically are represented by images. Asteroids come in three 
    different sizes (SMALL_ASTEROID, MEDIUM_ASTEROID, and LARGE_ASTEROID) that 
    determine the choice of image and asteroid radius. We MUST subclass GImage, because 
    we need extra attributes for both the size and the velocity of the asteroid.
    
    The class Wave will need to look at the size and velocity, so you will need getters 
    for them.  However, it is possible to write this assignment with no setters for 
    either of these. That is because they are fixed and cannot change when the planetoid 
    is created. 
    
    In addition to the getters, you need to write the __init__ method to set the size
    and starting velocity. Note that the SPEED of an asteroid is defined in const.py,
    so the only thing that differs is the velocity direction.
    
    You also want to create a method to update the asteroid. You update the asteroid 
    by adding the velocity to the position. While it is okay to add a method to detect 
    collisions in this class, you may find it easier to process collisions in wave.py.
    """
    # LIST ANY ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    # Attribute _velocity: The direction and speed the ship is travelling
    # Invariant: velocity is a float number

    # Attribute _size: The size of the Asteroids
    # Invariant: _size is small/medium/large.

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    @property
    def size(self):
        """Returns the size attribute"""
        return self._size
    @property
    def velocity(self):
        """Returns the velocity vector"""
        return self._velocity
    
    # INITIALIZER TO CREATE A NEW ASTEROID
    def __init__(self, x, y, direction, width, height, size, speed, source):
        """
        Initializes a Asteroid object at (x,y).

        Parameter x: the starting x-coordinate
        Precondition: x is a number (int or float)

        Parameter y: the starting y-coordinate
        Precondition: y is a number (int or float)

        Parameter direction: direction of the asteroid
        Precondition: direction is a list containing x and y direc.

        Parameter width: width of the asteroid
        Precondition: width is a number (int or float)

        Parameter height: height of the asteroid
        Precondition: height is a number (int or float)

        Parameter size: size of the asteroid
        Precondition: size is a string.

        Parameter source: source of the asteroid image
        Precondition: source is a file name in string.
        """
        super().__init__(x=x,y=y, width=2*width, height=2*height, size=size, source=source)
        self._size = size
        direction = Vector2(direction[0], direction[1])
        self._velocity = direction.normalize()*speed

    def update(self):
        """Update method for asteroid class
        updates the frame"""
        self.x += self._velocity.x
        self.y += self._velocity.y
        Ship._wrap_hori(self)
        Ship._wrap_vert(self)
