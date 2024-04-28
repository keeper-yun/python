# 5

def sequence_info(seq,i):
    result = []
    if isinstance(seq, str):
        result.append(max(seq))
        result.append(min(seq))
        result.append(len(seq))
    else:
        result.append(max(seq))
        result.append(min(seq))
        result.append(len(seq))
    return result[i]

list1 = [9, 7, 8, 3, 2, 1, 55, 6]
list2 = ["apple", "pear", "melon", "kiwi"]
list3 = "TheQuickBrownFox"

print(f'list1 = {list1}')
print(f"最大值: {sequence_info(list1,0)}, 最小值: {sequence_info(list1,1)}, 元素个数: {sequence_info(list1,2)}")
print(f'list2 = {list2}')
print(f"最大值: {sequence_info(list2,0)}, 最小值: {sequence_info(list2,1)}, 元素个数: {sequence_info(list2,2)}")
print(f'list3 = {list3}')
print(f"最大值: {sequence_info(list3,0)}, 最小值: {sequence_info(list3,1)}, 元素个数: {sequence_info(list3,2)}")
