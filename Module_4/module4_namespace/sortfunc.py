# Пузырьковая сортировка
nums = [5, 6, 3, 4, 2, 1, 8, 9]
def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                swapped = True


# bubble_sort(nums)
# print(nums)


# Сортировка выборкой
# nums = [5, 6, 3, 4, 2, 1, 8, 7, 9]
def selected_sort(ls):
    for i in range(len(ls)):
        lowes = i
        for j in range(i+1, len(ls)):
            if ls[j] < ls[lowes]:
                lowes = j
        ls[i], ls[lowes] = ls[lowes], ls[i]

# selected_sort(nums)
# print(nums)

# Сортировка вставкой
def insertion_sort(ls):
    for i in range(len(ls)):
        val = ls[i]
        lowes = i
        while lowes > 0 and ls[lowes-1] > val:
            ls[lowes] = ls[lowes-1]
            lowes -= 1
        ls[lowes] = val

# insertion_sort(nums)
# print(nums)