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

    def start(self):
        pygame.init()
        return pygame.display.set_mode((self.width, self.height))

####################################
