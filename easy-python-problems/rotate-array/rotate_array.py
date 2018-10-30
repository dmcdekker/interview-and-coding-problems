
'''Rotate arrays by k indices to left or right'''

def rotate_array_left(lst, k):
    length = len(lst)
    result_left = []
    for idx in range(length): 
        result_left.append(lst[(k % length + idx) % length])
    return result_left

def rotate_array_right(lst, k):
    length = len(lst)
    result_right = []
    for idx in range(length): 
        result_right.append(lst[(-k % length + idx) % length])      
    return result_right

def rotate_array_slice_left(lst, k):
    return lst[k:] + lst[:k]

def rotate_array_slice_right(lst, k):
    return lst[-k:] + lst[:k+1] 
    

def rotate_array_in_place(lst, k):
    length = len(lst)
    k = k % length
    if not k:
        return
    lst[:k], lst[k:] = lst[-k:], lst[:-k]
    

print(rotate_array_left([1, 2, 3, 4, 5], 2))
print(rotate_array_right([1, 2, 3, 4, 5], 2))
print(rotate_array_slice_left([1, 2, 3, 4, 5], 2))
print(rotate_array_slice_right([1, 2, 3, 4, 5], 2))
print(rotate_array_in_place([1, 2, 3, 4, 5], 2))