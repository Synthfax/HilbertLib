from hilbertlib.math_tools.probability import BernoulliDistribution

def main():
    bern = BernoulliDistribution(p=0.7)
    print("PDF at 0:", bern.pdf(0))
    print("PDF at 1:", bern.pdf(1))
    print("Sample:", bern.sample())
    print("Mean:", bern.mean())
    print("Variance:", bern.variance())

if __name__ == "__main__":
    main()
