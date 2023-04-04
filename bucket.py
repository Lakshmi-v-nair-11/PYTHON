from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE = 500
GLOBAL_Y = 20
FPS = 60


def init():
	glClearColor(1.0, 1.0, 1.0, 1.0)
	gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)


def drawBucket():
	global GLOBAL_Y

	x = 0.0
	y = 0.0

	glBegin(GL_QUADS)
	glColor3f(1.0, 0.0, 1.0)
	glVertex2f(x, y)
	glVertex2f(x + 20, y)
	glVertex2f(x + 20, y + 100)
	glVertex2f(x, y + 100)
	glEnd()

	glBegin(GL_QUADS)
	glColor3f(1.0, 0.0, 1.0)
	glVertex2f(x + 20, y)
	glVertex2f(x + 120, y)
	glVertex2f(x + 120, y + 20)
	glVertex2f(x + 20, y + 20)
	glEnd()

	glBegin(GL_QUADS)
	glColor3f(1.0, 0.0, 1.0)
	glVertex2f(x + 120, y)
	glVertex2f(x + 140, y)
	glVertex2f(x + 140, y + 100)
	glVertex2f(x + 120, y + 100)
	glEnd()

	glBegin(GL_QUADS)
	glColor3f(0.0, 0.0, 1.0)
	glVertex2f(x+20, y+20)
	glVertex2f(x+120, y+20)
	glVertex2f(x+20, GLOBAL_Y+20+1)
	glVertex2f(x+120, GLOBAL_Y+20+1)
	glEnd()

	glutSwapBuffers()


def animate(temp):
	global GLOBAL_Y

	if (GLOBAL_Y > 79):
		GLOBAL_Y = 0
	else:
		GLOBAL_Y = GLOBAL_Y + 1
	glutPostRedisplay()
	glutTimerFunc(int(1000/FPS), animate, 0)


def main():
	glutInit(sys.argv)
	glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
	glutInitWindowPosition(0, 0)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Bucket getting filled with water")
	glutDisplayFunc(drawBucket)
	glutTimerFunc(0, animate, 0)
	glutIdleFunc(drawBucket)
	init()
	glutMainLoop()


main()
