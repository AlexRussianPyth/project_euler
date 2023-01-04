# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
import cProfile


def brute_force_sum(target: int = 1000):
    """Simply check all natural numbers below target"""
    all_values_sum = 0

    for i in range(1, target):
        if i % 3 == 0 or i % 5 == 0:
            all_values_sum += i

    return all_values_sum


def elegant_sum(target: int = 1000):
    """Use natural numbers as multiplyers"""
    all_multiplies = set()

    for i in range(1, target):
        multiply = 3 * i
        if multiply < 1000:
            all_multiplies.add(multiply)

    for i in range(1, target):
        multiply = 5 * i
        if multiply < 1000:
            all_multiplies.add(multiply)

    return sum(all_multiplies)


print(f"Brute Force Alg gives answer: {brute_force_sum()}")
print(f"Elegant alg gives answer: {elegant_sum()}")


cProfile.run('brute_force_sum(10000000)')
cProfile.run('elegant_sum(10000000)')
