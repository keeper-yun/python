
alist = list(map(int, input().split(',')))

blist = list(map(int, input().split(',')))

new_list = list(set(alist + blist))

new_list = sorted(new_list)

print(new_list)
