from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE = 500
GLOBAL_X = 0.0
GLOBAL_Y = 0.0
FPS = 1000

j = 4320.0
k = 360.0

def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
	
def drawCircle():
	global j
	global k
	global GLOBAL_X
	global GLOBAL_Y
	
	x = GLOBAL_X
	y = GLOBAL_Y
	
	glClear(GL_COLOR_BUFFER_BIT)
	
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(1.0,0.0,1.0)
	glVertex2f(x,y)
	for i in range(360,-1,-1):
		glVertex2f(400 * math.cos(math.pi * i /180.0) + x,400 * math.sin(math.pi * i /180.0) + y)
	glEnd()
	
	glLineWidth(4.0)
	glBegin(GL_LINES)
	glColor3f(0.0,1.0,0.0)
	glVertex2f(x,y)
	glVertex2f(200 * math.cos(math.pi * j /180.0) + x,200 * math.sin(math.pi * j /180.0) + y)
	glEnd()
	
	glLineWidth(2.0)
	glBegin(GL_LINES)
	glColor3f(1.0,1.0,0.0)
	glVertex2f(x,y)
	glVertex2f(100 * math.cos(math.pi * k /180.0) + x,100 * math.sin(math.pi * k /180.0) + y)
	glEnd()
	
	glutSwapBuffers()
	
def animate(temp):
	global j,k
	if (j < 0 or k < 0) :
		j = 4320.0
		k = 360.0
	else:
		j = j - 1
		k = k - 1/12
	glutPostRedisplay()
	glutTimerFunc(int(1000/FPS),animate,0)
	
def main():
	glutInit(sys.argv)
	glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
	glutInitWindowPosition(0,0)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Clock")
	glutDisplayFunc(drawCircle)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(drawCircle)
	init()
	glutMainLoop()
	
main()
