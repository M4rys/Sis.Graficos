import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from functions import *

from cafeCultural import CafeCultural

def main():
    pg.init()

    display = (1680, 1050)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    glShadeModel(GL_SMOOTH) #tonalização

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # projeções

    #Ortogonal(-10, 10, -10, 10, 1.5, 100)
    Perspectiva(-1.5, 1.5, -1.5, 1.5, 1, 50)
    #gluPerspective(45, (display[0]/display[1]), 0.1, 100.0)
    #glOrtho(-10, 10, -10, 10, 1.5, 100)

    #objetos

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    #configurar ambiente

    Scale(-1, 0, 0)
    Translate(0, 0, -5)
    Rotate(-90, 1, 0, 0)
    Rotate(-90, 0, 1, 0)

    glLight(GL_LIGHT0, GL_POSITION,  (500, 500, 500, 1)) # point light from the left, top, front
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.8, 0.8, 0.8, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.2, 0.2, 0.2, 1))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1, 0.7, 0, 1))

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.1, 0.1, 0.1, 1]) #refexão

    glEnable(GL_DEPTH_TEST)

    #salvar matriz

    modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    button_down = False

    #instanciar café

    cafe = CafeCultural()

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

            if keys[K_w]:
                Translate(0.0, 0.25, 0.0)
            if keys[K_d]:
                Translate(-0.25, 0.0, 0.0)
            if keys[K_s]:
                Translate(0.0, -0.25, 0.0)
            if keys[K_a]:
                Translate(0.25, 0.0, 0.0)

            if event.type == pg.MOUSEMOTION:
                if button_down == True:
                    Rotate(event.rel[0]/2, 1, 0, 0)
                    Rotate(event.rel[1]/2, 0, 1, 0)
        
        for event in pg.mouse.get_pressed():
            if pg.mouse.get_pressed()[0] == 1:
                button_down = True
            elif pg.mouse.get_pressed()[0] == 0:
                button_down = False


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMultMatrixf(modelMatrix)
        modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        glLoadIdentity()

        #translate "camera"
        Translate(0, 0, -5)

        glMultMatrixf(modelMatrix)

        #Objetos do mapa

        cafe.gera_cafe_cultural()
        cafe.gera_colunas()
        cafe.gera_balanco()
        
        glPopMatrix()

        pg.display.flip()
        pg.time.wait(10)

if __name__ == "__main__":
    main()