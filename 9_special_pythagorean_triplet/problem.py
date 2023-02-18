# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt
from time import sleep

a = 1
b = 1

while True:
    for b in range(1, 1000 - a):
        c = sqrt((a ** 2) + (b ** 2))

        if c % 1 == 0:
            if a + b + c == 1000:
                print(a, b, c)
    a += 1
