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
        left_array = arr[:mid]
        right_array = arr[mid:]

        left_array = merge_sort(left_array)
        right_array = merge_sort(right_array)
        result = merge(left_array, right_array)

        return result


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    start_hi = mid + 1

    # if mid and start_hi already in order, return
    if arr[mid] <= arr[start_hi]:
        return
    # while pointers are within bounds
    while start <= mid and start_hi <= end:
        # if start elem is in order w/ respect to start_hi elem
        if arr[start] <= arr[start_hi]:
            # just increment start
            start += 1
        else:
            # current value is at start of start_hi
            value = arr[start_hi]
            # index is start_hi
            index = start_hi

            # while index is not equal to start
            while index != start:
                # swap item at index with it's left-neighbor
                arr[index] = arr[index-1]
                # decrement index (working toward exiting above while loop)
                index -= 1
            # value at arr start is new value (the other half of the swap)
            arr[start] = value
            # increment all pointers (except end)
            start += 1
            mid += 1
            start_hi += 1


def merge_sort_in_place(arr, l, r):
    if l < r:
        mid = (l + r) // 2

        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid+1, r)

        merge_in_place(arr, l, mid, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr


arr = [8, 7, 6, 5, 4, 3, 2, 1]
result = merge_sort_in_place(arr, 0, len(arr)-1)
print(result)
