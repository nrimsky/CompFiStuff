from typing import List


def allocate_logarithmic_utility(p: List[float], r: List[List[float]]):
    """
    :param p: Probabilities of each outcome
    :param r: Matrix representing expected rate of return for each asset for each outcome, dims # outcomes x # assets
    Prints out equations that need to be solved in order to solve the question
    """
    num_assets = len(r[0])
    expected_utility_equation_parts = []
    for outcome, probability in enumerate(p):
        parts = []
        for asset in range(num_assets):
            if r[outcome][asset] == 0:
                continue
            parts.append(f"{r[outcome][asset]}*w{asset+1}")
        expected_utility_equation_parts.append(f"{probability} * ln( {' + '.join(parts)} )")
    expected_utility_equation = " + ".join(expected_utility_equation_parts)
    print(f"E(U) = {expected_utility_equation}")
    print(f"{' + '.join([f'w{i+1}' for i in range(num_assets)])} - 1 = 0")
    print(f"L = {expected_utility_equation} - lambda * ({' + '.join([f'w{i+1}' for i in range(num_assets)])} - 1)")
    for asset in range(len(r[0])):
        partial_derivative_parts = []
        for outcome, probability in enumerate(p):
            if r[outcome][asset] == 0:
                continue
            denominator = ' + '.join([f'{r[outcome][i]}w{i + 1}' for i in range(num_assets) if r[outcome][i] != 0])
            partial_derivative_parts.append(f"{probability * r[outcome][asset]}/({denominator})")
        partial_derivative = " + ".join(partial_derivative_parts)
        print(f"dL/dw{asset+1} = 0 => {partial_derivative} = lambda")
    print(f"{' + '.join([f'w{i+1}' for i in range(num_assets)])} = 1")


if __name__ == "__main__":
    allocate_logarithmic_utility([0.3, 0.4, 0.3], [[3, 1.2, 6], [1, 1.2, 0], [0, 1.2, 0]])
