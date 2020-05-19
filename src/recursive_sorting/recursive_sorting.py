# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    elements = len(left) + len(right)
    merged_arr = [0] * elements

    lp = 0
    rp = 0
    i = 0

    # loop while there are elements in either array
    while lp < len(left) or rp < len(right):
        # if there are elements in both arrays
        if lp < len(left) and rp < len(right):
            if left[lp] < right[rp]:
                merged_arr[i] = left[lp]
                lp += 1
            else:
                merged_arr[i] = right[rp]
                rp += 1
            i += 1
        # if there are only elements in the left array
        elif lp < len(left):
            merged_arr[i] = left[lp]
            lp += 1
            i += 1
        # if there are only elements in the right array
        elif rp < len(right):
            merged_arr[i] = right[rp]
            rp += 1
            i += 1
    return merged_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = (len(arr)) // 2
        left_array = arr[0:mid]
        right_array = arr[mid:len(arr)]

        left_array = merge_sort(left_array)
        right_array = merge_sort(right_array)
        result = merge(left_array, right_array)

        return result


# implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # Your code here

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
