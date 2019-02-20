import viewport
from graphics import *
from drawLine import *

# sutherland- hodgeman
def suthHodgClip(subjectPolygon, clipPolygon):
   def inside(p):
      return(cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])

   def computeIntersection():
      dc = [ cp1[0] - cp2[0], cp1[1] - cp2[1] ]
      dp = [ s[0] - e[0], s[1] - e[1] ]
      n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
      n2 = s[0] * e[1] - s[1] * e[0]
      n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
      return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]

   outputList = subjectPolygon
   cp1 = clipPolygon[-1]

   for clipVertex in clipPolygon:
      cp2 = clipVertex
      inputList = outputList
      outputList = []
      s = inputList[-1]

      for subjectVertex in inputList:
         e = subjectVertex
         if inside(e):
            if not inside(s):
               outputList.append(computeIntersection())
            outputList.append(e)
         elif inside(s):
            outputList.append(computeIntersection())
         s = e
      cp1 = cp2
   return(outputList)

def polygonClipInterface():
	polygon = list()
	clipPolygon = list()
	print("Enter no of vertices of polygon:")
	N = int(input())
	print("Enter vertices one by one.")
	for i in range(N):
		a,b = input().split()
		polygon.append([int(a),int(b)])
	print("Enter no of vertices of clipping polygon: (anticlockwise)")
	C = int(input())
	print("Enter vertices one by one.")
	for i in range(C):
		a,b = input().split()
		clipPolygon.append([int(a),int(b)])
	
	points = suthHodgClip(polygon, clipPolygon)
	viewport.initWindow()
	# draw polygon
	for i in range(len(polygon)):
		drawLine(polygon[i-1][0],polygon[i-1][1],polygon[i][0],polygon[i][1])
	viewport.f = 2
	# draw surface
	for i in range(len(clipPolygon)):
		drawLine(clipPolygon[i-1][0],clipPolygon[i-1][1],clipPolygon[i][0],clipPolygon[i][1])
	viewport.f = 3
	# draw new polygon
	for i in range(len(points)):
		drawLine(int(points[i-1][0]),int(points[i-1][1]),int(points[i][0]),int(points[i][1]))
	viewport.closeWin()
