import doctest
def fib(n):
    '''
    >>> fib(0)
    0
    >>> fib(5)
    5
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(6)
    8
    '''
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__": 
    doctest.testmod()
