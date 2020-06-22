import numpy as np


class Triangle:
    def __init__(self, point1, point2, point3):
        self.points = np.array([
            point1, point2, point3
        ])

    def __str__(self):
        return str(self.points[0]) + "\n" + str(self.points[1]) + "\n" + str(self.points[2]) + "\n"
