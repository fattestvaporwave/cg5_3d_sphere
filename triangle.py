import numpy as np


class Triangle:
    def __init__(self, points, textures):
        self.points = np.array([
            points[0], points[1], points[2]
        ])
        self.textures = np.array([
            textures[0], textures[1], textures[2]
        ])

    def __str__(self):
        return str(self.points[0]) + "\n" + str(self.points[1]) + "\n" + str(self.points[2]) + "\n"
