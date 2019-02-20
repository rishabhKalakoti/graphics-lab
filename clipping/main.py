import sys
from viewport import *
from drawLine import *
from sutherland import *
from parametric import *
from polygonclip import *

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
		print("3. Line clipping using Cohen Sutherland algo")
		print("4. Line clipping using Parametric clipping")
		print("5. Polygon Clipping")
		print("0. Exit")
		choice = input()
		if choice == '0':
			sys.exit()
		elif choice == '1':
			changeViewportCoords()
		elif choice == '2':
			changeDeviceCoords()
		elif choice == '3':
			clipInterface()
		elif choice == '4':
			parametricClipInterface()
		elif choice == '5':
			polygonClipInterface()
		else:
			print("Invalid Choice.")
		print("")
