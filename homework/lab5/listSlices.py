

mylist = [1,4,12,25,7,9,110,24]
print(f'原列表:{mylist}')
tem = mylist[0]

mylist = mylist[1::]
mylist.append(tem)

print(f'改变后列表:{mylist}')

