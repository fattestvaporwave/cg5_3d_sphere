from pygame import Color


class Point:
    def __init__(self, p, t):
        self.x = p[0]
        self.y = p[1]
        self.u = t[0]
        self.v = t[1]

    def copy(self):
        return Point((self.x, self.y), (self.u, self.v))


def put_pixel(x, y, u, v, image, screen):
    width = image.width
    height = image.height

    if u <= 0 or v <= 0:
        return
    if u < 1:
        u_img = int(u * width)
    else:
        u_img = int(u * width) % width
    if v < 1:
        v_img = int(v * height)
    else:
        v_img = int(v * height) % height

    r, g, b = image.getpixel((u_img, v_img))
    screen.set_at((int(x), int(y)), Color(r, g, b))


def put_texture(points, texture_points, image, screen):
    # source : http://www-users.mat.uni.torun.pl/~wrona/3d_tutor/tri_fillers.html

    image_rgb = image.convert('RGB')
    t_ps = [Point(points[i], texture_points[i]) for i in range(len(points))]
    t_ps.sort(key=lambda p: p.y)
    A = t_ps[0]
    B = t_ps[1]
    C = t_ps[2]

    if B.y - A.y > 0:
        dx1 = (B.x - A.x) / (B.y - A.y)
        du1 = (B.u - A.u) / (B.y - A.y)
        dv1 = (B.v - A.v) / (B.y - A.y)
    else:
        dx1 = du1 = dv1 = 0
    if C.y - A.y > 0:
        dx2 = (C.x - A.x) / (C.y - A.y)
        du2 = (C.u - A.u) / (C.y - A.y)
        dv2 = (C.v - A.v) / (C.y - A.y)
    else:
        dx2 = du2 = dv2 = 0
    if C.y - B.y > 0:
        dx3 = (C.x - B.x) / (C.y - B.y)
        du3 = (C.u - B.u) / (C.y - B.y)
        dv3 = (C.v - B.v) / (C.y - B.y)
    else:
        dx3 = du3 = dv3 = 0

    S = A.copy()
    E = A.copy()

    if dx2 != dx1:
        du = (du2 - du1) / (dx2 - dx1)
        dv = (dv2 - dv1) / (dx2 - dx1)
    else:
        du = dv = 0
    if dx1 > dx2:
        while S.y <= B.y:
            u = S.u
            v = S.v
            for x in range(int(S.x), int(E.x)):
                put_pixel(x, int(S.y), u, v, image_rgb, screen)
                u += du
                v += dv
            S.u += du2
            E.u += du1
            S.v += dv2
            E.v += dv1
            S.y += 1
            E.y += 1
            S.x += dx2
            E.x += dx1
        E = B
        while S.y <= C.y:
            u = S.u
            v = S.v
            for x in range(int(S.x), int(E.x)):
                put_pixel(x, int(S.y), u, v, image_rgb, screen)
                u += du
                v += dv
            S.u += du2
            E.u += du3
            S.v += dv2
            E.v += dv3
            S.x += dx2
            E.x += dx3
            S.y += 1
            E.y += 1
    else:
        while S.y <= B.y:
            u = S.u
            v = S.v
            for x in range(int(S.x), int(E.x)):
                put_pixel(x, int(S.y), u, v, image_rgb, screen)
                u += du
                v += dv
            S.u += du1
            E.u += du2
            S.v += dv1
            E.v += dv2
            S.x += dx1
            E.x += dx2
            S.y += 1
            E.y += 1
        S = B
        while S.y <= C.y:
            u = S.u
            v = S.v
            for x in range(int(S.x), int(E.x)):
                put_pixel(x, int(S.y), u, v, image_rgb, screen)
                u += du
                v += dv
            S.u += du3
            E.u += du2
            S.v += dv3
            E.v += dv2
            S.x += dx3
            E.x += dx2
            S.y += 1
            E.y += 1
