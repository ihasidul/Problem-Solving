def powers_of_two(n):
    result = []
    for number in range(n + 1):
        result.append(2**number)
    return result
