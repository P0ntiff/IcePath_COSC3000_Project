#COSC3000 Graphics Assignment, Benedict Gattas (43915398)

#Icebreaker Game

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL.Image import *
from icePath.mouseInteractor import *
from icePath.Block import *

from sys import *
from math import *
from time import *

#Global window handle for game screen
windowHandle = 0

#Texture storage
blockTexID = 0
blockImage = Image( )
iceTexID = 0
iceImage = Image( )

#Rotating the block
Phi = 0
Theta = 0
Phi_sign = 1


def initGL( width, height ):
    # Black window background
    glClearColor( 0, 0, 0, 0 )
    glClearDepth( 1.0 )
    glDepthFunc( GL_LESS )
    glEnable( GL_DEPTH_TEST )
    glShadeModel( GL_SMOOTH )
    glEnable(GL_COLOR_MATERIAL)

    resizeGLScene( width, height )

def setupLight():
    x = 0.0
    y = 2.0
    z = 0.0

    #Setup light properties
    glLightfv(GL_LIGHT0, GL_DIFFUSE, GLfloat_3(1, 1, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT, GLfloat_3(0, 0, 0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, GLfloat_3(1, 1, 1))
    glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(x, y, z, 1))
    glEnable(GL_LIGHT0)

    #Make the light a yellow sphere
    glPushMatrix()
    glColor3f(1.0, 1.0, 0.0)
    glTranslatef(x, y, z)
    glutSolidSphere(0.125, 30, 30)
    # glDisable(GL_COLOR_MATERIAL)
    glPopMatrix()


def drawGLScene():
    global bAltTexCoords, mouseInteract, Theta

    #Clear screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #Reset matrix stack with the identity matrix
    glLoadIdentity()
    glTranslatef(0, 0, -6.0)
    setupLight()
    mouseInteract.applyTransformation()


    glEnable(GL_TEXTURE_2D)

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)  ####\
    glLineWidth(2)  #### > REMOVE at Task 3
    glColor4f(0, 0, 0, 1)  ####/

    player = Block(blockTexID)
    player.drawBlock()

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)  ####\
    glEnable(GL_POLYGON_OFFSET_FILL)  #### |
    glPolygonOffset(1, 1)  #### |
    glColor4f(1, 1, 1, 1)  #### > REMOVE at Task 3
    player.drawBlock()


    glDisable(GL_POLYGON_OFFSET_FILL)  ####/



    glutSwapBuffers()





#User input to game, configured here
def keyPressed(key, x, y):
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

    glutDisplayFunc( drawGLScene )

    glutIdleFunc( drawGLScene )

    glutReshapeFunc( resizeGLScene )
    glutKeyboardFunc( keyPressed )


    initGL( width, height )

    glutMainLoop( )

def resizeGLScene( width, height):
    # prevent a divide-by-zero error if the window is too small
    if height == 0:
        height = 1

    # reset the current viewport
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)

    # return to the modelview matrix mode
    glMatrixMode(GL_MODELVIEW)

main()