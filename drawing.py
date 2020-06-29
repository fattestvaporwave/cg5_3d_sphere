from texture import put_texture
import pygame
from math import sin, cos
import numpy as np


def draw_triangle(x1, y1, x2, y2, x3, y3, screen):
    """Draws a triangle on the screen based upon given coordinates.

        Parameters:
        x1, y1, x2, y2, x3, x4 (int): coordinates of points of the triangle
        screen (pygame.screen): screen upon which the triangle is drawn

       """
    pygame.draw.line(screen, pygame.color.THECOLORS['white'], (x1, y1), (x2, y2), 1)
    pygame.draw.line(screen, pygame.color.THECOLORS['white'], (x2, y2), (x3, y3), 1)
    pygame.draw.line(screen, pygame.color.THECOLORS['white'], (x3, y3), (x1, y1), 1)


def rot_x(theta):
    """Returns a rotation matrix used for rotating the sphere in the X axis
        based on the given value theta.

        Parameters:
        theta (float): angle of rotation

        Returns:
        numpy.array: X-axis rotation matrix

        """
    return np.array([
        [1, 0, 0, 0],
        [0, cos(theta), sin(theta), 0],
        [0, -sin(theta), cos(theta), 0],
        [0, 0, 0, 1]
    ])


def rot_y(theta):
    """Returns a rotation matrix used for rotating the sphere in the Y axis
        based on the given value theta.

        Parameters:
        theta (float): angle of rotation

        Returns:
        numpy.array: Y-axis rotation matrix

        """
    return np.array([
        [cos(theta), 0, -sin(theta), 0],
        [0, 1, 0, 0],
        [sin(theta), 0, cos(theta), 0],
        [0, 0, 0, 1]
    ])


def rot_z(theta):
    """Returns a rotation matrix used for rotating the sphere in the Z axis
        based on the given value theta.

        Parameters:
        theta (float): angle of rotation

        Returns:
        numpy.array: Z-axis rotation matrix

        """
    return np.array([
        [cos(theta), -sin(theta), 0, 0],
        [sin(theta), cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def draw_shape(shape, tx, ty, tz, is_textured, image, cst_screen, this_screen):
    """Primary function for computing the sphere coordinates and drawing the sphere.
        It computes the rotation matrix needed for rotation the sphere.
        Performs matrix multiplication for each point of each triangle in the sphere mesh grid.
        Uses projection matrix to simulate realistic depth.
        Uses offset vector to place the sphere in the center of the screen.
        Uses scaling matrix to scale the sphere for the zoom in and out effect.

        Parameters:
        shape (sphere): sphere class object with initialized triangle mesh grid
        tx (float): angle of rotation in the X axis
        ty (float): angle of rotation in the Y axis
        tz (float): angle of rotation in the Z axis
        is_textured (bool): determines whether the sphere is textured or not
        image (Image): texture of the sphere
        cst_screen (screen): screen class object containing objects needed for matrices computation
        this_screen (pygame.screen): screen upon which the shape is drawn

       """
    rotation_matrix = np.eye(4).dot(rot_y(ty)).dot(rot_x(tx)).dot(rot_z(tz)).dot(cst_screen.translation_matrix)
    for tri in shape.triangles:
        points = [tri.points[0], tri.points[1], tri.points[2]]
        texture = [tri.textures[0], tri.textures[1], tri.textures[2]]
        for i in range(3):
            points[i] = points[i].dot(rotation_matrix)
            points[i] = (points[i].dot(cst_screen.projection_matrix) / points[i][2] + cst_screen.offset_vector) / 2
            points[i] = points[i].dot(cst_screen.scaling_matrix)
        if not is_textured:
            draw_triangle(points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1],
                          this_screen)
        if is_textured:
            put_texture(points, texture, image, this_screen)
    pygame.display.flip()
