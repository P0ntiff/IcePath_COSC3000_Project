#COSC3000 Graphics Assignment, Benedict Gattas (43915398)

#Icebreaker Game

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from icePath.mouseInteractor import *
from icePath.Block import *
from PIL.Image import *

from math import *
from time import *

#Global window handle for game screen
windowHandle = 0

#Texture storage
blockTexID = 0
blockImage = Image( )
iceTexID = 0
iceImage = Image( )
waterTexID = 0
waterImage = Image( )

#Rotating the block
rotationMode = 0
player = Block(blockTexID)


def initGL( width, height ):
    global waterImage, iceImage, blockImage

    #load images
    waterImage = LoadImage( "water.bmp" )
    iceImage = LoadImage( "ice.bmp" )
    blockImage = LoadImage( "wood.bmp")
    InitTexturing()

    # Black window background
    glClearColor( 0, 0, 0, 0 )
    glClearDepth( 1.0 )
    glDepthFunc( GL_LESS )
    glEnable( GL_DEPTH_TEST )
    glShadeModel( GL_SMOOTH )

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    resizeGLScene( width, height )

def setupLight():
    x = 1.0
    y = 3.0
    z = -1.0

    #Setup light properties
    glLightfv(GL_LIGHT0, GL_DIFFUSE, GLfloat_3(1, 1, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT, GLfloat_3(0, 0, 0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, GLfloat_3(1, 1, 1))
    glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(x, y, z, 1))
    glEnable(GL_LIGHT0)

    #Make the light a white sphere
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glTranslatef(x, y, z)
    glutSolidSphere(0.125, 30, 30)
    glDisable(GL_COLOR_MATERIAL)
    glPopMatrix()


def drawGLScene():
    global bAltTexCoords, mouseInteract, Theta, Phi, blockHorizontal, rotationMode

    #Clear screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #Reset matrix stack with the identity matrix
    glLoadIdentity()
    glTranslatef(0, 0, -8.0)
    mouseInteract.applyTransformation()
    setupLight()

    #The Ice Rink
    glEnable(GL_LIGHTING)
    glEnable(GL_TEXTURE_2D)
    drawIceRink()
    glDisable(GL_LIGHTING)
    glDisable(GL_TEXTURE_2D)

 #   glEnable(GL_TEXTURE_2D)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    player.drawBlock()
    glDisable(GL_LIGHTING)


    glutSwapBuffers()


def drawIceRink():
    global iceTexID

    def drawLongTop():
        glPushMatrix()

        glBegin(GL_QUADS)
        glVertex3f(0, 0.5, 0.2); glTexCoord2f(0, 0)
        glVertex3f(-0.2, 0.5, 0.2); glTexCoord2f(1, 0)
        glVertex3f(-0.2, 0.5, -10.2); glTexCoord2f(1, 1)
        glVertex3f(0, 0.5, -10.2); glTexCoord2f(0, 1)
        glEnd()

        glPopMatrix()

    def drawLongSide():
        glPushMatrix()

        glBegin(GL_QUADS)
        glVertex3f(0, 0, 0.2); glTexCoord2f(1, 0)
        glVertex3f(0, 0.5, 0.2); glTexCoord2f(1, 1)
        glVertex3f(0, 0.5, -10.2); glTexCoord2f(0, 1)
        glVertex3f(0, 0, -10.2); glTexCoord2f(0, 0)
        glEnd()

        glPopMatrix()

    def drawShortSide():
        glPushMatrix()

        glBegin(GL_QUADS)
        glVertex3f(0, 0, 0.2)#; glTexCoord3f(0, 0, )
        glVertex3f(0, 0.5, 0.2)
        glVertex3f(-0.2, 0.5, 0.2)
        glVertex3f(-0.2, 0, 0.2)
        glEnd()

        glPopMatrix()


    #glColor3f(1.0, 0, 0)
    glBindTexture( GL_TEXTURE_2D, iceTexID )
    for i in range(0, 10):
        for j in range(0, 10):
            glPushMatrix()
            glBegin(GL_QUADS)
            glVertex3f(float(i), 0, float(-1*j));  glTexCoord2f(0, 0)
            glVertex3f(float(i) + 1, 0, float(-1*j));  glTexCoord2f(1, 0)
            glVertex3f(float(i) + 1, 0, float(-1*j) - 1);  glTexCoord2f(1, 1)
            glVertex3f(float(i), 0, float(-1*j) - 1);  glTexCoord2f(0, 1)
            glEnd()
            glPopMatrix()

    glBindTexture( GL_TEXTURE_2D, blockTexID )
    for i in range(0, 4):
        drawShortSide()
        drawLongSide()
        drawLongTop()
        glTranslatef(-0.2, 0, 0)
        drawLongSide()
        glTranslatef(0.2, 0, 0)
        glTranslatef(0, -0.5, 0)
        drawLongTop()
        glTranslatef(0, 0.5, 0)

        glTranslatef(0, 0, -10)
        glRotatef(-90, 0, 1.0, 0)


#User input to game, configured here
def keyPressed(key, x, y):
    global bAltTexCoords, bRepeatTexture, blockHorizontal, rotationMode, player

    key = ord(key)

    if key == 27:
        glutDestroyWindow(windowHandle)
        sys.exit()
    elif key == ord('W') or key == ord('w'):
        player.handleWPress()
    elif key == ord('S') or key == ord('s'):
        player.handleSPress()
    elif key == ord('A') or key == ord('a'):
        player.handleAPress()
    elif key == ord('D') or key == ord('d'):
        player.handleDPress()
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


def LoadImage(file):
    image = Image( )

    try:
        foo = open( file )

        image.sizeX = foo.size[0]
        image.sizeY = foo.size[1]
        image.data = foo.tobytes("raw", "RGBX", 0, -1)
    except:
        print("Could not load image :(")
        sys.exit()

    return image


#
# Initialises the textures being used for the scene
#
def InitTexturing():
    global waterImage, iceImage, waterTexID, iceTexID, blockImage, blockTexID

    # create textures
    waterTexID = glGenTextures( 1 )
    iceTexID = glGenTextures( 1 )
    blockTexID = glGenTextures( 1 )

    # just use linear filtering
    glBindTexture(GL_TEXTURE_2D, waterTexID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexImage2D(GL_TEXTURE_2D, 0, 4,
                 waterImage.sizeX, waterImage.sizeY,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, waterImage.data)

    glBindTexture(GL_TEXTURE_2D, iceTexID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexImage2D(GL_TEXTURE_2D, 0, 4,
                 iceImage.sizeX, iceImage.sizeY,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, iceImage.data)

    glBindTexture(GL_TEXTURE_2D, blockTexID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexImage2D(GL_TEXTURE_2D, 0, 4,
                 blockImage.sizeX, blockImage.sizeY,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, blockImage.data)

main()