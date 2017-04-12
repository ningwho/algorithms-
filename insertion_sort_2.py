def insertion_sort(my_array):
    #return a sorted list.

    for i in range(1,len(my_array)):
        currentValue = my_array[i]
        position = i


        while position > 0 and my_array[position-1] > currentValue:

            # this switches the value. if current position is less than next position then it will swap. new value becomse current value.
            my_array[position]=my_array[position-1]
            my_array[position-1]= currentValue
            position = position -1

my_array = [54, 26, 93, 17,77,31,44,55,20]

print(insertion_sort(my_array))


# def insertion_sort(list):
#     #return a sorted list.
#     list_length = len(list)
#     for i in range(1,len(list)):
#         currentValue = list[i]
#         position = i
#
#
#         while position > 0 and list[position-1] > currentValue:
#
#
#             list[position]=list[position-1]
#             position = position -1
#
#             list[position]=currentValue
#
# my_array = [54, 26, 93, 17,77,31,44,55,20]
#
# print(insertion_sort(my_array))




# def insertion_sort(list):
#     #return a sorted list.
#
#     for i in range(1,len(my_array)):
#         currentValue = my_array[i]
#         position = i
#
#
#         while position > 0 and my_array[position-1] > currentValue:
#
#
#
#             my_array[position]= currentValue
#             position = position -1
#
# my_array = [54, 26, 93, 17,77,31,44,55,20]
#
# print(insertion_sort(my_array))
