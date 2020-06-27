from texture import put_texture
import pygame
from math import sin, cos
import numpy as np


def draw_triangle(x1, y1, x2, y2, x3, y3, screen):
    pygame.draw.line(screen, pygame.color.THECOLORS['white'], (x1, y1), (x2, y2), 1)
    pygame.draw.line(screen, pygame.color.THECOLORS['white'], (x2, y2), (x3, y3), 1)
    pygame.draw.line(screen, pygame.color.THECOLORS['white'], (x3, y3), (x1, y1), 1)


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


def draw_shape(shape, tx, ty, tz, is_textured, image, cst_screen, this_screen):
    mat_world = np.eye(4).dot(rot_y(ty)).dot(rot_x(tx)).dot(rot_z(tz)).dot(cst_screen.translation_matrix)
    for tri in shape.triangles:
        points = [tri.points[0], tri.points[1], tri.points[2]]
        texture = [tri.textures[0], tri.textures[1], tri.textures[2]]
        for i in range(3):
            points[i] = points[i].dot(mat_world)
            points[i] = (points[i].dot(cst_screen.projection_matrix) / points[i][2] + cst_screen.offset_vector) / 2
            points[i] = points[i].dot(cst_screen.scaling_matrix)
        draw_triangle(points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1], this_screen)
        if is_textured:
            put_texture(points, texture, image, this_screen)
    pygame.display.flip()