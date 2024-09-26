from sortfunc import insertion_sort, bubble_sort, selection_sort

data_1 = [1, 2, 5, 8, 7, 3, 6, 10, 9, 4]
data_2 = [1, 2, 5, 8, 7, 3, 6, 10, 9, 4, 13, 12, 11]
data_3 = [1, 2, 5, 8, 7, 3, 6, 10, 9, 4, 25, 15, 33, 0]

print(insertion_sort(data_1))
print(insertion_sort(data_2))
print(insertion_sort(data_3))

print(bubble_sort(data_1))
print(bubble_sort(data_2))
print(bubble_sort(data_3))

print(selection_sort(data_1))
print(selection_sort(data_2))
print(selection_sort(data_3))
