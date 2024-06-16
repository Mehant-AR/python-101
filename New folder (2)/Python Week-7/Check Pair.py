def count_distinct_pairs(t, K):
    distinct_pairs = set()
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[i] + t[j] == K:
                distinct_pairs.add((min(t[i], t[j]), max(t[i], t[j])))
    return len(distinct_pairs)
t_input = input()
t = tuple(map(int, t_input.split(',')))
K = int(input())
print(count_distinct_pairs(t, K))
