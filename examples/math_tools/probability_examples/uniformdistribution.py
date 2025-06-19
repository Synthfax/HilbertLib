from hilbertlib.math_tools.probability import UniformDistribution

def main():
    uniform = UniformDistribution(a=0, b=10)
    print("PDF at 5:", uniform.pdf(5))
    print("CDF at 5:", uniform.cdf(5))
    print("Sample:", uniform.sample())
    print("Mean:", uniform.mean())
    print("Variance:", uniform.variance())

if __name__ == "__main__":
    main()
