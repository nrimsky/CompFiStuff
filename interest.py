import math
from typing import List


def rate(w0: float, wn: float, n: int) -> float:
    """
    :param w0: Wealth today
    :param wn: Wealth after n years
    :param n: Number of years
    :return: Rate if interest rate constant
    """
    ans = (wn / w0) ** (1 / n) - 1
    print(f"r = (wn/w0)^(1/n) - 1 = ({wn}/{w0})^(1/{n}) - 1 = {ans}")
    return ans


def effective_interest_rate(r: float, m: int = 1) -> float:
    """
    :param r: Nominal interest rate
    :param m: Number of equally spaced compounding intervals in a year
    :return: r_eff - effective interest rate
    """
    ans = ((1 + r / m) ** m) - 1
    print(f"r_eff = ((1 + r/m)^m) - 1 = ((1 + {r}/{m})^{m}) - 1 = {ans}")
    return ans


def effective_interest_rate_cont(r: float) -> float:
    """
    :param r: Nominal interest rate
    :return: r_eff - effective interest rate
    """
    ans = math.e ** r - 1
    print(f"r_eff = e^r - 1 = e^{r} - 1 = {ans}")
    return ans


def wealth_growth(r: float, k: int, m: int = 1) -> float:
    """
    :param r: Nominal interest rate
    :param m: Number of equally spaced compounding intervals in a year
    :param k: Number of periods
    :return: Growth of the account over k periods
    """
    ans = (1 + r / m) ** k
    print(f"growth = (1 + r/m)^k = (1 + {r}/{m})**{k} = {ans}")
    return ans


def wealth_growth_cont(r: float, t: float) -> float:
    """
    :param r: Nominal interest rate
    :param t: Time measured in years
    :return: Growth of the account over t years
    """
    ans = math.e ** (r * t)
    print(f"growth = e^(rt) = e^({r}{t}) = {ans}")
    return ans


def discount_factor(r: float, k: int, m: int = 1) -> float:
    """
    :param r: Nominal interest rate
    :param m: Number of equally spaced compounding intervals in a year
    :param k: Number of periods
    :return: Discount factor corresponding to period k
    """
    growth = wealth_growth(r, k, m)
    ans = 1 / growth
    print(f"d_k = 1/growth = 1/{growth} = {ans}")
    return ans


def present_value(a: float, r: float, k: int, m: int = 1) -> float:
    """
    :param a: Future value
    :param r: Nominal interest rate
    :param m: Number of equally spaced compounding intervals in a year
    :param k: Number of periods
    :return: Present value of a
    """
    d_k = discount_factor(r, k, m)
    ans = d_k * a
    print(f"PV = d_k * A = {d_k} * {a} = {ans}")
    return ans


def forward_rate(s_t1: float, s_t2: float, t1: float, t2: float) -> float:
    """
    :param s_t1: Spot rate at time t1
    :param s_t2: Spot rate at time t2
    :param t1: Time t1
    :param t2: Time t2
    :return: Forward rate - interest rate charged for borrowing money at t1 which is to be repaid with interest at time t2.
    f_(t1,t2) is agreed on today (t = 0).
    """
    ans = (((1+s_t2)**t2)/((1+s_t1)**t1))**(1/(t2-t1)) - 1
    print(f"f_(t1,t2) = (((1+s_t2)^t2)/((1+s_t1)^t1))^(1/(t2-t1)) - 1 = (((1+{s_t2})^{t2})/((1+{s_t1})^{t1}))^(1/({t2}-{t1})) - 1 = {ans}")
    return ans


def evolve_spot_rate_curve(s: List[float]) -> List[float]:
    """
    :param s: Current spot rate curve
    :return: Expected spot rate curve in a year
    """
    ans = []
    s_1 = s[0]
    for i, s_j in enumerate(s):
        j = i + 1
        if j == 1:
            continue
        f_1j = forward_rate(s_1, s_j, 1, j)
        ans.append(f_1j)
    print(f"s'_(j-1) = f_(1,j) for j = 2...n => s' = {ans}")
    return ans



