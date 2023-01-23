from OpenGL.GL import *
import math

from functions import Rotate, Translate

class Cilindro:
    def __init__(self, n_pontos=30, altura=10):
        self.n_pts = n_pontos
        self.altura = altura

    def draw(self):
        pontos_c1 = []
        pontos_c2 = []

        glBegin(GL_POLYGON)

        for i in range(self.n_pts):
            angle = 2 * math.pi * i / self.n_pts
            
            vet = math.cos(angle), math.sin(angle), -self.altura//2

            pontos_c1.append(vet)

            glVertex3f(*vet)

        glEnd()

        glBegin(GL_POLYGON)

        for i in range(self.n_pts):
            angle = 2 * math.pi * i / self.n_pts
            
            vet = math.cos(angle), math.sin(angle), self.altura//2

            pontos_c2.append(vet)

            glVertex3f(*vet)

        glEnd()

        pontos_c1.append(pontos_c1[0])
        pontos_c2.append(pontos_c2[0])

        i = 1

        while i < len(pontos_c1):

            glBegin(GL_QUADS)

            glVertex3f(*pontos_c1[i-1])
            glVertex3f(*pontos_c1[i])
            glVertex3f(*pontos_c2[i])
            glVertex3f(*pontos_c2[i-1])

            glEnd()

            i += 1

        #exit()

        # glPushMatrix()

        # glColor3f(0.29, 0.21, 0.12)

        # Rotate(45, 0, 1, 0)
        # Translate(10, 0, 0)

        # glBegin(GL_QUADS)

        # for cubeQuad in self.cuboFaces:
        #     for cubeVertex in cubeQuad:
        #         glVertex3fv(self.caixa[cubeVertex])
                
        # glEnd()

        # glPopMatrix()

class Cone:
    def __init__(self, n_pontos=30, altura=10, m_base=1):
        self.n_pts = n_pontos
        self.altura = altura
        self.m_base = m_base

    def draw(self):
        pontos_c1 = []
        pontos_c2 = []

        glBegin(GL_POLYGON)

        for i in range(self.n_pts):
            angle = 2 * math.pi * i / self.n_pts
            
            vet = math.cos(angle) * self.m_base, math.sin(angle) * self.m_base, -self.altura//2

            pontos_c1.append(vet)

            glVertex3f(*vet)

        glEnd()

        glBegin(GL_POLYGON)

        for i in range(self.n_pts):
            angle = 2 * math.pi * i / self.n_pts
            
            vet = math.cos(angle) * 0.05, math.sin(angle) * 0.05, self.altura//2

            pontos_c2.append(vet)

            glVertex3f(*vet)

        glEnd()

        pontos_c1.append(pontos_c1[0])
        pontos_c2.append(pontos_c2[0])

        i = 1

        while i < len(pontos_c1):

            glBegin(GL_QUADS)

            glVertex3f(*pontos_c1[i-1])
            glVertex3f(*pontos_c1[i])
            glVertex3f(*pontos_c2[i])
            glVertex3f(*pontos_c2[i-1])

            glEnd()

            i += 1