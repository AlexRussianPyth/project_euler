from functools import reduce


def sum_square_diff(num: int):
    x = range(1, num + 1)

    sum_squares = reduce(lambda x,y: x+(y**2), x)
    print(f"Сумма квадратов {sum_squares}")

    square_of_sum = reduce(lambda x, y: x + y, x) ** 2
    print(f"Квадрат суммы {square_of_sum}")
    
    return square_of_sum - sum_squares

print(sum_square_diff(100))

