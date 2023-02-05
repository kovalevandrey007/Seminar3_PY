# 23. Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

list1 = [0, -1, 5, 2, 3]
result =[]

count = 0

for i in range(1, len(list1)):
    if list1[i-1] < list1[i]:
        result.append(list1[i])
print(result)

result = [list1[i] for i in range(1, len(list1)) if list1[i-1] < list1[i]]
print(result)

lst1 = [11,22,33,46,58,61,72,80,94]
# for idx in range(len(lst1)):
#     if lst1[i] > lst1[i-1]:
# for el in lst1:
#     print(el)

for idx, el in enumerate(lst1):
    print(f"lst1[{idx}] = {el}")
    
    
    dict1 = {1:"saas", 2:"eaew"}
    for key  in dict1.keys():
        print(key)
        print("-"*12)
for value in dict1.values():
    print(value)
print("-"*12)