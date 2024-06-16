def is_prime_digit(digit):
    return digit in [2,3,5,7]
def christmasDiscount(n):
    s=discount=0
    prime_digitis=[2,3,5,7]
    for digit in str(n):
        digit=int(digit)
        if is_prime_digit(digit):
            discount+=digit
    return discount
