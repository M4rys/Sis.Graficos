from mesa import Mesa
from cadeira import Cadeira
from cafe import Cafe
from objetos import Cone

from functions import *

class CafeCultural:
    def __init__(self):
        self.mesa = Mesa()
        self.cadeira = Cadeira()
        self.cafe = Cafe()

        self.telhado = Cone(m_base=8, altura=6)

    def draw(self):
        self.cafe.cria_cafe((4,6,4), (0,0,3))
        self.mesa.cria_mesa((1,1,1),(10,7,0))
        self.cadeira.cria_cadeira((1,1,1), (10,5,0))

        Rotate(-90, 0, 0, 1)
        self.cadeira.cria_cadeira((1,1,1), (-7,8,0))

        Rotate(180, 0, 0, 1)
        self.cadeira.cria_cadeira((1,1,1), (7,-12,0))

        Rotate(90, 0, 0, 1)
        self.cadeira.cria_cadeira((1,1,1), (-10,-9,0))

        Rotate(90, 0, 0, 1)
        self.mesa.cria_mesa((1,1,1),(-18,6,0))
        self.cadeira.cria_cadeira((1,1,1), (-18,4,0))

        Rotate(-90, 0, 0, 1)
        self.cadeira.cria_cadeira((1,1,1), (-6,-20,0))

        Rotate(180, 0, 0, 1)
        self.cadeira.cria_cadeira((1,1,1), (6,16,0))

        Rotate(90, 0, 0, 1)
        self.cadeira.cria_cadeira((1,1,1), (18,-8,0))
        
        self.mesa.cria_mesa((1,1,1),(19,5,0))
        self.cadeira.cria_cadeira((1,1,1), (19,3,0))

        Rotate(-90, 0, 0, 1)
        self.cadeira.cria_cadeira((1,1,1), (-5,17,0))

        Rotate(180, 0, 0, 1)
        self.cadeira.cria_cadeira((1,1,1), (5,-21,0))

        Rotate(90, 0, 0, 1)
        self.cadeira.cria_cadeira((1,1,1), (-19,-7,0))

        #telhado

        glPushMatrix()

        Scale(3, 3, 2)
        Translate(0, 0, 6.8)
        self.telhado.draw()

        glPopMatrix()