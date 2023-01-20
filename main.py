import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from mesa import Mesa
from cadeira import Cadeira


def main():
    pg.init()
    display = (1680, 1050)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)
    glMatrixMode(GL_PROJECTION)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)  
    modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    button_down = False
    mesa = Mesa()
    cadeira = Cadeira()

    glTranslatef(0.0, 0.0, -5)  
    while True:
        glPushMatrix()
        glLoadIdentity()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0.0, 0.0, 0.5) 
                if event.button == 5:
                    glTranslatef(0.0, 0.0, -0.5)
            keys =pg.key.get_pressed()
            if keys[K_w]:
                glTranslatef(0.0, 0.5, 0.0)
            if keys[K_a]:
                glTranslatef(-0.5, 0.0, 0.0)
            if keys[K_s]:
                glTranslatef(0.0, -0.5, 0.0)
            if keys[K_d]:
                glTranslatef(0.5, 0.0, 0.0)
            if event.type == pg.MOUSEMOTION:
                if button_down == True:
                    glRotatef(event.rel[1], 1, 0, 0)
                    glRotatef(event.rel[0], 0, 1, 0)
        
        for event in pg.mouse.get_pressed():
            if pg.mouse.get_pressed()[0] == 1:
                button_down = True
            elif pg.mouse.get_pressed()[0] == 0:
                button_down = False

        

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glMultMatrixf(modelMatrix)
        modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        glLoadIdentity()
        glTranslatef(0, 0, -5)
        glMultMatrixf(modelMatrix)
        #tampo da mesa
        mesa.cria_mesa((1,1,1),(0,2,0))
        cadeira.cria_cadeira((1,1,1), (0,0,0))
 
        #wireCube(cubeEdges, cubeVertices)
        glPopMatrix()
        pg.display.flip()
        pg.time.wait(10)

if __name__ == "__main__":
    main()