import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 500, 500


# ---Section 1---
def square():
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_QUADS)        # Begin the sketch
    glVertex2f(100, 100)     # Coordinates for the bottom left point
    glVertex2f(200, 100)     # Coordinates for the bottom right point
    glVertex2f(200, 200)     # Coordinates for the top right point
    glVertex2f(100, 200)     # Coordinates for the top left point
    glEnd()                  # Mark the end of drawing


def right_triangle():
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_TRIANGLES)        # Begin the sketch
    glVertex2f(100, 100)     # Coordinates for the bottom left point
    glVertex2f(200, 200)     # Coordinates for the top right point
    glVertex2f(100, 200)     # Coordinates for the top left point
    glEnd()                  # Mark the end of drawing


def line_points():
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_POINTS)        # Begin the sketch
    for i in range(100):
        glVertex2f(i, i)     # create all coordinate
    glEnd()                  # Mark the end of drawing


# ---Section 2---
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)             # Projection (It is clip 2D space at certain distance from the camera view)
    glLoadIdentity()                        # Setting projection mode to be identity matrix
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)              # model view (Camera position and orientation in 3D whole space)
    glLoadIdentity()


# This alone isn't enough to draw our square
# ---Section 3---
def show_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    # Remove everything from screen (i.e. displays all white)
    glLoadIdentity()    # Reset all graphic/shape's position
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    line_points()                   # Draw a geometry function
    glutSwapBuffers()


# ---Section 3---
def call():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)        # Set the display mode to be colored
    glutInitWindowSize(w, h)              # Set the w and h of your window
    glutInitWindowPosition(0, 0)          # Set the position at which this windows should appear
    wind = glutCreateWindow("OpenGL Coding Practice")   # Set a window title
    glutDisplayFunc(show_screen)
    glutIdleFunc(show_screen)              # Keeps the window open
    glutMainLoop()                         # Keeps the above created window displaying/running in a loop
