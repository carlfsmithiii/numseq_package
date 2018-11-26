def fib(n):
    """ Returns nth Fibonacci number """
    if (n < 2):
        return n
    else:
        return fib(n-1) + fib(n-2)
