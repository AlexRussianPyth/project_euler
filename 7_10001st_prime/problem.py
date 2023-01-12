def prime_finder(number: int) -> int:
    """Finds number'st prime number. For example, for number 6 answer will be 13"""
    primes = [2]  # Primes starts from 2
    count = 2
    run = True

    while run:
        count += 1
        for prime in primes:
            if count % prime == 0:
                break
            else:
                if prime == primes[-1]:
                    primes.append(count)
                    if len(primes) == number:
                        run = False

    return primes

print(prime_finder(10001))
