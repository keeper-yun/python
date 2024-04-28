# 4

def min_n(a, b, *c):
    ans = min(a, b)
    for i in c:
        ans = min(ans, i)
    return ans

print(f'最小值为:{min_n(8,2)}')
print(f'最小值为:{min_n(16,1,7,4,15)}')