#Author: ALJ (AMDG) 3/1/21

def r_max(nested_num_lst):
    max1 = 0
    for element in nested_num_lst:
        if type(element) == list:
            max1 = r_max(element)
        else:
            if element > max1:
                max1 = element
    return max1

result = r_max([1, 2, 3, [24, 31], 5])
print(result)