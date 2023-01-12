# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 =91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome_checker(number: int) -> bool:
    if str(number) == str(number)[::-1]:
        return True
    return False


def palindrome_finder(max_number: int = 999) -> int:

    largest_palindrome = 0

    for x in range(0, max_number):
        for y in range(0, max_number):
            number = x * y
            if palindrome_checker(number):
                if number > largest_palindrome:
                    largest_palindrome = number

    return largest_palindrome

print(palindrome_finder(999))
                
