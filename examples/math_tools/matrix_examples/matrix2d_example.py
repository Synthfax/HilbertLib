# example_matrix2d.py
from math import pi
from hilbertlib.math_tools.matrix import Matrix2D
from hilbertlib.math_tools.vectors import Vector2D

# Create a point
point = Vector2D(5, 3)

# Apply rotation of 90 degrees (π/2 radians)
rotation_matrix = Matrix2D.rotation(pi / 2)
rotated_point = rotation_matrix.multiply_vector(point)
print("Rotated:", rotated_point)

# Apply scaling by 2x
scaling_matrix = Matrix2D.scale(2, 2)
scaled_point = scaling_matrix.multiply_vector(point)
print("Scaled:", scaled_point)

# Apply translation
translation_matrix = Matrix2D.translation(10, 15)
translated_point = translation_matrix.multiply_vector(point)
print("Translated:", translated_point)

# Combine translation and rotation
combined_matrix = translation_matrix.multiply_matrix(rotation_matrix)
result = combined_matrix.multiply_vector(point)
print("Translated + Rotated:", result)