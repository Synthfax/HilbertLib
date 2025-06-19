from hilbertlib.math_tools.polynomial_interpolator import Interpolator

# Points to interpolate
x_points = [1, 2, 3, 4]
y_points = [2, 4, 6, 8]

interp = Interpolator(x_points, y_points)

# Linear interpolation at 2.5
lin = interp.linear()
print("Linear interp at 2.5:", lin(2.5))

# Lagrange interpolation at 2.5
lag = interp.lagrange()
print("Lagrange interp at 2.5:", lag(2.5))

# Newton interpolation at 2.5
newt = interp.newton()
print("Newton interp at 2.5:", newt(2.5))
