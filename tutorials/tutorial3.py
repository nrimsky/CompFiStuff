import fixed_income


def ex1():
    # Part 1
    fixed_income.bond_price(1000, 0.15, 100, 3)
    fixed_income.bond_price(1000, 0.15, 50, 3)
    p3 = fixed_income.bond_price(1000, 0.15, 0, 3)
    p4 = fixed_income.bond_price(1000, 0.15, 0, 1)
    # Part 2
    d1 = fixed_income.simple_bond_macaulay_duration(1000, 0.15, 100, 3)
    d2 = fixed_income.simple_bond_macaulay_duration(1000, 0.15, 50, 3)
    d3 = fixed_income.simple_bond_macaulay_duration(1000, 0.15, 0, 3)
    d4 = fixed_income.simple_bond_macaulay_duration(1000, 0.15, 0, 1)
    durations = [d1, d2, d3, d4]
    # Part 3
    max_duration = ["A", "B", "C", "D"][durations.index(max(durations))]
    print(f"The bond most sensitive to a change in the yield is {max_duration} because it has the largest duration")
    # Part 4 / 5
    print(f"Present value of obligation: {2000 / (1.15 ** 2)}")
    x = fixed_income.immunize(2000 / (1.15 ** 2), 2, [p3, p4], [d3, d4])
    print(f"VC = p3 * x1 = {p3 * x[0]}, VD = p4 * x2 = {p4 * x[1]}")

# Other exercises are derivations


if __name__ == "__main__":
    ex1()
