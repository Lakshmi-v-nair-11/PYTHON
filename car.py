from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

size = 0
x = 0
y = 0
mode = 1
FPS = 60
WINDOW_SIZE = 500
theta = 0


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-500, 500, -500, 500)


def square():
    glClear(GL_COLOR_BUFFER_BIT)

    global size
    global x
    global y
    global theta

    glBegin(GL_POLYGON)
    glColor3f(0.9, 0.4, 1.0)
    glVertex2f(x+100, y-50)
    glVertex2f(x+100, y+50)
    glVertex2f(x-100, y+50)
    glVertex2f(x-100, y-50)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(x+50, y-55)
    for i in range(0, 361, 1):
        glVertex2f(35*math.cos(math.pi*i/180.0)+x+50,
                   35*math.sin(math.pi*i/180.0)+y-55)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(x+50, y-55)
    glVertex2f(35*math.cos(math.pi*theta/180.0)+x+50,
               35*math.sin(math.pi*theta/180.0)+y-55)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(x-50, y-55)
    for i in range(0, 361, 1):
        glVertex2f(35*math.cos(math.pi*i/180.0)+x-50,
                   35*math.sin(math.pi*i/180.0)+y-55)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(x-50, y-55)
    glVertex2f(35*math.cos(math.pi*theta/180.0)+x-50,
               35*math.sin(math.pi*theta/180.0)+y-55)
    glEnd()

    glutSwapBuffers()


def animate(temp):

    global mode
    global x
    global FPS
    global WINDOW_SIZE
    global theta

    if mode == 1:
        x = x+1
        theta = theta - 1
        if (x+50 > WINDOW_SIZE):
            mode = 0

    if mode == 0:
        x = x-1
        theta = theta - 1
        if (x+50 < -WINDOW_SIZE):
            mode = 1

    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS), animate, 0)


def main():
    glutInit(sys.argv)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutCreateWindow("square")
    glutDisplayFunc(square)
    glutTimerFunc(0, animate, 0)
    glutIdleFunc(square)
    init()
    glutMainLoop()


main()
