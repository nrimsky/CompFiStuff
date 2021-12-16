from typing import List
import numpy as np


def infinite_sum_from_0(x: float) -> float:
    """
    :param x: x in sum from 0 to infinity of x^k
    :return: sum from 0 to infinity of x^k
    """
    ans = 1 / (1 - x)
    print(f"S_infinity = 1/(1-x) = {ans}")
    return ans


def sum_from_0(x: float, n: int) -> float:
    """
    :param x: x in sum from 0 to n of x^k
    :param n: n in sum from 0 to n of x^k
    :return: sum from 0 to n of x^k
    """
    ans = (1 - x ** (n + 1)) / (1 - x)
    print(f"S_n = (1 - x^(n+1))/(1-x) = {ans}")
    return ans


def infinite_sum_from_1(x: float) -> float:
    """
    :param x: x in sum from 1 to infinity of x^k
    :return: sum from 1 to infinity of x^k
    """
    ans = (1 / (1 - x)) - 1
    print(f"S_(1,infinity) = 1/(1-x) - 1 = {ans}")
    return ans


def sum_from_1(x: float, n: int) -> float:
    """
    :param x: x in sum from 1 to n of x^k
    :param n: n in sum from 1 to n of x^k
    :return: sum from 1 to n of x^k
    """
    ans = ((1 - x ** (n + 1)) / (1 - x)) - 1
    print(f"S_(1,n) = (1 - x^(n+1))/(1-x) - 1 = {ans}")
    return ans


def annuity_present_value(r: float, n: int, a: float) -> float:
    """
    :param r: Constant interest rate
    :param n: Number of periods
    :param a: Amount received each periods
    :return: Present value of annuity
    """
    ans = a * sum_from_1(1 / (1 + r), n)
    print(f"PV = sum from 1 to n of A/(1+r)^k = sum from 1 to {n} of {a}/(1+{r})^k = {ans}")
    return ans


def amortize(r: float, n: int, pv: float) -> float:
    """
    :param r: Constant interest rate
    :param n: Number of periods
    :param pv: Present value of amount that needs to be repayed
    :return: Equal payments per period needed to repay over n periods
    """
    ans = (r * ((1 + r) ** n) * pv) / (((1 + r) ** n) - 1)
    print(f"A = (pv*r(1+r)^n)/((1+r)^n - 1) = ({pv}*{r}(1+{r})^{n})/((1+{r})^{n} - 1) = {ans}")
    return ans


def bond_price(f: float, ytm: float, c: float, n: int, m: int = 1) -> float:
    """
    :param f: Face value
    :param ytm: Yield to Maturity
    :param c: Coupon per year (c/m received per period)
    :param n: Number of remaining periods
    :param m: Number of coupon payments per year
    :return: Price / present value of bond
    """
    ans = f / ((1 + (ytm / m)) ** n) + (c / m) * sum_from_1(1 / (1 + ytm / m), n)
    print(f"""P = f/((1 + (ytm/m))^n) + sum from 1 to n of (c/m)/(1 + ytm/m)^k 
            = f/((1 + ({ytm}/{m}))^{n}) + sum from 1 to {n} of ({c}/{m})/(1 + {ytm}/{m})^k = {ans}""")
    return ans


def simple_bond_macaulay_duration(f: float, ytm: float, c: float, n: int, m: int = 1) -> float:
    """
    :param f: Face value
    :param ytm: Yield to Maturity
    :param c: Coupon per year (c/m received per period)
    :param n: Number of remaining periods
    :param m: Number of coupon payments per year
    :return: Price / present value of bond
    """
    numerator = []
    denominator = []
    for i in range(1, n):
        numerator.append((c/((1 + (ytm / m))**i)) * i)
        denominator.append(c/((1 + (ytm / m))**i))
    numerator.append(((c + f)/((1 + (ytm / m))**n)) * n)
    denominator.append((c + f) / ((1 + (ytm / m)) ** n))
    ans = sum(numerator)/sum(denominator)
    print(f"D = {'+'.join([str(k) for k in numerator])} / {'+'.join([str(k) for k in denominator])} = {ans}")
    return ans


def macaulay_duration(t: List[float], pv: List[float]) -> float:
    """
    :param t: Times t_0, ..., t_n
    :param pv: Present value of cash flow that occurs at time t_k for each t_k in t
    :return: Macaulay duration of cash flow stream
    """
    numerator = sum([pv[i] * t[i] for i in range(len(t))])
    ans = numerator / sum(t)
    print(f"D = PV(t0)t0 + ... + Pv(tn)tn / PV(t0) + ... + Pv(tn) = {ans}")
    return ans


def modified_duration(d: float, ytm: float, m: int) -> float:
    """
    :param d: Macaulay duration
    :param ytm: Yield to maturity
    :param m: Number of compounding periods per year
    :return: D_M - modified duration (sensitivity of price wrt yield)
    """
    ans = d / (1 + ytm / m)
    print(f"D_M = D / (1 + ytm/m) = {d} / (1 + {ytm}/{m}) = {ans}")
    return ans


def immunize(p: float, d: float, pb: List[float], db: List[float]) -> List[float]:
    """
    :param p: PV of stream of obligations
    :param d: Duration of stream of obligations
    :param pb: PV of bonds 1 to n
    :param db: Durations of bonds 1 to n
    :return: list of amounts invested in each bond
    """
    z = np.array([pb, [(pb[i]/p)*db[i] for i in range(len(db))]])
    m = np.linalg.inv(z)
    y = np.array([p, d])
    solution = np.matmul(m, y)
    ans = list(solution)
    print(f"P = x1*P1 + x2*P2 + ..., D = x1*P1*D1/P + x2*P2*D2/P + ... => X = {ans}")
    return ans



