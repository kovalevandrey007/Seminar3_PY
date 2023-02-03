# 19. Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# k = int(input())

k = 3
list1 = [1,2,3,4,5]
list2 = []
for i in range(k, len(list1)):
    list2.append(list1[i])
for i in range(0,k):
    list2.append(list1[i])
print(list2)


# методом среза 
print (list1[k:]) # последние 2 т.к. k = 3
print(list1[:k])  # первые 2 т.к. k = 3
print (list1[k:] + list1[:k])
