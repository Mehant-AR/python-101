def checkUgly(n):
    if n <= 0:
        return "not ugly”
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    while n % 5 == 0:
        n //=5
    return "ugly" if n == 1 else "not ugly"
