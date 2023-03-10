from OpenGL.GL import *
from functions import *
from objetos import Cilindro
from functions import Normal, solidCube

class Cafe():

    def __init__(self) -> None:
        self.cuboFaces = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))
        self.parede1 = ((0.05,-1,0.8),(0.05,-1,-1),(0.05,-1.5,-1),(0.05,-1.5,0.8),(-0.05,-1,0.8),(-0.05,-1.5,-1),(-0.05,-1.5,0.8),(-0.05,-1,-1))
        self.parede2 = ((0.05,1.5,0.8),(0.05,1.5,-1),(0.05,0.25,-1),(0.05,0.25,0.8),(-0.05,1.5,0.8),(-0.05,0.25,-1),(-0.05,0.25,0.8),(-0.05,1.5,-1))
        self.parede3 = ((0.05,0.25,0),(0.05,0.25,-1),(0.05,-1,-1),(0.05,-1,0),(-0.05,0.25,0),(-0.05,-1,-1),(-0.05,-1,0),(-0.05,0.25,-1))
        self.parede4 = ((0.05,1.5,1.2),(0.05,1.5,0.8),(0.05,-1.5,0.8),(0.05,-1.5,1.2),(-0.05,1.5,1.2),(-0.05,-1.5,0.8),(-0.05,-1.5,1.2),(-0.05,1.5,0.8))
        
        self.paredeLE = ((0.05,-1.4,1.2),(0.05,-1.4,-1),(0.05,-1.5,-1),(0.05,-1.5,1.2),(-2.35,-1.4,1.2),(-2.35,-1.5,-1),(-2.35,-1.5,1.2),(-2.35,-1.4,-1))
        
        self.paredeT = ((-2.35,1.5,1.2),(-2.35,1.5,-1),(-2.35,-1.5,-1),(-2.35,-1.5,1.2),(-2.45,1.5,1.2),(-2.45,-1.5,-1),(-2.45,-1.5,1.2),(-2.45,1.5,-1))
        
        self.paredeLD1 = ((-1,1.4,1.2),(-1,1.4,-1),(-1,1.5,-1),(-1,1.5,1.2),(-2.35,1.4,1.2),(-2.35,1.5,-1),(-2.35,1.5,1.2),(-2.35,1.4,-1))
        self.paredeLD2 = ((0.05,1.4,1.2),(0.05,1.4,-1),(0.05,1.5,-1),(0.05,1.5,1.2),(-0.2,1.4,1.2),(-0.2,1.5,-1),(-0.2,1.5,1.2),(-0.2,1.4,-1))
        self.paredeLD3 = ((0.05,1.4,1.2),(0.05,1.4,0.8),(0.05,1.5,0.8),(0.05,1.5,1.2),(-1,1.4,1.2),(-1,1.5,0.8),(-1,1.5,1.2),(-1,1.4,0.8))

        self.janela1 = ((0.01,0.25,0.8),(0.01,0.25,0),(0.01,-1,0),(0.01,-1,0.8),(-0.01,0.25,0.8),(-0.01,-1,0),(-0.01,-1,0.8),(-0.01,0.25,0))


        self.janela2 = ((0.05,0.25,0.41),(0.05,0.25,0.39),(0.05,-1,0.39),(0.05,-1,0.41),(-0.05,0.25,0.41),(-0.05,-1,0.39),(-0.05,-1,0.42),(-0.05,0.25,0.39))
        self.janela3 = ((0.05,0.01,0.8),(0.05,0.01,0),(0.05,-0.01,0),(0.05,-0.01,0.8),(-0.05,0.01,0.8),(-0.05,-0.01,0),(-0.05,-0.01,0.8),(-0.05,0.01,0))
        self.janela4 = ((0.05,-0.76,0.8),(0.05,-0.76,0),(0.05,-0.74,0),(0.05,-0.74,0.8),(-0.05,-0.76,0.8),(-0.05,-0.74,0),(-0.05,-0.74,0.8),(-0.05,-0.76,0))
        #aqui --------------------------------------------------------------------

        self.porta1 = ((-0.2,1.42,0.8),(-0.2,1.42,-1),(-0.2,1.43,-1),(-0.2,1.43,0.8),(-1,1.42,0.8),(-1,1.43,-1),(-1,1.43,0.8),(-1,1.42,-1))
        self.porta2 = ((-0.2,1.41,-0.05),(-0.2,1.41,-0.15),(-0.2,1.46,-0.15),(-0.2,1.46,-0.05),(-1,1.41,-0.05),(-1,1.46,-0.15),(-1,1.46,-0.05),(-1,1.41,-0.15))
        self.porta3 = ((-0.2,1.41,-0.9),(-0.2,1.41,-1),(-0.2,1.46,-1),(-0.2,1.46,-0.9),(-1,1.41,-0.9),(-1,1.46,-1),(-1,1.46,-0.9),(-1,1.41,-1))
        
        self.chao = ((7,7,-1.1),(7,7,-1.2),(7,-7,-1.2),(-7,-7,-1.1),(-7,7,-1.1),(-7,-7,-1.2),(-7,-7,-1.1),(-7, 7,-1.2))
        


    def cria_cafe(self, cl) :
        partes = []
        partes.append(self.paredeLE)
        partes.append(self.paredeT)
        partes.append(self.paredeLD1) 
        partes.append(self.paredeLD2) 
        partes.append(self.paredeLD3) 
        partes.append(self.porta1)
        partes.append(self.janela1)
        partes.append(self.parede1) 
        partes.append(self.parede2) 
        partes.append(self.parede3) 
        partes.append(self.parede4) 
        partes.append(self.janela2)
        partes.append(self.janela3)
        partes.append(self.janela4)
        partes.append(self.porta2)
        partes.append(self.porta3)
        
        
        glPushMatrix()

        glColor3f(0, 0.5, 0)

        solidCube(self.cuboFaces, self.chao, top=True)

        Translate(0, 1, -1)
        Scale(4, 4, 0.01)
        glColor3f(0.2, 0.2, 0.2)

        cl.draw()

        glPopMatrix()

        for parte in partes:
            if parte == self.janela1 or parte == self.porta1:
                glColor3f(0.24, 0.30, 0.30)
                
            else:
                glColor3f(0.89, 0.89, 0.89)
            solidCube(self.cuboFaces, parte)




