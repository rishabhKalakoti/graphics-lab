import sys
from viewport import *
from drawLine import *
from drawPolygon import *
from drawCircle import *
from drawEllipse import *

if __name__ == "__main__":
	print("")
	print("Welcome to DRAWBOARD".center(50,'-'))
	print("")
	printCoords()
	print("")
	while True:
		print("Select one of the choices below:")
		print("1. Change Viewport Coords")
		print("2. Change Device Coords")
		print("3. Draw a Line")
		print("4. Draw a Polygon")
		print("5. Draw a Circle")
		print("6. Draw an Ellipse")
		print("0. Exit")
		choice = input()
		if choice == '0':
			sys.exit()
		elif choice == '1':
			changeViewportCoords()
		elif choice == '2':
			changeDeviceCoords()
		elif choice == '3':
			drawLineInterface()
		elif choice == '4':
			drawPolygonInterface()
		elif choice == '5':
			drawCircleInterface()
		elif choice == '6':
			drawEllipseInterface()
		else:
			print("Invalid Choice.")
		print("")
