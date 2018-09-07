# first we gonna build the 2d ebviroment then we switch to 3d
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #main loop





        #end of display functions

        pygame.display.flip()
        pygame.time.wait(10)


main()
