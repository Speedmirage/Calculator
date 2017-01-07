print "The following calculator is able to calculate the area of a plethora of diferent shapes"

from math import pi
from time import sleep

sleep(3)

print "This Calculator by Addiel is being fired up... "

sleep(2)

hint = "Don't forget to include the correct units! :) \ nExiting... "

option = raw_input("Please input C for Circle, T for Triangle, S for Sqaure, R for Rectangle, P for Parallelogram, TR for Trapezoid, E for Ellipse, CS for Cube (surface), SS for Sphere (surface), or COS for Cone (surface) ")

option = option.upper()

if option == "C":
	print "You have selected CIRCLE"
	sleep(0.5)
	radius = float(raw_input("Please input the Circle's radius "))
	area = pi * (radius ** 2)
	print "The pie is baking..."
	sleep(1)
	print "Area= %s. Also %s " % (area, hint)
elif option == "T":
	print "You have selected TRIANGLE"
	sleep(0.5)
	base = float(raw_input("Enter a base "))
	height = float(raw_input("Enter the height "))
	area = (base * height) / 2
	print "Uni Bi Tri..."
	sleep(1)
	print "Area= %s. Also %s" % (area, hint)
elif option == "S":
	print "You have selected SQUARE"
	sleep(0.5)
	side = float(raw_input("Please input the length of the sides "))
	area = (side ** 2)
	print "Calculating ..." 
	sleep(1)
	print "Area= %s. Also %s" % (area, hint)
elif option == "R":
	print "You have selected RECTANGLE"
	sleep(0.5)
	length = float(raw_input("Please input the length of the Rectnagle "))
	width = float(raw_input("Please input the width of the Rectangle "))
	area = (length * width)
	print "Computing..."
	sleep(1)
	print "Area= %s. Also %s" % (area, hint)
elif option == "P":
	print "You have selected PARALLELOGRAM"
	sleep(0.5)
	base = float(raw_input("Please input the Parallelogram's base "))
	height = float(raw_input("Please input the Parallelogram's height "))
	area = (base * height)
	print "Computing... "
	sleep(1)
	print "Area= %s. Also %s" % (area, hint)
elif option == "TR":
	print "You have selected TRAPEZOID"
	sleep(0.5)
	base1 = float(raw_input("Please enter the first base of the Trapezoid "))
	base2 = float(raw_input("Please input the second base of the Trapezoid "))
	height = float(raw_input("Please input the height of the Trapezoid "))
	area = height * (base1 + base2) / 2 
	print "Calculating... "
	sleep(1)
	print "Area= %s. Also %s" % (area, hint)
elif option == "E":
	print "You have selected ELLIPSE"
	sleep(0.5)
	radius1 = float(raw_input("Please input the first radius of the Ellipse "))
	radius2 = float(raw_input("Please input the second radius of the Ellipse "))
	area = pi * radius1 * radius2
	print "Computing... "
	sleep(1)
	print "Area= %s. Also %s" % (area, hint)
elif option == "CS":
	print "You have selected CUBE (SURFACE)"
	sleep(0.5)
	side = float(raw_input("Please input the value of the Cube's side "))
	area = 6 * (side ** 2)
	print "Computing... "
	sleep(1)
	print "Area= %s. Also %s" % (area, hint)
elif option == "SS":
	print "You have selected SPHERE (SURFACE)"
	sleep(0.5)
	radius = float(raw_input("Please input the radius of the Sphere "))
	area = 4 * pi * ( radius ** 2)
	print "Calculating... "
	sleep(1)
	print "Area= %s. Also %s" % (area, hint)
elif option == "COS":
	print "You have selected CONE (SURFACE)"
	sleep(0.5)
	radius = float(raw_input("Please input the radius of the Cone "))
	side = float(raw_input("Please input the side of the Cone "))
	area = pi * radius * side
	print "Computing... "
	sleep (1)
	print "Area= %s. Also %s" % (area, hint)
else:
  print "The string you inputed is invalid, please try again!"
  sleep(1)
  print "Program quitting..."
  
  
  
  
  
  
  

