#This program illustrates the correct way of drawing two eyes using the clone method
from graphics import Circle, Point, GraphWin
leftEye = Circle (Point (80 , 50) , 5)
leftEye.setFill ('yellow')
leftEye.setOutline ('red')
rightEye = leftEye.clone ( ) # rightEye is an exact copy of the left
rightEye.move ( 20 , 0 )
win = GraphWin('Eyes')
leftEye.draw(win)
rightEye.draw(win)
