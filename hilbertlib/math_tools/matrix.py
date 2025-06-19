import math
from .vectors import Vector2D, Vector3D

class Matrix2D:
    def __init__(self, a=1, b=0, c=0, d=1, tx=0, ty=0):
        # | a b tx |
        # | c d ty |
        # | 0 0 1  |
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.tx = tx
        self.ty = ty

    def multiply_vector(self, vec):
        x = self.a * vec.x + self.b * vec.y + self.tx
        y = self.c * vec.x + self.d * vec.y + self.ty
        return Vector2D(x, y)

    def multiply_matrix(self, other):
        return Matrix2D(
            self.a * other.a + self.b * other.c,
            self.a * other.b + self.b * other.d,
            self.c * other.a + self.d * other.c,
            self.c * other.b + self.d * other.d,
            self.a * other.tx + self.b * other.ty + self.tx,
            self.c * other.tx + self.d * other.ty + self.ty,
        )

    @staticmethod
    def identity():
        return Matrix2D()

    @staticmethod
    def rotation(angle_rad):
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        return Matrix2D(cos_a, -sin_a, sin_a, cos_a)

    @staticmethod
    def scale(sx, sy):
        return Matrix2D(sx, 0, 0, sy)

    @staticmethod
    def translation(tx, ty):
        return Matrix2D(1, 0, 0, 1, tx, ty)

    def __repr__(self):
        return f"|{self.a:.2f} {self.b:.2f} {self.tx:.2f}|\n|{self.c:.2f} {self.d:.2f} {self.ty:.2f}|\n|0.00 0.00 1.00|"
    
class Matrix3D:
    def __init__(self, data=None):
        if data:
            self.data = data  # Expecting 4x4 list
        else:
            self.data = [[1 if i == j else 0 for j in range(4)] for i in range(4)]

    def multiply_vector(self, v):
        x = v.x
        y = v.y
        z = v.z
        w = 1

        tx = self.data[0][0]*x + self.data[0][1]*y + self.data[0][2]*z + self.data[0][3]*w
        ty = self.data[1][0]*x + self.data[1][1]*y + self.data[1][2]*z + self.data[1][3]*w
        tz = self.data[2][0]*x + self.data[2][1]*y + self.data[2][2]*z + self.data[2][3]*w
        tw = self.data[3][0]*x + self.data[3][1]*y + self.data[3][2]*z + self.data[3][3]*w

        if tw != 0 and tw != 1:
            tx /= tw
            ty /= tw
            tz /= tw

        return Vector3D(tx, ty, tz)

    def multiply_matrix(self, other):
        result = [[0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                result[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(4))
        return Matrix3D(result)

    @staticmethod
    def identity():
        return Matrix3D()

    @staticmethod
    def translation(tx, ty, tz):
        m = Matrix3D.identity()
        m.data[0][3] = tx
        m.data[1][3] = ty
        m.data[2][3] = tz
        return m

    @staticmethod
    def scale(sx, sy, sz):
        m = Matrix3D.identity()
        m.data[0][0] = sx
        m.data[1][1] = sy
        m.data[2][2] = sz
        return m

    @staticmethod
    def rotation_x(angle):
        m = Matrix3D.identity()
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        m.data[1][1] = cos_a
        m.data[1][2] = -sin_a
        m.data[2][1] = sin_a
        m.data[2][2] = cos_a
        return m

    @staticmethod
    def rotation_y(angle):
        m = Matrix3D.identity()
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        m.data[0][0] = cos_a
        m.data[0][2] = sin_a
        m.data[2][0] = -sin_a
        m.data[2][2] = cos_a
        return m

    @staticmethod
    def rotation_z(angle):
        m = Matrix3D.identity()
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        m.data[0][0] = cos_a
        m.data[0][1] = -sin_a
        m.data[1][0] = sin_a
        m.data[1][1] = cos_a
        return m

    def __repr__(self):
        return '\n'.join(['| ' + ' '.join(f"{val:6.2f}" for val in row) + ' |' for row in self.data])