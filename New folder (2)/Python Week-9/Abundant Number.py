def abundant(number):
    d_s=sum([divisor for divisor in range(1,number) if number % divisor == 0])
    if d_s>number:
        return"Yes"
    else:
        return "No"
