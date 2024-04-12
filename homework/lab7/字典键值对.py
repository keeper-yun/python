

alist = [1, 2, 3, 4, 5, 6, 7]

blist = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

new_list = dict(zip(alist,blist))

for key,values in new_list.items():
    print(f"({key},'{values}')",end=' ')