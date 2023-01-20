from OpenGL.GL import *


class Mesa():
    def __init__(self) -> None:
        self.cuboFaces = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))
        self.tmesa = ((1,1,1),(1,1,0.97),(1,-1,0.97),(1,-1,1),(-1,1,1),(-1,-1,0.97),(-1,-1,1),(-1,1,0.97))

        self.supD = ((0.96,0.65,0.97),(0.96,0.65,0.9),(0.96,-0.65,0.9),(0.96,-0.65,0.97),(0.9,0.65,0.97),(0.9,-0.65,0.9),(0.9,-0.65,0.97),(0.9,0.65,0.9))
        self.supE = ((-0.96,0.65,0.97),(-0.96,0.65,0.9),(-0.96,-0.65,0.9),(-0.96,-0.65,0.97),(-0.9,0.65,0.97),(-0.9,-0.65,0.9),(-0.9,-0.65,0.97),(-0.9,0.65,0.9))

        self.pernaED = ((0.96,-0.55,0.9),(0.96,0.75,-1),(0.96,0.65,-1),(0.96,-0.65,0.9),(0.9,-0.55,0.9),(0.9,0.65,-1),(0.9,-0.65,0.9),(0.9,0.75,-1))
        self.pernaEE = ((0.96,0.55,0.9),(0.96,-0.75,-1),(0.96,-0.65,-1),(0.96,0.65,0.9),(0.9,0.55,0.9),(0.9,-0.65,-1),(0.9,0.65,0.9),(0.9,-0.75,-1))

        self.pernaDD = ((-0.96,-0.55,0.9),(-0.96,0.75,-1),(-0.96,0.65,-1),(-0.96,-0.65,0.9),(-0.9,-0.55,0.9),(-0.9,0.65,-1),(-0.9,-0.65,0.9),(-0.9,0.75,-1))
        self.pernaDE = ((-0.96,0.55,0.9),(-0.96,-0.75,-1),(-0.96,-0.65,-1),(-0.96,0.65,0.9),(-0.9,0.55,0.9),(-0.9,-0.65,-1),(-0.9,0.65,0.9),(-0.9,-0.75,-1))

        self.juntapernaF = ((-0.96,-0.22,-0.3),(-0.96,-0.51,-0.7),(-0.96,-0.61,-0.7),(-0.96,-0.32,-0.3),(0.9,-0.22,-0.3),(0.9,-0.61,-0.7),(0.9,-0.32,-0.3),(0.9,-0.51,-0.7))
        self.juntapernaT = ((-0.96,0.22,-0.3),(-0.96,0.51,-0.7),(-0.96,0.61,-0.7),(-0.96,0.32,-0.3),(0.9,0.22,-0.3),(0.9,0.61,-0.7),(0.9,0.32,-0.3),(0.9,0.51,-0.7))


    def cria_mesa(self, prop, pos) :
        partes = []
        partes.append(self.tmesa) 
        partes.append(self.supD)
        partes.append(self.supE) 
        partes.append(self.pernaED)
        partes.append(self.pernaEE)
        partes.append(self.pernaDD)
        partes.append(self.pernaDE)
        partes.append(self.juntapernaF)
        partes.append(self.juntapernaT)
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

        self.mostra_mesa(new_partes[0], new_partes[1], new_partes[2], new_partes[3], new_partes[4], new_partes[5], new_partes[6], new_partes[7], new_partes[8])


    def mostra_mesa(self, tampa, suporte1, suporte2, peE1, peD1, peE2, pD2, jpF, jpT):

        glColor3f(0.29, 0.21, 0.12)
        solidCube(self.cuboFaces, tampa)
        solidCube(self.cuboFaces, suporte1)
        solidCube(self.cuboFaces, suporte2)
        solidCube(self.cuboFaces, peE1)
        solidCube(self.cuboFaces, peD1)
        solidCube(self.cuboFaces, peE2)
        solidCube(self.cuboFaces, pD2)
        solidCube(self.cuboFaces, jpF)
        solidCube(self.cuboFaces, jpT)


def solidCube(cubeQuads, cubeVertices):
    
    glBegin(GL_QUADS)
    for cubeQuad in cubeQuads:
        for cubeVertex in cubeQuad:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()
