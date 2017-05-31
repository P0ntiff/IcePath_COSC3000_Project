

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#Main player controlled rectangular prism
class Block:
    def __init__(self, texID):
        self._texID = texID

    def drawBlock(self):
        def DrawLongFace():
            glPushMatrix()

            glBegin(GL_QUADS)
            glVertex3f(0, 0, 0)
            glVertex3f(0.1, 0.1, 0)
            glVertex3f(0.1, 1.1, 0)
            glVertex3f(0, 1.2, 0)
            glEnd()

            glPopMatrix()

        def drawSquareFace():
            glPushMatrix()

            glBegin(GL_QUADS)
            glVertex3f(0, 0, 0)
            glVertex3f(0, 1.0, 0)
            glVertex3f(0, 1.0, -1.0)
            glVertex3f(0, 0, -1.0)
            glEnd()

            glPopMatrix()

        glPushMatrix()
        glPolygonMode(GL_BACK, GL_LINE)

        # FRONT
        glTranslatef(-0.6, -0.6, 0.05)
        DrawLongFace()
        glTranslatef(0, 1.2, 0)
        glRotatef(90, 0, 0, -1)
        DrawLongFace()
        glTranslatef(0, 1.2, 0)
        glRotatef(90, 0, 0, -1)
        DrawLongFace()
        glTranslatef(0, 1.2, 0)
        glRotatef(90, 0, 0, -1)
        DrawLongFace()

        glPopMatrix()

    def getTexID(self):
        return self._texID



