#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters """
    next = 'H'
    body = 'H'
    bj = 0
    while (len(body) < n):
        if n % len(body) == 0:
            bj += 2
            next = body
            body += body
        else:
            bj += 1
            body += next
    if len(body) != n:
        return 0
    return bj
