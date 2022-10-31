def swap_list(arr):
    if len(arr) == 0:
        return arr

    mid = len(arr)//2 - 1
    if len(arr) % 2:
        mid += 1
    
    arr[mid], arr[-1] = arr[-1], arr[mid]
    return arr