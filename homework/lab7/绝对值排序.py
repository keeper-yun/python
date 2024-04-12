

alist = list(map(int, input().split(' ')))

new_alist = sorted(alist, key=abs)

print(new_alist)
