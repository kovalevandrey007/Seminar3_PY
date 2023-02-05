# 21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

dict_list1 = [{"V": "S001 "}, {"V": "S002"}, {"VI": "S001 "},{"VI": "S005"}, {"VII": "S005 "}, {"V":"S009"}, {"VIII": "S007 "}]
# for idx in range(len(dict_list1)):
#     for j in dict_list1[idx]:
set1 = set()
for el in dict_list1:
    for value in el.values(): 
        set1.add(value.strip())
print(set1)

#**
new_set = {value.strip() for el in dict_list1 for value in el.values()}
