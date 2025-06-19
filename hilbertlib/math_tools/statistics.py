import math
from collections import Counter

class Statistics:
    def __init__(self, data):
        if not data:
            raise ValueError("Data list can't be empty")
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self):
        counts = Counter(self.data)
        max_count = max(counts.values())
        modes = [k for k, v in counts.items() if v == max_count]
        if len(modes) == len(counts):
            return None  # No mode if all values occur equally
        return modes

    def variance(self, sample=True):
        mean = self.mean()
        n = len(self.data)
        var_sum = sum((x - mean) ** 2 for x in self.data)
        return var_sum / (n - 1) if sample else var_sum / n

    def std_dev(self, sample=True):
        return math.sqrt(self.variance(sample))

    def summary(self):
        return {
            "mean": self.mean(),
            "median": self.median(),
            "mode": self.mode(),
            "variance_sample": self.variance(sample=True),
            "variance_population": self.variance(sample=False),
            "std_dev_sample": self.std_dev(sample=True),
            "std_dev_population": self.std_dev(sample=False)
        }
