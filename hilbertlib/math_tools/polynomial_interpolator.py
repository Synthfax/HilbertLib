class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients  # list: [a0, a1, a2, ..., an]

    def evaluate(self, x):
        return sum(c * (x ** i) for i, c in enumerate(self.coefficients))

    def __call__(self, x):
        return self.evaluate(x)

    def derivative(self):
        if len(self.coefficients) <= 1:
            return Polynomial([0])
        deriv = [i * c for i, c in enumerate(self.coefficients)][1:]
        return Polynomial(deriv)

    def __add__(self, other):
        length = max(len(self.coefficients), len(other.coefficients))
        result = []
        for i in range(length):
            a = self.coefficients[i] if i < len(self.coefficients) else 0
            b = other.coefficients[i] if i < len(other.coefficients) else 0
            result.append(a + b)
        return Polynomial(result)

    def __sub__(self, other):
        length = max(len(self.coefficients), len(other.coefficients))
        result = []
        for i in range(length):
            a = self.coefficients[i] if i < len(self.coefficients) else 0
            b = other.coefficients[i] if i < len(other.coefficients) else 0
            result.append(a - b)
        return Polynomial(result)

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
            for i, a in enumerate(self.coefficients):
                for j, b in enumerate(other.coefficients):
                    result[i + j] += a * b
            return Polynomial(result)
        else:  # scalar
            return Polynomial([c * other for c in self.coefficients])

    def __repr__(self):
        terms = []
        for i, c in enumerate(self.coefficients):
            if c:
                terms.append(f"{c}x^{i}" if i > 0 else str(c))
        return " + ".join(reversed(terms)) if terms else "0"


class Interpolator:
    def __init__(self, x_points, y_points):
        if len(x_points) != len(y_points):
            raise ValueError("x and y lists must be same length")
        self.x = x_points
        self.y = y_points

    def linear(self):
        def interp(x):
            for i in range(len(self.x) - 1):
                x0, x1 = self.x[i], self.x[i+1]
                y0, y1 = self.y[i], self.y[i+1]
                if x0 <= x <= x1:
                    t = (x - x0) / (x1 - x0)
                    return y0 * (1 - t) + y1 * t
            raise ValueError("x out of bounds")
        return interp

    def lagrange(self):
        def L(x):
            total = 0
            n = len(self.x)
            for i in range(n):
                xi, yi = self.x[i], self.y[i]
                term = yi
                for j in range(n):
                    if i != j:
                        term *= (x - self.x[j]) / (xi - self.x[j])
                total += term
            return total
        return L

    def newton(self):
        def divided_diff():
            n = len(self.x)
            coef = [y for y in self.y]
            for j in range(1, n):
                for i in range(n - 1, j - 1, -1):
                    coef[i] = (coef[i] - coef[i - 1]) / (self.x[i] - self.x[i - j])
            return coef

        coef = divided_diff()

        def N(x):
            n = len(coef)
            result = coef[0]
            for i in range(1, n):
                term = coef[i]
                for j in range(i):
                    term *= (x - self.x[j])
                result += term
            return result
        return N