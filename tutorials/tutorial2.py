import interest
from fixed_income import infinite_sum_from_0, infinite_sum_from_1


def ex1():
    interest.effective_interest_rate(0.03, 12)
    interest.effective_interest_rate(0.18, 12)
    interest.effective_interest_rate(0.18, 4)


def ex2():
    """
    You are considering the purchase of a nice home. It is in every way
    perfect for you and in excellent condition, except for the roof. The roof has
    only 5 years of life remaining. A new roof would last 20 years, but would
    cost $20, 000. The house is expected to last forever. Assuming that costs
    will remain constant and that the interest rate is 5%, what value would you
    assign to the existing roof? Note: It is assumed that the roof will be replaced
    every 20 years, forever.
    """
    pv1 = 20000 * infinite_sum_from_0(1 / ((1 + 0.05) ** 20))
    print(f"Change roof now, then every 20 years: {pv1}")
    pv2 = pv1 / ((1 + 0.05) ** 5)
    print(f"Change roof in 5 years, then every 20 years: {pv2}")
    v = pv1 - pv2
    print(f"Value of roof = pv1 - pv2 = {v}")


def ex3a():
    interest.evolve_spot_rate_curve([0.05, 0.053, 0.056, 0.058, 0.06, 0.061])


def ex3b():
    """
    Consider two 5-year bonds : one has a 9% coupon and sells for $101.00;
    the other has a 7% coupon and sells for $93.20. Assuming that both
    bonds have a face value of $100.00, find the price of a 5-year zero coupon bond.
    Note that all bonds are priced under the same spot rate curve.
    However, the spot rates are not given.
    """
    print("1) $101.00 = 9 * sum from 1 to 4 of d_k + 109 * d_5")
    print("2) $93.20 = 7 * sum from 1 to 4 of d_k + 107 * d_5")
    print(f"3) ${101.00 * 7} = {9 * 7} * sum from 1 to 4 of d_k + {109 * 7} * d_5")
    print(f"4) ${93.20 * 9} = {7 * 9} * sum from 1 to 4 of d_k + {107 * 9} * d_5")
    print(f"3) - 4) => {101.00 * 7 - 93.20 * 9} = {109 * 7 - 107 * 9} * d_5")
    print(f"d_5 = {(101.00 * 7 - 93.20 * 9) / (109 * 7 - 107 * 9)}")
    print(f"V of 5 year zero coupon bond = face value * d_5 = ${100 * ((101.00 * 7 - 93.20 * 9) / (109 * 7 - 107 * 9))}")


def ex4():
    """
    The Have A Nice Day Corporation has just paid a dividend of $1.37 per
    share. The company is expected to grow at 10% for the foreseeable future,
    and hence most analysts project a similar growth in dividends. The discount
    rate used for this type of company is 15%. The value of a share is given by
    the net present value of all future dividend payments. Calculate the share
    price.
    """
    multiplier = 1.10 / 1.15
    dividend_sum = 1.37 * infinite_sum_from_1(multiplier)
    print(f"Net present value of all future dividend payments: {dividend_sum}")


if __name__ == "__main__":
    ex1()
    ex2()
    ex3a()
    ex3b()
    ex4()
