from OpenGL.GL import *
import math

from functions import Normal

class Cilindro:
    def __init__(self, n_pontos=30, altura=10):
        self.n_pts = n_pontos
        self.altura = altura

    def draw(self):
        pontos_c1 = []
        pontos_c2 = []

        for i in range(self.n_pts):
            angle = 2 * math.pi * i / self.n_pts
            
            vet = math.cos(angle), math.sin(angle), -self.altura//2

            pontos_c1.append(vet)

        for i in range(self.n_pts):
            angle = 2 * math.pi * i / self.n_pts
            
            vet = math.cos(angle), math.sin(angle), self.altura//2

            pontos_c2.append(vet)

        glBegin(GL_POLYGON)

        Normal(pontos_c1[1], pontos_c1[0])

        for ponto in pontos_c1:
            glVertex3f(*ponto)

        glEnd()

        glBegin(GL_POLYGON)

        Normal(pontos_c2[0], pontos_c2[1])

        for ponto in pontos_c2:
            glVertex3f(*ponto)

        glEnd()

        pontos_c1.append(pontos_c1[0])
        pontos_c2.append(pontos_c2[0])

        i = 1

        while i < len(pontos_c1):

            glBegin(GL_QUADS)

            #glMaterialfv(GL_FRONT, GL_DIFFUSE, [0, 0, 0, 0])

            Normal(pontos_c1[i-1], pontos_c1[i])
            glVertex3f(*pontos_c1[i-1])
            glVertex3f(*pontos_c1[i])
            glVertex3f(*pontos_c2[i])
            glVertex3f(*pontos_c2[i-1])

            glEnd()

            i += 1

class Cone:
    def __init__(self, n_pontos=30, altura=10, m_base=1):
        self.n_pts = n_pontos
        self.altura = altura
        self.m_base = m_base

    def draw(self):
        pontos_c1 = []
        pontos_c2 = []

        for i in range(self.n_pts):
            angle = 2 * math.pi * i / self.n_pts
            
            vet = math.cos(angle) * self.m_base, math.sin(angle) * self.m_base, -self.altura//2

            pontos_c1.append(vet)

        for i in range(self.n_pts):
            angle = 2 * math.pi * i / self.n_pts
            
            vet = math.cos(angle) * 0.05, math.sin(angle) * 0.05, self.altura//2

            pontos_c2.append(vet)


        glBegin(GL_POLYGON)

        Normal(pontos_c1[1], pontos_c1[0])

        for ponto in pontos_c1:
            glVertex3f(*ponto)

        glEnd()

        glBegin(GL_POLYGON)

        Normal(pontos_c2[0], pontos_c2[1])

        for ponto in pontos_c2:
            glVertex3f(*ponto)

        glEnd()

        pontos_c1.append(pontos_c1[0])
        pontos_c2.append(pontos_c2[0])

        i = 1

        while i < len(pontos_c1):

            glBegin(GL_QUADS)

            Normal(pontos_c1[i-1], pontos_c1[i])
            glVertex3f(*pontos_c1[i-1])
            glVertex3f(*pontos_c1[i])
            glVertex3f(*pontos_c2[i])
            glVertex3f(*pontos_c2[i-1])

            glEnd()

            i += 1