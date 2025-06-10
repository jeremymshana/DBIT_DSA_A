def reverse_list(lst):
    return lst[::-1]

my_list = [1, 2, 3, 4, 5]
print(reverse_list(my_list))
#rotating list
def rotate_list(lst, k):
    if not lst:
        return lst
    k = k % len(lst)  # Handle rotations greater than list length
    return lst[-k:] + lst[:-k]


my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list(my_list, 2)
print(rotated_list)  # Output: [4, 5, 1, 2, 3]