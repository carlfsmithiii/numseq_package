def square(num):
    """ Returns (num)th square number, which is the square of num """
    return num * num


def triangle(num):
    """ Returns the (num)th triangle number """
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum


def cube(num):
    """ Returns the (num)th cube number, which is the cube of num """
    return num ** 3
