from math import sin, cos, pi
import numpy as np


class Sphere:

    def __init__(self, radius, n):
        self.radius = radius
        self.n = n
        self.horizontal = n
        self.vertical = n
        self.pts = []
        for m in range(self.horizontal):
            for n in range(self.vertical):
                tmp = ([
                    self.radius * sin(2 * pi * m / self.horizontal) * cos(2 * pi * n / self.vertical),
                    self.radius * sin(2 * pi * m / self.horizontal) * sin(2 * pi * n / self.vertical),
                    self.radius * cos(2 * pi * m / self.horizontal),
                    1.0
                ])
                self.pts.append(tmp)
        self.pts = np.array(self.pts)
