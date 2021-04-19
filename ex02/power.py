
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result


def power_recursive(base, exponent):
    if exponent == 0:
        return 1
    return base * power_recursive(base, exponent-1)


if __name__ == "__main__":
    print(power(2, 10))
    print(power_recursive(2, 10))
