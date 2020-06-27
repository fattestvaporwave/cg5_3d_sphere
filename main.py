from sphere import Sphere
from screen import Screen
from drawing import *
from PIL import Image
import pygame
from math import pi

cst_screen = Screen(768, 768)
this_screen = cst_screen.start()
shape = Sphere(1.5, 20)
theta_x = 0
theta_y = 0
theta_z = 0
tex = True
image = Image.open('texture/texture.png')
image = image.rotate(180)

draw_shape(shape, theta_x, theta_y, theta_z, tex, image, cst_screen, this_screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                theta_x += pi / 90
            if event.key == pygame.K_DOWN:
                theta_x -= pi / 90
            if event.key == pygame.K_LEFT:
                theta_y -= pi / 90
            if event.key == pygame.K_RIGHT:
                theta_y += pi / 90
            if event.key == pygame.K_k:
                theta_z += pi / 90
            if event.key == pygame.K_l:
                theta_z -= pi / 90
            if event.key == pygame.K_p:
                if cst_screen.translation_matrix[3, 2] > 2.5:
                    cst_screen.translation_matrix[3, 2] -= 0.5
            if event.key == pygame.K_m:
                cst_screen.translation_matrix[3, 2] += 0.5
            if event.key == pygame.K_t:
                tex = not tex
            this_screen.fill((0, 0, 0))
            draw_shape(shape, theta_x, theta_y, theta_z, tex, image, cst_screen, this_screen)

pygame.display.quit()
pygame.quit()
quit()
