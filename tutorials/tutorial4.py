import math
import portfolio_theory


def ex1():
    """
    Consider a simple market consisting of two assets. Relevant data about the
    asset returns is provided in the following table:
    Asset 1 r bar: 10% sigma: 15%
    Asset 2 r bar: 18% sigma: 30%
    Furthermore, the correlation between the assets’ rates of return amounts to
    rho = 0.1. Suppose that we hold a portfolio with weights w1 = 25% and
    w2 = 75%. Calculate the portfolio’s expected return and standard deviation.
    (Hint: recall that rho = sigma12/(sigma1*sigma2).)
    """
    sigma12 = 0.1*(0.15*0.3)
    portfolio_theory.portfolio_return([0.25, 0.75], [0.1, 0.18])
    var = portfolio_theory.portfolio_variance([0.25, 0.75], [[0.15**2, sigma12], [sigma12, 0.30**2]])
    sigma = math.sqrt(var)
    print(f"Portfolio standard deviation: {sigma}")


# Other exercises are derivations


if __name__ == "__main__":
    ex1()