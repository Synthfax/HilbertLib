from hilbertlib.math_tools.statistics import Statistics

data = [1, 2, 2, 3, 4, 5, 5, 5, 6]
stats = Statistics(data)
print("Mean:", stats.mean())
print("Median:", stats.median())
print("Mode:", stats.mode())
print("Sample Variance:", stats.variance())
print("Sample Std Dev:", stats.std_dev())
print("Summary:", stats.summary())