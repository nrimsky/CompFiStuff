from typing import List, Tuple
from collections import namedtuple
import math
import numpy as np


def total_return(x0: float, x1: float) -> float:
    """
    :param x0: price at which asset bought
    :param x1: price at which asset sold
    :return: total return R
    """
    ans = x1 / x0
    print(f"R = X1 / X0 = {x1} / {x0} = {ans}")
    return ans


def rate_of_return(x0: float, x1: float) -> float:
    """
    :param x0: price at which asset bought
    :param x1: price at which asset sold
    :return: rate of return r
    """
    ans = (x1 - x0) / x0
    print(f"r = (X1 - X0)/X0  = ({x1} - {x0})/{x0} = {ans}")
    return ans


def portfolio_return(w: List[float], r: List[float]) -> float:
    """
    :param w: asset weights
    :param r: asset returns
    :return: portfolio rate of return
    """
    assert (sum(w) == 1)
    ans = np.dot(np.array(w), np.array(r))
    print(f"r = sum of w_i r_i = {ans}")
    return ans


def portfolio_variance(w: List[float], sigma: List[List[float]]) -> float:
    """
    :param w: asset weights
    :param sigma: asset covariance matrix
    :return: sigma^2 - variance of portfolio
    """
    w = np.array(w)
    wt = np.transpose(w)
    sigma = np.array(sigma)
    ans = float(np.matmul(np.matmul(wt, sigma), w))
    print(f"sigma^2 = w^T Sigma w = {ans}")
    return ans


def solve_portfolio(r: List[float], sigma: List[List[float]], rp: float) -> List[float]:
    """
    :param r: asset expected returns
    :param sigma: asset covariance matrix
    :param rp: target return
    :return: asset weights
    """
    rows = [sigma[i] + [-1 * r[i], -1] for i in range(len(sigma))]
    rows.append([-r[i] for i in range(len(r))] + [0, 0])
    rows.append([-1] * len(r) + [0, 0])
    mat = np.linalg.inv(np.array(rows))
    v = [0] * len(sigma) + [-1 * rp, -1]
    sol = np.matmul(mat, v)
    ans = list(sol)[:-2]
    print(f"Solution of portfolio optimisation: {rows} ^-1 (0,...,0,-rp,-1)^T = {ans}")
    return ans


def estimate_return(r: List[float]) -> float:
    """
    :param r: sample returns
    :return: r bar hat - estimate of unknown mean rate of return
    """
    ans = sum(r) / len(r)
    print(f"r bar hat = mean r = {ans}")
    return ans


def estimate_variance(r: List[float]) -> float:
    """
    :param r: sample returns
    :return: sigma bar hat - estimate of unknown variance of rate of return
    """
    n = len(r)
    mean = estimate_return(r)
    ans = (1 / (n - 1)) * sum([(r[i] - mean) ** 2 for i in range(n)])
    print(f"sigma^2 bar hat = 1/(n-1) * sum for 1 to n of (r_i - r bar hat)^2 = {ans}")
    return ans


def estimate_covariance(ra: List[float], rb: List[float]) -> float:
    """
    :param ra: sample returns of asset a
    :param rb: sample returns of asset b
    :return: covariance of assets a and b
    """
    n = len(ra)
    mean_a = estimate_return(ra)
    mean_b = estimate_return(rb)
    ans = (1 / (n - 1)) * sum([(ra[i] - mean_a) * (rb[i] - mean_b) for i in range(n)])
    print(f"sigma AB = 1/(n-1) * sum for 1 to n of (r_Ai - r_A bar hat)*(r_Bi - r_B bar hat) = {ans}")
    return ans


def capm_r(r_f: float, r_m: float, sigma_m: float, sigma_i: float) -> float:
    """
    :param r_f: Risk free rate of return
    :param r_m: Market portfolio rate of return
    :param sigma_m: Market portfolio standard deviation
    :param sigma_i: Standard deviation of asset i
    :return: Expected return of asset on the capital market line
    """
    ans = r_f + ((r_m - r_f) / sigma_m) * sigma_i
    print(f"r = r_f + ((r_m - r_f) / sigma_m) * sigma_i = {r_f} + (({r_m} - {r_f})/{sigma_m})*{sigma_i} = {ans}")
    return ans


def capm_std(r_f: float, r_m: float, sigma_m: float, r_e: float) -> float:
    """
    :param r_f: Risk free rate of return
    :param r_m: Market portfolio rate of return
    :param sigma_m: Market portfolio standard deviation
    :param r_e: Expected return
    :return: Standard deviation of the position
    """
    ans = (r_e - r_f) * (sigma_m / (r_m - r_f))
    print(f"{r_f} + (({r_m} - {r_f})/{sigma_m})*sigma = {r_e} -> ({r_e} - {r_f})*({sigma_m}/({r_m} - {r_f})) = sigma = {ans}")
    return ans


def capm_equation(r_f: float, r_m: float, sigma_m: float) -> str:
    """
    :param r_f: Risk free rate of return
    :param r_m: Market portfolio rate of return
    :param sigma_m: Market portfolio standard deviation
    :return: String of the equation of the capital market line
    """
    mult = (r_m - r_f) / sigma_m
    ans = f"{r_f} + {mult}sigma"
    print(f"r = {r_f} + (({r_m} - {r_f})/{sigma_m})*sigma = {ans}")
    return ans


def beta_capm_r(sigma_im: float, sigma2_m: float, r_m: float, r_f: float) -> float:
    """
    :param sigma_im: Covariance of asset i and market portfolio
    :param sigma2_m: Variance of market portfolio
    :param r_m: Rate of return for market portfolio
    :param r_f: Risk free rate of return
    :return: Return of asset i
    """
    beta = sigma_im / sigma2_m
    ans = r_f + beta * (r_m - r_f)
    print(f"r_i = r_f + beta(r_m - r_f) [beta = sigma_im / sigma2_m = {sigma_im}/{sigma2_m}] -> r_i = {r_f} + {beta}({r_m} - {r_f}) = {ans}")
    return ans


def asset_weights(r_f: float, r_i: float, r_t: float) -> Tuple[float, float]:
    """
    :param r_f: Risk free rate of return
    :param r_i: Risky asset rate of return
    :param r_t: Target rate of return
    :return: Amount in risk free asset (negative is borrowing), amount in risky asset
    """
    ans = (r_t - r_i) / (r_f - r_i)
    print(f"{r_f}w + {r_i}(1 - w) = {r_t} -> w = {ans} (invest {ans} in risk free and {1 - ans} in risky asset)")
    return ans, 1 - ans


def two_fund(w1: List[float], w2: List[float], r: List[float]) -> Tuple[float, float]:
    """
    :param w1: Asset weights for one portfolio in the minimum variance set
    :param w2: Asset weights for another portfolio in the minimum variance set
    :param r: Rates of return for these assets
    :return: Assuming portfolio is efficient and short selling is allowed, minimum and maximum
    possible values for the expected rate of return on the market portfolio
    This is assuming we have no more info
    If we know that one of w1 or w2 is the minimum variance portfolio then the return of that portfolio
    is the lower bound because the expected return of the market cannot be less than that of the
    minimum variance portfolio
    """
    less_than = []
    greater_than = []
    # The market cannot contain assets in negative amounts
    for i in range(len(w1)):
        diff = w1[i] - w2[i]
        lim = (-w2[i]) / (w1[i] - w2[i])
        if diff < 0:
            less_than.append(lim)
        else:
            greater_than.append(lim)
    a_min = max(greater_than)
    a_max = min(less_than)
    r_1, r_2 = 0, 0
    for i in range(len(w1)):
        r_1 += (a_min * w1[i] + (1 - a_min) * w2[i]) * r[i]
        r_2 += (a_max * w1[i] + (1 - a_max) * w2[i]) * r[i]
    print(f"{a_min} < a < {a_max}")
    r_min = min([r_1, r_2])
    r_max = max([r_1, r_2])
    print(f"{r_min} < r < {r_max}")
    return r_min, r_max


StockData = namedtuple("StockData", ["no_shares", "price", "r", "sigma"])


def risk_free_two_assets(a: StockData, b: StockData, rho: float) -> float:
    """
    :param a: Stock A ( No. shares outstanding | Price per share | Expected rate of return | Standard deviation of return)
    :param b: Stock B ( No. shares outstanding | Price per share | Expected rate of return | Standard deviation of return)
    :param rho: correlation coefficient between the returns of stocks A and B
    :return: Risk-free rate given market satisfies the CAPM exactly
    """
    value_in_a = a.no_shares * a.price
    value_in_b = b.no_shares * b.price
    market_portfolio_weights = [value_in_a / (value_in_a + value_in_b), value_in_b / (value_in_a + value_in_b)]
    print(f"Market portfolio weights: A: {market_portfolio_weights[0]}, B: {market_portfolio_weights[1]}")
    r_m = portfolio_return(market_portfolio_weights, [a.r, b.r])
    sigma_ab = rho * (a.sigma * b.sigma)
    variance = portfolio_variance(market_portfolio_weights, [[a.sigma ** 2, sigma_ab], [sigma_ab, b.sigma ** 2]])
    std = math.sqrt(variance)
    print(f"Standard deviation of market portfolio = {std}")
    sigma_am = market_portfolio_weights[0] * (a.sigma ** 2) + market_portfolio_weights[1] * sigma_ab
    beta = sigma_am / variance
    print(f"beta_A = sigma_AB/sigma2_M = {sigma_am}/{variance} = {beta}")
    r_f = (0.15 - beta * r_m) / (1 - beta)
    print(f"r_f = (r_a - beta_a*r_m)/(1 - beta_a) = {r_f}")
    return r_f

