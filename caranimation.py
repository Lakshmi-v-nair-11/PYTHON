from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE = 500
x = 0.0
y = 0.0
FPS = 60
angle = 0.0


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)


def drawCar():
    global x
    global y
    global angle

    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(x-100, y+50)
    glVertex2f(x+100, y+50)
    glVertex2f(x+100, y-50)
    glVertex2f(x-100, y-50)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(x-50, y-85)
    for i in range(0, 361, 1):
        glVertex2f(35*math.cos(math.pi*i/180.0)+x-50,
                   35*math.sin(math.pi*i/180.0)+y-85)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(x+50, y-85)
    for i in range(0, 361, 1):
        glVertex2f(35*math.cos(math.pi*i/180.0)+x+50,
                   35*math.sin(math.pi*i/180.0)+y-85)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(x-50, y-85)
    glVertex2f(35*math.cos(math.pi*angle/180.0)+x-50,
               35*math.sin(math.pi*angle/180.0)+y-85)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(x-50, y-85)
    glVertex2f(35*math.cos(math.pi*angle/180.0)+x-50,
               35*math.sin(math.pi*angle/180.0)+y-85)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(x+50, y-85)
    glVertex2f(35*math.cos(math.pi*angle/180.0)+x+50,
               35*math.sin(math.pi*angle/180.0)+y-85)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(x+50, y-85)
    for i in range(0, 361, 1):
        glVertex2f(35*math.cos(math.pi*i/180.0)+x-50,
                   35*math.sin(math.pi*i/180.0)+y-85)
    glEnd()

    glutSwapBuffers()


def animate(key):
    global x
    global y
    global angle
    global WINDOW_SIZE

    if key == 'a':
        if (x-100 <= -WINDOW_SIZE):
            x = 400
        else:
            x -= 1
        angle += 10

    if key == 'd':
        if (x+100 >= WINDOW_SIZE):
            x = -400
        else:
            x += 1
        angle -= 10

    glutPostRedisplay()


def keyboard(key, x, y):
    key = key.decode()
    if key == 'a':
        animate('a')
    elif key == 'd':
        animate('d')
    elif key == 'f':
        glutFullScreen()
    elif key == 'z':
        glutLeaveMainLoop()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Car")
    glutDisplayFunc(drawCar)
    glutKeyboardFunc(keyboard)
    init()
    glutMainLoop()


main()
