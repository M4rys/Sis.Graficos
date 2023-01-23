from OpenGL.GL import *


class Cadeira():

    def __init__(self) -> None:
        self.cuboFaces = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))
        self.tmesa = ((0.6,0.7,0.2),(0.6,0.7,0.07),(0.6,-0.3,0.07),(0.6,-0.3,0.2),(-0.6,0.7,0.2),(-0.6,-0.3,0.07),(-0.6,-0.3,0.2),(-0.6,0.7,0.07))

        self.supD = ((0.6,0.75,0.07), (0.6,0.75,0.21), (0.6,-0.4,0.21), (0.6,-0.4,0.07), (0.65,0.75,0.07), (0.65,-0.4,0.21), (0.65,-0.4,0.07), (0.65,0.75,0.21))
        self.supE = ((-0.6,0.75,0.07),(-0.6,0.75,0.21),(-0.6,-0.4,0.21),(-0.6,-0.4,0.07),(-0.65,0.75,0.07),(-0.65,-0.4,0.21),(-0.65,-0.4,0.07),(-0.65,0.75,0.21))

        self.pernaED = ((0.65,-0.9,1.3),(0.65,0.75,-1),(0.65,0.65,-1),(0.65,-1,1.3),(0.71,-0.9,1.3),(0.71,0.65,-1),(0.71,-1,1.3),(0.71,0.75,-1))
        self.pernaEE = ((0.65,0.4,0.15),(0.65,-0.5,-1),(0.65,-0.4,-1),(0.65,0.5,0.15),(0.71,0.4,0.15),(0.71,-0.4,-1),(0.71,0.5,0.15),(0.71,-0.5,-1))
                        
        self.pernaDD = ((-0.65,-0.9,1.3),(-0.65,0.75,-1),(-0.65,0.65,-1),(-0.65,-1,1.3),(-0.71,-0.9,1.3),(-0.71,0.65,-1),(-0.71,-1,1.3),(-0.71,0.75,-1))
        self.pernaDE = ((-0.65,0.4,0.15),(-0.65,-0.5,-1),(-0.65,-0.4,-1),(-0.65,0.5,0.15),(-0.71,0.4,0.15),(-0.71,-0.4,-1),(-0.71,0.5,0.15),(-0.71,-0.5,-1))

        self.costas = ((-0.65,-0.84,1.23),(-0.65,-0.63,0.9),(-0.65,-0.73,0.9),(-0.65,-0.94,1.23),(0.65,-0.84,1.23),(0.65,-0.73,0.9),(0.65,-0.94,1.23),(0.65,-0.63,0.9))
        
        self.juntaTA= ((-0.65,-0.03,-0.5),(-0.65,-0.18,-0.6),(-0.65,-0.13,-0.6),(-0.65,-0.08,-0.5),(0.65,-0.03,-0.5),(0.65,-0.13,-0.6),(0.65,-0.08,-0.5),(0.65,-0.18,-0.6))
        self.juntaTB= ((-0.65,-0.17,-0.7),(-0.65,-0.33,-0.8),(-0.65,-0.27,-0.8),(-0.65,-0.23,-0.7),(0.65,-0.17,-0.7),(0.65,-0.27,-0.8),(0.65,-0.23,-0.7),(0.65,-0.33,-0.8))

        self.juntaFA= ((-0.65,0.30,-0.5),(-0.65,0.40,-0.6),(-0.65,0.45,-0.6),(-0.65,0.35,-0.5),(0.65,0.30,-0.5),(0.65,0.45,-0.6),(0.65,0.35,-0.5),(0.65,0.4,-0.6))
        self.juntaFB= ((-0.65,0.48,-0.7),(-0.65,0.53,-0.8),(-0.65,0.58,-0.8),(-0.65,0.43,-0.7),(0.65,0.48,-0.7),(0.65,0.58,-0.8),(0.65,0.43,-0.7),(0.65,0.53,-0.8))

    def cria_cadeira(self, prop, pos) :
        partes = []
        partes.append(self.tmesa) 
        partes.append(self.supD)
        partes.append(self.supE) 
        partes.append(self.pernaED)
        partes.append(self.pernaEE)
        partes.append(self.pernaDD)
        partes.append(self.pernaDE)
        partes.append(self.costas)
        partes.append(self.juntaTA)
        partes.append(self.juntaTB)
        partes.append(self.juntaFA)
        partes.append(self.juntaFB)
                    
        
        for parte in partes:
            
            glColor3f(0.29, 0.21, 0.12)
            solidCube(self.cuboFaces, parte)
    
def solidCube(cubeQuads, cubeVertices):
        
        glBegin(GL_QUADS)
        for cubeQuad in cubeQuads:
            for cubeVertex in cubeQuad:
                glVertex3fv(cubeVertices[cubeVertex])
        glEnd()