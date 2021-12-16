import math
import portfolio_theory


def ex1():
    """
    Consider a universe of just three securities. They have expected rates of return of 10%, 20% and 10%, respectively.
    Two portfolios are known to lie on the minimum-variance set. They are defined by the portfolio weights
    w = [0.6, 0.2, 0.2]
    v = [0.8, −0.2, 0.4]
    It is also known that the market portfolio is efficient. Furthermore, short selling is allowed.
    1. Given this information, what are the minimum and maximum possible values for the expected rate of return on the market portfolio?
    2. Now suppose you are told that w represents the minimum-variance portfolio. Does this change your answer to part (1)?
    """
    portfolio_theory.two_fund([0.6, 0.2, 0.2], [0.8, -0.2, 0.4], [0.1, 0.2, 0.1])


def ex2():
    """
    Assume that the expected rate of return on the market portfolio is 23% and the rate of return on T-bills (the risk-free rate)
    is 7%. The standard deviation of the market is 32%. Assume that the market portfolio is efficient.
    1) What is the equation of the capital market line?
    2) If an expected return of 39% is desired, what is the standard deviation of this position?
    3) If you have $1000 to invest, how should you allocate it to achieve the above position?
    4) If you invest $300 in the risk-free asset and $700 in the market portfolio, how much money should you expect to have at the end of the year?
    """
    portfolio_theory.capm_equation(0.07, 0.23, 0.32)
    portfolio_theory.capm_std(0.07, 0.23, 0.32, 0.39)
    portfolio_theory.asset_weights(0.07, 0.23, 0.39)
    print(f"300 in risk free + 700 in market -> expect to have {300*(1 + 0.07)} + {700*(1 + 0.23)} = {300*(1 + 0.07) + 700*(1 + 0.23)} at year end")


# ex 3 is derivation


def ex4():
    """
    In Simpleland there are only two risky stocks, A and B, whose details are listed in the following table.
              No. shares outstanding | Price per share | Expected rate of return | Standard deviation of return
    Stock A | 100                    | $1.5            | 15%                     | 15%
    Stock B | 150                    | $2              | 12%                     | 9%
    Furthermore, the correlation coefficient between the returns of stocks A and B is rhoAB = 1/3
    There is also a risk-free asset, and Simpleland satisfies the CAPM exactly.
    1. What is the expected rate of return of the market portfolio?
    2. What is the standard deviation of the market portfolio?
    3. What is the beta of stock A?
    4. What is the risk-free rate in Simpleland?
    """
    stock_a = portfolio_theory.StockData(100, 1.5, 0.15, 0.15)
    stock_b = portfolio_theory.StockData(150, 2, 0.12, 0.09)
    portfolio_theory.risk_free_two_assets(stock_a, stock_b, 1/3)


if __name__ == "__main__":
    ex1()
    ex2()
    ex4()
