"""
Primary module for Alien Invaders

This module contains the main controller class for the Planetoids application. There
is no need for any any need for additional classes in this module. If you need more
classes, 99% of the time they belong in either the wave module or the models module. If
you are ensure about where a new class should go, post a question on Ed Discussions.

YOUR NAME- SHRAVAN RAM
DATE- 09-05-2023
"""
from consts import *
from game2d import *
from wave import *
import json

# PRIMARY RULE: Planetoids can only access attributes in wave.py via getters/setters
# Planetoids is NOT allowed to access anything in models.py

class Planetoids(GameApp):
    """
    The primary controller class for the Planetoids application
    
    This class extends GameApp and implements the various methods necessary for processing
    the player inputs and starting/running a game.
        
        Method start begins the application.
        
        Method update either changes the state or updates the Play object
        
        Method draw displays the Play object and any other elements on screen
    
    Because of some of the weird ways that Kivy works, you SHOULD NOT create an
    initializer __init__ for this class. Any initialization should be done in
    the start method instead. This is only for this class. All other classes
    behave normally.
    
    Most of the work handling the game is actually provided in the class Wave.
    Wave should be modeled after subcontrollers.py from lecture, and will have
    its own update and draw method.
    
    The primary purpose of this class is managing the game state: when is the
    game started, paused, completed, etc. It keeps track of that in an attribute
    called _state. For a complete description of how the states work, see the 
    specification for the method update().
    
    As a subclass of GameApp, this class has the following (non-hidden) inherited
    INSTANCE ATTRIBUTES:
    
    Attribute view: the game view, used in drawing (see examples from class)
    Invariant: view is an instance of GView
    
    Attribute input: the user input, used to control the ship and change state
    Invariant: input is an instance of GInput
    
    This attributes are inherited. You do not need to add them. Any other attributes
    that you add should be hidden.
    """
    # LIST ANY ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    # THE ATTRIBUTES LISTED ARE SUGGESTIONS ONLY AND CAN BE CHANGED AS YOU SEE FIT
    # Attribute _state: the current state of the game as a value from consts.py
    # Invariant: _state is one of STATE_INACTIVE, STATE_LOADING, STATE_PAUSED, 
    #            STATE_ACTIVE, STATE_CONTINUE
    #
    # Attribute _wave: the subcontroller for a single wave, which manages the game
    # Invariant: _wave is a Wave object, or None if there is no wave currently active.
    #            _wave is only None if _state is STATE_INACTIVE.
    #
    # Attribute _title: the game title
    # Invariant: _title is a GLabel, or None if there is no title to display. It is None 
    #            whenever the _state is not STATE_INACTIVE.
    #
    # Attribute _message: the currently active message
    # Invariant: _message is a GLabel, or None if there is no message to display. It is 
    #            only None if _state is STATE_ACTIVE.
    # START REMOVE
    # Attribute _sdown: Whether the 'S' was help down last frame
    # Invariant: _sdown is a boolean
    # END REMOVE

    # DO NOT MAKE A NEW INITIALIZER!

    # ADD MORE ATTRIBUTES
    # Attribute _last: The number of keys pressed last frame
    # Invariant: _last is an int >= 0
    # 
    # Attribute _endmessage: the message to be shown at the ending
    # Invariant: _endmessage is a GLabel. It is 
    #            drawn when STATE_COMPLETE.


    # THREE MAIN GAMEAPP METHODS
    def start(self):
        """
        Initializes the application.

        This method is distinct from the built-in initializer __init__ (which you
        should not override or change). This method is called once the game is running.
        You should use it to initialize any game specific attributes.

        This method should make sure that all of the attributes satisfy the given
        invariants. When done, it sets the _state to STATE_INACTIVE and creates both 
        the title (in attribute _title) and a message (in attribute _message) saying 
        that the user should press a key to play a game.
        """
        self._last = 0
        self._state = STATE_INACTIVE
        self._title = GLabel(text="Planetoids",font_size = TITLE_SIZE, 
            font_name=TITLE_FONT, color = FONT_COLOR,x = GAME_WIDTH/2, y = GAME_HEIGHT/2+TITLE_OFFSET)
        self._message = GLabel(text="Press 'S' to start", font_size=MESSAGE_SIZE, 
            font_name=MESSAGE_FONT,color = FONT_COLOR, x=GAME_WIDTH/2, y=GAME_HEIGHT/2 + MESSAGE_OFFSET)
        self._wave = None
        self._endmessage = GLabel(text="Press 'S' to restart", 
                font_size=CONTINUE_SIZE, font_name=CONTINUE_FONT,x=GAME_WIDTH/2, y=GAME_HEIGHT/2+ MESSAGE_OFFSET)
        # for background
        # self._background = GImage(x=GAME_WIDTH/2, y=(GAME_HEIGHT/2)-60, width=GAME_WIDTH, height= GAME_HEIGHT+50,source= 'background3.png')

    def update(self,dt):
        """
        Animates a single frame in the game.
        
        It is the method that does most of the work. It is NOT in charge of playing the
        game. That is the purpose of the class Wave. The primary purpose of this
        game is to determine the current state, and -- if the game is active -- pass
        the input to the Wave object _wave to play the game.
        
        As part of the assignment, you are allowed to add your own states. However, at
        a minimum you must support the following states: STATE_INACTIVE, STATE_LOADING,
        STATE_ACTIVE, STATE_PAUSED, and STATE_CONTINUE. Each one of these does its own
        thing, and might even needs its own helper. We describe these below.
        
        STATE_INACTIVE: This is the state when the application first opens. It is a
        paused state, waiting for the player to start the game. It displays a simple
        message on the screen. The application remains in this state so long as the
        player never presses a key. In addition, the application returns to this state
        when the game is over (all lives are lost or all planetoids are destroyed).
        
        STATE_LOADING: This is the state creates a new wave and shows it on the screen.
        The application switches to this state if the state was STATE_INACTIVE in the
        previous frame, and the player pressed a key. This state only lasts one animation
        frame before switching to STATE_ACTIVE.
        
        STATE_ACTIVE: This is a session of normal gameplay. The player can move the
        ship and fire bullets. All of this should be handled inside of class Wave
        (NOT in this class). Hence the Wave class should have an update() method, just
        like the subcontroller example in lecture.
        
        STATE_PAUSED: Like STATE_INACTIVE, this is a paused state. However, the game is
        still visible on the screen.
        
        STATE_CONTINUE: This state restores the ship after it was destroyed. The
        application switches to this state if the state was STATE_PAUSED in the
        previous frame, and the player pressed a key. This state only lasts one animation
        frame before switching to STATE_ACTIVE.
        
        You are allowed to add more states if you wish. Should you do so, you should
        describe them here.
        
        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """
        self._state_inactive_helper()
        self._state_paused_helper()
        if self._state != STATE_INACTIVE:
            self._title = None
        if self._state == STATE_ACTIVE:
            self._message = None
            self._wave.update(self.input, self.view)
        elif self._state==STATE_PAUSED and self.input.is_key_down('s'):
                self._state = STATE_CONTINUE
                self._message = None
                self._wave.update(self.input, self.view)
                self._state = STATE_ACTIVE
        if self._state==STATE_COMPLETE:
            self._state_complete()
    
    def draw(self):
        """
        Draws the game objects to the view.
        
        Every single thing you want to draw in this game is a GObject. To draw a GObject
        g, simply use the method g.draw(self.view). It is that easy!
        
        Many of the GObjects (such as the ships, planetoids, and bullets) are attributes 
        in Wave. In order to draw them, you either need to add getters for these 
        attributes or you need to add a draw method to class Wave. We suggest the latter. 
        See the example subcontroller.py from class.
        """
        # self._background.draw(self.view)
        if self._state == STATE_INACTIVE:
            self._title.draw(self.view)
            self._message.draw(self.view)
        elif self._state == STATE_ACTIVE:
            self._wave.draw(self.view)
        elif self._state == STATE_PAUSED:
            self._wave.draw(self.view)
            self._message.draw(self.view)
        elif self._state == STATE_COMPLETE:
            self._message.draw(self.view)
            self._endmessage.draw(self.view)

    # HELPER METHODS FOR THE STATES GO HERE
    def _state_inactive_helper(self):
        """
        Updates the state if a key is pressed to start the game to 
        set the state to STATE_ACTIVE
        """
        # Determine the current number of keys pressed
        curr_keys = self.input.key_count
        # Only change if we have just pressed the keys in this frame
        change = curr_keys > 0 and self._last == 0
        if self._state == STATE_INACTIVE and self.input.is_key_down('s') and change:
            self._state = STATE_LOADING
            self._title = None
            self._message = None
            self._wave = Wave(self.load_json(DEFAULT_WAVE))
            self._state = STATE_ACTIVE
        # Update last_keys
        self._last = curr_keys

    def _state_paused_helper(self):
        """
        State helper for changing state to STATE_PAUSED AND STATE_COMPLETE depending on
        the condition.Also this method maintain good connectivity on different states by showing 
        result of the game. and the final score.
        """
        # Determine the current number of keys pressed
        curr_keys = self.input.key_count
        # # Only change if we have just pressed the keys in this frame
        change = curr_keys > 0 and self._last == 0
        if self._wave!= None:
            if self._wave.ship == None and self._wave.lives>0:
                self._state = STATE_PAUSED
                self._message = GLabel(text="Press 'S' to continue", font_size=CONTINUE_SIZE, 
                                font_name = CONTINUE_FONT,x = GAME_WIDTH/2, y=GAME_HEIGHT/2)
            elif len(self._wave.asteroids)==0:
                self._message = GLabel(text="YOU WON "+"Score: "+str(self._wave.score), 
                    font_size=CONTINUE_SIZE, font_name=CONTINUE_FONT,x=GAME_WIDTH/2, y=GAME_HEIGHT/2)
                self._state = STATE_COMPLETE
            elif self._wave.ship==None and self._wave.lives==0:
                self._state = STATE_COMPLETE
                self._message = GLabel(text="GAME OVER "+"Score: "+str(self._wave.score), 
                    font_size=CONTINUE_SIZE, font_name=CONTINUE_FONT,x=GAME_WIDTH/2, y=GAME_HEIGHT/2)
        # Update last_keys
        self._last = curr_keys

    def _state_complete(self):
        """Helper method for Restarting the game"""
        if self.input.is_key_down('s'):
            self._state = STATE_LOADING
            self._title = None
            self._message = None
            self._wave = Wave(self.load_json(DEFAULT_WAVE))
            self._state = STATE_ACTIVE