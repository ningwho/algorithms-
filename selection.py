def linear_search(unsorted_list, target):
    for i in range(len(unsorted_list)):
        if unsorted_list[i] == target:
            return i

    return -1



def selection_sort(unsorted_list):
    for i in range(0, len(unsorted_list)-1):

        min_index = i
        for j in range(i+1, len(unsorted_list)):
            # Loop through unsorted set.
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j

        if min_index !=i:
            unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
    return unsorted_list



unsorted_list = [1, 403, 10, 5, 13, 21]
sorted_array = selection_sort(unsorted_list)
print(sorted_array)
