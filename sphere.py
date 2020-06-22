from triangle import Triangle
from math import sqrt
import numpy as np


class Sphere:
    radius = 2.0
    t = (1.0 + sqrt(5.0)) / 2.0
    points = np.array([
        [-radius, t, 0, 1],
        [radius, t, 0, 1],
        [-radius, -t, 0, 1],
        [radius, -t, 0, 1],

        [0, -radius, t, 1],
        [0, radius, t, 1],
        [0, -radius, -t, 1],
        [0, radius, -t, 1],

        [t, 0, -radius, 1],
        [t, 0, radius, 1],
        [-t, 0, -radius, 1],
        [-t, 0, radius, 1]
    ])
    faces = np.array([
        [0, 11, 5],
        [0, 5, 1],
        [0, 1, 7],
        [0, 7, 10],
        [0, 10, 11],

        [1, 5, 9],
        [5, 11, 4],
        [11, 10, 2],
        [10, 7, 6],
        [7, 1, 8],

        [3, 9, 4],
        [3, 4, 2],
        [3, 2, 6],
        [3, 6, 8],
        [3, 8, 9],

        [4, 9, 5],
        [2, 4, 11],
        [6, 2, 10],
        [8, 6, 7],
        [9, 8, 1]
    ])

    def __init__(self):
        self.triangles = []
        for i in range(20):
            self.triangles.append(Triangle(
                self.points[self.faces[i][0]],
                self.points[self.faces[i][1]],
                self.points[self.faces[i][2]]
            ))

#    def __str__(self):
#        for tri in self.triangles:
#            print(tri)
#        return ""


sphere = Sphere()

