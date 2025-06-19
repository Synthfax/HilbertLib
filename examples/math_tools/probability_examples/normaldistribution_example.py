from hilbertlib.math_tools.probability import NormalDistribution

def main():
    normal = NormalDistribution(mean=0, std_dev=1)
    print("PDF at 0:", normal.pdf(0))
    print("CDF at 0:", normal.cdf(0))
    print("Sample:", normal.sample())
    print("Mean:", normal.mean())
    print("Variance:", normal.variance())

if __name__ == "__main__":
    main()