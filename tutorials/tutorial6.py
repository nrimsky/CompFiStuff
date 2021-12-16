from misc import roots


def ex1():
    """
    The utility function is U(x) = x − 0.04x^2
    Two investment possibilities are given.
    The first one is risk free and has a £5 payoff, the second one is based on a toss of a (fair) coin.
    When the outcome of the coin toss is heads, the payoff is £10, and when the outcome is tails, you earn nothing.
    a) Evaluate the expected utility of the two alternatives. Which one is to be preferred?
    b) Find the certainty equivalent to the risky investment.
    """

    def u(x: float) -> float:
        """
        :param x: Payoff
        :return: Utility
        """
        return x - 0.04 * (x ** 2)

    u_risk_free = u(5)
    u_risky = 0.5 * u(10) + 0.5 * u(0)
    print(f"Risk free U = {u_risk_free}, Risky U = {u_risky} -> Prefer risk free")
    print(f"For certainty equivalent C, solve 3 = C - 0.04C^2 -> 0.04C^2 - C + 3 = 0 -> C = {min(roots(0.04, -1, 3))}")


def ex2():
    """
    Jerome has the utility function U(x) = x^(1/4). Having worked for a well-known
    investment bank, he now has an offer from a reputable hedge-fund which
    pays £80000 as a basic salary. The bonus will be £0, £10000, £20000,
    £30000, £40000, £50000, or £60000, each with equal probability. What
    is the certainty equivalent of this offer?
    """

    def u(x: float) -> float:
        """
        :param x: Payoff
        :return: Utility
        """
        return x ** (1 / 4)

    u = sum([u(x + 80000) for x in [0, 10000, 20000, 30000, 40000, 50000, 60000]]) / 7
    print(f"Expected utility of offer: {u}")
    print(f"For certainty equivalent C, solve u = x^(1/4) -> x = u^4 = {u ** 4}")


# Other exercises are derivations


if __name__ == "__main__":
    ex1()
    ex2()
