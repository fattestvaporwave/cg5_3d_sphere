from math import sin, cos, pi, sqrt, pow, atan2
from triangle import Triangle
import numpy as np


class Sphere:

    def __init__(self, radius, ns):
        self.radius = radius
        self.ns = ns
        m = ns
        n = ns
        pts = []
        norms = []
        texture = []
        point = ([0, self.radius, 0, 1])
        magnitude = sqrt(pow(2 * point[0], 2) + pow(2 * point[1], 2) + pow(2 * point[2], 2))
        norm = np.array([2 * point[0], 2 * point[1], 2 * point[2], 0])
        norm = norm / magnitude

        u = atan2(norm[0], norm[2]) / (2 * pi) + 0.5
        v = norm[1] * 0.5 + 0.5

        texture.append([u, v])
        pts.append(point)
        norms.append(norm)

        for i in range(n):
            for j in range(m):
                point = ([
                    self.radius * cos(2 * pi / m * (j - 1)) * sin(pi / (n + 1) * i),
                    self.radius * cos(pi / (n + 1) * i),
                    self.radius * sin(2 * pi / m * (j - 1)) * sin(pi / (n + 1) * i),
                    1.0
                ])

                magnitude = sqrt(pow(2 * point[0], 2) + pow(2 * point[1], 2) + pow(2 * point[2], 2))
                norm = np.array([2 * point[0], 2 * point[1], 2 * point[2], 0])
                norm = norm / magnitude

                u = atan2(norm[0], norm[2]) / (2 * pi) + 0.5
                v = norm[1] * 0.5 + 0.5

                texture.append([u, v])
                pts.append(point)
                norms.append(norm)
        point = ([0, -self.radius, 0, 1])
        magnitude = sqrt(pow(2 * point[0], 2) + pow(2 * point[1], 2) + pow(2 * point[2], 2))
        norm = np.array([2 * point[0], 2 * point[1], 2 * point[2], 0])
        norm = norm / magnitude

        u = atan2(norm[0], norm[2]) / (2 * pi) + 0.5
        v = norm[1] * 0.5 + 0.5

        texture.append([u, v])
        pts.append(point)
        norms.append(norm)

        self.pts = np.array(pts)
        self.norms = np.array(norms)
        self.texture = np.array(texture)

        triangles = []
        for i in range(m-1):
            triangles.append(Triangle(
                [pts[0], pts[i + 1], pts[i + 2]],
                [texture[0], texture[i + 1], texture[i + 2]]
            ))
            triangles.append(Triangle(
                [pts[m * n + 1], pts[(n - 1) * m + i + 1], pts[(n - 1) * m + i + 2]],
                [texture[m * n + 1], texture[(n - 1) * m + i + 1], texture[(n - 1) * m + i + 2]]
            ))
        triangles.append(Triangle(
            [pts[0], pts[1], pts[m]],
            [texture[0], texture[1], texture[m]]
        ))
        triangles.append(Triangle(
            [pts[m * n + 1], pts[m * n], pts[(n - 1) * m + 1]],
            [texture[m * n + 1], texture[m * n], texture[(n - 1) * m + 1]]
        ))

        for i in range(n-1):
            for j in range(m):
                if j + 1 == m:
                    triangles.append(Triangle(
                        [pts[(i + 1) * m], pts[i * m + 1], pts[(i + 1) * m + 1]],
                        [texture[(i + 1) * m], texture[i * m + 1], texture[(i + 1) * m + 1]]
                    ))
                else:
                    triangles.append(Triangle(
                        [pts[i * m + j + 1], pts[i * m + j + 2], pts[(i + 1) * m + j + 2]],
                        [texture[i * m + j + 1], texture[i * m + j + 2], texture[(i + 1) * m + j + 2]]
                    ))

        for i in range(n-1):
            for j in range(m):
                if j + 1 == m:
                    triangles.append(Triangle(
                        [pts[(i + 1) * m], pts[(i + 1) * m + 1], pts[(i + 2) * m]],
                        [texture[(i + 1) * m], texture[(i + 1) * m + 1], texture[(i + 2) * m]]
                    ))
                else:
                    triangles.append(
                        Triangle(
                            [pts[i * m + j + 1], pts[(i + 1) * m + j + 2], pts[(i + 1) * m + j + 1]],
                            [texture[i * m + j + 1], texture[(i + 1) * m + j + 2], texture[(i + 1) * m + j + 1]]
                        ))

        self.triangles = np.array(triangles)


sphere = Sphere(2, 20)
