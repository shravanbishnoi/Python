"""
Subcontroller module for Planetoids

This module contains the subcontroller to manage a single level (or wave) in the 
Planetoids game.  Instances of Wave represent a single level, and should correspond
to a JSON file in the Data directory. Whenever you move to a new level, you are 
expected to make a new instance of the class.

The subcontroller Wave manages the ship, the asteroids, and any bullets on screen. These 
are model objects. Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or models.py.
Whether a helper method belongs in this module or models.py is often a complicated
issue.  If you do not know, ask on Ed Discussions and we will answer.

# YOUR NAME- SHRAVAN RAM
# DATE- 09-05-2023
"""
from game2d import *
from consts import *
from models import *
import random
import datetime
import math as m

# PRIMARY RULE: Wave can only access attributes in models.py via getters/setters
# Level is NOT allowed to access anything in app.py (Subcontrollers are not permitted
# to access anything in their parent. To see why, take CS 3152)

class Wave(object):
    """
    This class controls a single level or wave of Planetoids.
    
    This subcontroller has a reference to the ship, asteroids, and any bullets on screen.
    It animates all of these by adding the velocity to the position at each step. It
    checks for collisions between bullets and asteroids or asteroids and the ship 
    (asteroids can safely pass through each other). A bullet collision either breaks
    up or removes a asteroid. A ship collision kills the player. 
    
    The player wins once all asteroids are destroyed.  The player loses if they run out
    of lives. When the wave is complete, you should create a NEW instance of Wave 
    (in Planetoids) if you want to make a new wave of asteroids.
    
    If you want to pause the game, tell this controller to draw, but do not update.  See
    subcontrollers.py from Lecture 25 for an example.  This class will be similar to
    than one in many ways.
    
    All attributes of this class are to be hidden. No attribute should be accessed 
    without going through a getter/setter first. However, just because you have an
    attribute does not mean that you have to have a getter for it. For example, the
    Planetoids app probably never needs to access the attribute for the bullets, so 
    there is no need for a getter there. But at a minimum, you need getters indicating
    whether you one or lost the game.
    """
    # LIST ANY ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    # THE ATTRIBUTES LISTED ARE SUGGESTIONS ONLY AND CAN BE CHANGED AS YOU SEE FIT
    # Attribute _data: The data from the wave JSON, for reloading 
    # Invariant: _data is a dict loaded from a JSON file
    #
    # Attribute _ship: The player ship to control 
    # Invariant: _ship is a Ship object
    #
    # Attribute _asteroids: the asteroids on screen 
    # Invariant: _asteroids is a list of Asteroid, possibly empty
    #
    # Attribute _bullets: the bullets currently on screen 
    # Invariant: _bullets is a list of Bullet, possibly empty
    #
    # Attribute _lives: the number of lives left 
    # Invariant: _lives is an int >= 0
    #
    # Attribute _firerate: the number of frames until the player can fire again 
    # Invariant: _firerate is an int >= 0
    # 
    # Attribute _score: the score
    # Invariant: _score is a number
    # 
    # Attribute _scorecard: the score text
    # Invariant: _scorecard is a Glabel object to display score
    # 
    # Attribute _shield_time: the number of frames until the shield is active
    # Invariant: _shield_time is an int >= 0
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    @property
    def data(self):
        """Returns the data attribute"""
        return self._data
    @property
    def ship(self):
        """Returns the ship attribute"""
        return self._ship
    @property
    def asteroids(self):
        """Returns the asteroid attribute"""
        return self._asteroids
    @property
    def lives(self):
        """Returns the lives attribute"""
        return self._lives
    @property
    def score(self):
        """Returns the score attribute"""
        return self._score

    # INITIALIZER (standard form) TO CREATE SHIP AND ASTEROIDS
    def __init__(self, data):
        self._data = data
        x,y = self._data["ship"]["position"]
        angle = self._data["ship"]["angle"]
        self._lives = SHIP_LIVES
        self._ship = Ship(x, y, angle, source = SHIP_IMAGE)
        self._asteroids = [Asteroid( x=self._data["asteroids"][0]["position"][0], 
        y=self._data["asteroids"][0]["position"][1],direction=self._data["asteroids"][0]["direction"],
        width=LARGE_RADIUS, height=LARGE_RADIUS, size=LARGE_ASTEROID, speed=LARGE_SPEED, source=LARGE_IMAGE),
                            Asteroid(x=self._data["asteroids"][1]["position"][0],
        y=self._data["asteroids"][1]["position"][1],direction=self._data["asteroids"][1]["direction"], 
        width=LARGE_RADIUS, height=LARGE_RADIUS, size=LARGE_ASTEROID, speed=LARGE_SPEED, source=LARGE_IMAGE),
                            Asteroid(x=self._data["asteroids"][2]["position"][0], 
        y=self._data["asteroids"][2]["position"][1],direction=self._data["asteroids"][2]["direction"],
        width=MEDIUM_RADIUS, height=MEDIUM_RADIUS, size=MEDIUM_ASTEROID, speed=MEDIUM_SPEED,source=MEDIUM_IMAGE),
                            Asteroid(x=self._data["asteroids"][3]["position"][0],
        y=self._data["asteroids"][3]["position"][1],direction=self._data["asteroids"][3]["direction"], 
        width=MEDIUM_RADIUS, height=MEDIUM_RADIUS, size=MEDIUM_ASTEROID, speed=MEDIUM_SPEED, source=MEDIUM_IMAGE),
                            Asteroid(x=self._data["asteroids"][4]["position"][0], 
        y=self._data["asteroids"][4]["position"][1],direction=self._data["asteroids"][4]["direction"],
        width=SMALL_RADIUS, height=SMALL_RADIUS, size=SMALL_ASTEROID, speed=SMALL_SPEED, source=SMALL_IMAGE),
                            Asteroid(x=self._data["asteroids"][5]["position"][0],
        y=self._data["asteroids"][5]["position"][1],direction=self._data["asteroids"][5]["direction"],
        width=SMALL_RADIUS, height=SMALL_RADIUS, size=SMALL_ASTEROID, speed=SMALL_SPEED, source=SMALL_IMAGE)]
        self._bullets = []
        self._firerate = 0
        self._shield_time = 0
        self._score = 0
        self._scorecard = GLabel(text="Lives: "+str(self._lives)+" Score: "+str(self._score), 
            font_size = 30, font_name = CONTINUE_FONT,x = GAME_WIDTH-140, y = GAME_HEIGHT-20)

    # UPDATE METHOD TO MOVE THE SHIP, ASTEROIDS, AND BULLETS
    def update(self, inp, view):
        """Updates the frame according the inp and view

        first of all it updates the scorecard.and then
        If the shield time is over it sets shield to None.

        If the ship is not none it actually updates shield_time and firerate
        updates the turn, position, all the asteroid positions, generates bullet 
        on the basis of the input, movement of bullets, deletes the bullets which
        are in DEAD_ZONE and finally ensures Ship-asteroid, shield-asteroid and 
        bullet-asteroid collision.

        on the other hand, if ship is none and lives are remaining then it 
        regenerates the Ship.

        Parameter inp: inp is the current input by the user
        Precondition: inp is a Planetoid object containing current input.

        Parameter view: view is the current view to be drawn
        Precondition: view is a Planetoid object containing view.
        """
        # updating the scorecard
        self._scorecard.text = "Lives: "+str(self._lives)+" Score: "+str(self._score)
        if self._shield_time>=SHIELD_TIME:  # for shield deactivation
            self._ship.shield = None
        if self._ship != None:
            self._shield_time += 1
            self._firerate += 1
            self._ship._turn(inp)             # method in Ship class for turning the ship
            self._ship._move(inp, view)         # method in Ship class for moving the ship
            for i in range(len(self._asteroids)):
                self._asteroids[i].update()   # for updating asteroids position
            self._bullet_generater(inp)       # create bullet
            self._bullets_move()              # moving the bulllet
            self._check_bullet(self._bullets) # checks bullets in the game zone
            if self._ship.shield==None:
                self._ship_collision()        # for asteroids-ship collision
            else:
                self._shield_collision()      # for asteroids-shield collision
            if self._ship!=None:
                self._bullet_collision()      # for asteroids-bullet collision
        elif self._ship==None and self._lives>0:
            self._shield_time = 0             # reseting the shield time
            x,y = self._data["ship"]["position"]
            angle = self._data["ship"]["angle"]
            self._ship = Ship(x, y, angle, source = SHIP_IMAGE) # regenerating the Ship object

    # DRAW METHOD TO DRAW THE SHIP, ASTEROIDS, AND BULLETS
    def draw(self, view):
        """
        Draws the game objects to the view.
        
        Every single thing you want to draw in this game is a GObject. To draw a GObject
        g, simply use the method g.draw(self.view). It is that easy!

        Parameter view: view is the current view to be drawn
        Precondition: view is a Planetoid object containing view.
        """
        if self._shield_time<SHIELD_TIME and self._ship != None and self._ship.shield!=None:
            self._ship.shield.draw(view)
            self._ship.draw(view)
        elif self._ship != None:
            self._ship.draw(view)
        for i in range(len(self._asteroids)):
            self._asteroids[i].draw(view)
        for i in range(len(self._bullets)):
            self._bullets[i].draw(view)
        self._scorecard.draw(view)
    
    # HELPER METHODS FOR PHYSICS AND COLLISION DETECTION
    def _bullet_generater(self, inp):
        """Initiates a bullet object whenever a spacebar is pressed

        Parameter inp: inp is the current input by the user
        Precondition: inp is a Planetoid object containing current input.
        """
        if inp.is_key_down("spacebar") and self._firerate >= BULLET_RATE:
            bullet_obj = Bullet(x =self._ship.x, y=self._ship.y, facing=self._ship.facing)
            self._bullets.append(bullet_obj)
            self._firerate = 0

    def _bullets_move(self):
        """moving all the bullets and updates their position"""
        for i in range(len(self._bullets)):
            self._bullets[i].x += self._bullets[i].velocity.x
            self._bullets[i].y += self._bullets[i].velocity.y

    def _check_bullet(self, bullets):
        """Deletes all the bullets from _bullet if bullets are in dead zone"""
        i = 0
        while i < len(bullets):
            if bullets[i].x <= (-DEAD_ZONE) or bullets[i].x >= GAME_WIDTH + DEAD_ZONE:
                del bullets[i]
            elif bullets[i].y <= (-DEAD_ZONE) or bullets[i].y >= GAME_HEIGHT + DEAD_ZONE:
                del bullets[i]
            else:
                i += 1

    def _ship_collision(self):
        """Helper method for handling the ship-asteroid collision
        
        if the asteroid and ship are close enough for collision then
        ship sets to none and asteroid gets deleted, also produce a sound when
        collision happens.updates the score attribute  And lives deecreases by one.
        """
        i = 0
        aster_lst = []
        while i<len(self._asteroids):
            dist = self._distance_cal(self._asteroids[i].x, self._asteroids[i].y,
                                            self._ship.x, self._ship.y)
            if self._asteroids[i].width/2 + SHIP_RADIUS >= dist: # checks the collision
                collison_vect = self._ship_vector_1()
                self._break_down(i, collison_vect, aster_lst)
                self._lives -= 1
                self._shield_time = 0
                self._ship = None
                self._bullets = [] # to ensure that no bullet is visible in STATE_PAUSED
                self._play_sound('ship')
                self._score -= 10
                del self._asteroids[i]
                break
            else:
                i += 1
        self._asteroids += aster_lst

    def _bullet_collision(self):
        """Helper method for handling the bullet-asteroid collision
        
        if the asteroid and bullet are close enough for collision then
        both gets deleted, also produce a sound when collision happens.
        updates the score attribute 
        """
        i = 0
        aster_lst = []
        while i <len(self._asteroids):
            j = 0
            while j<len(self._bullets):
                if i<len(self._asteroids):
                    dist = self._distance_cal(self._asteroids[i].x, self._asteroids[i].y, 
                                                self._bullets[j].x, self._bullets[j].y)                   
                    if self._asteroids[i].width/2 + BULLET_RADIUS >= dist: # checks the collision
                        collison_vect = self._bullets[j].velocity.normalize()
                        self._break_down(i, collison_vect, aster_lst)
                        if self._asteroids[i].size==SMALL_ASTEROID:
                            self._score += 8
                            self._play_sound(SMALL_ASTEROID)
                        elif self._asteroids[i].size==MEDIUM_ASTEROID:  
                            self._score += 4
                            self._play_sound(MEDIUM_ASTEROID)
                        elif self._asteroids[i].size==LARGE_ASTEROID:
                            self._score += 2
                            self._play_sound(LARGE_ASTEROID)
                        del self._asteroids[i]
                        del self._bullets[j]
                    else:
                        j += 1
                else:
                    break
            i +=1
        self._asteroids += aster_lst

    def _shield_collision(self):
        """Helper method for handling the shield-asteroid collision
        
        if the asteroid and shield are close enough for collision then
        asteroid gets deleted, also produce a sound.
        """
        i = 0
        aster_lst = []
        while i<len(self._asteroids):
            dist = self._distance_cal(self._asteroids[i].x, self._asteroids[i].y,
                                         self._ship.shield.x, self._ship.shield.y)
            if self._asteroids[i].width/2 + SHIELD_RADIUS/2 >= dist: # checks the collision
                collison_vect = self._ship_vector_1()
                self._break_down(i, collison_vect, aster_lst)
                self._play_sound('shield')
                del self._asteroids[i]
                break
            else:
                i += 1
        self._asteroids += aster_lst

    def _distance_cal(self, x1, y1, x2, y2):
        """Returns the distance between two points

        parameter x1: x1 is x- coordinate of a point
        precondition: x1 is a number

        parameter y1: y1 is y- coordinate of a point
        precondition: y1 is a number

        parameter x2: x2 is x- coordinate of a point
        precondition: x2 is a number

        parameter y2: y2 is x- coordinate of a point
        precondition: y2 is a number"""
        return ((y2 - y1)**2 + (x2 - x1)**2)**(0.5)

    def _ship_vector_1(self):
        """Returns the normalized collision vector for a ship, a Vector2 object"""
        x = self._ship.velocity.x
        y = self._ship.velocity.y
        return self._ship.velocity.normalize() if x!=0 and y!=0 else self._ship.facing

    def _vector_2(self, collison_vect):
        """Returns the second resultant vector

        parameter collision_vect: collision_vect is the collision vector
        precondition: collision_vect is a vector object
        """
        x1 = (collison_vect.x*m.cos((2*m.pi)/3)) - (collison_vect.y*m.sin((2*m.pi)/3))
        y1 = (collison_vect.x*m.sin((2*m.pi)/3)) + (collison_vect.y*m.cos((2*m.pi)/3))
        return Vector2(x1, y1)

    def _vector_3(self, collison_vect):
        """Returns the third resultant vector

        parameter collision_vect: collision_vect is the collision vector
        precondition: collision_vect is a vector object
        """
        x2 = (collison_vect.x*m.cos(-(2*m.pi)/3)) - (collison_vect.y*m.sin(-(2*m.pi)/3))
        y2 = (collison_vect.x*m.sin(-(2*m.pi)/3)) + (collison_vect.y*m.cos(-(2*m.pi)/3))
        return Vector2(x2, y2)

    def _get_asteroid(self, idx, vector, radius):
        """Returns a Asteroid object of the given specification

        parameter idx: idx is the index
        precondition: idx is a int

        parameter vector: vector is the vector
        precondition: vector is a vector object
        
        parameter radius: radius is the radius of the asteroid
        precondition: radius is a string"""
        if radius==SMALL_RADIUS:
            return Asteroid(x=self._asteroids[idx].x+(vector.x*radius), y=self._asteroids[idx].y+(vector.y*radius),
                                direction=[vector.x, vector.y], width=radius,  height=radius,  size=SMALL_ASTEROID, 
                                speed=SMALL_SPEED, source=SMALL_IMAGE)
        elif radius==MEDIUM_RADIUS:
            return Asteroid(x=self._asteroids[idx].x+(vector.x*radius), y=self._asteroids[idx].y+(vector.y*radius),
                                direction=[vector.x, vector.y], width=radius,  height=radius,  size=MEDIUM_ASTEROID, 
                                speed=MEDIUM_SPEED, source=MEDIUM_IMAGE)

    def _play_sound(self, other=None):
        """Plays the specified sound

        parameter other: other is to specify the sound
        precondition: other is a string"""
        if other=='shield':
            ship_explode = Sound('blast1.wav')
            ship_explode.play()
        elif other=='ship':
            ship_explode = Sound('explosion.wav')
            ship_explode.play()
        elif other==SMALL_ASTEROID:
            ship_explode = Sound('blast1.wav')
            ship_explode.play()
        elif other==MEDIUM_ASTEROID:
            ship_explode = Sound('blast3.wav')
            ship_explode.play()
        elif other==LARGE_ASTEROID:
            ship_explode = Sound('blast6.wav')
            ship_explode.play()

    def _break_down(self, i, collison_vect, aster_lst):
        """Helper method for break down of asteroids

        parameter i: i is the index
        precondition: i is a int

        parameter collision_vect: collision_vect is the collision vector
        precondition: collision_vect is a vector object

        parameter aster_lst: to append the new asteroids
        precondition: aster_lst is a list"""
        vect2 = self._vector_2(collison_vect)
        vect3 = self._vector_3(collison_vect)
        if self._asteroids[i].size==MEDIUM_ASTEROID:
            aster1 = self._get_asteroid(i, collison_vect, SMALL_RADIUS)
            aster2 = self._get_asteroid(i, vect2, SMALL_RADIUS)
            aster3 = self._get_asteroid(i, vect3, SMALL_RADIUS)
        elif self._asteroids[i].size==LARGE_ASTEROID:
            aster1 = self._get_asteroid(i, collison_vect, MEDIUM_RADIUS)
            aster2 = self._get_asteroid(i, vect2, MEDIUM_RADIUS)
            aster3 = self._get_asteroid(i, vect3, MEDIUM_RADIUS) 
        try:
            aster_lst.append(aster1)
            aster_lst.append(aster2)
            aster_lst.append(aster3)
        except:
            pass
