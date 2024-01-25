"""
A module to draw cool shapes with the introcs Turtle.

You call all of these functions in the interactive shell, but you will have 
to create a Window first.  Alternatively, you can use the a4test.py test script
to try out the functions.

Name - SHRAVAN RAM
DATE - 18-03-2023
"""
from introcs.turtle import Window, Turtle, Pen
import introcs  # For the RGB and HSV objects
import math     # For the math computations


################# Helpers for Precondition Verification #################

def is_number(x):
    """
    Returns: True if value x is a number; False otherwise.
    
    Parameter x: the value to check
    Precondition: NONE (x can be any value)
    """
    return type(x) in [float, int]


def is_window(w):
    """
    Returns: True if w is a introcs Window; False otherwise.
    
    Parameter w: the value to check
    Precondition: NONE (w can be any value)
    """
    return type(w) == Window


def is_valid_color(c):
    """
    Returns: True c is a valid turtle color; False otherwise
    
    Parameter c: the value to check
    Precondition: NONE (c can be any value)
    """
    return (type(c) == introcs.RGB or type(c) == introcs.HSV or
            (type(c) == str and (introcs.is_tkcolor(c) or introcs.is_webcolor(c))))


def is_valid_speed(sp):
    """
    Returns: True if sp is an int in range 0..10; False otherwise.
    
    Parameter sp: the value to check
    Precondition: NONE (sp can be any value)
    """
    return (type(sp) == int and 0 <= sp and sp <= 10)


def is_valid_length(side):
    """
    Returns: True if side is a number >= 0; False otherwise.
    
    Parameter side: the value to check
    Precondition: NONE (side can be any value)
    """
    return (is_number(side) and 0 <= side)


def is_valid_iteration(n):
    """
    Returns: True if n is an int >= 1; False otherwise.
    
    Parameter n: the value to check
    Precondition: NONE (n can be any value)
    """
    return (type(n) == int and 1 <= n)


def is_valid_depth(d):
    """
    Returns: True if d is an int >= 0; False otherwise.
    
    Parameter d: the value to check
    Precondition: NONE (d can be any value)
    """
    return (type(d) == int and d >= 0)


def is_valid_turtlemode(t):
    """
    Returns: True t is a Turtle with drawmode True; False otherwise.
    
    Parameter t: the value to check
    Precondition: NONE (t can be any value)
    """
    return (type(t) == Turtle and t.drawmode)


def is_valid_penmode(p):
    """
    Returns: True t is a Pen with solid False; False otherwise.
    
    Parameter p: the value to check
    Precondition: NONE (p can be any value)
    """
    return (type(p) == Pen and not p.solid)


def report_error(message, value):
    """
    Returns: An error message about the given value.
    
    This is a function for constructing error messages to be used in assert 
    statements. We find that students often introduce bugs into their assert 
    statement messages, and do not find them because they are in the habit of 
    not writing tests that violate preconditions.
    
    The purpose of this function is to give you an easy way of making error 
    messages without having to worry about introducing such bugs. Look at 
    the function draw_two_lines for the proper way to use it.
    
    Parameter message: The error message to display
    Precondition: message is a string
    
    Parameter value: The value that caused the error
    Precondition: NONE (value can be anything)
    """
    return message+': '+repr(value)


#################### DEMO: Two lines ####################

def draw_two_lines(w,sp):
    """
    Draws two lines on to window w.
    
    This function clears w of any previous drawings. Then, in the middle of 
    the window w, this function draws a green line 100 pixels to the east, 
    and then a blue line 200 pixels to the north. It uses a new turtle that 
    moves at speed sp, 0 <= sp <= 10, with 1 being slowest and 10 fastest 
    (and 0 being "instant").
    
    REMEMBER: You need to flush the turtle if the speed is 0.
    
    This procedure asserts all preconditions.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # Assert the preconditions
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    
    # Clear the window first!
    w.clear()
    
    # Create a turtle and draw
    t = Turtle(w)
    t.speed = sp
    t.color = 'green'
    t.forward(100) # draw a line 100 pixels in the current direction
    t.left(90)     # add 90 degrees to the angle
    t.color = 'blue'
    t.forward(200)
    
    # This is necessary if speed is 0!
    t.flush()


#################### TASK 1: Triangle ####################

def draw_triangle(t, s, c):
    """
    Draws an equilateral triangle of side s and color c at current position.
    
    The direction of the triangle depends on the current facing of the turtle.
    If the turtle is facing west, the triangle points up and the turtle starts
    and ends at the east end of the base line.
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    position (x and y, within round-off errors), heading, color, and drawmode.
    If you changed any of these in the function, you must change them back.
    
    REMEMBER: You need to flush the turtle if the speed is 0.
    
    This procedure asserts all preconditions.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter s: The length of each triangle side
    Precondition: s is a valid side length (number >= 0)
    
    Parameter c: The triangle color
    Precondition: c is a valid turtle color (see the helper function above)
    """
    # Assert the preconditions
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(s), report_error('Invalid side length', s)
    assert is_valid_color(c), report_error('Invalid color', c)
    
    # Hint: each angle in an equilateral triangle is 60 degrees.
    # Note: In this function, DO NOT save the turtle position and heading
    # in the beginning and then restore them at the end. The turtle moves
    # should be such that the turtle ends up where it started and facing
    # in the same direction, automatically.
    
    # Also, 3 lines have to be drawn. Does this suggest a for loop that
    # processes the range 0..2?
    old_color = t.color # original color
    t.color = c
    for i in range(3):
        t.forward(s) # draw line of length s
        t.right(120)  # turns turtle 120 degrees
    t.color = old_color
    t.flush()


#################### TASK 2: Hexagon ####################

def draw_hex(t, s):
    """
    Draws six triangles using the color 'orange' to make a hexagon.
    
    The triangles are equilateral triangles, using draw_triangle as a helper.
    The drawing starts at the turtle's current position and heading. The
    middle of the hexagon is the turtle's starting position.
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    position (x and y, within round-off errors), heading, color, and drawmode.
    If you changed any of these in the function, you must change them back.
    
    REMEMBER: You need to flush the turtle if the speed is 0.
    
    This procedure asserts all preconditions.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter s: The length of each triangle side
    Precondition: s is a valid side length (number >= 0)
    """
    # Assert the preconditions
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(s), report_error('Invalid side length', s)

    # Note: Do not save any of the turtle's properties and then restore them
    # at the end. Just use 6 calls on procedures drawTriangle and t.left. Test
    # the procedure to make sure that t's final location and heading are the
    # same as t's initial location and heading (except for roundoff error).
    for i in range(6):
        draw_triangle(t, s, "orange")
        t.left(60)
    t.flush()


#################### Task 3A: Spirals ####################

def draw_spiral(w, side, ang, n, sp):
    """
    Draws a spiral using draw_spiral_helper(t, side, ang, n, sp)
    
    This function clears the window and makes a new turtle t.  This turtle
    starts in the middle of the canvas facing north (NOT the default east).
    It then calls draw_spiral_helper(t, side, ang, n, sp). When it is done,
    the turtle is left hidden (visible is False).
    
    REMEMBER: You need to flush the turtle if the speed is 0.
    
    This procedure asserts all preconditions.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter side: The length of each spiral side
    Precondition: side is a valid side length (number >= 0)
    
    Parameter ang: The angle of each corner of the spiral
    Precondition: ang is a number
    
    Parameter n: The number of edges of the spiral
    Precondition: n is a valid number of iterations (int >= 1)
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert -360<=ang<=360, report_error('ang is not a valid angle',ang)
    assert is_valid_iteration(n), report_error('n is not a valid number of iterations',n)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    
    # HINT: w.clear() clears window.
    # HINT: Set the visible attribute to False at the end, and remember to flush
    # Clear the window first!
    w.clear()
    t = Turtle(w)
    t.heading = 90
    draw_spiral_helper(t, side, ang, n, sp)
    t.visible = False
    t.flush()


def draw_spiral_helper(t, side, ang, n, sp):
    """
    Draws a spiral of n lines at the current position and heading.
    
    The spiral begins at the current turtle position and heading, turning ang
    degrees to the left after each line. Line 0 is side pixels long. Line 1
    is 2*side pixels long, and so on.  Hence each Line i is (i+1)*side pixels
    long. The lines alternate between blue, red, and orange, in that order, 
    with the first one blue.
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    color, speed, visible, and drawmode. However, the final position and
    heading may be different. If you changed any of these four in the 
    function, you must change them back.
    
    This procedure asserts all preconditions.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter side: The length of each spiral side
    Precondition: side is a valid side length (number >= 0)
    
    Parameter ang: The angle of each corner of the spiral
    Precondition: ang is a number
    
    Parameter n: The number of edges of the spiral
    Precondition: n is a valid number of iterations (int >= 1)
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert -360<=ang<=360, report_error('ang is not a valid angle',ang)
    assert is_valid_iteration(n), report_error('n is not a valid number of iterations',n)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)

    # NOTE: Since n lines must be drawn, use a for loop on a range of integers.
    old_color = t.color
    speed = t.speed
    t.speed = sp
    for i in range(0,n,3):
        t.color = 'blue'
        t.forward((i)*side)
        t.left(ang)
        t.color = 'red'
        t.forward((i+1)*side)
        t.left(ang)
        t.color = 'orange'
        t.forward((i+2)*side)
        t.left(ang)
    t.color = old_color
    t.speed = speed
    t.flush()

#################### TASK 3B: Polygons ####################

def multi_polygons(w, side, k, n, sp):
    """
    Draws polygons using multi_polygons_helper(t, side, k, n, sp)
    
    This function clears the window and makes a new turtle t. This turtle 
    starts in the middle of the canvas facing south (NOT the default east). 
    It then calls multi_polygons_helper(t, side, k, n, sp). When it is done, 
    the turtle is left hidden (visible is False).
    
    REMEMBER: You need to flush the turtle if the speed is 0.
    
    This procedure asserts all preconditions.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter side: The length of each polygon side
    Precondition: side is a valid side length (number >= 0)
    
    Parameter k: The number of polygons to draw
    Precondition: k is an int >= 1
    
    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 3
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert k>=1, report_error('k is not a valid number >=1', k)
    assert n>=3, report_error('n is not a valid number >=3', n)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    
    # HINT: w.clear() clears window.
    # HINT: Set the visible attribute to False at the end, and remember to flush
    # Clear the window first!
    w.clear()
    t = Turtle(w)
    t.heading = -90
    multi_polygons_helper(t, side, k, n, sp)
    t.visible = False
    t.flush()


def multi_polygons_helper(t, side, k, n, sp):
    """
    Draws k n-sided polygons of side length s.
    
    The polygons are drawn by turtle t, starting at the current position. The
    turtles alternate colors between green and blue (starting with green). 
    Each polygon is drawn starting at the same place (within roundoff errors),
    but t turns left 360.0/k degrees after each polygon.
    
    At the end, ALL ATTRIBUTES of the turtle are the same as they were in the 
    beginning (within roundoff errors). If you change any attributes of the 
    turtle. then you must restore them. Look at the helper draw_polygon for 
    more information.
    
    This procedure asserts all preconditions.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter side: The length of each polygon side
    Precondition: side is a valid side length (number >= 0)
    
    Parameter k: The number of polygons to draw
    Precondition: k is an int >= 1
    
    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 3
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert k>=1, report_error('k is not a valid number >=1', k)
    assert n>=3, report_error('n is not a valid number >=3', n)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    
    # HINT: Make sure you restore t's color and speed when done
    # HINT: Since k polygons should be drawn, use a for-loop on a range of numbers.
    old_color = t.color
    speed = t.speed
    t.speed = sp
    for i in range(k):
        if i%2==0:
            t.color = 'green'      
        else:
            t.color = 'blue'
        for j in range(n):
            t.forward(side)
            t.left(360.0/n)    
        t.left(360.0/k)
    t.heading = 0
    t.color = old_color
    t.speed = speed
    t.move(0,0)

# DO NOT MODIFY
def draw_polygon(t, side, n):
    """
    Draws an n-sided polygon using of side length side.
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    position (x and y, within round-off errors), heading, color, speed, 
    visible, and drawmode. There is no need to restore these.
    
    This procedure asserts all preconditions.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter side: The length of each polygon side
    Precondition: side is a valid side length (number >= 0)
    
    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 1
    """
    # Assert the preconditions
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert type(n) == int and n >= 1, report_error('n is an invalid # of poly sides',n)
    
    # Remember old speed
    ang = 360.0/n # exterior angle between adjacent sides
    
    # t is in position and facing the direction to draw the next line.
    for _ in range(n):
        t.forward(side)
        t.left(ang)


#################### TASK 3C: Radiating Petals ####################

def radiate_petals(w, radius, width, n, sp):
    """
    Draws a color flower with n petals using radiate_petals_helper(t, side, n, sp)
    
    This function clears the window and makes a new turtle t.  This turtle
    starts in the middle of the canvas facing west (NOT the default east).
    It then calls radiate_petals_helper(t, side, n, sp). When it is done, the
    turtle is left hidden (visible is False).
    
    REMEMBER: You need to flush the turtle if the speed is 0.
    
    This procedure asserts all preconditions.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter radius: The radius of the produced "flower"
    Precondition: radius is a valid side length (number >= 0)
    
    Parameter width: The width of an open petal
    Precondition: width is a valid side length (number >= 0)
    
    Parameter n: The number of lines to draw
    Precondition: n is an int >= 2
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_length(radius), report_error('radius is not a valid length',radius)
    assert is_valid_length(width),  report_error('width is not a valid length',width)
    assert n>=2, report_error('n is not a valid number greater than or equal to 2', n)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    
    # HINT: w.clear() clears window.
    # HINT: Set the visible attribute to False at the end, and remember to flush
    w.clear()
    t = Turtle(w)
    t.heading = 180
    radiate_petals_helper(t, radius, width, n, sp)
    t.visible = False
    t.flush()


def radiate_petals_helper(t, radius, width, n, sp):
    """
    Draws a color flower with n petals of length radius at equal angles.
    
    The petals alternate between open (a diamond of the given width) and
    closed (a straight line), starting with an open petal.. Open petals are 
    drawn with function draw_diamond, while closed petals are drawn by 
    moving the turtle in a straight line. After drawing each petal, the 
    turtle should return to its original position.
    
    The petals are drawn at equal angles starting from the initial turtle
    heading. A petal drawn at angle ang, 0 <= ang < 360 has the HSV color 
    (ang % 360.0, 1, 1).
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    color, speed, visible, and drawmode. However, the final position and
    heading may be different. If you changed any of these four in the 
    function, you must change them back.
    
    This procedure asserts all preconditions.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter radius: The radius of the produced "flower"
    Precondition: radius is a valid side length (number >= 0)
    
    Parameter width: The width of an open petal
    Precondition: width is a valid side length (number >= 0)
    
    Parameter n: The number of lines to draw
    Precondition: n is an int >= 2
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # Assert the preconditions
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(radius), report_error('radius is not a valid length',radius)
    assert is_valid_length(width),  report_error('width is not a valid length',width)
    assert (type(n) == int and n >= 2), report_error('n is an invalid # of petals',n)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    
    # Hints:
    # 1. Drawing the petals should be drawn with a range loop.
    # 2. The first petal should be open, alternating with closed petals afterwards
    # 3. Open petals should be drawn with the function draw_diamond
    # 4. The heading of the turtle should stay in the range 0 <= heading < 360.
    # 5. (t.heading % 360.0, 1, 1) is the HSV color of the turtle for each petal
    # 6. You can use an HSV object for the turtle's color attribute,
    #    even though all the examples use strings with color names
    old_color = t.color
    for i in range(n):
        t.color = introcs.HSV(t.heading%360.0, 1, 1)
        draw_diamond(t, radius, 0)
        t.heading += 360/n
        draw_diamond(t, radius, width)
    t.color = old_color


# DO NOT MODIFY
def draw_diamond(t, length, width):
    """
    Draws an diamond whose major axis (length) is along the current heading.
    
    The width is the size of the minor axis, which is perpendicular to the 
    current turtle heading.
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED: 
    position (x and y, within round-off errors), heading, color, speed, visible, 
    and drawmode. There is no need to restore these.
    
    This procedure asserts all preconditions.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter length: The size of the major axis
    Precondition: length is a valid side length (number >= 0)
    
    Parameter width: The size of the minor (perpendicular) axis
    Precondition: width is a valid side length (number >= 0)
    """
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(length), report_error('length is not a valid length',length)
    assert is_valid_length(width),  report_error('width is not a valid length',width)
    
    # Compute the next position to go to
    angle1 = t.heading*math.pi/180.0
    x2 = t.x+math.cos(angle1)*length/2
    y2 = t.y+math.sin(angle1)*length/2
    x2 -= math.sin(angle1)*width/2
    y2 += math.cos(angle1)*width/2
    
    # Compute the offset heading and edge length
    angle2 = math.atan2(y2-t.y,x2-t.x)*180.0/math.pi
    angle3 = angle2-t.heading
    edgesz = math.sqrt((x2-t.x)*(x2-t.x)+(y2-t.y)*(y2-t.y))
    
    # Draw the diamond, restoring position and heading
    t.right(angle3)
    t.forward(edgesz)
    t.left(2*angle3)
    t.forward(edgesz)
    t.right(2*angle3)
    t.backward(edgesz)
    t.left(2*angle3)
    t.backward(edgesz)
    t.right(angle3)


#################### TASK 4: Fractal Shapes #####################

# DO NOT MODIFY
def fill_rect(p, x, y, side, hght):
    """
    Fills a rectangle of lengths side, hght with center (x, y) using pen p.
    
    This procedure asserts all preconditions.
    
    Parameter p: The graphics pen
    Precondition: p is a Pen with solid attribute False.
    
    Parameter x: The x-coordinate of the rectangle center
    Precondition: x is a number
    
    Parameter y: The y-coordinate of the rectangle center
    Precondition: y is a number
    
    Parameter side: The width of the rectangle
    Precondition: side is a valid side length (number >= 0)
    
    Parameter hght: The height of the rectangle
    Precondition: hght is a valid side length (number >= 0)
    """
    # Precondition assertions omitted
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_number(x), report_error('x is not a valid position',x)
    assert is_number(y), report_error('x is not a valid position',y)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert is_valid_length(hght), report_error('hght is not a valid length',hght)
    
    # Move to the center and draw
    p.move(x - side/2.0, y - hght/2.0)
    p.solid = True
    p.drawLine(    0,  hght)
    p.drawLine( side,     0)
    p.drawLine(    0, -hght)
    p.drawLine(-side,     0)
    p.solid = False
    p.move(x - side/2.0, y - hght/2.0)


#################### TASK 4A: Vicsek Fractal ####################

def vicsek(w, size, d, sp):
    """
    Draws a Vicsek fractal of length size and depth d.
    
    This function clears the window and makes a new graphics pen p. This
    pen starts in the middle of the canvas at (0,0). It draws by calling
    the function vicsek_helper(p, 0, 0, size, d). The pen is visible
    during drawing and should be set to hidden at the end.
    
    The pen should have both a fill color and an edge color of blue.
    
    REMEMBER: You need to flush the pen if the speed is 0.
    
    This procedure asserts all preconditions.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter size: The width and height of the Vicsek fractal
    Precondition: size is a valid length (number >= 0)
    
    Parameter d: The recursive depth of the fractal
    Precondition: n is a valid depth (int >= 0)
    
    Parameter sp: The drawing speed.
    Precondition: sp is a valid turtle/pen speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_length(size), report_error('size is not a valid length', size)
    assert is_valid_depth(d), report_error('d is not a valid depth', d)
    assert is_valid_speed(sp), report_error('sp is not a valid speed', sp)
    
    # HINT: w.clear() clears window.
    # HINT: Keep the pen visible while drawing, and remember to flush
    w.clear()
    p = Pen(w)
    p.visible = True
    vicsek_helper(p, 0, 0, size, d)
    p.flush()


def vicsek_helper(p, x, y, size, d):
    """
    Draws a Vicsek fractal of length size and depth d centered at (x,y)
    
    The fractal is drawn with the current pen color and visibility attribute.
    Follow the instructions on the course website to recursively draw the
    Vicsek fractal.
    
    This procedure asserts all preconditions.
    
    Parameter p: The graphics pen
    Precondition: p is a Pen with solid attribute False.
    
    Parameter x: The x-coordinate of the fractal center
    Precondition: x is a number
    
    Parameter y: The y-coordinate of the fractal center
    Precondition: y is a number
    
    Parameter size: The width and height of the Vicsek fractal
    Precondition: size is a valid length (number >= 0)
    
    Parameter d: The recursive depth of the fractal
    Precondition: n is a valid depth (int >= 0)
    """
    # ARE THESE ALL OF THE PRECONDITIONS? YES
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)

    # Hint: Use fill_rect to draw the base case
    hght = size
    p.fillcolor = 'blue'
    p.edgecolor = 'blue'
    if d==0:
        fill_rect(p, x, y, size, hght)
    
    else:
        vicsek_helper(p,        x,        y, size/3, d-1)
        vicsek_helper(p, x+size/3,        y, size/3, d-1)
        vicsek_helper(p,        x, y+hght/3, size/3, d-1)
        vicsek_helper(p, x-size/3,        y, size/3, d-1)
        vicsek_helper(p,        x, y-hght/3, size/3, d-1)

#################### TASK 4B: Cantor Stool ####################

def cantor(w, side, hght, d, sp):
    """
    Draws a Cantor Stool of dimensions side x hght, and depth d.
    
    This function clears the window and makes a new graphics pen p.  This
    pen starts in the middle of the canvas at (0,0). It draws by calling
    the function cantor_helper(p, 0, 0, side, hght, d). The pen is visible
    during drawing and should be set to hidden at the end.
    
    The pen should have both fill color and edge color 'red'.
    
    REMEMBER: You need to flush the pen if the speed is 0.
    
    This procedure asserts all preconditions.
    
    Parameter w: The window to draw upon.
    Precondition: w is a Window object.
    
    Parameter side: The width of the Cantor stool
    Precondition: side is a valid side length (number >= 0)
    
    Parameter hght: The height of the Cantor stool
    Precondition: hght is a valid side length (number >= 0)
    
    Parameter d: The recursive depth of the stool
    Precondition: d is a valid depth (int >= 0)
    
    Parameter sp: The drawing speed.
    Precondition: sp is a valid turtle/pen speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is not a valid window',w)
    
    # HINT: w.clear() clears window.
    # HINT: Set the visible attribute to False at the end, and remember to flush
    pass


def cantor_helper(p, x, y, side, hght, d):
    """
    Draws a stool of dimensions side x hght, and depth d centered at (x,y)
    
    The stool is draw with the current pen color and visibility attribute.
    Follow the instructions on the course website to recursively draw the
    Cantor stool.
    
    This procedure asserts all preconditions.
    
    Parameter p: The graphics pen
    Precondition: p is a Pen with fill attribute False.
    
    Parameter x: The x-coordinate of the stool center
    Precondition: x is a number
    
    Parameter y: The y-coordinate of the stool center
    Precondition: y is a number
    
    Parameter side: The width of the Cantor stool
    Precondition: side is a valid side length (number >= 0)
    
    Parameter hght: The height of the Cantor stool
    Precondition: hght is a valid side length (number >= 0)
    
    Parameter d: The recursive depth of the stool
    Precondition: d is a valid depth (int >= 0)
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    
    # Hint: Use fill_rect to draw an individual rectangle
    pass


#################### TASK 5: Three-Branches Tree ####################

def branches(w, hght, ang, d, sp):
    """
    Draws a three-branches tree with height hght, angle ang, and depth d.
    
    This function clears the window and makes a new turtle t with color 
    'forest green'. This turtle starts at the bottom of the tree facing north 
    (NOT the default east). Since the tree should be centered at (0,0), this 
    means the turtle is positioned at (0,-hght/2). This function then calls
    branches_helper(t,hght,ang,d), which does all the drawing. When it is 
    done, the turtle is left hidden (visible is False).
    
    REMEMBER: You need to flush the turtle if the speed is 0.
    
    This procedure asserts all preconditions.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter hght: The height of the three-branches tree
    Precondition: hght is a valid side length (number >= 0)
    
    Parameter angle: The branch angles (measured from the central branch)
    Precondition: angle is a number, 0 < angle < 180
    
    Parameter d: The recursive depth of the three-branches tree
    Precondition: n is a valid depth (int >= 0)
    
    Parameter sp: The drawing speed.
    Precondition: sp is a valid turtle/pen speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_length(hght), report_error('hght is not a valid length', hght)
    assert 0<ang<180, report_error('ang is not a valid angle',ang)
    assert type(d)==int, report_error('d is not an integer', d)
    assert d>=0, report_error('d is not a valid number', d)
    assert is_valid_speed(sp), report_error('sp is not a valid speed', sp)
    
    # HINT: w.clear() clears window.
    # HINT: Set the visible attribute to False at the end, and remember to flush
    w.clear()
    t = Turtle(w)
    t.speed = sp
    t.heading = 90
    t.move(0, -hght/2)
    t.color = 'forest green'
    branches_helper(t, hght, ang, d)
    t.visible = False
    t.flush()


def branches_helper(t, hght, ang, d):
    """
    Draws a tree of height hght, angle ang, and depth d at the current position.
    
    The tree is draw with the current turtle color, and and assuming that 
    the current turtle position is the bottom of the tree. The up-direction 
    of the tree is the current direction of the turtle. The two branches of 
    the tree have angle ang measured from the center branch.  So 90 degrees 
    has the two branches parallel, while 60 degrees has all three branches 
    reaching upward.
    
    At the end, ALL ATTRIBUTES of the turtle are the same as they were in the 
    beginning (within roundoff errors). If you change any attributes of the 
    turtle. then you must restore them.
    
    This procedure asserts all preconditions.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter hght: The height of the three-branches tree
    Precondition: hght is a valid side length (number >= 0)
    
    Parameter angle: The branch angles (measured from the central branch)
    Precondition: angle is a number, 0 < angle < 180
    
    Parameter d: The recursive depth of the three-branches tree
    Precondition: n is a valid depth (int >= 0)
    """
    # ARE THESE ALL OF THE PRECONDITIONS? YES
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    
    # Hint: To draw the branches, move the turtle left/right by ang
    
    if d==0:
        t.forward(hght)
        t.backward(hght)
        
    else:
        t.forward(hght/2)
        t.left(ang)
        branches_helper(t, hght/2, ang, d-1)
        t.right(ang)
        branches_helper(t, hght/2, ang, d-1)
        t.right(ang)
        branches_helper(t, hght/2, ang, d-1)
        t.left(ang)
        t.backward(hght/2)