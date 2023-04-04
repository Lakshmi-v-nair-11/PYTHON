from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE = 500
x = 0.0
y = 0.0
angle = 0
FPS = 60
mode = 1


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)


def drawpendulum():
    global x, y
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)

    glColor3f(0.4, 0.6, 0.2)
    glVertex2f(x, y)
    glVertex2f(300*math.cos(angle*math.pi/180)+x,
               300*math.sin(angle*math.pi/180)+y)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(300*math.cos(angle*math.pi/180)+x,
               300*math.sin(angle*math.pi/180)+y)
    for i in range(0, 361, 1):
        glVertex2f(70*math.cos(i*math.pi/180)+300*math.cos(angle*math.pi/180),
                   70*math.sin(i*math.pi/180)+300*math.sin(angle*math.pi/180))
    glEnd()
    glutSwapBuffers()


def animate(temp):

    global angle, mode

    if mode == 1:
        angle = angle-1
        if (angle == 180):
            mode = 0

    if mode == 0:
        angle = angle+1
        if (angle == 0):
            mode = 1

    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS), animate, 0)


def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Pendulum")
    glutDisplayFunc(drawpendulum)
    glutTimerFunc(0, animate, 0)
    glutIdleFunc(drawpendulum)
    init()
    glutMainLoop()


main()
