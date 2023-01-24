from OpenGL.GL import *
from functions import Normal, solidCube

class Balanco():

    def __init__(self) -> None:

        self.cuboFaces = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))
        self.banco = ((0.3,0.5,0.25),(0.3,0.5,0.15),(0.3,-0.5,0.15),(0.3,-0.5,0.25),(-0.3,0.5,0.25),(-0.3,-0.5,0.15),(-0.3,-0.5,0.25),(-0.3,0.5,0.15))
        self.cordaD = ((0.05,0.5,6.05),(0.05,0.5,0.23),(0.05,0.6,0.23),(0.05,0.6,6.05),(-0.05,0.5,6.05),(-0.05,0.6,0.23),(-0.05,0.6,6.05),(-0.05,0.5,0.23))
        self.cordaE = ((0.05,-0.5,6.05),(0.05,-0.5,0.23),(0.05,-0.6,0.23),(0.05,-0.6,6.05),(-0.05,-0.5,6.05),(-0.05,-0.6,0.23),(-0.05,-0.6,6.05),(-0.05,-0.5,0.23))

    def cria_balanco(self):
        partes = []
        partes.append(self.banco) 
        partes.append(self.cordaD)
        partes.append(self.cordaE) 
        for parte in partes:
            if parte == self.banco:
                glColor3f(0.31, 0.25, 0.16)
            else:
                glColor3f(0.9, 0.9, 0.9)
            solidCube(self.cuboFaces, parte)

