from hilbertlib.math_tools.polynomial_interpolator import Polynomial

# Create a polynomial: P(x) = 2 + 3x + 5x^2
p = Polynomial([2, 3, 5])
print("Polynomial:", p)

# Evaluate P(2)
val = p.evaluate(2)
print("P(2) =", val)

# Derivative: P'(x)
dp = p.derivative()
print("Derivative:", dp)

# Evaluate derivative at x=2
dval = dp.evaluate(2)
print("P'(2) =", dval)

# Add two polynomials
p2 = Polynomial([1, 0, 4])  # 1 + 0x + 4x^2
p_sum = p + p2
print("Sum:", p_sum)

# Multiply polynomials
p_mul = p * p2
print("Product:", p_mul)