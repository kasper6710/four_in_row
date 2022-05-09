from OpenGL.GL import *
from OpenGL.GLUT import *
import matplotlib
import numpy
import pandas
import math
import os
import sys

global WinWidth
global WinHeight

global matrix
global number_of_move
global winner_is

global rx
global ry
global tx
global ty
global tz
global tt
global ldown
global rdown
global list
global mx
global my


def init():
    global number_of_move
    global matrix
    global winner_is
    global rx
    global ry
    global tx
    global ty
    global tz
    global tt
    global ldown
    global rdown
    global list
    global WinWidth
    global WinHeight

    matrix = []
    for i in range(6):
        row = []
        for j in range(7):
            row.append('x')
        matrix.append(row)

    number_of_move = 0
    winner_is = 'x'

    rx = 0
    ry = 0

    tx = 0
    ty = 0
    tz = 0
    tt = 0
    ldown = False
    rdown = False
    list = 0

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_LINE_SMOOTH)
    glClearColor(0.9, 0.9, 0.6, 1)


def board():
    glColor3f(0.289, 0.34, 0.289)
    glBegin(GL_QUADS)
    glVertex3f(-4, -3, 0)
    glVertex3f(4, -3, 0)
    glVertex3f(4, 4, 0)
    glVertex3f(-4, 4, 0)
    glEnd()

    glColor3f(0.289, 0.34, 0.289)
    glBegin(GL_QUADS)
    glVertex3f(-4, -3, -0.5)
    glVertex3f(-4, 4, -0.5)
    glVertex3f(4, 4, -0.5)
    glVertex3f(4, -3, -0.5)
    glEnd()

    glColor3f(0.289, 0.34, 0.289)
    glBegin(GL_QUADS)
    glVertex3f(-4, 4, 0)
    glVertex3f(-4, -3, 0)
    glVertex3f(-4, -3, -0.5)
    glVertex3f(-4, 4, -0.5)
    glEnd()

    glColor3f(0.289, 0.34, 0.289)
    glBegin(GL_QUADS)
    glVertex3f(4, 4, 0)
    glVertex3f(-4, 4, 0)
    glVertex3f(-4, 4, -0.5)
    glVertex3f(4, 4, -0.5)
    glEnd()

    glColor3f(0.289, 0.34, 0.289)
    glBegin(GL_QUADS)
    glVertex3f(4, 4, 0)
    glVertex3f(4, -3, 0)
    glVertex3f(4, -3, -0.5)
    glVertex3f(4, 4, -0.5)
    glEnd()

    glColor3f(0.289, 0.34, 0.289)
    glBegin(GL_QUADS)
    glVertex3f(-4, -3, 0)
    glVertex3f(4, -3, 0)
    glVertex3f(4, -3, -0.5)
    glVertex3f(-4, -3, -0.5)
    glEnd()

    for i in range(-3, 4):
        for j in range(-2, 4):
            glColor3f(0, 0, 0)
            glBegin(GL_QUADS)
            glVertex3f(i - 0.3, j - 0.3, 0.01)
            glVertex3f(i - 0.3, j + 0.3, 0.01)
            glVertex3f(i + 0.3, j + 0.3, 0.01)
            glVertex3f(i + 0.3, j - 0.3, 0.01)
            glEnd()

            glColor3f(0, 0, 0)
            glBegin(GL_QUADS)
            glVertex3f(i - 0.3, j - 0.3, -0.51)
            glVertex3f(i + 0.3, j - 0.3, -0.51)
            glVertex3f(i + 0.3, j + 0.3, -0.51)
            glVertex3f(i - 0.3, j + 0.3, -0.51)
            glEnd()


def chips():
    global matrix

    for i in range(6):
        for j in range(7):
            if matrix[i][j] == 'r':
                glColor3f(1, 0, 0)
                glBegin(GL_QUADS)
                glVertex3f(j - 0.3 - 3, i - 0.3 - 2, 0.011)
                glVertex3f(j - 0.3 - 3, i + 0.3 - 2, 0.011)
                glVertex3f(j + 0.3 - 3, i + 0.3 - 2, 0.011)
                glVertex3f(j + 0.3 - 3, i - 0.3 - 2, 0.011)
                glEnd()
            elif matrix[i][j] == 'b':
                glColor3f(0, 0, 1)
                glBegin(GL_QUADS)
                glVertex3f(j - 0.3 - 3, i - 0.3 - 2, 0.011)
                glVertex3f(j - 0.3 - 3, i + 0.3 - 2, 0.011)
                glVertex3f(j + 0.3 - 3, i + 0.3 - 2, 0.011)
                glVertex3f(j + 0.3 - 3, i - 0.3 - 2, 0.011)
                glEnd()

            if matrix[i][j] == 'r':
                glColor3f(1, 0, 0)
                glBegin(GL_QUADS)
                glVertex3f(j - 0.3 - 3, i - 0.3 - 2, -0.511)
                glVertex3f(j + 0.3 - 3, i - 0.3 - 2, -0.511)
                glVertex3f(j + 0.3 - 3, i + 0.3 - 2, -0.511)
                glVertex3f(j - 0.3 - 3, i + 0.3 - 2, -0.511)
                glEnd()
            elif matrix[i][j] == 'b':
                glColor3f(0, 0, 1)
                glBegin(GL_QUADS)
                glVertex3f(j - 0.3 - 3, i - 0.3 - 2, -0.511)
                glVertex3f(j + 0.3 - 3, i - 0.3 - 2, -0.511)
                glVertex3f(j + 0.3 - 3, i + 0.3 - 2, -0.511)
                glVertex3f(j - 0.3 - 3, i + 0.3 - 2, -0.511)
                glEnd()


def push_chip_in_column(column):
    global matrix
    global number_of_move

    color_of_chip = 'r' if number_of_move % 2 == 0 else 'b'

    for i in range(6):
        if matrix[i][column] == 'x':
            matrix[i][column] = color_of_chip
            number_of_move += 1
            break


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    # glPolygonMode(GL_FRONT, GL_FILL)
    # glPolygonMode(GL_BACK, GL_LINE)

    glPushMatrix()
    glTranslatef(tx, ty, tz)
    glRotatef(rx, 1, 0, 0)
    glRotatef(ry, 0, 1, 0)

    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(2)
    glBegin(GL_LINES)

    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(3.0, 0.0, 0.0)
    glEnd()

    glColor3f(0.0, 0.8, 0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 3.0, 0.0)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 3.0)
    glEnd()

    board()
    chips()

    glPopMatrix()

    glutSwapBuffers()


def check_winner_in_row():
    global matrix
    global winner_is

    for i in range(len(matrix)):
        count_b = 0
        count_r = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'x':
                count_b = 0
                count_r = 0

            if matrix[i][j] == 'r':
                count_b = 0
                count_r += 1
                if count_r == 4:
                    winner_is = 'r'

            if matrix[i][j] == 'b':
                count_b += 1
                count_r = 0
                if count_b == 4:
                    winner_is = 'b'


def check_winner_in_column():
    global matrix
    global winner_is

    for i in range(7):
        count_b = 0
        count_r = 0
        for j in range(6):
            if matrix[j][i] == 'x':
                count_b = 0
                count_r = 0

            if matrix[j][i] == 'r':
                count_b = 0
                count_r += 1
                if count_r == 4:
                    winner_is = 'r'

            if matrix[j][i] == 'b':
                count_b += 1
                count_r = 0
                if count_b == 4:
                    winner_is = 'b'


def check_winner_in_diagonal():
    global matrix
    global winner_is

    for i in range(3):
        for j in range(4):
            if matrix[i + 3][j] == 'r' and matrix[i + 2][j + 1] == 'r'\
                    and matrix[i + 1][j + 2] == 'r' and matrix[i][j + 3] == 'r':
                winner_is = 'r'
                return

            if matrix[i + 3][j] == 'b' and matrix[i + 2][j + 1] == 'b'\
                    and matrix[i + 1][j + 2] == 'b' and matrix[i][j + 3] == 'b':
                winner_is = 'b'
                return

    for i in range(3):
        for j in range(4):
            if matrix[i][j] == 'r' and matrix[i + 1][j + 1] == 'r'\
                    and matrix[i + 2][j + 2] == 'r' and matrix[i + 3][j + 3] == 'r':
                winner_is = 'r'
                return

            if matrix[i][j] == 'b' and matrix[i + 1][j + 1] == 'b'\
                    and matrix[i + 2][j + 2] == 'b' and matrix[i + 3][j + 3] == 'b':
                winner_is = 'b'
                return


def check_winner():
    global winner_is
    global matrix

    is_draw = True
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'x':
                is_draw = False
                break

    if is_draw:
        print('Draw')
        glutLeaveMainLoop()

    if winner_is == 'r':
        print('Winner is RED')
        glutLeaveMainLoop()

    if winner_is == 'b':
        print('Winner is BLUE')
        glutLeaveMainLoop()


def keyboard(key, x, y):
    global matrix
    if key == b'1':
        push_chip_in_column(0)
    if key == b'2':
        push_chip_in_column(1)
    if key == b'3':
        push_chip_in_column(2)
    if key == b'4':
        push_chip_in_column(3)
    if key == b'5':
        push_chip_in_column(4)
    if key == b'6':
        push_chip_in_column(5)
    if key == b'7':
        push_chip_in_column(6)

    glutPostRedisplay()

    check_winner_in_row()
    check_winner_in_column()
    check_winner_in_diagonal()
    check_winner()



def reshape(Width, Height):
    global WinWidth
    global WinHeight

    glViewport(0, 0, Width, Height)
    WinWidth = Width
    WinHeight = Height

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10.0, 10.0, -10.0, 10.0, -10.0, 10.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def Mouse(button, state, x, y):
    global mx
    global my
    global ldown
    global rdown

    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            ldown = True
            mx = x
            my = y
        elif state == GLUT_UP:
            ldown = False
    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            rdown = True
            mx = x
            my = y
        elif state == GLUT_UP:
            rdown = False


def MouseMotion(x, y):
    global rx
    global ry
    global tx
    global ty
    global tz
    global mx
    global my
    global ldown
    global rdown

    if ldown:
        rx += 0.5 * (y - my)
        ry += 0.5 * (x - mx)
        mx = x
        my = y
        glutPostRedisplay()
    if rdown:
        tx += 0.01 * (x - mx)
        if tt:
            tz += 0.01 * (y - my)
        else:
            ty += 0.01 * (my - y)
        mx = x
        my = y
        glutPostRedisplay()


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(700, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b'MyGame')

    init()

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(reshape)
    glutMouseFunc(Mouse)
    glutMotionFunc(MouseMotion)

    glutMainLoop()
