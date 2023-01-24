from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from mesa import Mesa
from cadeira import Cadeira
from cafe import Cafe
from balanco import Balanco
from objetos import *

from functions import *


class CafeCultural():
    def __init__(self) -> None:
        
        self.mesa = Mesa()
        self.cafe = Cafe()
        self.cadeira = Cadeira()
        self.cl = Cilindro(altura=8) #cilindro central
        self.chao = Cilindro(n_pontos=10)
        self.cone = Cone(m_base=8, altura=6)
        self.ba = Balanco()

    def gera_cafe_cultural(self):
        glPushMatrix()
        Translate(0,4,2)
        Scale(4,4,3)
        self.cafe.cria_cafe(self.chao)
        glPopMatrix()

        glPushMatrix()
        Translate(0,9,3)
        Scale(2.5,2.5,0)
        self.cl.draw()
        glPopMatrix()

        glPushMatrix()
        Translate(10,7,0)
        self.mesa.cria_mesa((1,1,1),(10,7,0))
        glPopMatrix()

        glPushMatrix()
        Translate(10,5,0)
        self.cadeira.cria_cadeira((1,1,1), (10,5,0))
        Rotate(-90, 0, 0, 1)
        Translate(-2,-2,0)
        self.cadeira.cria_cadeira((1,1,1), (-7,8,0))
        Rotate(180, 0, 0, 1)
        Translate(0,-4,0)
        self.cadeira.cria_cadeira((1,1,1), (7,-12,0))
        Rotate(90, 0, 0, 1)
        Translate(2,-2,0)
        self.cadeira.cria_cadeira((1,1,1), (-10,-9,0))
        glPopMatrix()

        glPushMatrix()
        Translate(6,16,0)
        self.mesa.cria_mesa((1,1,1),(6,16,0))
        glPopMatrix()
        glPushMatrix()
        Translate(6,14,0)
        self.cadeira.cria_cadeira((1,1,1), (-18,4,0))
        Rotate(-90, 0, 0, 1)
        Translate(-2,-2,0)
        self.cadeira.cria_cadeira((1,1,1), (-6,-20,0))
        Rotate(180, 0, 0, 1)
        Translate(0,-4,0)
        self.cadeira.cria_cadeira((1,1,1), (6,16,0))
        Rotate(90, 0, 0, 1)
        Translate(2,-2,0)
        self.cadeira.cria_cadeira((1,1,1), (18,-8,0))
        glPopMatrix()
        
        glPushMatrix()
        Translate(-5,18,0)
        self.mesa.cria_mesa((1,1,1),(6,16,0))
        glPopMatrix()
        # mesa.cria_mesa((1,1,1),(19,5,0))
        glPushMatrix()
        Translate(-5,16,0)
        self.cadeira.cria_cadeira((1,1,1), (-18,4,0))
        Rotate(-90, 0, 0, 1)
        Translate(-2,-2,0)
        self.cadeira.cria_cadeira((1,1,1), (-6,-20,0))
        Rotate(180, 0, 0, 1)
        Translate(0,-4,0)
        self.cadeira.cria_cadeira((1,1,1), (6,16,0))
        Rotate(90, 0, 0, 1)
        Translate(2,-2,0)
        self.cadeira.cria_cadeira((1,1,1), (18,-8,0))
        glPopMatrix()

    def gera_colunas(self):
        
        glPushMatrix()

        glColor3f(0.41, 0.35, 0.26)
        Scale(2, 2, 2)
        Translate(0, 4, 5.8)
        self.cone.draw()
        glPopMatrix()

        glPushMatrix()
        glColor3f(0.31, 0.25, 0.16)
        Scale(0.5, 0.5, 0.85)
        Translate(25, -2.5, 2.59)
        self.cl.draw()
        Translate(6, 19, 0)
        self.cl.draw()
        Translate(-6, 18, 0)
        self.cl.draw()
        Translate(-15, 11, 0)
        self.cl.draw()
        Translate(-20, 0, 0)
        self.cl.draw()
        Translate(-15, -11, 0)
        self.cl.draw()
        Translate(-6, -18, 0)
        self.cl.draw()
        Translate(6, -19, 0)
        self.cl.draw()
        Translate(15, -11, 0)
        self.cl.draw()
        Translate(20, 0, 0)
        self.cl.draw()

        glPopMatrix()

    def gera_balanco(self):
        glPushMatrix()
        Scale(2, 2, 0)
        Translate(7.25, 2, 0)
        Rotate(-15, 0, 0, 1)
        self.ba.cria_balanco()
        
        Translate(-1.25, 4, 0)
        Rotate(30, 0, 0, 1)
        self.ba.cria_balanco()
        Translate(-1.75, 4.5, 0)
        Rotate(40, 0, 0, 1)
        self.ba.cria_balanco()

        glPopMatrix()