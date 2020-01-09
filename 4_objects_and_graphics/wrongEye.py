#Incorrect way to create two eyes
from graphics import Circle, Point, GraphWin
leftEye = Circle (Point (80 , 50) , 5)
leftEye.setFill ('yellow')
leftEye.setOutline ('red')
rightEye = leftEye
rightEye.move ( 20 , 0 )
win = GraphWin('Wrong Eyes')
leftEye.draw(win)
rightEye.draw(win)