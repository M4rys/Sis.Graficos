
from OpenGL.GL import *

class Cord():
    def __init__(self) -> None:
        self.cuboFaces = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))
        self.x = ((100,0.5,0.5),(100,0.5,-0.5),(100,-0.5,-0.5),(100,-0.5,0.5),(-100,0.5,0.5),(-100,-0.5,-0.5),(-100,-0.5,0.5),(-100,0.5,-0.5))
        self.y = ((0.5,100,0.5),(0.5,100,-0.5),(0.5,-100,-0.5),(0.5,-100,0.5),(-0.5,100,0.5),(-0.5,-100,-0.5),(-0.5,-100,0.5),(-0.5,100,-0.5))
        self.z = ((0.5,0.5,100),(0.5,0.5,-100),(100,-0.5,-100),(0.5,-0.5,100),(-0.5,0.5,100),(-0.5,-0.5,-100),(-0.5,-0.5,100),(-0.5,0.5,-100))

    def cria_cords(self, prop, pos) :
        partes = []
        partes.append(self.x) 
        partes.append(self.y)
        partes.append(self.z) 
        axisList = []
        new_partes = []

        for parte in partes:
            for ponto in parte:
                x = ponto[0] * prop[0] + pos[0]
                y = ponto[1] * prop[1] + pos[1]
                z = ponto[2] * prop[2] + pos[2]
                axisList.append((x, y, z))
            new_partes.append((axisList[0], axisList[1], axisList[2]))
            axisList = []

        


    def mostra_crods(self):

        glColor3f(0.29, 0.21, 0.12)
        solidCube(self.cuboFaces, self.x)
        solidCube(self.cuboFaces, self.y)
        solidCube(self.cuboFaces, self.z)


def solidCube(cubeQuads, cubeVertices):
    
    glBegin(GL_QUADS)
    for cubeQuad in cubeQuads:
        for cubeVertex in cubeQuad:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()
