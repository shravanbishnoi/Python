"""This module contains classes and functions
Author: Shravan
Date: 18/02/2023
"""
import math

class Point3:
	"""docstring for Point3"""
	def __init__(self, x,y,z):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		"""Returning: string with contents"""
		return '('+str(self.red) +','+ str(self.green) +','+ str(self.blue) +')'

	def __repr__(self):
		return str(self.__class__)+ str(self)
		
	def distance(self, other):
		assert type(other)==Point3, repr(other)+ ' is not a point'
		dx = self.x - other.x
		dy = self.y - other.y
		dz = self.y - other.z
		return math.sqrt(dx**2 + dy**2 + dz**2)
