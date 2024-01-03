import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective


def drawChessboard():
    """
    Draws a chessboard using OpenGL.

    The chessboard consists of 15x15 squares, alternating between blue and white colors.

    Parameters:
    None

    Returns:
    None
    """
    for i in range(8):
        # Draw a row of squares
        for j in range(8):
            # Draw a square at position (i, j)
            pass  # Placeholder for drawing logic
        for j in range(8):
            if (i + j) % 2 == 0:
                glColor4f(1.0, 1.0, 1.0, 0.5)  # White with alpha value of 0.5
            else:
                glColor4f(0.0, 0.0, 1.0, 0.5)  # Blue with alpha value of 0.5
            glBegin(GL_QUADS)
            glVertex3f(i * 50.0, 0.0, j * 50.0)
            glVertex3f((i + 1) * 50.0, 0.0, j * 50.0)
            glVertex3f((i + 1) * 50.0, 0.0, (j + 1) * 50.0)
            glVertex3f(i * 50.0, 0.0, (j + 1) * 50.0)
            glEnd()


def drawReversedChessboard():
    """
    Draws a reversed chessboard using OpenGL.

    The chessboard consists of 15x15 squares, alternating between blue and white colors.
    This chessboard rotates in the opposite direction compared to the original chessboard.

    Parameters:
    None

    Returns:
    None
    """
    for i in range(8):
        # Draw a row of squares
        for j in range(8):
            # Draw a square at position (i, j)
            pass  # Placeholder for drawing logic
        for j in range(8):
            if (i + j) % 2 == 0:
                glColor4f(1.0, 1.0, 0.8, 0.5)  # White with alpha value of 0.5
            else:
                glColor4f(0.0, 0.0, 1.0, 0.5)  # Blue with alpha value of 0.5
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

    gluPerspective(45, (display[0] / display[1]), 0.1, 800.0)
    glTranslatef(-350.0, -50.0, -700.0)  # Camera position

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)  # Animation: 3 degrees rotation around the axes
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        drawChessboard()
        # Reverse the rotation for the second chessboard
        glRotatef(-1, 3, 1, 1)
        drawReversedChessboard()
        pygame.display.flip()
        pygame.time.wait(10)  # Small pause


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 800.0)
    glTranslatef(-350.0, -50.0, -700.0)  # Camera position

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)  # Animation: 3 degrees rotation around the axes
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        drawChessboard()
        pygame.display.flip()
        pygame.time.wait(10)  # Small pause


if __name__ == "__main__":
    main()
