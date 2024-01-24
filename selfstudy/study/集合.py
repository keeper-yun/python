
# 集合是无序的......
# 集合可修改.......
# 定义一个集合
"""
assembly={'Sam','hello','black'}
emptySet=set()

print(assembly)
print(f'{emptySet},{type(emptySet)}')

assembly.add('python')
print(assembly)

assembly.remove('Sam')
print(assembly)

assembly.clear()
print(assembly)


set1={1,2,3}
set2={1,4,5}
set3=set1.difference(set2)
print(f'{set3}')

set1={1,2,3}
set2={1,4,5}
set3=set1.difference_update(set2)
print(set1)
print(f'{set2}\n')

set1={1,2,3}
set2={1,5,6}
set3=set1.union(set2)
print(set3)

set1={1,2,3,4,5}
for line in set1:
    print(f'{line}')
"""

my_list=['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']

emptySet=set()

for line in my_list:
    print(line)
    emptySet.add(line)
print('\n\n')
print(emptySet)
