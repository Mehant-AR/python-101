def index_mapping(A, B):
    index_map = {num: i for i, num in enumerate(B)}
    return ' '.join(str(index_map[num]) for num in A)
n=int(input())  
A = list(map(int, input().split()))  
B = list(map(int, input().split()))  
print(index_mapping(A, B))
