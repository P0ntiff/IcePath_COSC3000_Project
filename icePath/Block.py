

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from time import *

#For a rectangular prism pivoting along the ground
#0 = rest
#1 = Hor. to Vert. North
#2 = Hor. to Vert. South
#3, 4, 5, 6 = Vert. to Hor. for North, South, East, West respectively
#7 = Hor. to Hor. East
#8 = Hor. to Hor. West

#Main player controlled rectangular prism
class Block:
    def __init__(self, texID):
        self._texID = texID
        #Rotating on 3 axes
        self._alpha = 0
        self._beta = 0
        self._gamma = 0
        self._state = 1

    def drawBlock(self):
        def ruler():
            # ORIGIN = PINK
            glPushMatrix()
            glColor3f(1.0, 0, 1.0)
            glTranslatef(0, 0, 0)
            glutSolidCube(0.125)
            glPopMatrix()

            # 1 in Y direction = BLUE
            glPushMatrix()
            glColor3f(0, 0, 1.0)
            glTranslatef(0, 1.0, 0)
            glutSolidCube(0.125)
            glTranslatef(0, -1.0, 0)
            glPopMatrix()

            # -1 in Z direction = RED
            glPushMatrix()
            glColor3f(1.0, 0, 0)
            glTranslatef(0, 0, -1.0)
            glutSolidCube(0.125)
            glTranslatef(0, 0, 1.0)
            glPopMatrix()

            # 1 in X direction = GREEN
            glPushMatrix()
            glColor3f(0, 1.0, 0)
            glTranslatef(1.0, 0, 0)
            glutSolidCube(0.125)
            glTranslatef(-1.0, 0, 0)
            glPopMatrix()

            x = [20, 0, 0]
            y = [0, 20, 0]
            z = [0, 0, -20]
            o = [0, 0, 0]

            glBegin(GL_LINES)

            glColor3fv([0, 1, 0])
            glVertex3fv(o)
            glVertex3fv(x)

            glColor3fv([0, 0, 1])
            glVertex3fv(o)
            glVertex3fv(y)

            glColor3fv([1, 0, 0])
            glVertex3fv(o)
            glVertex3fv(z)

            glEnd()

        def drawLongFace():
            glPushMatrix()

            glBegin(GL_QUADS)
            glVertex3f(0, 0, 0)
            glVertex3f(1.0, 0, 0)
            glVertex3f(1.0, 2.0, 0)
            glVertex3f(0, 2.0, 0)
            glEnd()

            glPopMatrix()

        def drawSquareFace():
            glPushMatrix()

            glBegin(GL_QUADS)
            glVertex3f(0, 0, 0)
            glVertex3f(0, 0, -1.0)
            glVertex3f(0, 1.0, -1.0)
            glVertex3f(0, 1.0, 0)
            glEnd()

            glPopMatrix()


        glPushMatrix()
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        # #State 1 to State 2
        # glTranslatef(1.0, 0, 0)
        # glRotatef(90, 0, 1.0, 0)
        # glTranslatef(-1.0, 0, 0)
        # glRotatef(90, 1.0, 0, 0)


        #State 2 to State 2
        # glRotatef(90, 0, 1.0, 0)
        # glTranslatef(0, 0, -1)
        # glRotatef(-90, 0, 1.0, 0)

        ruler()
        glColor3f(0.6, 0.6, 0.6)
        #TOP, 2 SIDES, and BOTTOM
        # glTranslatef(-1.0, -1.0, 0)
        drawLongFace()
        glRotatef(90, 0, 0, -1)
        drawSquareFace()
        glRotatef(-90, 0, 0, -1)
        glTranslatef(0, 0, -1.0)
        drawLongFace()
        glRotatef(-90, 0, 0, -1)
        glTranslatef(2.0, -1.0, 1.0)
        drawSquareFace()

        #OTHER TWO SIDES
        glRotatef(90, 1.0, 0, 0)
        glRotatef(90, 0, 0, 1.0)
        glTranslatef(-1.0, 0, 0)
        drawLongFace()

        glTranslatef(0, 0, -1.0)
        drawLongFace()


        glPopMatrix()

    def handleRotation(self, blockHorizontal, rotationMode):
        self._rotationMode = rotationMode
        if (self._rotationMode == 0):
            self.drawBlock()

        elif (self._rotationMode == 2):
            self._theta += 3
            if (self._theta >= 90):
                self._rotationMode = 0
                self._theta = 0
                self._horizontal = False
            else:
                glRotatef(self._theta, 1.0, 0, 0)
                self.drawBlock()


    def handleWPress(self):
        return

    def handleAPress(self):
        return

    def handleSPress(self):
        return

    def handleDPress(self):
        return

    def getTexID(self):
        return self._texID

    def getRotationMode(self):
        return self._rotationMode

    def getHorizontal(self):
        return self._horizontal




#ZERO TO ONE and ONE TO TWO ('W')
#    glTranslatef(1.0, 0, 0)
#    glRotatef(90, 0, 1.0, 0)

#   glRotatef(90, 1.0, 0, 0)