from OpenGL.GL import *


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
        
        self.chao = ((5,5,-1),(5,5,-1.1),(5,-5,-1.1),(-5,-5,-1),(-5,5,-1),(-5,-5,-1.1),(-5,-5,-1),(-5,5,-1.1))
        


    def cria_cafe(self, prop, pos) :
        partes = []
        partes.append(self.parede1) 
        partes.append(self.parede2) 
        partes.append(self.parede3) 
        partes.append(self.parede4) 
        partes.append(self.paredeLE)
        partes.append(self.paredeT)
        partes.append(self.paredeLD1)
        partes.append(self.paredeLD2)
        partes.append(self.paredeLD3)
        partes.append(self.janela1)
        partes.append(self.janela2)
        partes.append(self.janela3)
        partes.append(self.janela4)
        partes.append(self.porta1)
        partes.append(self.porta2)
        partes.append(self.porta3)
        partes.append(self.chao)
        
                    
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

        self.mostra_mesa(new_partes[0], new_partes[1], new_partes[2],new_partes[3], new_partes[4], new_partes[5], 
                    new_partes[6], new_partes[7], new_partes[8], new_partes[9], new_partes[10], new_partes[11], new_partes[12],
                    new_partes[13], new_partes[14], new_partes[15], new_partes[16])
    
    def mostra_mesa(self, par1, par2, par3, par4, par5, par6, par7, par8, par9, par10, par11, par12, par13, par14, par15, par16, chao):

        glColor3f(0.5, 0.5, 0.5)
        solidCube(self.cuboFaces, chao)
        glColor3f(0.89, 0.89, 0.89)
        solidCube(self.cuboFaces, par6)
        solidCube(self.cuboFaces, par5)
        solidCube(self.cuboFaces, par7)
        solidCube(self.cuboFaces, par8)
        solidCube(self.cuboFaces, par9)
       
        glColor3f(0.24, 0.30, 0.30)
        solidCube(self.cuboFaces, par10)
        glColor3f(0.89, 0.89, 0.89)
        glColor3f(0.24, 0.30, 0.30)
        solidCube(self.cuboFaces, par14)
        glColor3f(0.89, 0.89, 0.89)
        solidCube(self.cuboFaces, par1)
        solidCube(self.cuboFaces, par2)
        solidCube(self.cuboFaces, par3)
        solidCube(self.cuboFaces, par4)
        solidCube(self.cuboFaces, par11)
        solidCube(self.cuboFaces, par12)
        solidCube(self.cuboFaces, par13)
        solidCube(self.cuboFaces, par15)
        solidCube(self.cuboFaces, par16)


def solidCube(cubeQuads, cubeVertices):
        
        glBegin(GL_QUADS)
        for cubeQuad in cubeQuads:
            for cubeVertex in cubeQuad:
                glVertex3fv(cubeVertices[cubeVertex])
        glEnd()


