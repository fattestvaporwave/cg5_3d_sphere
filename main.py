from sphere import Sphere
from screen import Screen
import pygame
import numpy as np

cstScreen = Screen(1024, 1024)
scrn = cstScreen.start()
sphere = Sphere()
vCamera = np.zeros(3)


def draw_triangle(x1, y1, x2, y2, x3, y3):
    pygame.draw.line(scrn, pygame.color.THECOLORS['white'], (x1, y1), (x2, y2), 1)
    pygame.draw.line(scrn, pygame.color.THECOLORS['white'], (x2, y2), (x3, y3), 1)
    pygame.draw.line(scrn, pygame.color.THECOLORS['white'], (x3, y3), (x1, y1), 1)


factor = 400
S = np.eye(4)
S[0, 0] *= factor
S[1, 1] *= factor

for tri in sphere.triangles:
    points = tri.points
    line1 = points[1] - points[0]
    line2 = points[2] - points[1]

    normal = np.zeros(4)
    normal[0] = line1[1] * line2[2] - line1[2] * line2[1]
    normal[1] = line1[2] * line2[0] - line1[0] * line2[2]
    normal[2] = line1[0] * line2[1] - line1[1] * line2[0]

    normal = normal / np.sqrt(np.sum(normal ** 2))

    ctr = np.array([2.5, 1.5, 0, 0])
    for i in range(3):
        if points[i][2] == 0:
            points[i] = (points[i].dot(cstScreen.projection_matrix) + ctr) / 2
        else:
            points[i] = (points[i].dot(cstScreen.projection_matrix) / points[i][2] + ctr) / 2
        points[i] = points[i].dot(S)
    draw_triangle(points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1])
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.display.quit()
