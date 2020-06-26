from sphere import Sphere
from screen import Screen
import pygame
from math import sin, cos, pi
import numpy as np

cstScreen = Screen(768, 768)
this_screen = cstScreen.start()
sphere = Sphere(2, 20)
theta_x = 0
theta_y = 0
theta_z = 0


def draw_triangle(x1, y1, x2, y2, x3, y3):
    pygame.draw.line(this_screen, pygame.color.THECOLORS['white'], (x1, y1), (x2, y2), 1)
    pygame.draw.line(this_screen, pygame.color.THECOLORS['white'], (x2, y2), (x3, y3), 1)
    pygame.draw.line(this_screen, pygame.color.THECOLORS['white'], (x3, y3), (x1, y1), 1)


def rot_x(theta):
    return np.array([
        [1, 0, 0, 0],
        [0, cos(theta), sin(theta), 0],
        [0, -sin(theta), cos(theta), 0],
        [0, 0, 0, 1]
    ])


def rot_y(theta):
    return np.array([
        [cos(theta), 0, -sin(theta), 0],
        [0, 1, 0, 0],
        [sin(theta), 0, cos(theta), 0],
        [0, 0, 0, 1]
    ])


def rot_z(theta):
    return np.array([
        [cos(theta), -sin(theta), 0, 0],
        [sin(theta), cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def draw_shape(tx, ty, tz):
    mat_world = np.eye(4).dot(rot_y(ty)).dot(rot_x(tx)).dot(rot_z(tz)).dot(cstScreen.translation_matrix)
    for p in range(len(sphere.pts) - sphere.n):
        points = [sphere.pts[p], sphere.pts[p + 1], sphere.pts[p + sphere.n]]
        for i in range(3):
            points[i] = points[i].dot(mat_world)
            points[i] = (points[i].dot(cstScreen.projection_matrix) / points[i][2] + cstScreen.offset_vector) / 2
            points[i] = points[i].dot(cstScreen.scaling_matrix)
        draw_triangle(points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1])
    pygame.display.flip()


draw_shape(theta_x, theta_y, theta_z)

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
                if cstScreen.translation_matrix[3, 2] > 2.5:
                    cstScreen.translation_matrix[3, 2] -= 0.5
            if event.key == pygame.K_m:
                cstScreen.translation_matrix[3, 2] += 0.5
            this_screen.fill((0, 0, 0))
            draw_shape(theta_x, theta_y, theta_z)


pygame.display.quit()
pygame.quit()
quit()
