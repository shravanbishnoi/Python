"""This module contains test functions"""
import inspect
import numpy
import numbers
import math
 
def assert_equals(expected,received):
	"""Quits if expected and receved differ

	Precondition: expected and received should not be floats"""

	if(expected!=received):
		print("Expected "+str(expected)+" but received "+str(received))
		previous_frame = inspect.currentframe().f_back
		(filename, line_number, function_name, lines, index) = inspect.getframeinfo(previous_frame)
		print("Line "+str(line_number)+" of "+str(filename))
		print("Quitting with error")
		exit()


def assert_floats_equal(expected,received):
	"""Quits if expected and receved differ

	Precondition: expected and received should be numbers"""

	if not isinstance(expected,int) and not isinstance(expected,float):
		print("The first argument is not a number.")
		previous_frame = inspect.currentframe().f_back
		(filename, line_number, function_name, lines, index) = inspect.getframeinfo(previous_frame)
		print("Line "+str(line_number)+" of "+str(filename))
		print("Quitting with error")
		exit()

	if not isinstance(received,int) and not isinstance(received,float):
		print("The second argument is not a number.")
		previous_frame = inspect.currentframe().f_back
		(filename, line_number, function_name, lines, index) = inspect.getframeinfo(previous_frame)
		print("Line "+str(line_number)+" of "+str(filename))
		print("Quitting with error")
		exit()

	if not(numpy.isclose(expected,received)):
		print("Expected "+str(expected)+" but received "+str(received))
		previous_frame = inspect.currentframe().f_back
		(filename, line_number, function_name, lines, index) = inspect.getframeinfo(previous_frame)
		print("Line "+str(line_number)+" of "+str(filename))
		print("Quitting with error")
		exit()


class RGB:
  def __init__(self,r,g,b,a=255):
    self.red = r
    self.green = g
    self.blue = b
    self.alpha = a

  def __str__(self):
    """Returning: string with contents"""
    return '('+str(self.red) +','+ str(self.green) +','+ str(self.blue) +')'
  
  def __repr__(self):
    return str(self.__class__)+ str(self)
  # def __repr__(self):
  #       return "rgb.RGB(%s,%s,%s)"%(self.red,self.green,self.blue)
  
  @property
  def red(self):
    return self._red 

  @red.setter
  def red(self,value):
    if not isinstance(value,int):
      raise ValueError("attribute red must be an int.")
    if not (0<=value<=255):
      raise ValueError("value "+str(value)+" for attribute red is outside of range [0,255].")

    self._red = value 

  @property
  def green(self):
    return self._green 

  @green.setter
  def green(self,value):
    if not isinstance(value,int):
      raise ValueError("attribute green must be an int.")
    if not (0<=value<=255):
      raise ValueError("value "+str(value)+" for attribute green is outside of range [0,255].")

    self._green = value

  @property
  def blue(self):
    return self._blue 

  @blue.setter
  def blue(self,value):
    if not isinstance(value,int):
      raise ValueError("attribute blue must be an int.")
    if not (0<=value<=255):
      raise ValueError("value "+str(value)+" for attribute blue is outside of range [0,255].")

    self._blue = value

  @property
  def alpha(self):
    return self._alpha 

  @alpha.setter
  def alpha(self,value):
    if not isinstance(value,int):
      raise ValueError("attribute alpha must be an int.")
    if not (0<=value<=255):
      raise ValueError("value "+str(value)+" for attribute alpha is outside of range [0,255].")

    self._alpha = value

  def glColor(self):
      return [self.red/255.0,self.green/255.0,self.blue/255.0,self.alpha/255.0]  


class CMYK:
  def __init__(self,c,m,y,k):
    self.cyan = c
    self.magenta = m
    self.yellow = y
    self.black = k

  def __str__(self):
    """Returning: string with contents"""
    return '('+str(self.cyan) +','+ str(self.magenta) +','+ str(self.yellow) +','+ str(self.black) +')'
  
  def __repr__(self):
    return str(self.__class__)+ str(self)
  
  @property
  def cyan(self):
    return self._cyan 

  @cyan.setter
  def cyan(self,value):
    if not isinstance(value,float):
      raise ValueError("attribute cyan must be a float.")
    if not (0.0<=value<=100.0):
      raise ValueError("value "+str(value)+" for attribute cyan is outside of range [0.0,100.0].")

    self._cyan = value 

  @property
  def magenta(self):
    return self._magenta 

  @magenta.setter
  def magenta(self,value):
    if not isinstance(value,float):
      raise ValueError("attribute magenta must be a float.")
    if not (0.0<=value<=100.0):
      raise ValueError("value "+str(value)+" for attribute magenta is outside of range [0.0,100.0].")

    self._magenta = value

  @property
  def yellow(self):
    return self._yellow 

  @yellow.setter
  def yellow(self,value):
    if not isinstance(value,float):
      raise ValueError("attribute yellow must be a float.")
    if not (0.0<=value<=100.0):
      raise ValueError("value "+str(value)+" for attribute yellow is outside of range [0.0,100.0].")

    self._yellow = value

  @property
  def black(self):
    return self._black 

  @black.setter
  def black(self,value):
    if not isinstance(value,float):
      raise ValueError("attribute black must be a float.")
    if not (0.0<=value<=100.0):
      raise ValueError("value "+str(value)+" for attribute black is outside of range [0.0,100.0].")

    self._black = value


class HSV:
  def __init__(self,h,s,v):
    self.hue = h
    self.saturation = s
    self.value = v

  def __str__(self):
    """Returning: string with contents"""
    return '('+str(self.hue) +','+ str(self.saturation) +','+ str(self.value) +')'
  
  def __repr__(self):
    return str(self.__class__)+ str(self)
  
  @property
  def hue(self):
    return self._hue 

  @hue.setter
  def hue(self,val):
    if not isinstance(val,float):
      raise ValueError("attribute hue must be a float.")
    if not (0.0<=val<360.0):
      raise ValueError("value "+str(val)+" for attribute hue is outside of range [0.0,360.0).")

    self._hue = val 

  @property
  def saturation(self):
    return self._saturation 

  @saturation.setter
  def saturation(self,val):
    if not isinstance(val,float):
      raise ValueError("attribute saturation must be a float.")
    if not (0.0<=val<=1.0):
      raise ValueError("value "+str(val)+" for attribute saturation is outside of range [0.0,1.0].")

    self._saturation = val

  @property
  def value(self):
    return self._value 

  @value.setter
  def value(self,val):
    if not isinstance(val,float):
      raise ValueError("attribute value must be a float.")
    if not (0.0<=val<=1.0):
      raise ValueError("value "+str(val)+" for attribute value is outside of range [0.0,1.0].")

    self._value = val


class Point3:
  def __init__(self,x=0,y=0,z=0):
    self.x = x
    self.y = y
    self.z = z

  def __str__(self):
    """Returning: string with contents"""
    return '('+str(self.x) +','+ str(self.y) +','+ str(self.z) +')'
  
  def __repr__(self):
        return "point.Point3(%s,%s,%s)"%(self.x,self.y,self.z)
  
  @property
  def x(self):
    return self._x 

  @x.setter
  def x(self,value):
    if not isinstance(value,int) and not isinstance(value,float):
        raise ValueError("attribute x must be an int or float.")
    self._x = float(value) 

  @property
  def y(self):
    return self._y

  @y.setter
  def y(self,value):
    if not isinstance(value,int) and not isinstance(value,float):
        raise ValueError("attribute y must be an int or float.")
    self._y = float(value) 

  @property
  def z(self):
    return self._z

  @z.setter
  def z(self,value):
    if not isinstance(value,int) and not isinstance(value,float):
        raise ValueError("attribute z must be an int or float.")
    self._z = float(value) 

  def distance(self, other):
    assert type(other) == Point3, repr(other)+' is not a point'
    dx = self.x - other.x
    dy = self.y - other.y
    dz = self.z - other.z
    return math.sqrt(dx**2 + dy**2 + dz**2)

  def clamp(self,low, high):
    if self.x >= high:
      self.x = high
    elif self.x <= low:
      self.x = low

    if self.y >= high:
      self.y = high
    elif self.y <= low:
      self.y = low

    if self.z >= high:
      self.z = high
    elif self.z <= low:
      self.z = low