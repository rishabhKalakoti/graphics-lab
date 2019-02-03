import sys
from viewport import *
from drawLine import *
from floodfill import *
from scanline import *
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
		print("3. Fill a Polygon using floodfill")
		print("4. Fill a Polygon using scanline")
		print("0. Exit")
		choice = input()
		if choice == '0':
			sys.exit()
		elif choice == '1':
			changeViewportCoords()
		elif choice == '2':
			changeDeviceCoords()
		elif choice == '3':
			floodfillInterface()
		elif choice == '4':
			scanlineInterface()
		else:
			print("Invalid Choice.")
		print("")
