from hilbertlib.math_tools.vectors import Vector3D

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print("v1 =", v1)
print("v2 =", v2)

print("Addition:", v1 + v2)
print("Subtraction:", v1 - v2)
print("Magnitude of v1:", v1.magnitude())
print("Dot product:", v1.dot(v2))
print("Cross product:", v1.cross(v2))
print("Normalized v1:", v1.normalize())