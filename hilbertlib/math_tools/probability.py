import math
import random
from abc import ABC, abstractmethod

class Distribution(ABC):
    @abstractmethod
    def pdf(self, x):
        pass
    
    @abstractmethod
    def cdf(self, x):
        pass
    
    @abstractmethod
    def sample(self):
        pass
    
    @abstractmethod
    def mean(self):
        pass
    
    @abstractmethod
    def variance(self):
        pass

class NormalDistribution(Distribution):
    def __init__(self, mean=0, std_dev=1):
        self.mean_val = mean
        self.std_dev_val = std_dev
    
    def pdf(self, x):
        m = self.mean_val
        s = self.std_dev_val
        return (1 / (s * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - m)/s)**2)
    
    def cdf(self, x):
        # Approximate with error function
        m = self.mean_val
        s = self.std_dev_val
        return 0.5 * (1 + math.erf((x - m) / (s * math.sqrt(2))))
    
    def sample(self):
        return random.gauss(self.mean_val, self.std_dev_val)
    
    def mean(self):
        return self.mean_val
    
    def variance(self):
        return self.std_dev_val ** 2
    
class BernoulliDistribution(Distribution):
    def __init__(self, p=0.5):
        assert 0 <= p <= 1, "Probability must be between 0 and 1"
        self.p = p
    
    def pdf(self, k):
        if k not in (0,1):
            return 0
        return self.p if k == 1 else 1 - self.p
    
    def cdf(self, k):
        if k < 0:
            return 0
        elif k < 1:
            return 1 - self.p
        else:
            return 1
    
    def sample(self):
        return 1 if random.random() < self.p else 0
    
    def mean(self):
        return self.p
    
    def variance(self):
        return self.p * (1 - self.p)

class BinomialDistribution(Distribution):
    def __init__(self, n, p):
        assert n >= 0 and isinstance(n, int), "n must be non-negative int"
        assert 0 <= p <= 1, "Probability must be between 0 and 1"
        self.n = n
        self.p = p
    
    def pmf(self, k):
        if k < 0 or k > self.n:
            return 0
        return math.comb(self.n, k) * (self.p ** k) * ((1 - self.p) ** (self.n - k))
    
    def pdf(self, k):
        return self.pmf(k)
    
    def cdf(self, k):
        total = 0
        for i in range(0, math.floor(k)+1):
            total += self.pmf(i)
        return total
    
    def sample(self):
        successes = 0
        for _ in range(self.n):
            if random.random() < self.p:
                successes += 1
        return successes
    
    def mean(self):
        return self.n * self.p
    
    def variance(self):
        return self.n * self.p * (1 - self.p)

class UniformDistribution(Distribution):
    def __init__(self, a=0, b=1):
        assert a < b, "a must be less than b"
        self.a = a
        self.b = b
    
    def pdf(self, x):
        if self.a <= x <= self.b:
            return 1 / (self.b - self.a)
        return 0
    
    def cdf(self, x):
        if x < self.a:
            return 0
        elif x > self.b:
            return 1
        else:
            return (x - self.a) / (self.b - self.a)
    
    def sample(self):
        return random.uniform(self.a, self.b)
    
    def mean(self):
        return (self.a + self.b) / 2
    
    def variance(self):
        return ((self.b - self.a) ** 2) / 12

class ExponentialDistribution(Distribution):
    def __init__(self, lambd=1):
        assert lambd > 0, "Lambda must be positive"
        self.lambd = lambd
    
    def pdf(self, x):
        if x < 0:
            return 0
        return self.lambd * math.exp(-self.lambd * x)
    
    def cdf(self, x):
        if x < 0:
            return 0
        return 1 - math.exp(-self.lambd * x)
    
    def sample(self):
        return random.expovariate(self.lambd)
    
    def mean(self):
        return 1 / self.lambd
    
    def variance(self):
        return 1 / (self.lambd ** 2)