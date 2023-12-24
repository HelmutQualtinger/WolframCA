import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective


def drawChessboard():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                glColor3f(1.0, 1.0, 1.0)  # Weiß
            else:
                glColor3f(0.0, 0.0, 0.0)  # Schwarz
            glBegin(GL_QUADS)
            glVertex3f(i * 50.0, 0.0, j * 50.0)
            glVertex3f((i + 1) * 50.0, 0.0, j * 50.0)
            glVertex3f((i + 1) * 50.0, 0.0, (j + 1) * 50.0)
            glVertex3f(i * 50.0, 0.0, (j + 1) * 50.0)
            glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 500.0)
    glTranslatef(-200.0, -50.0, -400.0)  # Kamera-Position

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)  # Animation: 3 Grad Drehung um die Achsen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        drawChessboard()
        pygame.display.flip()
        pygame.time.wait(10)  # kleine Pause


if __name__ == "__main__":
    main()
