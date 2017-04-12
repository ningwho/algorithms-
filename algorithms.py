def linear_search(unsorted_list, target):
    for i in range(len(unsorted_list)):
        if unsorted_list[i] == target:
            return i

    return -1

unsorted_list = [1, 403, 10, 5, 13, 21]
index = linear_search(unsorted_list, 13)
print(index)
