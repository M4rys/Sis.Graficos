import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from mesa import Mesa
from cord import Cord
from cadeira import Cadeira
from cafe import Cafe
from objetos import *

from functions import *

from functions import Rotate, Translate
def gera_cafe_cultural(cadeira, mesa, cafe):
    cafe.cria_cafe((4,6,4), (0,0,3))
    mesa.cria_mesa((1,1,1),(10,7,0))
    cadeira.cria_cadeira((1,1,1), (10,5,0))
    Rotate(-90, 0, 0, 1)
    cadeira.cria_cadeira((1,1,1), (-7,8,0))
    Rotate(180, 0, 0, 1)
    cadeira.cria_cadeira((1,1,1), (7,-12,0))
    Rotate(90, 0, 0, 1)
    cadeira.cria_cadeira((1,1,1), (-10,-9,0))
    Rotate(90, 0, 0, 1)

    mesa.cria_mesa((1,1,1),(-18,6,0))
    cadeira.cria_cadeira((1,1,1), (-18,4,0))
    Rotate(-90, 0, 0, 1)
    cadeira.cria_cadeira((1,1,1), (-6,-20,0))
    Rotate(180, 0, 0, 1)
    cadeira.cria_cadeira((1,1,1), (6,16,0))
    Rotate(90, 0, 0, 1)
    cadeira.cria_cadeira((1,1,1), (18,-8,0))
    
    mesa.cria_mesa((1,1,1),(19,5,0))
    cadeira.cria_cadeira((1,1,1), (19,3,0))
    Rotate(-90, 0, 0, 1)
    cadeira.cria_cadeira((1,1,1), (-5,17,0))
    Rotate(180, 0, 0, 1)
    cadeira.cria_cadeira((1,1,1), (5,-21,0))
    Rotate(90, 0, 0, 1)
    cadeira.cria_cadeira((1,1,1), (-19,-7,0))
def main():
    pg.init()
    display = (1680, 1050)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)
    glMatrixMode(GL_PROJECTION)

    gluPerspective(45, (display[0]/display[1]), 0.1, 100.0)
    #glOrtho(-10, 10, -10, 10, 1.5, 100)

    glMatrixMode(GL_MODELVIEW)
    modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    button_down = False

    mesa = Mesa()
    cafe = Cafe()
    cadeira = Cadeira()
    cl = Cilindro()
    cone = Cone(m_base=8, altura=6)

    vez_de = "na"

    Translate(0.0, 0.0, -5)  
    while True:
        glPushMatrix()
        glLoadIdentity()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 4:
                    Translate(0.0, 0.0, 0.5) 
                if event.button == 5:
                    Translate(0.0, 0.0, -0.5)
            keys =pg.key.get_pressed()
            if keys[K_s]:
                Translate(0.0, 0.25, 0.0)
            if keys[K_d]:
                Translate(-0.25, 0.0, 0.0)
            if keys[K_w]:
                Translate(0.0, -0.25, 0.0)
            if keys[K_a]:
                Translate(0.25, 0.0, 0.0)
            if event.type == pg.MOUSEMOTION:
                if button_down == True:
                    Rotate(event.rel[0]/2, 1, 0, 0)
                    Rotate(-event.rel[1]/2, 0, 1, 0)

                #     if event.rel[0] != 0 and ("x" in vez_de or vez_de == "na"):
                #         Rotate(event.rel[0]/2, 1, 0, 0)
                #         vez_de = "x"
                    
                #     if event.rel[1] != 0 and ("y" in vez_de or vez_de == "na"):
                #         Rotate(-event.rel[1]/2, 0, 1, 0)
                #         vez_de = "y"
                # else:
                #     vez_de = "na"
        
        for event in pg.mouse.get_pressed():
            if pg.mouse.get_pressed()[0] == 1:
                button_down = True
            elif pg.mouse.get_pressed()[0] == 0:
                button_down = False

        

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glMultMatrixf(modelMatrix)
        modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        glLoadIdentity()
        Translate(0, 0, -5)
        glMultMatrixf(modelMatrix)

        #Scale(10, 0, 0)
        gera_cafe_cultural(cadeira=cadeira, cafe=cafe, mesa=mesa)

        glPushMatrix()

        Scale(3, 3, 2)
        Translate(0, 0, 6.8)
        cone.draw()

        glPopMatrix()
        
        #wireCube(cubeEdges, cubeVertices)
        glPopMatrix()
        pg.display.flip()
        pg.time.wait(10)

if __name__ == "__main__":
    main()