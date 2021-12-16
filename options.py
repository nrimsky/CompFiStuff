import math
from collections import namedtuple
from typing import List, Tuple

Option = namedtuple("Option", ["type", "strike", "expiry", "is_american"])


def payoff(option: Option, curr_price: float) -> float:
    """
    :param option: The option
    :param curr_price: Current stock price
    :return: Payoff if option can be exercised now
    """
    if option.type == "call":
        if option.strike > curr_price:
            print(f"Strike price {option.strike} of call > Current price {curr_price} => out of the money")
            return 0
        else:
            print(f"Payoff of call is current price {curr_price} - strike price {option.strike} = {curr_price - option.strike}")
            return curr_price - option.strike
    elif option.type == "put":
        if option.strike < curr_price:
            print(f"Strike price {option.strike} of put < Current price {curr_price} => out of the money")
            return 0
        else:
            print(f"Payoff of put is strike price {option.strike} - current price {curr_price} = {option.strike - curr_price}")
            return option.strike - curr_price
    else:
        raise


def value_single_period(option: Option, r: float, s: float, u: float, d: float) -> float:
    """
    :param option: The option
    :param r: Risk free return ( 1 + nominal interest rate * compounding period (eg 1/12 for monthly) )
    :param s: Stock price currently
    :param u: Multiplier for up in single period in binomial lattice
    :param d: Multiplier for down in single period in binomial lattice
    :return: PV of option
    """
    q = (r - d) / (u - d)
    c_u, c_d, c = 0, 0, 0
    if option.type == "call":
        c_u = max([u * s - option.strike, 0])
        c_d = max([d * s - option.strike, 0])
    elif option.type == "put":
        c_u = max([option.strike - u * s, 0])
        c_d = max([option.strike - d * s, 0])
    c = (1 / r) * (q * c_u + (1 - q) * c_d)
    print(f"Payoff if stock goes up (c_u): {c_u}; down (c_d): {c_d}, q = (r - d) / (u - d), c = (1 / r) * (q * c_u + (1 - q) * c_d) = {c}")
    return c


def value_x_periods_arr(option: Option, r: float, s: float, u: float, d: float, x: int) -> float:
    """
    :param option: The option
    :param r: Risk free return ( 1 + nominal interest rate * compounding period (eg 1/12 for monthly) )
    :param s: Stock price currently
    :param u: Multiplier for up in single period in binomial lattice
    :param d: Multiplier for down in single period in binomial lattice
    :param x: Number of periods to calculate
    :return: PV of option
    """
    q = (r - d) / (u - d)
    s_arr = [[0.0 for _ in range(x + 1)] for _ in range(x + 1)]
    o_arr = [[0.0 for _ in range(x + 1)] for _ in range(x + 1)]

    s_arr[0][0] = s

    for j in range(x):
        for i in range(j + 1):
            s_arr[i][j + 1] = s_arr[i][j] * u
            s_arr[i + 1][j + 1] = s_arr[i][j] * d

    for i, o in enumerate(o_arr):
        if option.type == "call":
            o[x] = max([s_arr[i][x] - option.strike, 0])
        else:
            o[x] = max([option.strike - s_arr[i][x], 0])

    for j in range(x - 1, -1, -1):
        for i in range(j + 1):
            lower_bound = (s_arr[i][j] - option.strike if option.type == "call" else option.strike - s_arr[i][j]) if option.is_american else 0
            o_arr[i][j] = max([(1 / r) * (q * o_arr[i][j + 1] + (1 - q) * o_arr[i + 1][j + 1]), lower_bound, 0])

    print("Stock prices")
    for s in s_arr:
        print(" ".join([str(round(n * 1000) / 1000) for n in s]))
    print("=====================")
    print("Option values")
    for o in o_arr:
        print(" ".join([str(round(n * 1000) / 1000) for n in o]))

    return o_arr[0][0]


def stock_lattice(x: int, u: float, d: float, p: float, s_0: float) -> Tuple[List[List[float]], List[List[float]]]:
    """
    :param x: Number of periods
    :param u: Up multiplier
    :param d: Down multiplier
    :param p: Probability up
    :param s_0: Starting stock price
    :return: Stock price lattice, Probability lattice
    """
    s_arr = [[0.0 for _ in range(x + 1)] for _ in range(x + 1)]
    p_arr = [[0.0 for _ in range(x + 1)] for _ in range(x + 1)]
    s_arr[0][0] = s_0
    p_arr[0][0] = 1
    for j in range(x):
        for i in range(j + 1):
            s_arr[i][j + 1] = s_arr[i][j] * u
            s_arr[i + 1][j + 1] = s_arr[i][j] * d
            p_arr[i][j + 1] += p_arr[i][j] * p
            p_arr[i + 1][j + 1] += p_arr[i][j] * (1 - p)

    print("Stock prices")
    for s in s_arr:
        print(" ".join([str(round(n * 1000) / 1000) for n in s]))
    print("=====================")
    print("Probabilities")
    for p in p_arr:
        print(" ".join([str(round(n * 1000) / 1000) for n in p]))

    return s_arr, p_arr


def stock_lattice_log_normal(x: int, nu: float, sigma: float, s_0: float, exact=True) -> Tuple[List[List[float]], List[List[float]]]:
    """
    :param x: Number of periods
    :param nu: Expected growth rate of logarithm of stock value
    :param sigma: Volatility (standard deviation) of nu
    :param s_0: Initial stock price
    :param exact: Whether to use exact or estimated formulae for u, d and p
    :return: Stock price lattice, Probability lattice
    """
    if exact:
        p = (1 / 2) + (1 / 2) / math.sqrt(((sigma ** 2) / ((nu ** 2) * (1 / x))) + 1)
        exp = math.sqrt((sigma ** 2) * (1 / x) + (nu * (1 / x)) ** 2)
        u = math.e ** exp
        d = math.e ** (-1 * exp)
        print(f"Using exact formulae for u, d and p (u={u}, d={d}, p={p})")
    else:
        p = (1 / 2) + (1 / 2) * (nu / sigma) * math.sqrt(1 / x)
        exp = sigma * math.sqrt(1 / x)
        u = math.e ** exp
        d = math.e ** (-1 * exp)
        print(f"Using estimated formulae for u, d and p (u={u}, d={d}, p={p})")

    return stock_lattice(x, u, d, p, s_0)

