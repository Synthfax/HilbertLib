from hilbertlib.math_tools.vectors import Vector2D

v1 = Vector2D(3, 4)
v2 = Vector2D(1, -2)

print("v1 =", v1)
print("v2 =", v2)

print("Addition:", v1 + v2)
print("Subtraction:", v1 - v2)
print("Magnitude of v1:", v1.magnitude())
print("Dot product:", v1.dot(v2))
print("Normalized v1:", v1.normalize())