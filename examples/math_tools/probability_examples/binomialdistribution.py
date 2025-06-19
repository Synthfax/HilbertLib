from hilbertlib.math_tools.probability import BinomialDistribution

def main():
    binom = BinomialDistribution(n=10, p=0.5)
    print("PMF at 5:", binom.pmf(5))
    print("CDF at 5:", binom.cdf(5))
    print("Sample:", binom.sample())
    print("Mean:", binom.mean())
    print("Variance:", binom.variance())

if __name__ == "__main__":
    main()
