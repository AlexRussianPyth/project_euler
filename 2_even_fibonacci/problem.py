# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

border_val = 4_000_000

def brute_force_alg(border_val: int = 4_000_000):
    """Brute force alg for breaking problem"""
    sum_even_elements = 0

    fibonacci_sequence = [1, 1]
    current_elem = None

    while True:
        current_elem = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(current_elem)
        if current_elem >= border_val:
            break
        if current_elem % 2 == 0:
            print(current_elem)
            sum_even_elements += current_elem

    return sum_even_elements



print(brute_force_alg())
