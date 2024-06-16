def automorphic(n):
    if(n<0):
        return "Invalid input"
    square = n  * n
    n_s=str(n)
    s_s=str(square)
    if s_s.endswith(n_s):
        return "Automorphic"
    else:
        return "Not Automorphic"
