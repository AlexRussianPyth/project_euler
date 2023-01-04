# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


number_to_factor = 600851475143


def brute_force_alg(number: int):
    for i in range(2, number // 2):
        print(i)


print(brute_force_alg(number_to_factor))
