#COSC3000 Graphics Assignment

#Icebreaker Game

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL.Image import *
from icePath.mouseInteractor import *

import sys
import math
import time

#Global window handle for game screen
windowHandle = 0
#Texture storage
blockTexID = 0
blockImage = Image( )
iceTexID = 0
iceImage = Image( )


def ResizeGLScene( width, height):
    # prevent a divide-by-zero error if the window is too small
    if height == 0:
        height = 1

    # reset the current viewport and recalculate the perspective transformation
    # for the projection matrix
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)

    # return to the modelview matrix mode
    glMatrixMode(GL_MODELVIEW)


def InitGL( width, height ):
    # use black when clearing the colour buffers -- this will give us a black
    # background for the window
    glClearColor( 0, 0, 0, 0 )
    # enable the depth buffer to be cleared
    glClearDepth( 1.0 )
    # set which type of depth test to use
    glDepthFunc( GL_LESS )
    # enable depth testing
    glEnable( GL_DEPTH_TEST )
    # enable smooth colour shading
    glShadeModel( GL_SMOOTH )

    ResizeGLScene( width, height )


def DrawGLScene():
    global bAltTexCoords, nAngle, nTailLength, tColour, mouseInteract

    # clear the screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # reset the matrix stack with the identity matrix
    glLoadIdentity()

    # translate away from the camera then rotate the axis according
    # to the user-changeable rotation values
    glTranslatef(0, 0, -3.0)
    # glRotated( nRotX, 1, 0, 0 )
    # glRotated( nRotY, 0, 1, 0 )
    mouseInteract.applyTransformation()  # Perform transforms accourding to mouse input

    glEnable(GL_TEXTURE_2D)

    # *********************************************************************************#
    # *To see the window model without textures, redundant lines have been added below.#
    # *From Task 3 on, comment or delete all lines indicated with with #### below:     #
    # *********************************************************************************#
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)  ####\
    glLineWidth(2)  #### > REMOVE at Task 3
    glColor4f(0, 0, 0, 1)  ####/

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)  ####\
    glEnable(GL_POLYGON_OFFSET_FILL)  #### |
    glPolygonOffset(1, 1)  #### |
    glColor4f(1, 1, 1, 1)  #### > REMOVE at Task 3

    glDisable(GL_POLYGON_OFFSET_FILL)  ####/


    # since this is double buffered, we need to swap the buffers in order to
    # display what we just drew
    glutSwapBuffers()


#User input to game, configured here
def KeyPressed(key, x, y):
    global bAltTexCoords, bRepeatTexture

    key = ord(key)

    if key == 27:
        glutDestroyWindow(windowHandle)
        sys.exit()
    else:
        return


def main():
    global windowHandle, mouseInteract

    width = 640
    height = 480

    glutInit( "" )
    glutInitDisplayMode( GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize( width, height )
    glutInitWindowPosition( 50, 50 )

    #Initialise Game Screen
    windowHandle = glutCreateWindow ( b"Ice Path, A Game Written in PyOpenGL")

    #Permit Mouse Interaction
    mouseInteract = MouseInteractor( 0.01, 1 )
    mouseInteract.registerCallbacks( )

    glutDisplayFunc( DrawGLScene )

    glutIdleFunc( DrawGLScene )

    glutReshapeFunc( ResizeGLScene )
    glutKeyboardFunc( KeyPressed )


    InitGL( width, height )

    glutMainLoop( )


main()