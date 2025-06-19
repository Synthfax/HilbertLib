from hilbertlib.math_tools.probability import ExponentialDistribution

def main():
    expo = ExponentialDistribution(lambd=1.5)
    print("PDF at 1:", expo.pdf(1))
    print("CDF at 1:", expo.cdf(1))
    print("Sample:", expo.sample())
    print("Mean:", expo.mean())
    print("Variance:", expo.variance())

if __name__ == "__main__":
    main()
