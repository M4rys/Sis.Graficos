from OpenGL.GL import *

from functions import Rotate, Translate

class Cilindro:
    def __init__(self):
        self.cuboFaces = [(0, 3, 6, 4), (2, 5, 6, 3), (1, 2, 5, 7), (1, 0, 4, 7), (7, 4, 6, 5), (2, 3, 0, 1)]

        self.caixa = [(1, 1, 5), (1, 1, -5), (1, -1, -5), (1, -1, 5), (-1, 1, 5), (-1, -1, -5), (-1, -1, 5), (-1, 1, -5)]

    def draw(self):
        glPushMatrix()

        glColor3f(0.29, 0.21, 0.12)

        Rotate(45, 0, 1, 0)
        Translate(10, 0, 0)

        glBegin(GL_QUADS)

        for cubeQuad in self.cuboFaces:
            for cubeVertex in cubeQuad:
                glVertex3fv(self.caixa[cubeVertex])
                
        glEnd()

        glPopMatrix()