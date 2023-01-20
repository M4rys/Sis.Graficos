from OpenGL.GL import *


class Cadeira():

    def __init__(self) -> None:
        self.cuboFaces = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))
        self.tmesa = ((0.6,0.5,0.3),(0.6,0.5,0.17),(0.6,-0.5,0.17),(0.6,-0.5,0.3),(-0.6,0.5,0.3),(-0.6,-0.5,0.17),(-0.6,-0.5,0.3),(-0.6,0.5,0.17))

        self.supD = ((0.6,0.6,0.43),(0.6,0.6,0.24),(0.6,-0.6,0.24),(0.6,-0.6,0.43),(0.65,0.6,0.43),(0.65,-0.6,0.24),(0.65,-0.6,0.43),(0.65,0.6,0.4))
        self.supE = ((-0.6,0.6,0.53),(-0.6,0.6,0.34),(-0.6,-0.6,0.34),(-0.6,-0.6,0.53),(-0.65,0.6,0.53),(-0.65,-0.6,0.34),(-0.65,-0.6,0.53),(-0.65,0.6,0.34))

        self.pernaED = ((0.96,-0.55,1.1),(0.96,0.75,-1),(0.96,0.65,-1),(0.96,-0.65,1.1),(0.9,-0.55,1.1),(0.9,0.65,-1),(0.9,-0.65,1.1),(0.9,0.75,-1))
        


    def cria_cadeira(self, prop, pos) :
        partes = []
        partes.append(self.tmesa) 
        partes.append(self.supD)
        partes.append(self.supE) 
        partes.append(self.pernaED)

        axisList = []
        new_partes = []

        for parte in partes:
            for ponto in parte:
                x = ponto[0] * prop[0] + pos[0]
                y = ponto[1] * prop[1] + pos[1]
                z = ponto[2] * prop[2] + pos[2]
                axisList.append((x, y, z))
            new_partes.append((axisList[0], axisList[1], axisList[2], axisList[3], axisList[4], axisList[5], axisList[6], axisList[7]))
            axisList = []

        self.mostra_mesa(new_partes[0], new_partes[1], new_partes[2], new_partes[3])
    
    def mostra_mesa(self, tampa, suporte1, suporte2, peE1):

        glColor3f(0.29, 0.21, 0.12)
        solidCube(self.cuboFaces, tampa)
        glColor3f(0.89, 0.71, 0.12)
        solidCube(self.cuboFaces, suporte1)
        solidCube(self.cuboFaces, suporte2)
        solidCube(self.cuboFaces, peE1)
        #solidCube(self.cuboFaces, peD1)
        #solidCube(self.cuboFaces, peE2)
        #solidCube(self.cuboFaces, pD2)
        #solidCube(self.cuboFaces, jpF)
        #solidCube(self.cuboFaces, jpT)

def solidCube(cubeQuads, cubeVertices):
        
        glBegin(GL_QUADS)
        for cubeQuad in cubeQuads:
            for cubeVertex in cubeQuad:
                glVertex3fv(cubeVertices[cubeVertex])
        glEnd()