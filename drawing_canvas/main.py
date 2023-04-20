import pygame
import numpy as np
from number_recogniser.model import prediction


def create_image(drawing):
    image = np.zeros((8, 8), dtype=np.int32)

    for i in range(8):
        for j in range(8):
            if drawing[i][j] == 255:
                image[i][j] = 15

    return image


def GUI():
    pygame.init()

    WINDOW_SIZE = (800, 800)
    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption("Draw a number")

    drawing = np.zeros((8, 8), dtype=np.int32)

    brush_color = (255, 255, 255)

    brush_size = 20

    drawing_active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing_active = True

            elif event.type == pygame.MOUSEBUTTONUP:
                drawing_active = False

            elif event.type == pygame.MOUSEMOTION and drawing_active:
                mouse_pos = pygame.mouse.get_pos()
                pygame.draw.circle(screen, brush_color, mouse_pos, brush_size)
                i = mouse_pos[1] // 100
                j = mouse_pos[0] // 100
                drawing[i][j] = 255

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    image = create_image(drawing)
                    return image
        pygame.display.update()
        pygame.display.flip()

GUI()
