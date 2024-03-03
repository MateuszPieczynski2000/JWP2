class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Vector3D(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def norm(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3D(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)

    @staticmethod
    def are_orthogonal(vec1, vec2):
        return vec1.dot(vec2) == 0


vector1 = Vector3D(1, 2, 3)
vector2 = Vector3D(4, 5, 6)

print(vector1)
print(vector2)

print(vector1.norm())
print(vector2.norm())

print(vector1 + vector2)
print(vector1 - vector2)

print(vector1 * 3)
print(vector2 * 3)

print(vector1.dot(vector2))
print(vector1.cross(vector2))

print(Vector3D.are_orthogonal(vector1, vector2))
