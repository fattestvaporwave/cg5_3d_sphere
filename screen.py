from math import pi, tan
import numpy as np
import pygame


class Screen:

    def __init__(self, width, height):
        self.z_near = 0.1
        self.z_far = 1000.0
        self.theta = pi / 2
        self.width = width
        self.height = height
        self.aspect_ratio = width/height
        self.projection_matrix = np.array([
            [self.aspect_ratio * (1 / tan(self.theta / 2)), 0, 0, 0],
            [0, 1 / tan(self.theta / 2), 0, 0],
            [0, 0, self.z_far / (self.z_far - self.z_near), 1],
            [0, 0, -((self.z_far * self.z_near) / (self.z_far - self.z_near)), 0]
        ])
        self.translation_matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 2.5, 1]
        ])
        self.factor = 400
        self.scaling_matrix = np.array([
            [1 * self.factor, 0, 0, 0],
            [0, 1 * self.factor, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        self.offset_vector = np.array([1.9, 1.9, 0, 0])

    def start(self):
        pygame.init()
        return pygame.display.set_mode((self.width, self.height))

####################################
